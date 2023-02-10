import csv


class SimpleIterator:
    def __init__(self, filename: str, classname: str):
        self.filename = filename
        self.limit = -1
        self.counter = -1
        self.classname = classname
        self.rows = list()
        with open(filename, mode="r", newline="\n", encoding = "utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[2] == classname:
                    self.rows.append(row[0])
                    self.limit += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.rows[self.counter]
        else:
            print("None")
            raise StopIteration


if __name__ == "__main__":
    s_iter1 = SimpleIterator("annotation.csv", "3")
    print(next(s_iter1))
    print(next(s_iter1))
    print(next(s_iter1))
    print(next(s_iter1))