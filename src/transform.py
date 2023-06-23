def identify_and_remove_duplicates(df):
    if df.duplicated().sum() > 0:
        # identify duplicated data
        print("Number of duplicated rows:", df.duplicated().sum())

        # drop duplicated data and only keep first appearance
        df_cleaned = df.drop_duplicates(keep='first')

        print("-" * 60)
        print("Shape of data before removing duplicated data", df.shape)
        print("Shape of data after removing duplicated data", df_cleaned.shape)
        print("-" * 60)

    else:
        print("No duplicated data found")
        df_cleaned = df

    return df_cleaned