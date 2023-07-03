#Write your code below this line 👇
def prime_checker(number):
    prime = True
    for digit in range(2, 10):
        if number != digit and number % digit == 0:
            prime = False
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")                
        
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)