import time as TimeSystem
from datetime import datetime as Time


class Task(object):


    def __init__(self, task_time, task_name):
        self.task_time = float(task_time)
        self.task_name = task_name
        self.completed = False
        self.start_time = None
        self.end_time = None
        self.run_time = 0

    def execute_round_rabin(self, quantum):
        if self.start_time is None:
            self.start_time = Time.now().microsecond
        if self.task_time > quantum:
            print("{} running for {}".format(self.task_name, quantum))
            self.task_time -= quantum
            # run
            start = Time.now().microsecond
            TimeSystem.sleep(quantum)
            end = Time.now().microsecond
            self.run_time += end - start
            # run
        else:
            print("{} running for {}".format(self.task_name, self.task_time))
            # run
            start = Time.now().microsecond
            TimeSystem.sleep(quantum)
            end = Time.now().microsecond
            self.run_time += end - start
            # run
            self.completed = True
            self.end_time = end
            print("{} completed ".format(self.task_name))

    def get_info(self):
        wait = round(self.end_time - (self.start_time + self.run_time),5)
        print("{} wait time {} ".format(self.task_name,wait),end="")
        response = round(self.end_time - self.start_time,5)
        print("{} response time {} ".format(self.task_name, response), end="")
        print()

    def is_completed(self):
        return self.completed

    def __str__(self):
        return self.task_name