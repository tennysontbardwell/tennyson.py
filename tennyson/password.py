import os
from random import SystemRandom
import pkg_resources
import functools

@functools.lru_cache()
def words():
    return pkg_resources.resource_string('tennyson', 'static/diceware.txt').decode('utf-8').splitlines()

def password():
    rnd = SystemRandom()
    return "-".join(rnd.choice(words()) for _  in range(5))

def for_display_passwords():
    rnd = SystemRandom()
    words_ = [rnd.choice(words()) for _ in range(5)]
    yield "-".join(words_[:5])
    yield " ".join(words_[:5])
    yield "-".join(words_[:4])
    yield ("-".join(words_[:4])) + "-A1"
