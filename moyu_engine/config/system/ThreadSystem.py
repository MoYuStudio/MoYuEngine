
import threading
import multiprocessing

class ThreadSystem:

    def thread1(thread_def):
        thread = threading.Thread(
            target = thread_def
        )
        thread.start()
        thread.join()

    def thread2(thread_def="1"):
        thread = multiprocessing.Process(
            target = print(thread_def)
        )
        thread.start()
        thread.join()
        
if __name__ == "__main__":
    while True:
        ThreadSystem.thread2()
        ThreadSystem.thread2()


