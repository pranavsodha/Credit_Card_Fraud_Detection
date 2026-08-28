age=int(input("Enter Your Age:"))

if(age >= 18):
    print("You Are Eligible For Vote...")
else:
    print("You Are Not Eligible For Vote...")

num=int(input("Enter Number:"))

if(num%2==0):
    print("Number Is Even...")
elif(num%2!=0):
    print("Number Is Odd....")
else:
    print("Invallid Input.")

marks=int(input("Enter Your Marks:"))

if(marks<=100 and marks>=90):
    print("A Grade...")
elif(marks<90 and marks>=80):
    print("B Grade....")
elif(marks<80 and marks>=70):
    print("C Grade....")
elif(marks<70 and marks>=60):
    print("D Grade....")
elif(marks<60):
    print("Fail....")
else:
    print("Invalid Input...")

id=2554
password=1234
if(password==1234 and id==2554):
    print("Login Successfull..")
else:
    print("Login Failed...")