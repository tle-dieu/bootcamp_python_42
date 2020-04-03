def ft_filter(function_to_apply, list_of_inputs):
    return (i for i in list_of_inputs if function_to_apply(i))


def main():
    memes = [21, 23, "ad", 2, "fs", 1]
    print(list(ft_filter(lambda x: isinstance(x, int), memes)))
    print(list(filter(lambda x: isinstance(x, int), memes)))


if __name__ == "__main__":
    main()
