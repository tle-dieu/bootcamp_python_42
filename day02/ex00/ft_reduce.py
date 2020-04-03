from functools import reduce


def ft_reduce(function_to_apply, list_of_inputs):
    try:
        acc = next(iter(list_of_inputs))
    except StopIteration:
        raise TypeError('reduce() of an empty sequence')
    for i in list_of_inputs:
        acc = function_to_apply(i, acc)
    return acc


def main():
    print(reduce(lambda a, b: a * b, [1, 2]))
    print(ft_reduce(lambda a, b: a * b, [1, 2]))


if __name__ == "__main__":
    main()
