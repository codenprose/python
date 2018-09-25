from fractions import Fraction

'''
Fractions
'''

f = Fraction(3, 4)

print(f) # 3/4
print(f + 1 + 1.5) # 3.25

'''
Complex Numbers

python uses (j) to represent imaginary numbers instead of (i) which is used in mathematical notation
'''

c = 2 + 3j
print(type(c)) # complex
print(c.real, c.imag) # 2 3
print(c.conjugate()) # (2-3j)

# Find the magnitude of a complex number
print(abs(c))

# The standard library has a cmath (complex math) module that provides more 
# functions for working with complex numbers

'''
Factors
'''

'''Checks to see if a is a factor of b'''
def is_factor(a, b):
  if b % a == 0:
    return True
  else:
    return False

print(is_factor(4, 1024)) # True