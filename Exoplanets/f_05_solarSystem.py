def f_solarSystem(df):

    dict_Earth = {'Planet_Name': 'Earth',
            'Mp': '',
            'Tday': '',
            'Teq': 286.9,
            'log10g_p': '',
            'Period': 365,
            'K_mag': '',
            'Teff': '',
            'Rp_ERadia': 1.0,
            'Distance_LJ': 1,
            'period_Earth': 365
        }

    dict_Mercury = {'Planet_Name': 'Mercury',
            'Mp': '',
            'Tday': '',
            'Teq': 750,
            'log10g_p': '',
            'Period': 87.9691,
            'K_mag': '',
            'Teff': '',
            'Rp_ERadia': 0.3829,
            'Distance_LJ': 1,
            'period_Earth': 365
        }

    dict_Mars = {'Planet_Name': 'Mars',
            'Mp': '',
            'Tday': '',
            'Teq': 260,
            'log10g_p': '',
            'Period': 686.980,
            'K_mag': '',
            'Teff': '',
            'Rp_ERadia': 0.533,
            'Distance_LJ': 1,
            'period_Earth': 365
        }

    dict_Venus = {'Planet_Name': 'Venus',
            'Mp': '',
            'Tday': '',
            'Teq': 737,
            'log10g_p': '',
            'Period': 224.701,
            'K_mag': '',
            'Teff': '',
            'Rp_ERadia': 0.9499,
            'Distance_LJ': 1,
            'period_Earth': 365
        }

    df = df.append(dict_Earth, ignore_index = True)
    df = df.append(dict_Mercury, ignore_index = True)
    df = df.append(dict_Mars, ignore_index = True)
    df = df.append(dict_Venus, ignore_index = True)

    df.head(-1)

    return(df)