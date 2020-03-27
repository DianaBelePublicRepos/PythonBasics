import datetime as dt

class Member:
    expiry_days = 365
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.date_joined = dt.date.today()
        self.expiry_date = dt.date.today() + dt.timedelta(days = Member.expiry_days)
        self.secret_code = ' '

    def showexpiry(self):
        return f"{self.firstname} {self.lastname} expires on {self.expiry_date}"

class Admin(Member):
    #Admin accounts don't expire for 100 years
    expiry_days = 365.2422 * 100

    #Subclass parameters
    def __init__(self, firstname, lastname, secret_code):
        super().__init__(firstname, lastname)
        #Assign the remaining params to this object
        self.secret_code = secret_code

#Subclass for Users
class User(Member):
    pass

Ann = Admin("Annie", "Angst", "PRESTO")
print(Ann.firstname, Ann.lastname, Ann.expiry_date, Ann.secret_code)

Uli = User('Uli', 'Ungula')
print(Uli.firstname, Uli.lastname, Uli.expiry_date, Uli.secret_code)