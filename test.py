import sched
import time
sch1=sched.scheduler(time.time,time.sleep)
def f1():
    print("func running")
sch1.enter(5,1,f1)
sch1.run()