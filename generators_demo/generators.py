def week():
    weeks = ["Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday"]
    for day in weeks:
        try:
            yield day
        except:
            StopIteration


days = week()
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))


def yes_or_no():
    start = "yes"
    while True:
        yield start
        start = "no" if start == "yes" else "yes"


gen = yes_or_no()
print(next(gen))  # 'yes'
print(next(gen))  # 'no'
print(next(gen))  # 'yes'
print(next(gen))  # 'no'
