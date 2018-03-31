# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Sloth']
print residents['Burmese Python']# Prints Puffin's room number

# Your code here!

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!

menu['Egg']=1.00
menu['Ham']=3.00
menu['Spam']=5.00


print "There are " + str(len(menu)) + " items on the menu."
print menu

# key - animal_name : value - location 
zoo_animals = {
  'Unicorn' : 'Cotton Candy House',
  'Sloth' : 'Rainforest Exhibit',
  'Bengal Tiger' : 'Jungle House',
  'Atlantic Puffin' : 'Arctic Exhibit',
  'Rockhopper Penguin' : 'Arctic Exhibit'
}
# A dictionary (or list) declaration may break across multiple lines
# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]
zoo_animals["Rockhopper Penguin"]="Cockroach"



print zoo_animals


inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory["pocket"]=["seashell","strange berry","lint"]
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
inventory["gold"]+=50

print inventory