class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def check_result(self):
        if self.score >= 6:
            return f"{self.name} has passed with no back log of {self.score}."
        else:
            return f"{self.name} has failed with 2 back log of {self.score}."

student1 = Student("prajwal",7.5)
student2 = Student("shankar",5.5)

print(student1.check_result())  
print(student2.check_result())  
