from FileLoader import FileLoader


def youngestFellah(df, year):
    df = df[df['Year'] == year]
    return {'f': df[df['Sex'] == 'F']['Age'].min(),
            'm': df[df['Sex'] == 'M']['Age'].min()}


def main():
    loader = FileLoader()
    data = loader.load('day04/athlete_events.csv')
    print(youngestFellah(data, 2004))


if __name__ == "__main__":
    main()
