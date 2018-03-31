zoo_animals = ["pangolin", "cassowary", "sloth","halu" ];
# One animal is missing!

if len(zoo_animals) > 3:
  print "The first animal at the zoo is the " + zoo_animals[0]
  print "The second animal at the zoo is the " + zoo_animals[1]
  print "The third animal at the zoo is the " + zoo_animals[2]
  print "The fourth animal at the zoo is the " + zoo_animals[3]
  
  zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
# the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
zoo_animals[3]="cat"

suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("wewza")
suitcase.append("wewza")
suitcase.append("wewza")

list_length=len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

#Slices
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle = suitcase[2:4]

# The last two items (index four and five)
last =  suitcase[4:6]


animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:]

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index =animals.index("duck") # Use index() to find "duck"

# Your code here!

animals.insert(duck_index,"cobra")
print animals # Observe what prints after the insert operation

my_list = [1,9,3,8,5,7]

for number in my_list:
  
  print (number)
  # Your code here
  

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!

for num in start_list:
  square_list.append(num**2)




square_list.sort()
print square_list

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']

backpack.remove("dagger")

def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x

print my_function(range(3))


n = [3, 5, 7]

def total(numbers):
  result=0;
  for x in numbers:
    result+=x
  return result
  
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result=""
  for x in words:
    result+=x
  return result


print join_strings(n)


m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x,y):
  return x+y

print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]


n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results=[]
  for numbers in lists:
    for x in numbers:
      results.append(x)
  return results



print flatten(n)