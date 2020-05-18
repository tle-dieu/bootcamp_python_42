from FileLoader import FileLoader
from math import sqrt
import matplotlib.pyplot as plt

class Komparator:
    def __init__(self, df):
        self.df = df.drop_duplicates("Name")
    
    def compare_box_plots(self, categorical_var, numerical_var):
        groups = self.df.groupby(categorical_var)
        if isinstance(numerical_var, str):
            numerical_var = [numerical_var]
        for i in numerical_var:
            fig = plt.figure()
            size = sqrt(len(groups.groups.keys()))
            x = size + (size % 1 != 0)
            y = size + (size % 1 >= 0.5)
            num = 1
            for group in groups.groups.keys():
                ax = fig.add_subplot(x, y, num)
                groups.get_group(group)[i].plot.box()
                ax.set_title(group)
                num += 1
            plt.tight_layout()
            plt.show()

    def density(self, categorical_var, numerical_var):
        groups = self.df.groupby(categorical_var)
        for i in numerical_var:
            for group in groups.groups.keys():
                groups.get_group(group)[i].plot.density(label=group)
            plt.title(i)
            plt.tight_layout()
            plt.legend()
            plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        groups = self.df.groupby(categorical_var)
        if isinstance(numerical_var, str):
            numerical_var = [numerical_var]
        for i in numerical_var:
            for group in groups.groups.keys():
                groups.get_group(group)[i].hist(label=group, alpha=0.75)
            plt.title(i)
            plt.tight_layout()
            plt.legend()
            plt.show()
    

def main():
    loader = FileLoader()
    data = loader.load("day04/resources/athlete_events.csv")
    komp = Komparator(data)
    komp.density("Sex", ["Weight", "Height"])
    komp.compare_histograms("Sex", ["Weight", "Height"])
    komp.compare_box_plots("Sex", ["Weight", "Height"])


if __name__ == "__main__":
    main()
