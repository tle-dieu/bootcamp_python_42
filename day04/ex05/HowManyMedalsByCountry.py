from FileLoader import FileLoader

def howManyMedalsByCountry(df, country):
    df = df[df['Team'] == country]
    medals = {}
    for year in sorted(df['Year'].unique()):
        tmp = df[df['Year'] == year]
        gold = len(tmp[tmp['Medal'] == 'Gold']['Event'].unique())
        silver = len(tmp[tmp['Medal'] == 'Silver']['Event'].unique())
        bronze = len(tmp[tmp['Medal'] == 'Bronze']['Event'].unique())
        medals[year] = {'G': gold, 'S': silver, 'B': bronze}
    return medals

def main():
    loader = FileLoader()
    data = loader.load('day04/athlete_events.csv')
    print(howManyMedalsByCountry(data, 'Finland'))

if __name__ == "__main__":
    main()
