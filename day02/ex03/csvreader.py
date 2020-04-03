class CsvReader:
    def __init__(self, file, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.file = open(file, 'r')
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []

    def __enter__(self):
        content = self.file.read()[self.skip_top:]
        if self.skip_top > 0:
            content = content[self.skip_top:]
        if self.skip_bottom > 0:
            content = content[:-self.skip_bottom]

    def __exit__(self, exception_type, exception_value, traceback):
        self.file.close()

    def getdata(self):
        return self.data[1:] if self.header and self.data else self.data

    def getheader(self):
        return self.data[1] if self.header and self.data else None


def main():
    with CsvReader('test.csv') as file:
        if file is None:
            print("File is corrupted")
        else:
            data = file.getdata()
            header = file.getheader()
            print(data)
            print(header)


if __name__ == "__main__":
    main()
