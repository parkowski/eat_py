https://www.w3resource.com/python-exercises/python-basic-exercises.php

1.
mult_lines = """
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
"""


Using_escapes = "Twinkle, twinkle, little star,\n\tHow I wonder what you are! \n\t Up above the world so high,\n\t Like a diamond in the sky. \n Twinkle, twinkle, little star, \n\t How I wonder what you are"

2. 
import sys
sys.version

3. 
import time
time.strftime("%m/%d/%YY %HH:%M")

4.
# Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504

A = 3.14*r*r

5.
# Write a program which accepts the user's first and last name and print them in reverse order with a space between them

fn = "Yong"
ln = "Park"
# get length of string
for i in range(len(fn), 0, -1):
	ren_fn = ren_fn + " " + fn[i-1]

print(ren_fn)

6.
