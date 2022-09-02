
#Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
#kilograms in a separate list using Loop. N: No of students (Read input from user)
#Ex: L1: [150, 155, 145, 148]
#Output: [68.03, 70.3, 65.77, 67.13]

Students_num = int(input("please enter the student count in a class"))
print("Total no of students in a class is",Students_num)
Student_wt = []
for i in range(0,Students_num):
    Student_wt.append(int(input('please enter the weight')))
print("Weights of students in lbs:", Student_wt)
Student_kgs = []
for i in range(0,Students_num):
    Student_kgs.append(Student_wt[i]*0.453592)
print('weights of students in kgs :', Student_kgs)     