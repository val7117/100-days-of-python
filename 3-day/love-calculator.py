# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string = name1 + name2
lowered_combined_string = combined_string.lower() 

t = lowered_combined_string.count('t')
r = lowered_combined_string.count('r')
u = lowered_combined_string.count('u')
e = lowered_combined_string.count('e')

l = lowered_combined_string.count('l')
o = lowered_combined_string.count('o')
v = lowered_combined_string.count('v')

true_score = t + r + u + e
love_score = l + o + v + e

final_score = int(str(true_score) + str(love_score))

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")