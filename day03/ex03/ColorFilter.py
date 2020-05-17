import numpy as np
from ImageProcessor import ImageProcessor


class ColorFilter:
    @staticmethod
    def invert(array):
        return 1 - array

    @staticmethod
    def to_blue(array):
        blue = np.zeros(np.shape(array))
        blue[:, :, 2] = array[:, :, 2]
        return blue

    @staticmethod
    def to_green(array):
        return array * [0, 1, 0]

    def to_red(self, array):
        return array - self.to_blue(array) - self.to_green(array)

    @staticmethod
    def to_celluloid(array, thresholds=4):
        new = np.array(array)
        copy = np.array(array)
        for val in np.linspace(0, 1, thresholds, False)[::-1]:
            new[val <= copy] = val
            copy[val <= copy] = -1
        return new

    @staticmethod
    def to_grayscale(array, filt='weighted'):
        if filt in ('m', 'mean'):
            return np.sum(array, -1) / 3
        if filt in ('w', 'weighted'):
            return np.sum(array * [0.299, 0.587, 0.114], -1)


def main():
    imp = ImageProcessor()
    arr = imp.load("day03/ex03/test.png")
    cf = ColorFilter()
    imp.display(arr)
    # imp.display(cf.invert(arr))
    # imp.display(cf.to_blue(arr))
    # imp.display(cf.to_green(arr))
    # imp.display(cf.to_red(arr))
    # imp.display(cf.to_celluloid(arr, 4))
    imp.display(cf.to_grayscale(arr, 'm'))
    imp.display(cf.to_grayscale(arr, 'weighted'))



if __name__ == "__main__":
    main()
