# # 1.Fibonacci Sequence: Write a program that 
# # generates the Fibonacci sequence up to the nth term 
# # (where n is a positive integer input by the user) using a loop.


# # 2. Prime Numbers: Create a function that prints all prime numbers between 1 and 100 using a loop.
# #  A prime number is a number that is only divisible by 1 and itself. 

# # 3.Character Count: Create a program that counts the occurrences of each character in a given string
# #  using a loop and prints the results in a dictionary format.

# # 4. Reverse a String: Using a loop, write a program that takes a user-input string 
# # and returns the string reversed (without using any built-in methods).
# # 5. Count Vowels and Consonants: Create a program that takes a string as 
# # input and counts the number of vowels and consonants using a loop.


# # fibonacci sequence series of number that increments after the first 2 numbers 
# 0,1,1,2,3,5,8


# # number = int(input('input a number'))




# # fibonacci_seq=[0,1] 
# # for i in range(2, number):
# #     num =fibonacci_seq[i-1] + fibonacci_seq[i-2]
# #     fibonacci_seq.append(num)
# #     print(fibonacci_seq)

# # print(range(1,10))


# # print(range(1,10))
# # for number in range(1,10):
# #     print(number)



# # for num in range(2,101):
# #     prime=True
# #     for i in range(2,int(num**0.5)+1):
# #         if num % i == 0:
# #             prime=False
# #             break
# #         if prime:
# #             print(num, end=" ")


# for num in range(2, 101):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")

# # print("Prime numbers between 1 and 100 are:")
# # print_prime_numbers()



# # input_string = input('enter ')
# # vowels = "aeiouAEIOU"
# # v_count = 0
# # c_count = 0
# # for char in input_string:
# #     if char.isalpha():
# #         if char in vowels:
# #             v_count += 1
# #         else:
# #             c_count += 1
# # print(v_count, c_count) 



# # count_dict = {}
# # for char in input_string:
# #     if char in count_dict:
# #         count_dict[char] += 1
# #     else:
# #         count_dict[char] = 1
# # print(count_dict)

# def character_count(input_string):
#     count_dict = {}
#     for char in input_string:
#         if char in count_dict:
#             count_dict[char] += 1
#         else:
#             count_dict[char] = 1
#     return count_dict

# input_string = input("Enter a string: ")
# print(f"Character count: {character_count(input_string)}")


# # 1.Fibonacci Sequence: Write a program that 
# # generates the Fibonacci sequence up to the nth term 
# # (where n is a positive integer input by the user) using a loop.


# # 2. Prime Numbers: Create a function that prints all prime numbers between 1 and 100 using a loop.
# #  A prime number is a number that is only divisible by 1 and itself. 

# # 3.Character Count: Create a program that counts the occurrences of each character in a given string
# #  using a loop and prints the results in a dictionary format.

# # 4. Reverse a String: Using a loop, write a program that takes a user-input string 
# # and returns the string reversed (without using any built-in methods).
# # 5. Count Vowels and Consonants: Create a program that takes a string as 

0,1,1,2,3,5,8,13,21,34


# print(range(1,10))

# for item in range(11):
#     print(item)



# for num in range(2,inputSequence):
#     sequence = [0,1]
#     nextNumber = sequence[num -1] + sequence[num -2]
#     print(nextNumber)
# inputSequence = int(input('input a squence'))
# num1,num2 = 0,1
# sequence = []

# for num in range(inputSequence):
#     sequence.append(num1)
#     num1,num2 = num2,num1+num2
# print(sequence)



for num in range(1,101):
    prime = True
    for newnumber in range(2, int(num **0.5)+1 ):
        if num % newnumber == 0:
            prime = False
            break
        
    if(prime):
        print(num)


# 'aade'

# {'name':'ade'}


# countedAlphabets = {}
# for alphabets in inputString:
#     countedAlphabets[alphabets] = countedAlphabets.get(alphabets,0)+ 1
# print(countedAlphabets)

# from collections import Counter

# text = 'school'
# # countAlpha = Counter(inputString)

# print(Counter(text))


# 'ayo'
# inputString = input('input a text')

# ayo
def ReverseString(inputString):
    reversedAphabet = ''
    for alphabets in inputString:
        reversedAphabet = alphabets + reversedAphabet
    print(reversedAphabet)


ReverseString('tomato')



# num3= 5
# num3+=3

# string = 'world'
# newString = string[::-1]
# print(newString)



# inputstringz = input('write a text')
# vowels = 'aeiouAEIOU'

# vowelSound =0
# consonatSound =0

# for alphabets in inputstringz:
#     if alphabets:
#         if alphabets in vowels:
#             vowelSound += 1
#         else:
#             consonatSound+=1
# print(f' th number of vowel sound is {vowelSound} and num of consonan sound is {consonatSound}')


# def counter(inputstringz):
#     vowelSound =''
#     consonatSound =''

#     for alphabets in inputstringz:
#         if alphabets:
#             if alphabets in vowels:
#                 vowelSound 
#             else:
#                 consonatSound
#     print(f' th number of vowel sound is {vowelSound} and num of consonan sound is {consonatSound}')

# counter('')



# pi r 2

import math

print(math.pi)

def radiusOfCircle(radius):
    return(
       math.pi * radius **2 
    )

print(radiusOfCircle(10))


# def radiusOfCircle(radius):
#     return (math.pi * radius **2)

# print(radiusOfCircle(4))



# lambda function is aka Anonymous

# def addz(num1, num2):
#     return num1+ num2


# print(addz(13,5))

addition = lambda num1,num2: num1+num2
print(addition(5,4))


def calc(num):
    return lambda a : a * num

newFunction =calc(4)
print(newFunction(4))


def func(num):
    return lambda num2: num2 * num
answer = func(4)
# answer = func(4)
# print(answer(3))

# nefunction2 = lambda a, b : a * b
# print(nefunction2(3,3))

# def newfunction(a,b):
#     return a * b

# print(newfunction(4,5))

def Calculator(operator):
    if operator =='add':
        return lambda a,b: a+b
    elif operator =='subtract':
        return lambda a,b: a-b
    elif operator =='divide':
        return lambda a,b : a /b
    else:
        return lambda a,b: "unsupported operation"
    
addition=Calculator('mmultiply')
print(addition(5,3))

subtract = Calculator('subtract')
print(subtract(7,3))



# []-list
# ()-tuple
# {}-set
# {}-dictionary

myList =['amala','Spirit','Spirit',23,29.0,True,[],{}]
myTuple=('amala','Spirit',23,29.0,True,[],{})
mySet = {'car','house',45,'house'}
myDictionary ={"name":'Hosanna', "age":12,'is_online':False,'address':''}
print(myDictionary)


print(myList)
print(mySet)


print(type(mySet))


# a list is ordered changeable, and allows duplicates
listOfAnimals=['dog','cat','Giraff','Rabbit']
list_convert = [item.lower() for item in listOfAnimals]
list_convert.sort()
print(list_convert)

listOfAnimals.sort()
print(listOfAnimals)



# print(len(listOfAnimals))
# print(listOfAnimals[1:3])
# listOfAnimals[0:3] =['goat','goat','goat']

# listOfAnimals.append('lion')
# print(listOfAnimals)
# listOfAnimals.insert(1,'lion')
# print(listOfAnimals)
# listOfAnimals.remove('Rabbit')

# listOfAnimals.pop(1)

# for names in listOfAnimals:
#     print(names)





