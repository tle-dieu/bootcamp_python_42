from time import time


def ft_progress(lst):
    n = len(lst)
    start_time = time()
    eta = 0.01 * n
    for i in lst:
        elapsed_time = time() - start_time
        eta = elapsed_time / (i + 1) * (n - i - 1)
        percent = int((i + 1) / n * 100)
        align = int((i + 1) / n * 24)
        print(f"ETA: {eta:.2f}s [ {percent}%] "
              f"[{'':=>{align}}{'>':<{24 - align}}] {i + 1} / {n}"
              f"| elapsed time {elapsed_time:.2f}s", end="\r")
        yield i
