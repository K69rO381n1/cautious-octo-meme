import random

def generate_turn():
    return [str(random.randint(0,4)) for i in range(18)]
def generate_game_into_file():
    with open("botrix.txt","w") as f:
        for i in range(1000):
            f.write(" ".join(generate_turn())+"\n")
generate_game_into_file()