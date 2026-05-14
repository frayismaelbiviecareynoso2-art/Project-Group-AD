""" DATA BASE """
data_base = [{'name':'Fray Ismael','age':23,'email':'frayismael@gmail.com','password':'80931336211329'}]

class SystemAccount:
    """ Constructor <- This recieve and save the date of account"""
    def __init__(self):
        self.name = None
        self.age = None
        self.__email = None
        self.__password = None 

    """ Register """
    
    def register(self,name,age,email,password):
        """ In this method is for to validate the date that attribute going to recieve"""
        if len(name) >= 5 and len(name) <= 15:
            self.name = name.lower()
        else:
            return "Error in the name"

        if age >= 18 and age <= 50:
            self.age = age
        else:
            return "You are younger"
        
        if email.endswith("@gmail.com") or email.endswith("@hotmail.com"):
            self.__email = email.lower()
        else:
            return "ERROR the Email is incorrect "

        if len(str(password)) >= 8 or len(str(password)) <= 18:
            self.__password = password
        else:
            return "ERROR the password is incorrect"
        if self.name and self.age and self.__email and self.__password:
            for i in data_base:
                if i.get('email') == self.__email.lower():
                    raise PermissionError('ERROR THE ACCOUNT ALREADY EXIT')
                
            data_base.append({
                    'name': self.name,
                    "age": self.age,
                    'email': self.__email,
                    'password': str(self.__password)
                })
            return "ACCESS ACTIVE"

    def n_register(self):
        name = input("Write you name: ")
        age = int(input("Write you year old: "))
        email = input("Write you email: ")
        password = input("Write you password: ") 
        return self.register(name,age,email,password)

    """ Method Login """
    def login(self):
        email = input("Write you email: ").lower()
        password = input('Write you password: ')
        for i in data_base:
            if i.get("email") == email and i.get('password') == str(password):
                return "ACCESS ACTIVE"
        else:
            return "Try Again"

        

example = SystemAccount()
print(example.n_register())
print(data_base)
print(example.login())