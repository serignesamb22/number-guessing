# this is the import of the random module.
import random

# this is the print function.
print('welcome to the number Guessing Game') 
print('pick a random number between 1 to 20')



# this assign a value to the variable
number = random.randint(1,20)

# this is the while loop. 
maxnumber=8
while maxnumber > 0:
  maxnumber=maxnumber-1
  # input ask for guess
  guess=int(input("select your random number:"))
  # if while is true then print guess is correct
  if (guess == number):
    print('you win!')
    break; 
  elif(guess < number): 
    print('you have ', maxnumber , 'gusses left')
    print('Too low')
  else:
    print('you have ', maxnumber , 'gusses left')
    print('Too high') 
    
  
    
  






