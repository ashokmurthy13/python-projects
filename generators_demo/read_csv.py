
# open and read csv file
# open() -- returns a generator object
# read() -- load entire file into memory
# if the file size is too large, then we may face memory error

def read_csv_file(file_path):
    file = open(file_path)
    result = file.read().split("\n")
    return result
# print(read_csv_file(file_path))


# to overcome the above issue, we can use Generators


def read_csv_generator(file_path):
    for row in open(file_path, "r"):
        yield row


def count_lines():
    file_path = "C:\\TechStack\\DataSets\\flights\\flights.csv"
    rows = read_csv_generator(file_path)
    count = 0
    for row in rows:
        count += 1
    return count


print(f"There are {count_lines()} lines in the file")
