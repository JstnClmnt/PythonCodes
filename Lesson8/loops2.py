from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!

while guesses_left>0:
  guess=int(raw_input("Guess:"))
  if guess==random_number:
    print "You win!"
    break
  else:
   	guesses_left-=1
else:
	print "You lose."
	
	
	print "Counting..."

for i in range(20):
  print i
  
  
  hobbies = []

# Add your code below!
for i in range(3):
  hobby=raw_input("What is your hobby?:")
  hobbies.append(hobby)
  
  
print hobbies


thing = "spam!"

for c in thing:
  print c

word = "eggs!"

# Your code here!
for c in word:
  print c
  
  
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
  if char=="A" or char=="a":
    print "X",
  else:
    print char,




#Don't delete this print statement!
print

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Your code here!
  print key,d[key]
  
'''
Iterating over two lists at once, can be greater than 2 lists
'''
  
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
  if(a>b):
    print a
  else:
    print b
	
	
	
