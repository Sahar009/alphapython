# Assignments
# 1a.Create a List: Create a list of your five favorite movies. Print the list.
# 1b.Access Elements: Print the first and last movie from your list.
# 1c.Modify a List: Change the second movie in your list to a new favorite and print the updated list.
# 1d. Add a Movie: Append another movie to your list and print the updated list.
# 1e.Remove a Movie: Remove the fourth movie from your list and print the updated list.


# 2a. Slice the List: Create a list of at least 10 integers. Print the first three numbers, the last three numbers, and the middle five numbers.
# 2b. Negative Indexing: Use negative indexing to print the last two numbers in your list.


# 3a Create a Nested List: Create a list that contains three other lists. Each of the inner lists should have three integers. Print the nested list.
# Access Nested Elements: Retrieve and print the second element of the first inner list.

# extra:
# Create a Tuple: Create a tuple containing the names of five animals. Print the tuple.
# Access Elements: Print the first and last animal from your tuple.

# extra extra:
# Create a Dictionary: Create a dictionary to store the names and ages of five people. Print the dictionary.
# Access Values: Access and print the age of one of the people in your dictionary.
# Modify Values: Change the age of one of the people in your dictionary and print the updated dictionary.

# 1a
favorite_movies = ["matrix", "toy soldiers", "power", "movie2", "World war"]
print(favorite_movies)
# 1b
print(favorite_movies[0])
print(favorite_movies[4])
# or
print(favorite_movies[-1])

# 1c
favorite_movies[1] = "Aki and paw paw"
print(favorite_movies)

# 1d

favorite_movies.append("star wars")
print(favorite_movies)

# 1e
favorite_movies.remove("movie2")
print(favorite_movies)

# or
del favorite_movies[3]
# print(favorite_movies)


# number 2
listOfIntegers = [7, 9, 10, 15, 20, 25, 60, 100, 120, 150]

# first 3 numbers
print(listOfIntegers[:3])

# last 3 numbers
print(listOfIntegers[7:])
# or
print(listOfIntegers[-3:])

# midle 5
print(listOfIntegers[3:8])

# 2b
print(listOfIntegers[-2:])


# 3a

nestedList = [[1, 2, 3], [5, 6, 7], [11, 12, 15]]

# nestedList[0][1]=50
print(nestedList[0][1])

newList = [["ade", "simbi"], ["ali", "samuel", ["taiye", "trump"], 23]]


print(newList[1][2][1])

print(newList[1][3])


animalTuple = ("dog", "cat", "goat", "lion", "giraff")
# newAnimalList =['dag','cat']


print(animalTuple[0])
print(animalTuple[4])

my_dictionary = {
    "David": 50,
    "Iyke": 22,
    "Stella": 16,
    "Busayo": 16,
    "Seyi": 12,
}

print(my_dictionary["Seyi"])
my_dictionary['Seyi'] =58
print(my_dictionary)


userIyke = {
    'name': "iYke's", 
    "age": 12,
    "favoriteFood":"Akpu",
    "hasPaid":True,
    "hobbies":['coding','soccer','data']
    }
# userIyke.clear()
userIkecopy=userIyke.copy()
userIyke.clear()
print(userIyke)
print(userIkecopy)
# print(userIkecopy.items())







# print(userIyke["hobbies"][1])



# print(type(my_dictionary))
