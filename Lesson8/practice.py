'''def is_int(x):
  if type(x)==int or (x - round(x))==0 :
    return True
  else:
    return False
  
print is_int(7.0)   # True    
print is_int(7.5)   # False    
print is_int(-1)    # True
'''

n=1234;
sum=0
while n>0:
	sum+=n%10
	n=n//10
print sum

def factorial(n):
  fact=1;
  while n>0:
    fact*=n
    n-=1
  return fact
  
  
def is_prime(x):
  if x<2:
    	return False
  for n in range(2,x):
    if(x%n==0):
      return False
  return True
  
  
def reverse(text):
  string=""
  for i in text:
    string=i+string
  return string
  
def anti_vowel(text):
  for i in text:
    if i in "aeiouAEIOU":
      text = text.replace(i, '')
  return text

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  sum=0;
  for i in word:
    sum+=score[i.lower()]
  return sum
  
  
def censor (text, word):
	temp = text
	if word in temp:
		temp = temp.replace(word, "*" * len(word))
	return temp
	
	
def count(sequence,item):
  increment=0
  for i in sequence:
    if i==item:
      increment+=1
  return increment
        
def purify(numbers):
  even=[]
  for i in numbers:
    if i%2==0:
      even.append(i)
  return even
  
def product(numbers):
  product=1
  for i in numbers:
    product*=i
  return product
def remove_duplicates(numbers):
  result=[]
  for i in numbers:
    if i not in result:
      result.append(i)
  return result
  
def median(numbers):
  result=sorted(numbers)
  length=len(result)
  if length%2==0:
    avg=0.0
    num1=result[length/2]
    num2=result[(length/2)-1]
    avg=num1+num2
    return avg/2.0
  else:
    return result[length/2]