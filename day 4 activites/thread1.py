import threading, time
def a():
    print("A")
    time.sleep(6)
    print("B")
b=threading.Thread(target=a)
b.start()
b.join()
print("Completed the execution of thread a")