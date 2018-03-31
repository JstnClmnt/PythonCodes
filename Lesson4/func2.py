def one_good_turn(n):
    return n + 1
    
def deserves_another(n):
    return one_good_turn(n) + 2 
	
def cube(number):
    return number**3
    
def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False