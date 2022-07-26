
def f_df_filter(df, filter_Rp_ERadia, bubble_size, filter_argument):
    
    if filter_argument == "<":

        df = df.loc[df["Rp_ERadia"] < filter_Rp_ERadia]
        max_größe = df["Rp_ERadia"].max()
        df["marker_size"] = bubble_size * (df["Rp_ERadia"] / max_größe)
        max_größe

    elif filter_argument == ">":
        df = df.loc[df["Rp_ERadia"] > filter_Rp_ERadia]
        max_größe = df["Rp_ERadia"].max()
        df["marker_size"] = bubble_size * (df["Rp_ERadia"] / max_größe)
        max_größe
    
    return(df, max_größe)