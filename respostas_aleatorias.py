import random

def random_string():
    random_list = [
        "nao etedir",
        "poderia repetir",
        "irineu, vc nao sabe nem eu"
    ]
    
    list_count = len(random_list)
    random_item = random.randrange(list_count)
    
    return random_list[random_item]