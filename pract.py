
class person:
    def __int__(self, lname, fname):
        self.first_name = fname
        self.last_name = lname
    def print_details(self):
        print(self.first_name,self.last_name)

class student(person):
    def __init__(self, lname, fname, sid):
        super().__init__(lname, fname)
        self.student_id = sid

    def print_details(self):
        print(self.first_name, self.last_name, self.student_id)
#p= person()
#p.last_name = "Adeloju"
#p.first_name = "Israel"

s = student()

s.print_details()

