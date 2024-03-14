import multiprocessing
import os
import time
from collections import deque
import logging

def worker(process_num):

    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    milliseconds = int((time.time() % 1) * 1000)
    logger.info(f"{current_time}.{milliseconds:03d} - Process Pnumber[{process_num}]  PID[{os.getpid()}] started.")
    while 100:
        logger.info(f"Pnumber [{process_num}] executing")
        time.sleep(0.3)
    logger.info(f"{current_time}.{milliseconds:03d} - Process Pnumber[{process_num}]  PID[{os.getpid()}] finished.")


if __name__ == "__main__":
    processes = deque()
    temp = deque()
    # Create 10 processes
    for i in range(10):
        process = multiprocessing.Process(target=worker, args=(i,))
        processes.append(process)
        process.start()

    print("All start")
    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("All processes have finished.")
