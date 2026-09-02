print("Student Profile & Marking System.....")
# Create A Basic Variables

student_id=250210132061
student_name="Sodha Pranav"
student_course="Data Analytics"
print(student_id, type(student_id), id(student_id))
print(student_name, type(student_name), id(student_name))
print(student_course, type(student_course), id(student_course))

# Python Data Types

marks=99
version=3.14
name="Python"
value=True
tpl=(1,)
lst=[1,2,3]
abc={1,2,3,4}
dict={
    "Pranav":"ICT",
}
print(type(marks))
print(type(version))
print(type(name))
print(type(value))
print(type(tpl))
print(type(lst))
print(type(abc))
print(type(dict))

# Take Details

name=input("Enter Your Name:")
age=float(input("Enter Your Age:"))
print(type(age))

# Multiple Assignment Statements

city="Rajkot"
college="GTU"
semester="3"
print("My College Name is: "+college+" It is In: "+city+" I am Studying in: "+semester)

marks1,marks2=map(int, input("Enter The Marks Of Both Subjects:").split())
print(marks1,marks2)

# Display Student Profile 

print("Hello My Name Is:\t "+name+"And I Am In:\n"+college+"I am In Semester:"+semester+" The College is in:"+city)

# Marks=9/10