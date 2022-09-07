
import random

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
attack_hit_or_miss = ["ATTACK HIT!", "ATTACK MISSED!"]
opponent_hp = 100
hercules_hp = 100
random_opponent = random.choice(opponent_characters)
random_opponent_name = random_opponent["Name"]

def user_hercules():
    global opponent_hp
    user_input = input("Select an attack for Hercules! Punch, Kick, Jumping Punch, Grapple: ")
    if user_input == "Punch" or "punch" or "Kick" or "kick" or "Jumping Punch" or "jumping punch" or "Grapple" or "grapple":
        hit_or_miss = random.choice(attack_hit_or_miss)
        if hit_or_miss == "ATTACK HIT!":
            opponent_hp -= 10
    else:
        print("Invalid input: Skip a turn")
    print(f"Hercules attacked with {user_input}. {hit_or_miss}")
    print(f"Opponent HP: {opponent_hp}") 

# user_hercules()

def cpu_opponent():
    global hercules_hp
    random_opponent_attack = random.choice(random_opponent["Attack Moves"])
    # print(random_opponent_attack)
    hit_or_miss = random.choice(attack_hit_or_miss)
    if hit_or_miss == "ATTACK HIT!":
        hercules_hp -= random_opponent["Attack Power"]
    print(f"{random_opponent_name} attacked with {random_opponent_attack}. {hit_or_miss}")
    print(f"Hercules HP: {hercules_hp}")

# cpu_opponent()

def attack():
    while opponent_hp and hercules_hp > 0:
        user_hercules()
        cpu_opponent()
    if hercules_hp <= 0:
        print("Hercules has been defeated. YOU LOSE!")
    elif opponent_hp <= 0:
        print(f"{random_opponent_name} has been defeated. YOU WIN!")

def RunGame():
    attack()

RunGame()

        


