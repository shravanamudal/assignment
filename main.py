from stats_manager import StatsManager
import time

stats_manager = StatsManager()
stats_manager.start_timer()
time.sleep(1)
elapsed_time = stats_manager.stop_timer()
print(f"Elapsed time: {elapsed_time} seconds")
memory_usage = stats_manager.get_memory_usage()
print(f"Memory usage: {memory_usage} bytes")
