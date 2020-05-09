import os.path


class CsvReader:
    def __init__(self, file, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = file
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []
        self.dataheader = []
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
        except FileNotFoundError:
            return None
        content = [[x.strip() for x in x.split(self.sep)]
                   for x in self.file.read().splitlines()]
        list_len = len(content[0])
        for i in content[1:]:
            if len(i) != list_len:
                return None
        if self.header:
            self.dataheader = content[0]
            content = content[1:]
        self.data = content[self.skip_top:len(content) - 1 - self.skip_bottom]
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.file.close()

    def getdata(self):
        return self.data

    def getheader(self):
        return self.dataheader


def main():
    print('############### GOOD ###############')
    with CsvReader(f'{os.path.dirname(__file__)}/good.csv', ',', True) as file:
        if file is None:
            print("File is corrupted")
        else:
            print(f"===== HEADER =====\n{file.getheader()}")
            print(f"===== DATA =====\n{file.getdata()}")
    print('############### BAD ###############')
    with CsvReader(f'{os.path.dirname(__file__)}/bad.csv') as file:
        if file is None:
            print("File is corrupted")
        else:
            print(f"===== HEADER =====\n{file.getheader()}")
            print(f"===== DATA =====\n{file.getdata()}")


if __name__ == "__main__":
    main()
