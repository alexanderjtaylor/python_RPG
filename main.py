
import random

def user_hercules(list_hit, hero, opponent):
    user_input = input("Select an attack for Hercules! Punch, Kick, Jumping Punch, Grapple: ")
    for x in hero["Attack Moves"]:
        if user_input == "Punch" or user_input == "punch" or user_input == "Kick" or user_input == "kick" or user_input == "Jumping Punch" or user_input == "jumping punch" or user_input == "Grapple" or user_input == "grapple":
            hit_or_miss = random.choice(list_hit)
            if hit_or_miss == "ATTACK HIT!":
                opponent['Health'] -= 10
            print(f"Hercules attacked with {user_input}. {hit_or_miss}")
            print(f"Opponent HP: {opponent['Health']}")
            break
    else:
        print("Invalid input: Skip a turn")

def cpu_opponent(list_hit, opponent, hero):
    random_opponent_attack = random.choice(opponent["Attack Moves"])
    # print(random_opponent_attack)
    hit_or_miss = random.choice(list_hit)
    if hit_or_miss == "ATTACK HIT!":
        hero["Health"] -= opponent["Attack Power"]
    print(f"{opponent['Name']} attacked with {random_opponent_attack}. {hit_or_miss}")
    print(f"Hercules HP: {hero['Health']}")

def attack(hero, enemy):
    attack_hit_or_miss = ["ATTACK HIT!", "ATTACK MISSED!"]

    while enemy["Health"] > 0 and hero["Health"] > 0:
        user_hercules(attack_hit_or_miss, hero, enemy)
        cpu_opponent(attack_hit_or_miss, enemy, hero)
    if hero["Health"] <= 0:
        print("Hercules has been defeated. YOU LOSE!")
    elif enemy["Health"] <= 0:
        print(f"{enemy['Name']} has been defeated. YOU WIN!")

def RunGame():

    Hercules = {
        "Name" : "Hercules",
        "Health" : 100,
        "Attack Power" : 10,
        "Attack Moves" : ["Punch", "Kick", "Jumping Punch", "Grapple"]
    }

    Nemean_Lion = {
        "Name" : "Nemean Lion",
        "Health" : 100,
        "Attack Power" : 5,
        "Attack Moves" : ["Punch", "Kick", "Jumping Punch", "Grapple"]
    }

    Lernaean_Hydra = {
        "Name" : "Lernaean Hydra",
        "Health" : 100,
        "Attack Power" : 10,
        "Attack Moves" : ["Punch", "Kick", "Jumping Punch", "Grapple"]
    }

    Cerberus = {
        "Name" : "Cerberus",
        "Health" : 100,
        "Attack Power" : 15,
        "Attack Moves" : ["Punch", "Kick", "Jumping Punch", "Grapple"]
    }

    opponent_characters = [Nemean_Lion, Lernaean_Hydra, Cerberus]
    random_opponent = random.choice(opponent_characters)
    
    attack(Hercules, random_opponent)

RunGame()
