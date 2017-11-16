'''
logical simulation of a calendar
set a certain date and advance it by one day
'''

import doctest

class Calendar(object):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]

    def leapyear(year):
        '''
        returns True if year is leapyear, else False

        >>> Calendar.leapyear(299)
        False
        >>> Calendar.leapyear(2000)
        True
        >>> Calendar.leapyear(15000)
        False
        '''
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def __init__(self, d, m, y):
        self.set_calendar(d,m,y)

    def set_calendar(self, d, m, y):
        '''
        parameters must be integers and in date format
        '''
        if m > 12 or m < 1:
            raise ValueError("Month must be between 1 and 12")

        if d > Calendar.months[m-1] or d < 1:
            raise ValueError("Day must fit to the month")
        
        if type(d) == int and type(m) == int and type(y) == int:
            self.day = d
            self.month = m
            self.year = y
        else:
            raise TypeError("inputs must be integers")

    def __str__(self):
        '''
        overloads builtin __str__ to show date
        '''
        return "{0:02d}.{1:02d}.{2:4d}".format(self.day, self.month, self.year)

    def advance(self):
        '''
        advance to next day
        '''
        max_days = Calendar.months[self.month-1]
        if self.month == 2 and Calendar.leapyear(self.year):
            max_days += 1
        if self.day == max_days:
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1

# unit test
if __name__ == "__main__":
    c = Calendar(31,12,2012)
    print(c, end=" ")
    c.advance()
    print("after advance:", c)

    # doctest
    doctest.testmod()
