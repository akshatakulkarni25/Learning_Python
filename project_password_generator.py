import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m',
         'n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M',
         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','*','.','@','#','$']

print("Welcome to Password Generator!!")
n_letters=int(input("How many letters would you like in your password?\n"))
n_numbers=int(input("How many numbers would you like in your password?\n"))
n_symbols=int(input("How many symbols would you like in your password?\n"))

# inorder i.e. letters numbers symbols like gjdsa45!!
# password=""

# for character in range(1,n_letters+1):
#     c=random.choice(letters)
#     password=password+c
    
# for num in range(1,n_numbers+1):
#     n=random.choice(numbers)
#     password=password+n
# for sym in range(1,n_symbols+1):
#     s=random.choice(symbols)
#     password=password+s
# print(password)

#random order
password_list=[]
for character in range(1,n_letters+1):
    c=random.choice(letters)
    password_list.append(c)
    
for num in range(1,n_numbers+1):
    n=random.choice(numbers)
    password_list.append(n)
for sym in range(1,n_symbols+1):
    s=random.choice(symbols)
    password_list.append(s)
# print(password_list)
random.shuffle(password_list)
password=""
for i in password_list:
    password=password+i
print(f"Your password is: {password}")
