import time
from getpass import getuser


def log(func):
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        exec_time = time.time() - start
        exec_time = (f"{exec_time:.3f} s" if exec_time >= 1
                     else f"{exec_time * 1000:.3f} ms")
        with open("machine.log", "a") as file:
            file.write(f"({getuser()})Running: {func.__name__.capitalize():30}"
                       f"{'[ exec-time = ' + exec_time + ' ]'}\n")
        return res
    return inner
