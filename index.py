# # variables
# # container that stores a value

# firstName = 'john doe'
# print(firstName)
# firstName ='James'
# print(firstName)

# # cntrl ? for commenting
# # Text Type:	str
# # Numeric Types:	int, float, complex
# # Sequence Types:	list, tuple, range
# # Mapping Type:	dict
# # Set Types:	set, frozenset
# # Boolean Type:	bool
# # Binary Types:	bytes, bytearray, memoryview
# # None Type:	NoneType

# # string
# userName ="DEV SEYI"
# favoriteCar = 'Benz'
# word = "school's"
# # print(type(userName))
# # the function type is to check type of data


# # concatination 
# print("my name is " + userName + " and i drive a " + favoriteCar)

# # formatting
# print(f"my name is {userName} and i drive a {favoriteCar} and i like \n christmas")

# # declare 3 variables and fv food fav drink fav time of the day 
# # accessing index possition of a string
# surName ='akinwumi'


# print(surName[7])

# # total length of characters in a container 
# print(len(surName))

# print(surName.capitalize())
# print(surName.upper())
# # lower lower() converts to lowercase
# print(surName.casefold())
# print('ali'.center(10))

# # print('my name is {0}'.format('Taiye'))

# surName='  akinwumi  '
# editedSurName =surName.strip()
# # remove white spacing
# print(len(surName))
# print(len(editedSurName))


# print(surName[0:4])
# print(surName[4:])

# Assignments
# 1. A. Create a string variable greeting with the value "Hello, World!" and perform the following operations:
# B. Print the string in all uppercase.
# C. Print the string in all lowercase.
# D. Replace "World" with your name.

# 2. Given the string quote = "The only limit to our realization of tomorrow is our doubts of today.", perform the following:
# A. Find the index of the word "doubts."
# B. Count how many times the letter "o" appears.
# C. Check if the string starts with "The" and ends with "today."

# 3. Given the string text = "Data Science", write a program to:
# A. Count how many times the letter "a" appears in the string.
# B. Count the total number of characters in the string, excluding spaces.

# greeting ="Hello, World!"
# # print in uppercase
# print(greeting.upper())
# #print in lowerCase

# # replaced_greeting = greeting.replace('World','Stella')
# # print(replaced_greeting)

# text = "The only limit to our realization of tomorrow is our doubts of today."

# # print(text.find('doubts'))

# index_of_doubts = text.find('doubts') 

# print(f'the index of doubts is: {index_of_doubts}')
# # print("the index of doubts is " + index_of_doubts)


# # count
# print(text.count('o'))
# print(text.startswith("The"))
# print(text.endswith('today.'))


# word ="Data Science"
# print(word.count('a'))

# print(len(word))

# word_without_space =word.replace(' ','')
# print(len(word_without_space))



# numberOne = 34j

# # import random

# # print(random.randrange(1,10))


# # # operators 

# # numberOne  =5
# # numberTwo = 14

# # print( numberTwo // numberOne)
# # # modulus returns the remaining value of a division %
# # #exponention 

# # # print(2**3)


# # # assignment operators
# # newNumber = 8
# # # newNumber = newNumber + 3
# # newNumber%=3
# # print(newNumber)
# # #

# # # comparison operators
# # # returns a boolean when u compare

# # print(7 != 7)



# # Python Logical Operators
# #logical operators are used to combine conditional statement 

# # age = 16 and above and the score =70 admission 

# # and or not
# age = 10
# score= 10

# print(not(age > 16 or score > 70 ))
# print(not(True))


# # if(age > 16 and score> 70):
# #     print('you are eligible for admission ')

# print('name' is not'name')

# # is ==
# # is not !=

# #Python Identity Operators
# # Python Membership Operators
# # in and not in
# school ='university of bath'
# print('n' in school)

# # control structure
# # if statement
# # loops

# age = 18
# score = 69
# # aage is only 18

# if( age >= 18 and score >= 70 ):
#     print('you are eligible for admission!')
# elif((age >=18 and score < 70)):
#     print('go and learn mechanic')
# else:
#     print('you are not eligible')





# # userColor = input('enter your favorite color? ')

# # if(userColor == 'blue'):
# #     print('blue is a very cool color')
# # elif(userColor=='red'):
# #     print('red red red danger!')
# # elif(userColor =='pink'):
# #     print('pink is cool')
# # else:
# #     print('i dont have an idea of this color')


# # input the year you were born it should calculate the persons age and return the persons age with
# # statement based on a condition

# ageInput = input("i was born in:  ")
# userAge = 2024 - int(ageInput)
# # print(userAge)

# if(userAge >= 18 and userAge <= 65):
#     print(f"your age is {userAge} that means you are eligible")
# elif(userAge > 65):
#     print(f"your age is {userAge}you are too old")
# elif(userAge == 17):
#     print(f"your age is {userAge}you have one more year to be eligible")
# else:
#     print(f"your age is {userAge} that means you are not eligible")


# git video 1:45

# Check for Vowel or Consonant
# Write a Python program that checks if a given letter is a vowel or a consonant.
# • Vowels: 'a', 'e', 'i', 'o', 'u' (consider both uppercase and lowercase letters)
# Divisibility Check
# Write a Python program that checks if a number is divisible by 3 and 5.
# • If divisible by both, print "Divisible by both"
# • If divisible by only 3, print "Divisible by 3"
# • If divisible by only 5, print "Divisible by 5"
# • Otherwise, print "Not divisible by 3 or 5"
# write a Python program to check the type of triangle (equilateral, isosceles, or scalene) based on the lengths of its sides.
# • Equilateral: All sides are equal
# • Isosceles: Two sides are equal
# • Scalene: All sides are different

# vowel_sound = "aeiou"

# user_input = input('enter an alphabet ')

# if user_input.lower() in vowel_sound:
#     print('alphabet is a vowel sound!')
# else:
#     print('alphabet is a consonant! ')


# def alphabet_checker(a):
#    vowel_sound = "aeiou"
#    if(a in vowel_sound):
#       print('alphabet is a vowel')


# alphabet_checker('k')

# user_number = int(input('INPUT A NUMBER '))

# if(user_number% 3 ==0 and user_number%5 == 0):
#     print(f'{user_number} is divisible by both 3 and 5')
# elif user_number % 3 ==0:
#     print(f"{user_number} divisible by only 3")
# elif user_number % 5 ==0:
#     print(f"{user_number} divisible by only 5")
# else:
#     print(f"{user_number} not divisible by both 5 and 3")


# write a Python program to check the type of triangle (equilateral, isosceles, or scalene) based on the lengths of its sides.
# • Equilateral: All sides are equal
# • Isosceles: Two sides are equal
# • Scalene: All sides are different

# first_line = float(input('first line value'))
# second_line = float(input('second line value'))
# third_line = float(input('third line value'))

# if first_line == second_line ==third_line:
#     print('equalateral angles All sides are equal')
# elif first_line == second_line or second_line == third_line or first_line == third_line:
#     print(' Isosceles: Two sides are equal')
# else:
#     print('Scalene: All sides are different')



# print(range(1,20))
# iteration over a sequence 

# words = 'Adeoluwa'

# print(words)

# for items in words:
#     print(items) 

# names = ['Hosanna','Busayo','Iyke','Thoe','Stella','Seyi']

# for name in names:
#     print(name +'@alphapython.com')

# list_of_numbers =[1,2,3,4,5]

# for number in list_of_numbers:
#     print(number *7)


# range(1,100)

# for number in range(1500,3600):
#     if number % 5 == 0 and number % 7 ==0:
#         print(number)


# print numbers divisible by 5 and 7 btw 1500 - 3600

# iterate



# print(6%2)
# remaining value after division 

# details ='pepsicola'
# users =['ade','musa','hosanna','david','supo']
# # print(users)
# # print(details)
# for alphabets in details:
#     print(alphabets)

# for names in users:
#     if names == 'musa':
#         continue
#     print(names +'s')

# for user in users:
#     if user == 'hosanna':
#         break
#     print( user +" $ "+ str(500))

# float() str() int() list()


    

# dictionary list set tuple
# number= 25
# while(number <= 50):
#     number+=1
#     if number % 2 == 0:
#         if number == 32:
#             continue
#         if number == 42:
#             break
#         print(number)
    



    
    
    #assignment operator
# 25-50
# 30
#
# 1.Fibonacci Sequence: Write a program that 
# generates the Fibonacci sequence up to the nth term 
# (where n is a positive integer input by the user) using a loop.


# 2. Prime Numbers: Create a function that prints all prime numbers between 1 and 100 using a loop.
#  A prime number is a number that is only divisible by 1 and itself. 

# 3.Character Count: Create a program that counts the occurrences of each character in a given string
#  using a loop and prints the results in a dictionary format.

# 4. Reverse a String: Using a loop, write a program that takes a user-input string 
# and returns the string reversed (without using any built-in methods).
# 5. Count Vowels and Consonants: Create a program that takes a string as 
# input and counts the number of vowels and consonants using a loop.


# fibonacci sequence series of number that increments after the first 2 numbers 
# 0,1,1,2,3,5,8


# input('input a number')


# a function a block of code that runs whenever call it 

def greet():
    print('hello every one')

greet()


def greetz(name):
    print('hello '+ name)

greetz('iyke')
greetz('Hosanna')

# write a function that squares itself 

def squares(num):
    print(num**2)

squares(2)
squares(8)

# takes 2 numbers and add them together

def calculate(num1,num2):
    print(f'the addition of {num1} and {num2} is {num1 + num2}')

calculate(1,3)


# function to calc age

def ageCalc(year):
    return (2024 -year)

print(ageCalc(2015))


# convert dollar to naira

def nairaConvert(dollar):

     return(f'the current rate of {dollar} is {dollar * 1500} naira' )


print(nairaConvert(17))

number1 = 5
number2 =5

number3=number2 + number1


# function to check if an alphaet is a vowel or consonant

def alphabetChecker(alphabet):
    vowel = 'aeiouAEIOU'
    if(alphabet in vowel):
        print('alphabet is a vowel')
    else:
        print('alphabet is a consonant') 

alphabetChecker('z')









































 






