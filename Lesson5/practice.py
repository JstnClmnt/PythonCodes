names = ["Adam","Alex","Mariah","Martine","Columbus"]

for name in names:
  print name
  
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Add your code below!
for word in webster:
  print webster[word]
  
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for x in a:
  if x%2==0:
  	print x
	
# Write your function below!
def fizz_count(x):
  count=0
  
  
  for item in x:
    if item=="fizz":
      count=count+1
  return count
  
prices={"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3}

stock={"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15}

for x in prices:
  print x
  print "price: %s"%prices[x]
  print "stock: %s"%stock[x]
  
  
total=0; 
for x in prices:
	total=total+(prices[x]*stock[x])
print total

shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
  total=0
  
  for x in food:
    if stock[x]>0:
    	total=total+prices[x]
     	stock[x]=stock[x]-1
  return total