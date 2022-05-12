from madlibs_samples import harry_potter, code, Zombie, hunger_games
import random

if __name__ == "__main__":
    m = random.choice([harry_potter, code, Zombie, hunger_games])
    m.madlib()
