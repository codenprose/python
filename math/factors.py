'''
Find factors of a an integer
'''

def factors(x):
  for i in range(1, x+1):
    if x % i == 0:
      print(i)


if __name__ == "__main__":
  
  x = input('Enter a number: ')
  x = float(x)

  if x > 0 and x.is_integer():
    factors(int(x))
  else:
    print('Please enter a positive integer')