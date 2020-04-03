from random import shuffle


def generator(text, sep=" ", option=None):
    if (not isinstance(text, str) or not isinstance(sep, str)
            or option not in ("shuffle", "unique", "ordered", None)):
        yield "ERROR"
    else:
        text = text.split(sep)
        if option == "shuffle":
            shuffle(text)
        elif option == "ordered":
            text.sort()
        elif option == "unique":
            uniq = set()
            text = [i for i in text if i not in uniq and (uniq.add(i) or True)]
        for i in text:
            yield i


def main():
    text = "Le Lorem Ipsum est simplement du faux texte. Le texte est faux"
    for word in generator(text, sep=" "):
        print(word)
    print()
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print()
    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print()
    for word in generator(text, sep=" ", option="unique"):
        print(word)


if __name__ == "__main__":
    main()
