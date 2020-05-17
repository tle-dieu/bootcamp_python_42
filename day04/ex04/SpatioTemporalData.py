from FileLoader import FileLoader


class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def when(self, location):
        return list(self.df[self.df['City'] == location]['Year'].unique())

    def where(self, date):
        return list(self.df[self.df['Year'] == date]['City'].unique())


def main():
    loader = FileLoader()
    data = loader.load('day04/athlete_events.csv')
    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))


if __name__ == "__main__":
    main()