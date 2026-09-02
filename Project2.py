print("Students Marks & Result Calculator...")
# Student Data
name=input("Enter Your Name:")
roll_number=int(input("Enter Your Roll Number:"))
marks1=int(input("Enter Marks Of Subject 1:"))
marks2=int(input("Enter Marks Of Subject 2:"))

# Arithmatic Operators

print(f"Total Marks Of Both Subjects Are: {marks1+marks2}")
print(f"Diffrence Of Marks Is:{marks1-marks2}")
print(f"Multiplication Of Both Marks Is:{marks1*marks2}")
print(f"Average Of Both Marks Is:{(marks1+marks2)/2}")
print(f"Percentage Of Student Is:{marks1%marks2}")
print(f"Power Of Marks Are:{marks1**marks2}")
print(f"Division Of Both Marks Is:{marks1//marks2}")

# Assignment Operators

marks1+=100
marks2-=100
marks1*=2
marks2/=5
marks1/=12
marks1//=12

print(marks1,marks2)

# Comparsion Operator

print(marks1==marks2)
print(marks1!=marks2)
print(marks1>marks2)
print(marks1<marks2)
print(marks1>=33)
print(marks2>=33)

# Logical Operators

print(marks1>=33 and  marks2>=33)
print(marks1>=33 or marks2>=33)
print(not(True))
print(not(False))

# Bitwise Operator

a=5
b=2
print(a>>b)
print(a<<b)
print(True & False)
print(True | False)
print(a^b)

# marks=8.5/10