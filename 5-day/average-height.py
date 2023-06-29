# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
sum_of_heights = 0
number_of_students = 0

for height in student_heights:
  sum_of_heights += int(height)
  number_of_students += 1

average_height = round(sum_of_heights / number_of_students)
print(average_height)
