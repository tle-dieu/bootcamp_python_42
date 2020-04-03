import sys


def operations(a, b):
    return(a + b, a - b, a * b, a / b if b else None, a % b if b else None)


try:
    assert len(sys.argv) <= 3
    res = operations(int(sys.argv[1]), int(sys.argv[2]))
    print('{:13}{}\n{:13}{}\n{:13}{}\n{:13}{}\n{:13}{}'.format(
          'Sum:', res[0],
          'Difference:', res[1],
          'Product:', res[2],
          'Quotient:', 'ERROR (div by zero)' if res[3] is None else res[3],
          'Remainder:', 'ERROR (modulo by zero)' if res[4] is None else res[4]
          ))
except Exception:
    try:
        raise
    except ValueError:
        print('InputError: only numbers\n')
    except IndexError:
        pass
    except AssertionError:
        print('InputError: too many arguments\n')
    finally:
        print("Usage: python operations.py <number1> <number2>\n"
              "Example:\n\tpython operations.py 10 3")
