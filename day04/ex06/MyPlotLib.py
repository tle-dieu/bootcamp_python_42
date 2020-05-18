import matplotlib.pyplot as plt
import pandas as pd
import scipy
from FileLoader import FileLoader


class MyPlotLib:
    @staticmethod
    def histogram(df, features):
        df.drop_duplicates("Name").hist(column=features)
        plt.show()

    @staticmethod
    def density(df, features):
        df.drop_duplicates("Name")[features].plot.density()
        plt.show()

    @staticmethod
    def pair_plot(df, features):
        pd.plotting.scatter_matrix(df.drop_duplicates("Name")[features])
        plt.show()

    @staticmethod
    def box_plot(df, features):
        df.drop_duplicates("Name")[features].boxplot()
        plt.show()


def main():
    loader = FileLoader()
    data = loader.load("day04/resources/athlete_events.csv")
    mpl = MyPlotLib()
    mpl.histogram(data, ["Weight", "Height"])
    mpl.density(data, ["Weight", "Height"])
    mpl.pair_plot(data, ["Weight", "Height"])
    mpl.box_plot(data, ["Weight", "Height"])


if __name__ == "__main__":
    main()
