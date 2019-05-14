import time as Time


class Task(object):
    def __init__(self, task_name, task_time):
        self.task_time = int(task_time)
        self.task_name = task_name
        self.end_time = None
        self.run_time = 0
        self.start_time = Time.time()
        self.completed = False

    def get_info(self):
        wait_time = self.end_time - (self.start_time + self.run_time)
        print("{} wait time : {} ".format(self.task_name, wait_time), end="")
        response_time = self.end_time - self.start_time
        print("{} response time : {} ".format(self.task_name, response_time), end="")
        print("")
        return {"wait_time": wait_time, "response_time": response_time}

    def is_completed(self):
        return self.completed

    def __str__(self):
        return "{} task on thread".format(self.task_name)

    def __le__(self, other):
        return self.task_time <= other.task_time

    def __lt__(self, other):
        return self.task_time < other.task_time

    def __ge__(self, other):
        return self.task_time >= other.task_time

    def __gt__(self, other):
        return self.task_time > other.task_time


    def execute_round_rabin(self, quantum):
        if self.task_time > quantum:
            print("{} runs for {} ".format(self.task_name, quantum))
            self.task_time -= quantum
            # running block
            Time.sleep(quantum)
            self.run_time += quantum
            # running block
        else:
            print("{} runs for {} ".format(self.task_name, self.task_time))
            # running block
            Time.sleep(self.task_time)
            self.run_time += self.task_time
            # running block
            print("{} is completed !".format(self.task_name))
            self.completed = True
            self.end_time = Time.time()

    def execute_FIFO(self):
        print("{} runs for {} ".format(self.task_name, self.task_time))
        # running block
        Time.sleep(self.task_time)
        self.run_time += self.task_time
        # running block
        self.completed = True
        self.end_time = Time.time()
        print("{} is completed !".format(self.task_name))
