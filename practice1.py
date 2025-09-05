from datetime import datetime
# This is a basic program to take user input and generate the output for name and age.
name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_year= datetime.now().year
year_100= current_year + (100-age)

print(f"Hello {name}! You will turn 100 years old in the year {year_100}.")

#This is a program to reverse an array, array=[1,2,3,4,5].

arr=[1,2,3,4,5]
n=len(arr)

for i in range(n//2):
    arr[i], arr[n-i-1]= arr[n-i-1], arr[i]
    print("Reversed array is: ", arr)

# Program for slicing a name.
name = "mayank"
result = name[-1:1:-1]
print(result)
