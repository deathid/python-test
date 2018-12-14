print(1>5)

num = 10
print("Guess what i think?")
answer = int(input("input a number"))

result = num < answer
print("too big?")
print(result)

result = num > answer
print("too small?")
print(result)

result = num == answer
print("equal?")
print(result)