import math


class TinyStatistician:
    @staticmethod
    def mean(x):
        if not x:
            return None
        return float(sum(x) / len(x))

    @staticmethod
    def median(x):
        if not x:
            return None
        x.sort()
        index = len(x)
        if index % 2:
            return float(x[index // 2])
        return float((x[index // 2 - 1] + x[index // 2]) / 2)

    @staticmethod
    def quartile(x, percentile):
        if not x:
            return None
        x.sort()
        pc = percentile / 100
        index = pc * len(x)
        if index % 1:
            return float(x[int(index // 1)])
        return float((x[int(index) - 1] + x[int(index)]) / 2)

    def var(self, x):
        if not x:
            return None
        mean = self.mean(x)
        return sum([(n - mean) ** 2 for n in x]) / len(x)

    def std(self, x):
        return math.sqrt(self.var(x))


if __name__ == "__main__":
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    print(tstat.median(a))
    print(tstat.quartile(a, 25))
    print(tstat.quartile(a, 75))
    print(tstat.var(a))
    print(tstat.std(a))
