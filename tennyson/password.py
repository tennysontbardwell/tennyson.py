import os
from random import SystemRandom

def words():
    path = os.path.join(os.path.dirname(__file__), 'resources', 'diceware.txt')
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def password():
    words_ = words()
    rnd = SystemRandom()
    return "-".join(rnd.choice(words_) for _  in range(5))
