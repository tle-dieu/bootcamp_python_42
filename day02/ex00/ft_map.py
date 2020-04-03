def ft_map(function_to_apply, list_of_inputs):
    return (function_to_apply(i) for i in list_of_inputs)


def main():
    memes = ["It's over 9000 !", "All your base are belong to us."]
    print(list(ft_map(str.upper, memes)))
    print(list(map(str.upper, memes)))


if __name__ == "__main__":
    main()
