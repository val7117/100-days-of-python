# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma and a space. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
list_length = len(names)
random_number = random.randint(0, list_length - 1)
random_person = names[random_number]

print(f"{random_person} is going to buy the meal today!")