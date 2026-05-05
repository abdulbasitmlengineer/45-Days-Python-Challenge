Name = input("What is Your Name?:")
Marks = int(input("Type Marks:"))
MarksNeed = int(50)
Attendance = int(input("Type Attendace: "))
AttendanceNeed = int(70)

if Marks >= MarksNeed and Attendance >= AttendanceNeed:
    print("You Passed...")
else:
    print("You Failed...You Need Both Marks And Attendance...")

