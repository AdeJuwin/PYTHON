class person: #A person class containing name and email as attriutes
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def Print_details(self): # A method that print the person class name and email address
        print (f"I am {self.name} with email address {self.email}")

my_data = person('Israel', 'olajuwon1@gmail.com') # my_data is an instant object of the class person

