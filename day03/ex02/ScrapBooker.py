import numpy as np


class ScrapBooker:
    @staticmethod
    def crop(array, dimensions, position=(0, 0)):
        end = position[0] + dimensions[0], position[1] + dimensions[1]
        if len(array) < end[0] or len(array[0]) < end[1]:
            raise 'Error: array too small'
        return array[position[0]:end[0], position[1]:end[1]]

    @staticmethod
    def thin(array, n, axis):
        axis = 1 - axis
        return np.delete(array, list(range(n - 1, array.shape[axis], n)), axis)

    @staticmethod
    def juxtapose(array, n, axis):
        if axis:
            return np.tile(array, n)
        return np.tile(array, (n, 1))

    def mosaic(self, array, dimensions):
        return self.juxtapose(self.juxtapose(array, dimensions[0], 0),
                              dimensions[1], 1)


def main():
    sb = ScrapBooker()
    arr = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', 'L'])
    arr = np.tile(arr, (11, 1))
    print(f"arr1:\n{arr}")
    print(f"arr2:\n{np.transpose(arr)}")
    print(f"arr1 thin:\n{sb.thin(arr, 3, 0)}")
    print(f"arr2 thin:\n{sb.thin(np.transpose(arr), 4, 1)}")
    print(f"arr1 juxtapose:\n{sb.juxtapose(arr, 3, 0)}")
    print(f"arr2 juxtapose:\n{sb.juxtapose(np.transpose(arr), 2, 1)}")
    print(f"arr1 mosaic:\n{sb.mosaic(arr, (3, 2))}")


if __name__ == "__main__":
    main()
