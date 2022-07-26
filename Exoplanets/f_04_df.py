import pandas as pd

def f_df(pfad):

    # import data
    df = pd.read_csv(pfad + "search.csv", sep=",")
    df = df.drop(columns=['SNR_Emission_15_micron',
                        'SNR_Emission_5_micron',
                        'SNR_Transmission_K_mag',
                        'Transit_Flag',
                        'Catalog_Name',
                        'Transit_Duration'
                        ])
   
   # calculate planet size from jupiter radia into earth radia
    r_Jupiter = 69_911
    r_Earth = 6_371
    df['Rp_km'] = df['Rp'] * r_Jupiter
    df['Rp_ERadia'] = round(df['Rp'] * ( r_Jupiter / r_Earth) , 2)

    # calculate distance from parsec into lightyears
    Parsec_In_Lightyears = 3.26156
    df['Distance_LJ'] = round(df['Distance'] * Parsec_In_Lightyears , 2)


    df = df.drop(columns=['Rp',
                        'Rp_km',
                        'Distance'])

    period_Earth = 365
    df['period_Earth'] = period_Earth

    return(df)