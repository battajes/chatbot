import random

hi = {
    "intents": [
        {
            "subject": "Hi",
            "patterns": [
                "Hi",
                "How are you",
                "Hey",
                "Hi there",
                "Hello",
                "Good day",
                "yo",
                "Hi"
            ],
            "responses": [
                "Hello....."
            ]

        },
        {
            "subject": "Bye",
            "patterns": [
                "Bye",
                "See you later",
                "Goodbye",
                "Get lost",
                "Till next time",
                "bye"
            ],
            "responses": [
                "Goodbye."
            ]
        },

        {
            "subject": "grocary",
            "patterns": [
                "grocery",
            ],
            "responses": [
                "Adding to grocery."
            ]
        },



        {
            "subject": "search",
            "patterns": [
                "google",
                "search",
                "internet",
                "find",
                "Who is"
            ],
            "responses": [
                "Searching google: ",
            ]


        },

        {
            "subject": "thank",
            "patterns": [
                "Thanks",
                "Thank you"

            ],
            "responses": [
                "Happy to help!",
                "My pleasure!",
                "Your welcome"
            ]
        },
        {
            "subject": "options",
            "patterns": [
                "  help me?",
                " can  do?",
                " help you provide?",
                " you can be helpful?",
                " support is offered"
                "Help"
            ],
            "responses": [
                "I am a general purpose chatbot. My capabilities are : \n 1. I can chat with you. Try asking me for jokes. \n 2. I can add a new contact\n 3. I can search something in google for you \n 4. I can get you the weather for any country. \n 5. I can add to your grocery list\n 6. I can set a timer \n "
            ]
        },

        {
            "subject": "jokes",
            "patterns": [
                "Tell me a joke"
            ],
            "responses": [
                "Today I went to buy some camo pants but couldn’t find any.",
                "I was wondering why the frisbee kept getting bigger and bigger, but then it hit me.",
                "The easiest time to add insult to injury is when you’re signing someone’s cast.",
                "It takes a lot of balls to golf the way I do.",
                " Russian dolls are so full of themselves. ",
                "People who use selfie sticks really need to have a good, long look at themselves.  ",
                "How does a penguin build a house? Igloos it together",
            ]
        },
        {
            "subject": "Identity",
            "patterns": [
                "Who are you",
                "what are you"
            ],
            "responses": [
                "I am a chatbot"
            ]
        },
        {
            "subject": "whatsup",
            "patterns": [
                "Whats up",
                "How are you",
                "Sup"
            ],
            "responses": [
                "Im good how are you"
            ]
        },
        {
            "subject": "haha",
            "patterns": [
                "haha",
                "lol",
                "rofl",
                "lmao",
                "thats funny"
            ],
            "responses": [
                "Haha"
            ]
        },

        {
            "subject": "exclaim",
            "patterns": [
                "Awesome",
                "Great",
                "I know",
                "ok",
                "yeah"
            ],
            "responses": [
                "Yeah!"
            ]
        },

        {
            "subject": "weather",
            "patterns": [
                "temperature",
                "weather",
                "how hot is it",
                "humidity",
                "wind speed",
                "wind",
                "speed",
                "city",

            ],
            "responses": [
                "Giving atmospheric conditions...",
            ]
        },

        {
            "subject": "no",
            "patterns": [
                "no",
                "nope"
            ],
            "responses": [
                "ok"
            ]
        },

        {
            "subject": "contact",
            "patterns": [
                "Contact"
            ],
            "responses": [
                "Adding contact...",
            ]
        },
        {
            "subject": "alarm",
            "patterns": [
                "set a alarm",
                "alarm",
                "start a alarm"
            ],
            "responses": [
                "Setting the alarm...",
            ]

        },
        {"subject": "riddle",
         "patterns": [
             " riddle",
             " question",
             "Riddle",
             " riddle"
         ],
         "responses": [
             " What has to be broken before you can use it?... An egg!",
             "I’m tall when I’m young, and I’m short when I’m old. What am I? ...  A candle!",
             " What month of the year has 28 days??... All of them!",
             "What is full of holes but still holds water? ... A sponge!"
         ]
         },
        {
            "subject": "grocery",
            "patterns": [
                "Add to grocery list"
            ],
            "responses": [
                "Adding to a grocery list..."
            ]
        }
    ]
}


class Prompts:

    def __init__(self, subject, patterns, responses):
        self.subject = subject
        self.patterns = patterns
        self.responses = responses

    def get_responses(self):
        hi = random.randint(0, len(self.responses) - 1)
        return self.responses[hi]





