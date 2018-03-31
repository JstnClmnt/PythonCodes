def shut_down(s):
    if s=="yes":
        return "Shutting down"
    elif s=="no":
        return "Shutdown aborted"
    else:
        return "Sorry"
		
import math

print math.sqrt(13689)

def distance_from_zero(n):
#python can do this. cool
    if type(n)==int or type(n)==float:
        return abs(n)
    else:
        return "Nope"