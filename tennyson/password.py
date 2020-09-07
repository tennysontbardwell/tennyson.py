import os
from random import SystemRandom
import pkg_resources

def words():
    return pkg_resources.resource_string('tennyson', 'static/diceware.txt').decode('utf-8').splitlines()

def password():
    words_ = words()
    rnd = SystemRandom()
    return "-".join(rnd.choice(words_) for _  in range(5))
