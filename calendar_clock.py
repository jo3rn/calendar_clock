'''
logical simulation of a calendar + clock
'''

from clock import Clock
from calendar import Calendar

class CalendarClock(Clock, Calendar):
    def __init__(self, day, month, year, hours, minutes, seconds):
        Clock.__init__(self,hours,minutes,seconds)
        Calendar.__init__(self,day,month,year)

    def tick(self):
        previous_hour = self.hours
        Clock.tick(self)
        if self.hours < previous_hour:
            self.advance()

    def __str__(self):
        s = "{0:02d}.{1:02d}.{2:4d}".format(self.day, self.month, self.year)
        s += " "
        s += "{0:02d}:{1:02d}:{2:02d}".format(self.hours,self.minutes,
                                              self.seconds)
        return s


# unit test
if __name__ == "__main__":
    cc = CalendarClock(31,12,2013,23,59,59)
    print("One tick from", cc, end=" ")
    cc.tick()
    print("to", cc)
