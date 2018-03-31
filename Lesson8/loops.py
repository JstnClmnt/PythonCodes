loop_condition = True

while loop_condition:
  print "I am a loop"
  loop_condition=False;
  
num = 1

while num<=10:  # Fill in the condition
  # Print num squared
  # Increment num (make sure to do this!)
  print num*num
  num+=1

choice = raw_input('Enjoying the course? (y/n)')

while choice!="y" and choice!="n":  # Fill in the condition (before the colon)
  choice = raw_input("Sorry, I didn't catch that. Enter again: ")

  
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"
  
#If the loop exits as the result of a break, the else will not be executed.