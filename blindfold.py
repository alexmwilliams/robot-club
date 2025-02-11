import random

def random_gobbie_distributor():
    names = ["Webb", "Janke", "Pj", "Brunner"]
    random.shuffle(names)
    
    receiver = random.choice(names)

    print(f"Gobbie giver: Hunter Gobbie receiver: {receiver}")

if __name__ == "__main__":
    random_gobbie_distributor()