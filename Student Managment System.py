import statistics as sta

print('Insert Your UserName')
UserName = input()
print('Insert Your Password')
Password = input()

StudentsGreadDictory = {
    'Aby': [89, 78],
    'Dav': [88, 70],
    'Emu': [70, 100],
    'Jack': [67, 94],
    'Sam': [89, 78],
    'Bacy': [88, 70],
    'Sol': [70, 100],
    'Kal': [67, 94]
}


def InsertGrade(name, grade):
    StudentsGreadDictory[name].append(int(grade))
    print(StudentsGreadDictory)


def RemoveStudent(name):
    del StudentsGreadDictory[name]
    print(StudentsGreadDictory)


def AverageGradeForStudent(name):
    ave = sta.mean(StudentsGreadDictory[name])
    print('Student Average is: ', ave)


def detailedApp(x):
    if x == '1':
        print('Greade Insertion')
        print('insert name')
        name = input()
        print('insert grade')
        grade = input()

        InsertGrade(name, grade)
        AverageGradeForStudent(name)

    if x == '2':
        print('Remove Student')
        print('insert name')
        name = input()

        RemoveStudent(name)
    if x == '3':
        print('Remove Student')
        print('insert name')
        name = input()

        AverageGradeForStudent(name)
    if x == '4':
        print('...................End...................')
        print('*******************//********************')


def LogOut(check):
    if check == 'Y' or check == 'y':
        detailedApp('4')
    if check == 'N' or check == 'n':
        Services()


def Services():
    print('Well Come to Grade Central')
    print('*****************************************')
    print(" ")
    print("[1]-Enter Grade")
    print("[2]-Remove Student")
    print("[3]-Student Average Greade")
    print("[4]-Exit")
    print(" What Would you like to Do? Choose A Number")
    print('*****************************************')
    x = input()
    detailedApp(x)
    print('Do you Finish What You Came for?Y/N')
    check = input()
    LogOut(check)


def signIn(UserName, Password):
    if UserName == 'ptn' and Password == '123':
        Services()
    else:
        print("You have Inserted Wrong UserName or PassWord")


signIn(UserName, Password)
