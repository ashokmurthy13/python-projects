'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''


def statistics(file_name):
    line_count = 0
    word_count = 0
    with open(file_name, "r", encoding="UTF-8") as file:
        for line in file:
            line_count += 1
            words = line.split(' ')
            word_count += len(words)

    with open(file_name, "r", encoding="UTF-8") as file:
        data = file.read()

    result = {'lines': line_count,
              'words': word_count, 'characters': len(data)}
    return result


# more optimized way
def statistics_opt(file_name):
    with open(file_name, "r", encoding="UTF-8") as file:
        lines = file.readlines()
    return {"lines": len(lines),
            "words": sum(len(line.split(' ')) for line in lines),
            "characters": sum(len(line) for line in lines)}


def find_and_replace(file_name, search_for, replace_with):
    with open(file_name, "r+", encoding="UTF-8") as file:
        data = file.read()
        new_data = data.replace(search_for, replace_with)
        file.seek(0)
        file.write(new_data)
        file.truncate()


print(statistics("story.txt"))
print(statistics_opt("story.txt"))
find_and_replace("story.txt", "Alice", "Ashok")
