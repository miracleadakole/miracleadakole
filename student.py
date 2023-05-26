class Student:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    def on_honor_roll(self):
        if self.gpa >= 3.2:
            return True
        else:
            return False

    def on_class(self):
        if self.major == "Engineering":
            return True
        else:
            return False



