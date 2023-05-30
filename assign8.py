###..1..Build a module which will provide users with functionality to save and get stats for functionality like time take, memory usage etc.
import time
import sys
class StatsManager:
    def __init__(self):
        self.start_time = 0

    def start_timer(self):
       self.start_time = time.time()

    def stop_timer(self):
        elapsed_time = time.time() - self.start_time
        return elapsed_time

    def get_memory_usage(self):
        return sys.getsizeof(self)

if __name__ == '__main__':
    stats_manager = StatsManager()
    stats_manager.start_timer()
    time.sleep(1)
    elapsed_time = stats_manager.stop_timer()
    print(f"Elapsed time: {elapsed_time} seconds")
    memory_usage = stats_manager.get_memory_usage()
    print(f"Memory usage: {memory_usage} bytes")
