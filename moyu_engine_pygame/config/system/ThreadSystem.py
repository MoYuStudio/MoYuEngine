
import threading
import multiprocessing

class ThreadSystem:

    def thread0(thread_def):
        thread = threading.Thread(
            target = thread_def
        )
        thread.start()
        thread.join()

    def thread1(thread_def):
        thread = threading.Thread(
            target = thread_def
        )
        thread.start()

    def multiprocess0(multiprocess_def):
        multiprocess = multiprocessing.Process(
            target = multiprocess_def
        )
        multiprocess.start()
        multiprocess.join()

    def multiprocess1(multiprocess_def):
        multiprocess = multiprocessing.Process(
            target = multiprocess_def
        )
        multiprocess.start()
        
if __name__ == "__main__":
    while True:
        ThreadSystem.thread1()
        ThreadSystem.multiprocess1()


