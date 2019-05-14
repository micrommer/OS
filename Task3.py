from threading import Thread
import time

class Task:
    savedTime = None
    startTime = None
    endTime = None
    runTime = 0

    def __init__(self, taskTime, taskName):
        self.taskTime = float(taskTime)
        self.completed = False
        self.taskName = taskName
        self.savedTime = float(taskTime) * 10

    def executeRR(self, runningTime):
        if self.startTime is None:
            self.startTime = time.time()
        if self.taskTime > runningTime:
            print("{} runs for {}'s".format(self.taskName, runningTime))
            self.taskTime -= runningTime
            st = time.time()
            time.sleep(runningTime)
            r = time.time() - st
            self.runTime += r
            string = ""
        else:
            print("{} runs for {}'s".format(self.taskName, self.taskTime))
            # self.taskTime = 0
            st = time.time()
            time.sleep(self.taskTime)
            self.endTime = time.time()
            r = time.time() - st
            self.runTime += r
            self.completed = True
            print("{} task competed".format(self.taskName))

    def is_completed(self):
        return self.completed

    def get_proccess_info(self):
        wait_time = self.endTime - (self.startTime + self.runTime)
        print("{} wait time is '{}' ".format(self.taskName, wait_time), end="")
        response_time = self.endTime - self.startTime

        print("{} response time is '{}' ".format(self.taskName, response_time, end=""))

    def __str__(self):
        return "A task with {} seconds working thread".format(self.taskName)
