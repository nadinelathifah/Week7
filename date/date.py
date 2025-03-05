# Date class
class Date:
    def __init__(self, day=0, month=0, year=0):
        self._day = day
        self._month = month
        self._year = year

    def __str__(self):
        return "%02d/%02d/%d"%(self._day, self._month, self._year)

    def __add__(self, value):
        retn = Date(self._day, self._month, self._year)
        retn._day = retn._day + value
        return retn

    def display_date(self):
        return "%02d/%02d/%d" % (self._day, self._month, self._year)