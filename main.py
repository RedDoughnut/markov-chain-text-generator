import random

d = dict()
start = ()

with open("frankenstein.txt", "r", encoding="utf-8-sig") as f:
    text = f.read()
    text = text.replace("\n", " ").lower().split()
    for i in range(len(text)-2):
        try:
            d[(text[i], text[i+1])].append(text[i+2])
        except KeyError:
            d[(text[i], text[i+1])] = [text[i+2]]
    r = random.randint(0, len(text)-100)
    start = (text[r], text[r+1])

last = start
out = f"{last[0]} {last[1]}"
WORDS = int(input("How many words do you want to generate? : "))
for i in range(WORDS-2):
    nextWord = random.choice(d[last])
    out += f" {nextWord}"
    last = (last[1], nextWord)
print(out)