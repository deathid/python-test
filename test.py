from random import randint

num = randint(1,100)
print(num)
print(num > 20)
print("Guess what i think?")
answer = int(input("input a number\n"))

while answer != num:
    if num < answer:
        print(answer,"too big")

    if num > answer:
        print("too small")

    answer = int(input("input a number"))

if num == answer:
    print("equal")


