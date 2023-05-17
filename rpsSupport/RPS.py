import random

RPS_dict = {"rock": ["paper"],
            "paper": ["scissors"],
            "scissors": ["rock"],
            "lizard": [""],
            "spock": [""]}

RPS_convert = {1: "rock",
            2: "paper",
            3: "scissors",
            4: "lizard",
            5: "spock"}

def rps():
    while True:
        player = RPS_convert[int(input("1: Rock/n2: Paper/n3: Scissors"))]
        computer = RPS_convert[random.randint(1, 3)]
        if computer in RPS_dict[player]:
            return "Player LOSES! >;D"
        elif computer == player:
            continue
        elif computer not in RPS_dict[player]:
            return "Player WINS! :)"










