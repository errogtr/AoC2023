import re

with open("data") as f:
    text = f.read()


def sum_first_last(text: str) -> int:
    return sum(
        int(line[0] + line[-1]) for line in re.sub(r"[A-z]", "", text).split("\n")
    )


# PART 1
print(sum_first_last(text))

# PART 2
letters2digits = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "4",
    "five": "5e",
    "six": "6",
    "seven": "7n",
    "eight": "e8t",
    "nine": "n9e",
}


def replace_letters(text: str) -> str:
    for letters, digits in letters2digits.items():
        text = text.replace(letters, digits)
    return text


print(sum_first_last(replace_letters(text)))
