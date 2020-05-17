from FileLoader import FileLoader


def proportionBySport(df, year, sport, gender):
    df = df[(df.Year == year) & (df.Sex == gender)]
    df = df.drop_duplicates(['Sport', 'Name'])
    return df[df['Sport'] == sport].shape[0] / df.shape[0]


def main():
    loader = FileLoader()
    data = loader.load('./day04/athlete_events.csv')
    print(proportionBySport(data, 2004, 'Tennis', 'F'))


if __name__ == "__main__":
    main()
