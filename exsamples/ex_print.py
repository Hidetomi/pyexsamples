import sys
import time
from threading import Thread, Timer, Event


class SubSystemControl:
    def __init__(self):
        self.threads = []

    def thread_status(self):
        for thread in self.threads:
            print(f"thread status => [{thread}]")

    def child_thread(self):
        timer_thread = Timer(3, self.child_thread)
        self.threads.append(timer_thread)
        self.thread_status()
        timer_thread.start()
        print("timer thread start < child thread")


def main():
    print("main")
    ssc = SubSystemControl()
    timer_thread = Timer(3, ssc.child_thread)
    ssc.threads.append(timer_thread)
    timer_thread.start()
    print("timer thread start")
    time.sleep(20)


if __name__ == "__main__":
    main()
    print("exit main process.")
    sys.exit(0)
