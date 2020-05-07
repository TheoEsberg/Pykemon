import time

class Timer:
    def __init__(self, wait):
        self.wait = wait

    def Start(self):
        #   Get a starting time in Epoch time, aka seconds
        #   that has passed from the first of januari 1970
        self.StartingTime = time.time()
        self.Started = True
        self.Finished = False

        #   Update the timer and check if the timer is done
    def UpdateTimer(self):
        if (self.Started):
            if (time.time() - self.StartingTime >= self.wait):
                self.Started = False
                self.Finished = True
