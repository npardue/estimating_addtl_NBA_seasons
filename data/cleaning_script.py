def clean_season(folder, year):
    """Cleans dataframes scraped from basketball-reference.com, and overwrites them.

    Keyword arguments:

    folder = string, the folder within our 'data' folder where the dataframes are stored
    year = int, the season of the .csv file to be cleaned

    Ex.
    clean_bballref('regseason', 2000)
            - Would access the 1999-2000 regular season's .csv file, clean it, and then
            save a new copy of that file on top of the existing file.
    """
    # Importing packages
    import pandas as pd
    
    #Loading in dataframe
    df = pd.read_csv(f'/Users/npardue/Desktop/Capstone/data/raw/{folder}/{year}_stats.csv')
    
    # Adding a 'current year' column for organizational purposes.
    df['current_year'] = year


    # Some players were traded during the middle of a season, and as such will have 3+ rows.
    # The first will be a player's total stats for the season (df.Tm == TOT), and the following
    # will be stats for each of the teams the player recorded stats for, and subsequently drop them
    # from the dataframe. 
    df= df.drop(df.loc[df.Player.duplicated() == True].index, axis=0)

    # Dropping a leftover row that served as a header on the original document.
    df = df.drop(df.loc[df['Player'].isna()].index, axis=0)


    # Removing the '*' denoting any player that has made the Hall of Fame, as
    # not all .csv files to be used are formatted the same way.
    df.Player = df.Player.apply(lambda x: x.replace('*', ''))


    # Removing the unnecesary 'Unnamed: 0' column.
    df = df.drop(columns='Unnamed: 0')

    # Re-saving 
    df.to_csv(f'/Users/npardue/Desktop/Capstone/data/clean/{folder}/{year}_stats.csv')

    # So we have a way of tracking where we're at in the cleaning process
    print(f'Stats for {folder} {year} cleaned! {2019 - year} seasons to go.')