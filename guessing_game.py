# Online Python compiler (interpreter)
# Write and run Python online using this editor.
import random
secret = random.randint(1, 10)
print("Hello world")
name = input ("What is your name? ")
print("Hello", name)
age = input ("How old are you? ")
next_year = int(age)+1
print ("Next year, you will be", str(next_year)+"!")
while True:
  guess = int(input("Guess a number from 1 to 10: "))
  if guess == secret:
    print("You got it!")
    break
  elif guess < secret:
    print("Too low!")
  else:
    print("Too high!")
