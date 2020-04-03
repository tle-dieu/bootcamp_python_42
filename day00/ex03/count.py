import string


def text_analyzer(*args):
    """\nThis function counts the number of upper characters,
lower characters, punctuation and spaces in a given text."""

    if len(args) > 1:
        exit("ERROR")
    text = args[0] if len(args) else input('What is the text to analyse?\n')
    print("The text contains %d characters:" % len(text))
    print("\n- %d upper letters\n" % sum(1 for c in text if c.isupper()))
    print("\n- %d lower letters\n" % sum(1 for c in text if c.islower()))
    print("\n- %d punctuation marks\n" %
          sum(1 for c in text if c in string.punctuation))
    print("\n- %d spaces" % sum(1 for c in text if c.isspace()))
