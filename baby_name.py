import string
import random


def generator():
     nam_let1 = random.choice(string.ascii_lowercase)
     nam_let2 = random.choice(string.ascii_lowercase)
     nam_let3 = random.choice(string.ascii_lowercase)
     nam_let4 = random.choice(string.ascii_lowercase)
     nam_let5 = random.choice(string.ascii_lowercase)
     name = nam_let1 + nam_let2 + nam_let3 + nam_let4 + nam_let5

     return name

def gen():
    vowel = 'aeiou'
    consonant = 'bcdfghjklmnpqrstvwxyz'
    rand_letter = string.ascii_lowercase

    letter1 = input("Enter v for vowel c for consonant l for random letter: ")
    letter2 = input("Enter v for vowel c for consonant l for random letter: ")
    letter3 = input("Enter v for vowel c for consonant l for random letter: ")
    letter4 = input("Enter v for vowel c for consonant l for random letter: ")
    letter5 = input("Enter v for vowel c for consonant l for random letter: ")

    if letter1 == 'v':
        name_letter1 = random.choice(vowel)
    elif letter1 == 'c':
        name_letter1 = random.choice(consonant)
    else:
        name_letter1 = random.choice(rand_letter)

    if letter2 == 'v':
        name_letter2 = random.choice(vowel)
    elif letter2 == 'c':
        name_letter2 = random.choice(consonant)
    else:

        name_letter2 = random.choice(rand_letter)

    if letter3 == 'v':
        name_letter3 = random.choice(vowel)
    elif letter3 == 'c':
        name_letter3 = random.choice(consonant)
    else:
        name_letter3 = random.choice(rand_letter)

    if letter4 == 'v':
        name_letter4 = random.choice(vowel)
    elif letter4 == 'c':
        name_letter4 = random.choice(consonant)
    else:
        name_letter4 = random.choice(rand_letter)

    if letter5 == 'v':
        name_letter5 = random.choice(vowel)
    elif letter5 == 'c':
        name_letter5 = random.choice(consonant)
    else:
        name_letter5 = random.choice(rand_letter)

    name = name_letter1 + name_letter2 + name_letter3 + name_letter4 + name_letter5
    return name


def main():
    for i in range(20):
#       print(generator())
        print(gen())


if __name__ == '__main__':
    main()



