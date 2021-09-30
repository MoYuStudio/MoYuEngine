
import threading

class ThreadSystem:

    def thread1(thread_def):
        thread = threading.Thread(
            target = thread_def
        )
        thread.start()
        thread.join()
        



if __name__ == "__main__":

    ThreadSystem.thread1()


