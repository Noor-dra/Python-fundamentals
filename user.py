class User:
    def __init__ (self,first_name,last_name,DOB,Email,password,login_attempts=0):
        self.f_name=first_name
        self.l_name=last_name
        self.dob=DOB
        self.email=Email
        self.__pw=password #private attribute
        self.login_attempt=login_attempts

    def describe_user(self):
        print("User credentials: ")
        print("Name:",self.f_name,self.l_name)    
        print('DOB:',self.dob)
        print("Email:",self.email)
        print(f"Password: {self.__pw}") 

    def greet_user(self):
        print(f"Hello {self.f_name} {self.l_name}")

    def increment_login_attempts(self):
        self.login_attempt+=1

    def reset_login_attempts(self):
        self.login_attempt=0    

user1=User("Noor","Sarif","19-10-2004","noor@69gmail.com","noor@123")        
user1.greet_user()
user1.describe_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"login attempts: {user1.login_attempt}")
user1.reset_login_attempts()
print(f"login attempts: {user1.login_attempt}")