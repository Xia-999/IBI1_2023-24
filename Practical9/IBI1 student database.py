class students(object):  #create a class called students
    def __init__(self,name,major,code_portfolio_score,group_project_score,exam_score):  #define class attributue
        self.name=name
        self.major=major
        self.code_portfolio_score=code_portfolio_score
        self.group_project_score=group_project_score
        self.exam_score=exam_score
    
    def print_information(self):
        print(f"student name:{self.name},major:{self.major},code portfolio score:{self.code_portfolio_score},gourp project scoroe:{self.group_project_score},exam score:{self.exam_score}")
              
student=students("Summer","BMI",100,100,100)  #an example
student.print_information()

