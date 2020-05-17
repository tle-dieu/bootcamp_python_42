from FileLoader import FileLoader


def howManyMedals(df, name):
    df = df[df['Name'] == name]
    medals = {}
    for year in sorted(df['Year'].unique()):
        tmp = df[df['Year'] == year]
        gold = len(tmp[tmp['Medal'] == 'Gold'])
        silver = len(tmp[tmp['Medal'] == 'Silver'])
        bronze = len(tmp[tmp['Medal'] == 'Bronze'])
        medals[year] = {'G': gold, 'S': silver, 'B': bronze}
    return medals


def main():
    loader = FileLoader()
    data = loader.load('day04/athlete_events.csv')
    print(howManyMedals(data, 'Kjetil Andr Aamodt'))


if __name__ == "__main__":
    main()
