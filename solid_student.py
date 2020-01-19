# Define a Python class named Student. This class will have 5 properties.

# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)
# Define getters for all properties.

class Student: 
    @property
    def firstName(self):
        try:
            return self.__firstName
        except AttributeError:
            return "Jane"

    @property
    def lastName(self):
        try: 
            return self.__lastName
        except AttributeError:
            return "Smith"

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 34
    @property
    def cohortNumber(self):
        try: 
            return self.__cohortNumber
        except AttributeError:
            return 36
    @property
    def fullName(self):
        try: 
            return self.firstName + " " + self.lastName
        except AttributeError:
            return "Jane Smith"

# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by a space. It's value cannot be set.
    
    @firstName.setter 
    def firstName(self, newFirstName):
        if type(newFirstName) is str:
            self.__firstName = newFirstName
        else: 
            print("Hey, this needs to be a string!")
    
    @lastName.setter
    def lastName(self, newLastName):
        if type(newLastName) is str:
            self.__lastName = newLastName
        else: 
            print("This needs to be a string!")

    @age.setter
    def age(self, newAge):
        if type(newAge) is int:
            self.__age = newAge
        else:
            print("Data type must be an integer")
    
    @cohortNumber.setter
    def cohortNumber(self, newCohortNumber):
        if type(newCohortNumber) is int:
            self.__cohortNumber = newCohortNumber
        else: 
            print("Data type must be an integer")
    
    
    
    
    def __str__(self):
        return(f"{str(self.fullName)} is {self.age}. She is in Cohort {self.cohortNumber}.")


student = Student()

print(student)

