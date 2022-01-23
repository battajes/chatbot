from googlesearch import search


def google_search():
    q = input("What would you like to search: ")

    for char in search(q, tld="co.in", num=13, stop=13, pause=3):
        print(char)
