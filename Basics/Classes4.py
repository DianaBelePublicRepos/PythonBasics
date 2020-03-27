import datetime as dt

class Member:
    free_days = 0
    def __init__(self, username, fullname):
        # Define attributes and give them values
        self.username = username
        self.fullname = fullname
        self.expiry_day = dt.date.today() + dt.timedelta(days = Member.free_days)

    @classmethod
    def setfreedays(cls, days):
        cls.free_days = days

    @staticmethod
    def currenttime():
        now = dt.datetime.now()
        return f"{now:%I:%M:%p}"

#Try out the new static method
print(Member.currenttime())