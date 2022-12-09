import random

def random_string():
    random_list = [
        "Não entendi, poderia repetir, por favor?",
    ]
    
    list_count = len(random_list)
    random_item = random.randrange(list_count)
    
    return random_list[random_item]