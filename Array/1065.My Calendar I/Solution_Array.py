class MyCalendar:
    
    def __init__(self):
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if len(self.events) == 0:
            self.events.append([start, end])
            return True

        else:
            for event in self.events:
                if not (event[1] <= start or event[0] >= end):
                    return False

            self.events.append([start, end])
            self.events.sort()
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)