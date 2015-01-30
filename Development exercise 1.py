#Callum Brown
#Development exercise 1


class Students:
    def __init__(self):
        name = None
        self.aLevel_1 = None
        self.aLevel_2 = None
        self.aLevel_3 = None
        self.aLevel_4 = None
        self.grade_1 = None
        self.grade_2 = None
        self.grade_3 = None
        self.grade_4 = None



list_ = []
for count in range(5):
    Alevel = Students()
    Alevel.name = input("Please enter a name: ")
    Alevel.aLevel_1 = input("Please enter your first A Level course: ")
    Alevel.aLevel_2 = input("Please enter your second A Level course: ")
    Alevel.aLevel_3 = input("Please enter your third A Level course: ")
    Alevel.aLevel_4 = input("Please enter your fourth A Level course: ")
    Alevel.grade_1 = input("Please enter your first grade: ")
    Alevel.grade_2 = input("Please enter your second grade: ")
    Alevel.grade_3 = input("Please enter your third grade: ")
    Alevel.grade_4 = input("Please enter your fourth grade: ")
    list_.append(Alevel)

print("_"*74)
print("|Name        |Course 1|Grade|Course 2|Grade|Course 3|Grade|Course 4|Grade|")
print("~"*74)
for student in list_:
    print("|{0:12}|{1:8}|{2:5}|{3:8}|{4:5}|{5:8}|{6:5}|{7:8}|{8:5}|".format(student.name,student.aLevel_1,student.aLevel_2,student.aLevel_3,student.aLevel_4,student.grade_1,student.grade_2,student.grade_3,student.grade_4))
    
print("-"*74)
