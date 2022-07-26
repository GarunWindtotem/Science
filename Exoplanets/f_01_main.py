import os
# from matplotlib.cbook import print_cycles
from f_02_now import f_now
from f_03_options import f_options
from f_04_df import f_df
from f_05_solarSystem import f_solarSystem
from f_06_visualize1 import f_visualize1
from f_07_visualize2 import f_visualize2
from f_04_df_filter import f_df_filter

# function 02
now = f_now()
# function 03
bool_period_Earth = f_options()

# function 04

# pfad = "D:\\Github\\Science\\Exoplanets\\"
pfad = str(os.path.abspath(os.getcwd()))+ "\\"


# 
df = f_df(pfad)
df = f_solarSystem(df)

# filter
filter_Rp_ERadia = 2
bubble_size = 30
filter_argument = "<"
df, max_größe = f_df_filter(df, filter_Rp_ERadia, bubble_size, filter_argument)

# function 06
name_chart = "Exoplanets_1"
f_visualize1(df, pfad, now, name_chart, filter_argument, filter_Rp_ERadia, max_größe)


# function 07
df = f_df(pfad)
# filter
filter_Rp_ERadia = 100
bubble_size = 100
filter_argument = "<"
df, max_größe = f_df_filter(df, filter_Rp_ERadia, bubble_size, filter_argument)

# filter
name_chart = "Exoplanets_2"
bool_textfield = False
f_visualize2(df, pfad, now, name_chart, filter_argument, filter_Rp_ERadia, bool_textfield, max_größe)


# function 08
df = f_df(pfad)
df = f_solarSystem(df)
# filter
filter_Rp_ERadia = 2
bubble_size = 30
filter_argument = "<"

df, max_größe = f_df_filter(df, filter_Rp_ERadia, bubble_size, filter_argument)

name_chart = "Exoplanets_3"
bool_textfield = True
f_visualize2(df, pfad, now, name_chart, filter_argument, filter_Rp_ERadia, bool_textfield, max_größe)


# function 08
df = f_df(pfad)
# filter
filter_Rp_ERadia = 7
bubble_size = 100
filter_argument = ">"
df, max_größe = f_df_filter(df, filter_Rp_ERadia, bubble_size, filter_argument)

name_chart = "Exoplanets_4"
bool_textfield = False
f_visualize2(df, pfad, now, name_chart, filter_argument, filter_Rp_ERadia, bool_textfield, max_größe)


print('fertig')