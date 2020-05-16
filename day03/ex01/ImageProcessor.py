from matplotlib import pyplot as plt


class ImageProcessor:
    @staticmethod
    def load(path):
        return plt.imread(path, 'png')

    @staticmethod
    def display(array):
        plt.imshow(array)
        plt.show()


def main():
    imp = ImageProcessor()
    img = "day03/ex01/42AI.png"
    arr = imp.load(img)
    imp.display(arr)


if __name__ == "__main__":
    main()
