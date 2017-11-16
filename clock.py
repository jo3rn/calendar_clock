'''
logical simulation of a clock
a method advances the clock one unit
'''

class Clock(object):
    def __init__(self, h, m, s):
        self.set_clock(h, m, s)

    def set_clock(self, h, m, s):
        '''
        parameters must be integers and in clock format
        '''
        if type(h) == int and 0 <= h and h < 24:
            self.hours = h
        else:
            raise TypeError("Hours must be int and between 0 and 23")

        if type(m) == int and 0 <= m and m < 60:
            self.minutes = m
        else:
            raise TypeError("Minutes must be int and between 0 and 59")

        if type(s) == int and 0 <= s and s < 60:
            self.seconds = s
        else:
            raise TypeError("Seconds must be int and between 0 and 59")

    def __str__(self):
        '''
        overloads builtin __str__ to show time
        '''
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hours, self.minutes,
                                                self.seconds)

    def tick(self):
        '''
        forward one seconds
        '''
        if self.seconds == 59:
            self.seconds = 0
            if self.minutes == 59:
                self.minutes = 0
                if self.hours == 23:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1

# unit test
if __name__ == "__main__":
    c = Clock(12,59,59)
    print(c)
    c.tick()
    print(c)
