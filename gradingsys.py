# Defining the global variables
student_name = input("Enter student name: ") 
students = (student_name)
courses = ["algebra", "laboratory", "science"]
years = 4
semesters = 8


# To find the average marks in Year 1 semester 1 
def year_one_sem_one_avm(): 
    year = int(input ("Enter Year: "))
    sem = int(input ("Enter Semester: "))
    yearsem = ("Year" + " " + str(year) + " " + "Semester" + " " + str(sem))
    print(yearsem)
    sem1_mark1 = int(input("Enter algebra score: "))
    sem1_mark2 = int(input("Enter laboratory score: "))
    sem1_mark3 = int(input("Enter science score: "))
    marks = (sem1_mark1, sem1_mark2, sem1_mark3)
    sum_marks = sum(marks)
    av_marks = (sum_marks / len(marks)) 
    global average_marks 
    average_marks = av_marks
    print("\n")
    return av_marks

# To find the average marks in Year 1 semester 2
def year_one_sem_two_avm(): 
    to_pass = year_one_sem_one_avm()
    year = int(input ("Enter Year: "))
    sem = int(input ("Enter Semester: "))
    yearsem = ("Year" + " " + str(year) + " " + "Semester" + " " + str(sem))
    print(yearsem)
    sem2_mark1 = int(input("Enter algebra2 score: "))
    sem2_mark2 = int(input("Enter laboratory2 score: "))
    sem2_mark3 = int(input("Enter science2 score: "))
    marks = (sem2_mark1, sem2_mark2, sem2_mark3)
    sum_marks = sum(marks)
    av_marks2 = (sum_marks / len(marks)) 
    global average_marks2
    average_marks2 = av_marks2
    print("\n")
    return av_marks2

# To find the average marks in Year 2 semester 1
def year_two_sem_one_avm(): 
    to_pass = year_one_sem_two_avm()
    year = int(input ("Enter Year: "))
    sem = int(input ("Enter Semester: "))
    yearsem = ("Year" + " " + str(year) + " " + "Semester" + " " + str(sem))
    print(yearsem)
    sem2_mark1 = int(input("Enter algebra2 score: "))
    sem2_mark2 = int(input("Enter laboratory2 score: "))
    sem2_mark3 = int(input("Enter science2 score: "))
    marks = (sem2_mark1, sem2_mark2, sem2_mark3)
    sum_marks = sum(marks)
    av_marks3 = (sum_marks / len(marks)) 
    global average_marks3
    average_marks3 = av_marks3
    print("\n")
    return av_marks3


# To find the average marks in Year 2 semester 2
def year_two_sem_two_avm(): 
    to_pass = year_two_sem_one_avm()
    year = int(input ("Enter Year: "))
    sem = int(input ("Enter Semester: "))
    yearsem = ("Year" + " " + str(year) + " " + "Semester" + " " + str(sem))
    print(yearsem)
    sem2_mark1 = int(input("Enter algebra2 score: "))
    sem2_mark2 = int(input("Enter laboratory2 score: "))
    sem2_mark3 = int(input("Enter science2 score: "))
    marks = (sem2_mark1, sem2_mark2, sem2_mark3)
    sum_marks = sum(marks)
    av_marks4 = (sum_marks / len(marks)) 
    global average_marks4
    average_marks4 = av_marks4
    print("\n")
    return av_marks4


# To find the average marks in Year 3 semester 1
def year_three_sem_one_avm(): 
    to_pass = year_two_sem_two_avm()
    year = int(input ("Enter Year: "))
    sem = int(input ("Enter Semester: "))
    yearsem = ("Year" + " " + str(year) + " " + "Semester" + " " + str(sem))
    print(yearsem)
    sem2_mark1 = int(input("Enter algebra2 score: "))
    sem2_mark2 = int(input("Enter laboratory2 score: "))
    sem2_mark3 = int(input("Enter science2 score: "))
    marks = (sem2_mark1, sem2_mark2, sem2_mark3)
    sum_marks = sum(marks)
    av_marks5 = (sum_marks / len(marks)) 
    global average_marks5
    average_marks5 = av_marks5
    print("\n")
    return av_marks5


# To find the average marks in Year 3 semester 2
def year_three_sem_two_avm(): 
    to_pass = year_three_sem_one_avm()
    year = int(input ("Enter Year: "))
    sem = int(input ("Enter Semester: "))
    yearsem = ("Year" + " " + str(year) + " " + "Semester" + " " + str(sem))
    print(yearsem)
    sem2_mark1 = int(input("Enter algebra2 score: "))
    sem2_mark2 = int(input("Enter laboratory2 score: "))
    sem2_mark3 = int(input("Enter science2 score: "))
    marks = (sem2_mark1, sem2_mark2, sem2_mark3)
    sum_marks = sum(marks)
    av_marks6 = (sum_marks / len(marks)) 
    global average_marks6
    average_marks6 = av_marks6
    print("\n")
    return av_marks6


# To find the average marks in Year 4 semester 1
def year_four_sem_one_avm(): 
    to_pass = year_three_sem_two_avm()
    year = int(input ("Enter Year: "))
    sem = int(input ("Enter Semester: "))
    yearsem = ("Year" + " " + str(year) + " " + "Semester" + " " + str(sem))
    print(yearsem)
    sem2_mark1 = int(input("Enter algebra2 score: "))
    sem2_mark2 = int(input("Enter laboratory2 score: "))
    sem2_mark3 = int(input("Enter science2 score: "))
    marks = (sem2_mark1, sem2_mark2, sem2_mark3)
    sum_marks = sum(marks)
    av_marks7 = (sum_marks / len(marks)) 
    global average_marks7
    average_marks7 = av_marks7
    print("\n")
    return av_marks7


# To find the average marks in Year 4 semester 2
def year_four_sem_two_avm(): 
    to_pass = year_four_sem_one_avm()
    year = int(input ("Enter Year: "))
    sem = int(input ("Enter Semester: "))
    yearsem = ("Year" + " " + str(year) + " " + "Semester" + " " + str(sem))
    print(yearsem)
    sem2_mark1 = int(input("Enter algebra2 score: "))
    sem2_mark2 = int(input("Enter laboratory2 score: "))
    sem2_mark3 = int(input("Enter science2 score: "))
    marks = (sem2_mark1, sem2_mark2, sem2_mark3)
    sum_marks = sum(marks)
    av_marks8 = (sum_marks / len(marks)) 
    global average_marks8
    average_marks8 = av_marks8
    print("\n")
    return av_marks8




# To get the result in the total year
def cgpa(): 
    to_pass = year_four_sem_two_avm()
    total_cgpa = (
        (average_marks + average_marks2 
        + average_marks3 + average_marks4 + 
        average_marks5 + average_marks6
        + average_marks7 + average_marks8) 
        / semesters
        )
    print(total_cgpa)
    return total_cgpa


# To assign the grading system
def grades ():
    score = cgpa()
    if score >= 70 and score <= 100: 
        print("A")
    elif score >= 60 and score <= 69.99:
        print("B")
    elif score >= 50 and score <= 59.99:
        print("C")
    elif score >= 40 and score <= 49.99:
        print("D")
    else: 
        print("F", "\n", "Dear" + student_name + "Repeat this programme")
    

grades ()


