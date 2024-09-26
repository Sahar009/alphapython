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

vowel_sound = "aeiou"

user_input = input('enter an alphabet ')

if user_input.lower() in vowel_sound:
    print('alphabet is a vowel sound!')
else:
    print('alphabet is a consonant! ')


def alphabet_checker(a):
   vowel_sound = "aeiou"
   if(a in vowel_sound):
      print('alphabet is a vowel')


alphabet_checker('k')

user_number = int(input('INPUT A NUMBER '))

if(user_number% 3 ==0 and user_number%5 == 0):
    print(f'{user_number} is divisible by both 3 and 5')
elif user_number % 3 ==0:
    print(f"{user_number} divisible by only 3")
elif user_number % 5 ==0:
    print(f"{user_number} divisible by only 5")
else:
    print(f"{user_number} not divisible by both 5 and 3")


# write a Python program to check the type of triangle (equilateral, isosceles, or scalene) based on the lengths of its sides.
# • Equilateral: All sides are equal
# • Isosceles: Two sides are equal
# • Scalene: All sides are different

first_line = float(input('first line value'))
second_line = float(input('second line value'))
third_line = float(input('third line value'))

if first_line == second_line ==third_line:
    print('equalateral angles All sides are equal')
elif first_line == second_line or second_line == third_line or first_line == third_line:
    print(' Isosceles: Two sides are equal')
else:
    print('Scalene: All sides are different')
