import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Ensure Seaborn is installed
from datetime import datetime
import matplotlib.dates as mdates
import numpy as np
import sys

# Apply Seaborn's default settings for better aesthetics
sns.set()

# Define the API endpoint
api_url = "https://ssd-api.jpl.nasa.gov/cad.api"

# Filters and settings
filter_distance_ld = 20  # Maximum distance in Lunar Distances (LD)
filter_date_max = '2121-12-31'  # Maximum date for data retrieval
show_top5_labels = False  # Set to True to label the top 5 largest NEOs
show_iss_orbit = False  # Set to True to display the ISS orbit
show_geostationary_orbit = False  # Set to True to display the geostationary orbit
show_moon_orbit = True  # Set to True to display the Moon's orbit

# Parameters for the API request
params = {
    'date-min': datetime.now().strftime('%Y-%m-%d'),
    'date-max': filter_date_max,
    'dist-max': filter_distance_ld,  # Numeric value as per API documentation
    'dist-unit': 'LD',  # Specify the unit separately
    'sort': 'date',
    'fullname': 'true',
    # 'limit': 'all',  # Removed as 'all' is invalid
}

# Implement pagination to retrieve all records
all_data = []
fields = None  # To store 'fields' from the first response
limit = 1000  # Number of records to fetch per request
limit_from = 1  # Starting record number

while True:
    # Update parameters for pagination
    params['limit'] = limit
    params['limit-from'] = limit_from

    # Make the API request
    response = requests.get(api_url, params=params)

    # Check if the request was successful
    if response.status_code != 200:
        print('Error fetching data:', response.status_code)
        print(response.text)  # Print error message from the server
        sys.exit(1)

    # Load data from the JSON response
    try:
        data = response.json()
    except ValueError:
        print("Error: Response content is not valid JSON.")
        print(response.text)
        sys.exit(1)

    # On the first successful response, capture 'fields'
    if fields is None:
        if 'fields' not in data:
            print("Error: 'fields' key not found in the API response.")
            print("Response:", data)
            sys.exit(1)
        fields = data['fields']

    # Check if there are any results
    if data.get('count', 0) == 0:
        break  # No more data to fetch

    # Append the fetched data
    fetched_data = data.get('data', [])
    if not fetched_data:
        print("Warning: 'data' key is empty in the response.")
        break
    all_data.extend(fetched_data)

    # Check if we've retrieved all available records
    total = data.get('total', None)
    if total is not None and len(all_data) >= total:
        break

    # Update 'limit_from' for the next batch
    limit_from += limit

# Create DataFrame from all fetched data
if not all_data:
    print("No data retrieved based on the current filters.")
    sys.exit(0)

# Ensure 'fields' is captured
if fields is None:
    print("Error: 'fields' were not captured from any API response.")
    sys.exit(1)

df = pd.DataFrame(all_data, columns=fields)

# Data Processing

# Convert 'cd' (close approach date) to datetime objects
df['cd'] = pd.to_datetime(df['cd'], errors='coerce')
if df['cd'].isnull().all():
    print("Error: All 'cd' (close approach date) entries could not be parsed.")
    sys.exit(1)

# Convert 'dist' (distance) to float
df['dist_au'] = pd.to_numeric(df['dist'], errors='coerce')
if df['dist_au'].isnull().all():
    print("Error: All 'dist' (distance) entries could not be parsed.")
    sys.exit(1)

# Convert distances from astronomical units to kilometers and lunar distances
AU_TO_KM = 149597870.7
LD_TO_KM = 384400
df['dist_km'] = df['dist_au'] * AU_TO_KM
df['dist_ld'] = df['dist_km'] / LD_TO_KM

# Convert 'h' (absolute magnitude) to numeric
df['H'] = pd.to_numeric(df['h'], errors='coerce')  # 'h' is lowercase as per documentation

# Estimate diameters from absolute magnitude 'H' using albedo pv
# Diameter (km) = (1329 / sqrt(albedo)) * 10^(-0.2 * H)
# Assume a standard albedo value for NEOs
pv = 0.14  # Assumed geometric albedo
df['diameter_km'] = (1329 / np.sqrt(pv)) * (10 ** (-0.2 * df['H']))

# Filter data within the specified distance
df = df[df['dist_ld'] <= filter_distance_ld]

# Remove entries without diameter estimates
df = df.dropna(subset=['diameter_km'])

# Calculate marker sizes based on NEO diameters
if not df.empty:
    max_diameter = df['diameter_km'].max()
    df['marker_size'] = 300 * (df['diameter_km'] / max_diameter)
else:
    df['marker_size'] = []

# Identify the top 5 largest NEOs
if show_top5_labels:
    df_top5 = df.nlargest(5, 'diameter_km')
else:
    df_top5 = pd.DataFrame()

# Visualization

# Use Seaborn style
plt.style.use('seaborn')

fig, ax = plt.subplots(figsize=(20, 9))

# Scatter plot of NEOs
scatter = ax.scatter(df['cd'], df['dist_km'], s=df['marker_size'], alpha=0.7, c='purple', label='NEOs')

# Annotate top 5 largest NEOs
if show_top5_labels and not df_top5.empty:
    for _, row in df_top5.iterrows():
        ax.annotate(row['des'], (row['cd'], row['dist_km']), textcoords="offset points",
                    xytext=(0,10), ha='center', fontsize=12, color='black')

# Reference lines for Earth, ISS, geostationary orbit, and Moon
earth_radius_km = 6371  # Earth's radius
earth_diameter_km = earth_radius_km * 2  # Earth's diameter
iss_orbit_km = earth_radius_km + 408  # ISS orbit altitude from Earth's center
geostationary_orbit_km = earth_radius_km + 35786  # Geostationary orbit altitude
moon_orbit_km = LD_TO_KM  # Moon's average distance from Earth

# Earth representation spanning the entire date range
ax.fill_between([df['cd'].min(), df['cd'].max()], 0, earth_diameter_km, color='blue', alpha=0.5, label='Earth')

# Optional reference lines
if show_iss_orbit:
    ax.axhline(y=iss_orbit_km, color='orange', linestyle='-', label='ISS Orbit')

if show_geostationary_orbit:
    ax.axhline(y=geostationary_orbit_km, color='red', linestyle='-', label='Geostationary Orbit')

if show_moon_orbit:
    ax.axhline(y=moon_orbit_km, color='gray', linestyle='--', label='Moon Orbit')

# Formatting the plot
ax.set_xlabel("Date of Close Approach", fontsize=20)
ax.set_ylabel("Distance from Earth (km)", fontsize=20)
ax.set_title("Upcoming Near Earth Objects Approaching Earth", fontsize=24)
ax.tick_params(axis='both', which='major', labelsize=14)

# Date formatting on the x-axis
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Rotate date labels for better readability
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

# Legend positioning
ax.legend(loc='upper right', fontsize=14)

# Display the plot
plt.tight_layout()
plt.show()
