import nltk
import timer, google, weather, AddContact
contacts = AddContact.Contact()
import prompts

from prompts import Prompts
list_greetings =     ["Hi",
                                  "How are you",
                                  "Hey",
                                  "Hi there",
                                  "Hello",
                                  "Good day",
                                  "yo",
                                  "Hi"]

all_prompts = []
a = True

for intent in prompts.hi["intents"]:
    patterns = []
    for char in intent["patterns"]:
        patterns += nltk.word_tokenize(char)
    hi = prompts.Prompts(intent["subject"], patterns, intent["responses"])
    all_prompts.append(hi)


def grocery():
    grocery_list = []
    while True:
        x = input("Will you like to add, show, remove, quit or start a new grocery list.")
        if x == "add":
            c = input("Enter the item you would like to add: ")
            grocery_list.append(c)
            print("Great your item has been added!")
        elif x == "show":
            print("Your grocer list: ")
            return grocery_list
        elif x == "remove":
            l = input("Enter the item you would like to remove: ")
            grocery_list.remove(l)
            print("Your item has been deleted!")
        elif x == "start a new grocery list":
            grocery_list.clear()
            print("Cheers to a fresh start!")
        elif x == "quit":
            print("Goodbye!")
            break


while a:
    print ("\n" )
    try :
        user_input = input("Hi, How can I help you? ")
        count = {}
        for char in list_greetings:
            if (user_input.lower == char.lower):
                print ("Hi, how can I help you?")


        for char in nltk.word_tokenize((user_input)):
            for prompt in all_prompts:
                for word in prompt.patterns:
                    if (word.lower() == char.lower()):
                        count[prompt] = count.get(prompt, 0) + 1
        print ((max(count, key=count.get)).get_responses())
        hi =  ((max(count, key=count.get)).subject)
        if (hi == "weather"):
            weather.get_weather()
        if (hi == "search"):
            google.google_search()
        if (hi == "contact") :
            contacts.options_menu()
        if (hi == "alarm"):
            timer.set_alarm()
        if (hi == "grocery"):
            grocery()

        if ((max(count, key=count.get).subject) == "Bye"):
            a = False
    except:
        print ("Invalid Entry: Please try again")





