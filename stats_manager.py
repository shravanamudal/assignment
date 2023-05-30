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
