import numpy as np


class NumPyCreator:
    @staticmethod
    def from_list(lst, dtype=None):
        return np.array(lst, dtype)

    @staticmethod
    def from_tuple(tlp, dtype=None):
        return np.array(tlp, dtype)

    @staticmethod
    def from_iterable(itr, dtype=None):
        return np.array(itr, dtype)

    @staticmethod
    def from_shape(shape, value=0, dtype=None):
        return np.full(shape, value, dtype)

    @staticmethod
    def random(shape):
        return np.random.random_sample(shape)

    @staticmethod
    def identity(n, dtype=None):
        return np.identity(n, dtype)


def main():
    npc = NumPyCreator()
    print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
    print(npc.from_tuple(("a", "b", "c")))
    print(npc.from_iterable(range(5)))
    print(npc.from_shape((3, 5)))
    print(npc.random((3, 5)))
    print(npc.identity(4))


if __name__ == "__main__":
    main()
