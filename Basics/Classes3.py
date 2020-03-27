import datetime as dt

class Member:
    free_days = 365
    def __init__(self, username, fullname):
        self.date_joined = dt.date.today()
        self.free_expires = dt.date.today() + dt.timedelta(days = Member.free_days)

    @classmethod
    def setfreedays(cls, days):
        cls.free_days = days

wilbur = Member('wblomgren', 'Wilbur Blomegren')
wilbur.setfreedays(30)
print(wilbur.free_expires)