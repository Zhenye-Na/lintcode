class MyCalendar:
    
    def __init__(self):
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        start_interval, end_interval = (start, 1), (end, -1)
        self.events.append(start_interval)
        self.events.append(end_interval)
        self.events.sort()

        # sweep line
        num_of_event, max_concurrent_events = 0, -1
        for _, delta in self.events:
            num_of_event += delta
            max_concurrent_events = max(max_concurrent_events, num_of_event)
            if max_concurrent_events > 1:
                self.events.remove(start_interval)
                self.events.remove(end_interval)
                return False

        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)