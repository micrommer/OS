from Task import Task

QUANTUM_TIME_1 = 5.0
STATIC_TASKS_1 = ["p1/8/0", "p2/4/1", "p3/9/2", "p4/5/3"]


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
        enter your task with |task name/time/incoming time| format: """)
        if inp == "x":
            return
        if inp == "clear":
            arr = []
        elif inp == "RR":
            round_rabin(arr)
        # elif inp == "FIFO":
        #     FIFO(arr)
        # elif inp == "SJF":
        #     SJF(arr)
        # elif inp == "SRT":
        #     SJF(arr)
        # elif inp == "HRRN":
        #     HRRN(arr)
        # else:
        #     arr.append(inp)


def round_rabin(arr):
    pass
