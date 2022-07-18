import os
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

"""
Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d 
(with space in between), inclusively. In other words, we should include 
elements s[b] and s[d] in our slice.
"""
#slicing s[a:b] would not include b


def slice_it(s, a, b, c, d):
    return s[a:b+1] + ' ' + s[c:d+1]


s = "vXjgMZb5XWG94FshkE3O5US71WDlsuHkQbTjYgcvnzhyTDTpNnX6fmo2llm4kPBhcOE2uazr99QJMergusUP0mMZtHapesSDaCdpaBgtg4cyC7rkX9PZ8QzYL8WjpH27h4ZVJeH1JffTdjlPYt0QmtnljbKIssFcaudatusPF."

slice_it(s, 76, 81, 159, 166)

s[76:81]


"""
Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.
"""


def sum_odd_integers(a, b):
    s = 0
    for i in range(a, b+1):
        if i % 2 != 0:
            s = s + i
    return s


sum_odd_integers(4703, 9491)

"""
Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. 
Assume 1-based numbering of lines.
"""

#why is this returning the odd lines?
def even_lines(file):
    import os
    with open(os.path.expanduser(file)) as f:
        lines = f.readlines()
    even_lines = ''
    for i in range(len(lines)):
        if i % 2 == 0:
            even_lines += ''+lines[i]
    even_lines.split('\n')
    return even_lines


b = "~/Downloads/rosalind_ini5 (1).txt"


b_file = even_lines(b)

f = open(os.path.expanduser('~/Desktop/even_lines2.txt'), 'x')
f.write(b_file)
f.close()

