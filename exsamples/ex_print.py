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
        print(f"threads status => [{self.thread_status()}]", flush=True)
        timer_thread = Timer(3, self.child_thread)
        self.threads.append(timer_thread)
        print(f"threads status => [{self.thread_status()}]", flush=True)
        timer_thread.start()
        print("timer thread start < child thread", flush=True)


def main():
    print("main", flush=True)
    ssc = SubSystemControl()
    timer_thread = Timer(3, ssc.child_thread)
    ssc.threads.append(timer_thread)
    timer_thread.start()
    print("timer thread start", flush=True)
    time.sleep(20)


if __name__ == "__main__":
    main()
    print("exit main process.", flush=True)
    sys.exit(0)
