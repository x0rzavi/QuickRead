import random

tips_list = ['Looking for a no BS blogging platform? checkout https://bearblog.dev/',
            'Might wanna checkout HackerNews for blogs?',
            "Wish you a great day!"]

def get_tips():
    return(random.choice(tips_list))