import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

nr_letters = int(4)
nr_symbols = int(4)
nr_numbers = int(4)

let_length = len(letters)
sym_length = len(symbols)
num_length = len(numbers)

random_letters = random.sample(letters, nr_letters)
random_symbols = random.sample(symbols, nr_symbols)
random_numbers = random.sample(numbers, nr_numbers)

random_list = random_letters + random_symbols + random_numbers

shuffled_list = random.shuffle(random_list)

password = ""

for item in random_list:
    password += item

