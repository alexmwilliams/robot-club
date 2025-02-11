import random

def random_gobbie_distributor():
    names = ["Webb", "Janke", "Pj", "Brunner"]
    random.shuffle(names)
    
    cunt_what_gets_gobbed = random.choice(names)

    print(f"Gobbie giver: Hunter Gobbie receiver: {cunt_what_gets_gobbed}")

if __name__ == "__main__":
    random_gobbie_distributor()