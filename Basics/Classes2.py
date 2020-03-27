import datetime as dt

class Member:
    free_days = 365
    def __init__(self, username, fullname):
        self.date_joined = dt.date.today()
        self.free_expires = dt.date.today() + dt.timedelta(days = Member.free_days)


wilbur = Member('wblomgren', 'Wilbur Blomegren')

print(wilbur.date_joined)
print(wilbur.free_expires)