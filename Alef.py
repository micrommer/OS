from Task import Task

QUANTUM_TIME_1 = 5.0
STATIC_TASKS_1 = ["p1/8", "p2/4", "p3/9", "p4/5"]


def main():
    arr = STATIC_TASKS_1
    while True:
        inp = input("""
        for exit type (x)
        for clear the list type (clear)
        for Round Raven type (RR)
        for FIFO type (FIFO)
        for SJF type (SJF)
        for HRRN type (HRRN)
        for SRT type (SRT)
        enter your task with |task name/time| format: """)
        if inp == "x":
            return
        if inp == "clear":
            arr = []
        elif inp == "RR":
            round_rabin(arr)
        elif inp == "FIFO":
            FIFO(arr)
        elif inp == "SJF":
            SJF(arr)
        elif inp == "SRT":
            SJF(arr)
        elif inp == "HRRN":
            HRRN(arr)
        else:
            arr.append(inp)


def round_rabin(arr):
    print("-----------------------------------------Round Rabin-----------------------------------------")
    jobs = []
    for i in arr:
        parts = i.split("/")
        jobs.append(Task(parts[0], parts[1]))
    while True:
        completed_counter = 0
        for index, task in enumerate(jobs):
            if not task.is_completed():
                task.execute_round_rabin(QUANTUM_TIME_1)
            else:
                completed_counter += 1
        if completed_counter == len(arr):
            break
    print("")
    awt = 0  # average wait time
    art = 0  # average response time
    for task in jobs:
        res = task.get_info()
        awt += res.get("wait_time")
        art += res.get("response_time")
    print("average wait time -> {} | average response time -> {} ".format(awt / len(arr), art / len(arr)))
    print("")
    print("-----------------------------------------Round Rabin-----------------------------------------")


def FIFO(arr):
    print("-----------------------------------------FIFO-----------------------------------------")
    jobs = []
    for i in arr:
        parts = i.split("/")
        jobs.append(Task(parts[0], parts[1]))

    for task in jobs:
        task.execute_FIFO()

    print("")
    awt = 0  # average wait time
    art = 0  # average response time
    for task in jobs:
        res = task.get_info()
        awt += res.get("wait_time")
        art += res.get("response_time")
    print("average wait time -> {} | average response time -> {} ".format(awt / len(arr), art / len(arr)))
    print("-----------------------------------------FIFO-----------------------------------------")


def SJF(arr):
    print("-----------------------------------------SJF-----------------------------------------")
    jobs = []
    for i in arr:
        parts = i.split("/")
        jobs.append(Task(parts[0], parts[1]))

    jobs = sorted(jobs)
    for task in jobs:
        task.execute_FIFO()

    print("")
    awt = 0  # average wait time
    art = 0  # average response time
    for task in jobs:
        res = task.get_info()
        awt += res.get("wait_time")
        art += res.get("response_time")
    print("average wait time -> {} | average response time -> {} ".format(awt / len(arr), art / len(arr)))


def HRRN(arr):
    print("-----------------------------------------HRRN-----------------------------------------")
    jobs = []
    for i in arr:
        parts = i.split("/")
        jobs.append(Task(parts[0], parts[1]))
    while True:
        counter = 0
        maximum = 0
        process = None
        for task in jobs:
            if task.is_completed():
                counter += 1
            else:
                if maximum < task.get_HRRN():
                    maximum = task.get_HRRN()
                    process = task
        if counter == len(arr):
            break
        process.execute_FIFO()

    print("")
    awt = 0  # average wait time
    art = 0  # average response time
    for task in jobs:
        res = task.get_info()
        awt += res.get("wait_time")
        art += res.get("response_time")
    print("average wait time -> {} | average response time -> {} ".format(awt / len(arr), art / len(arr)))

    print("-----------------------------------------HRRN-----------------------------------------")


if __name__ == '__main__':
    main()
