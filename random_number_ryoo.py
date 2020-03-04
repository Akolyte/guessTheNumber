import random as rn

u = int(rn.randrange(1, 10, 1))

def randomguess():
	while True:
		i = int(input("Please try to guess a number!!!: "))
		if u < i:
			print("Sorry, you guessed wrong, the number is lower than your guess!")
		elif u > i: 
			print("Sorry, you guessed wrong, the number is greater than your guess!")
		else: 
			return str(u) + " Congratulations, you're correct!"

p = randomguess()
print(p)