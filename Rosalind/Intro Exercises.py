import this

from numpy import square
python3

"""
problem
Given: Two positive integers a and b, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.
"""




#hypotenuse calc c = sqrt{a^2 + b^2}
#to get sqrt would:
#from math import sqrt
#import this
#c = sqrt{a^2 + b^2}
#then square c, which is undoing the sqrt

#to get problem answer simply eliminate the sqrt
def hyp_sq(a,b):
    sum = a**2 + b**2
    return sum

print(hyp_sq(918,846))




