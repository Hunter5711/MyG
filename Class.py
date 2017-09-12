class Student :
    def __init__(self,rollNo , name ):
     self.rollNo =rollNo
     self.name = name

    def disp(self):
     print "rollNo is ",self.rollNo,"Student name ",self.name
st1 = Student(101, "Hunter")
st2 = Student(102,"Anonymous")
st1.disp()
st2.disp()