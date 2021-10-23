import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

url = "https://icanhazdadjoke.com/search"

# set the banner and color of the banner
header = figlet_format("DAD 3000!")
header = colored(header, color="blue")
print(header)
print("Enter 'q' to quit any time.")

# send request with the keyword as parameters and with headers


def get_response():
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": keyword})
    return response.json()

# print the actual joke


def print_joke():
    count = get_response()["total_jokes"]
    res = get_response()["results"]

    if count == 0:
        print(
            f"Sorry I don't have any jokes about {keyword}. Please try again.")
    elif count == 1:
        print(f"Ther is only one joke about {keyword}. Here's the one:")
        print(res[0]["joke"])
    else:
        print(f"I have got {count} jokes about {keyword}. Here's one:")
        print(choice(res)["joke"])


while True:
    # get the input from the user
    keyword = input("Let me tell you a joke! Give me a topic: ")

    if keyword == 'q':
        break
    else:
        print_joke()
