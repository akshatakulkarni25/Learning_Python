# Loops in Python
# for loop : Used for sequential traversal
# for i in range(0,11):
#     print(i)


# while loop
# while is used to execute a block of stmts repeatedly until a condition is satisfied
# python uses indentation as a method to group statements for a block

# count = 0
# while (count < 3):
#     count = count + 1
#     print("Hello Geek")

# Else can also be used with while and it is executed when the while condition is false. 
#the else block is not executed if we break out of while loop or if an exception is raised
# while(condition):
#   stmts
# else:
#   stmts


# Loop control statements
# 1. Continue: brings control to the beginning of the loop
# for i in range(0,11):            prints only odd numbers
#   if(i%2 == 0):
#       continue
#   else:
#       print(i)

# 2. break : brings control out of the loop
# for i in range(2,11):            prints all prime numbers            
#   for j in range(2,i):
#       if(i%j==0):
#           break
#    else:
#        print(i)

# 3. pass : it is used to write empty loops
#   for i in range(0,101):
#       pass

# For loop behind the scene uses an iterator and loops the iterable objet using next() function inside a while True block
# num_iterator = iter(numbers)
# while True:
#     try:
#         # get the next item
#         number = next(num_iterator)
#     except StopIteration:
#         break

fruits= ['Apple','Banana','Chikoo','Dragonfruit']
for fruit in fruits:
    print(fruit)

#range function
#prints numbers from 1 to 100 (101 is not included)(for loop in python is similar to for(i=1;i<101;i++) print(i);)
for i in range(1,101):   
    print(i)

#range function case2
#range(start,end,step)
for i in range(2,101,2):
    print(i)

# FizzBuzz Interview Question
# print Fizz if number is divisible by 3. print Buzz if number if divisible by 5 
# and print FizzBuzz if number is divisible by both 3 and 5

for number in range(1,101):
    if(number%3 == 0 and number%5 == 0):
        print("FizzBuzz")
    elif (number%3 == 0):
        print("Fizz")
    elif (number%5 == 0):
        print("Buzz")
    else:
        print(number)

for i in range(2,11):            
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)