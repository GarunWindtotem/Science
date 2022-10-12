from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.patches as mpatches

def f_visualize1(df, pfad, now, name_chart, filter_argument, filter_Rp_ERadia, max_größe):

    plt.clf()

    def y_axis_thousands(x, pos):
        # 'The two args are the value and tick position'
        return '{:0,d}'.format(int(x)).replace(",", ".")

    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(20, 9))
    formatter = FuncFormatter(y_axis_thousands)
    ax.yaxis.set_major_formatter(formatter)

    # Temperature < 100°C
    [ax.plot(
            row['Distance_LJ'], row['Period'], '.', 
            markersize=row['marker_size']*1, 
            alpha=0.7, 
            color = "blue" if row['Teq'] <= 273 else 'None',
            label = "") for idx, row in df.iterrows()]

    # Temperature > 100°C
    [ax.plot(
            row['Distance_LJ'], row['Period'], '.', 
            markersize=row['marker_size']*1, 
            alpha=0.7, 
            color = "red" if row['Teq'] >= 373 else 'None',
            label = "") for idx, row in df.iterrows()]

    # Temperature 0°C to 100°C
    [ax.plot(
            row['Distance_LJ'], row['Period'], '.', 
            markersize=row['marker_size']*1, 
            alpha=1, 
            color = "green" if 273 <= row['Teq'] <= 373 else 'None',
            label = "") for idx, row in df.iterrows()]

    # Temperature 0°C to 100°C
    [ax.plot(
            row['Distance_LJ'], row['Period'], '.', 
            markersize=row['marker_size']*1, 
            alpha=1, 
            color = "yellow" if 282 <= row['Teq'] <= 292 else 'None',
           # markeredgewidth=0.5,
           # markeredgecolor = 'black',
            label = "") for idx, row in df.iterrows()]

    ax.set_xlabel("Distance in Lightyears", color="black", fontsize=25)
    ax.set_ylabel("Period in days", color="black", fontsize=25)
    ax.set_yscale('log')
    ax.set_xscale('log')

    ax.tick_params(labelsize=25)

    red_patch = mpatches.Patch(color='red', label = 'T > 373 K')
    blue_patch = mpatches.Patch(color='blue', label = 'T < 273 K')
    yellow_patch = mpatches.Patch(color='yellow', label = 'T between 282 and 292 K')
    green_patch = mpatches.Patch(color='green', label = 'T between 273 and 373 K')
    # ax.legend(handles=[red_patch])

    plt.legend(loc='center',
                handles=[blue_patch, red_patch, green_patch, yellow_patch],
                bbox_to_anchor=(0.5, -0.25),
                fancybox=True,
                shadow=True,
                ncol=4,
                fontsize=20)

    plt.title(f' Exoplanetes (Data: NASA) \n\n', fontsize=25)


    # place a text box in upper left in axes coords
    #      (x, y)
    ax.text(0.05, 0.98, "Mars", transform=ax.transAxes, fontsize=16, verticalalignment='top')
    ax.text(0.05, 0.91, "Earth", transform=ax.transAxes, fontsize=16, verticalalignment='top')
    ax.text(0.05, 0.86, "Venus", transform=ax.transAxes, fontsize=16, verticalalignment='top')
    ax.text(0.05, 0.75, "Mercury", transform=ax.transAxes, fontsize=16, verticalalignment='top')
    ax.text(0.78, 0.92, "Kepler-452 b", transform=ax.transAxes, fontsize=16, verticalalignment='top')
    ax.text(0.72, 0.79, "Kepler-62 e", transform=ax.transAxes, fontsize=16, verticalalignment='top')

    plt.suptitle(f'Filter: radius {filter_argument} {filter_Rp_ERadia}, max= {max_größe} Earth Radia \n https://catalogs.mast.stsci.edu/eaot# \n {now} PW', fontsize=15, y=0.95)
    plt.savefig(f'{pfad}{name_chart}.png', dpi=300, bbox_inches='tight')
