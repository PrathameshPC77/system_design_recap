import time
import requests
from django.core.cache import cache
import threading

# Measure external HTTP latency
def measure_http_latency(url):
    start = time.time()
    requests.get(url)
    end = time.time()
    return f"Latency: {(end - start) * 1000:.2f} ms"

# Cached result
def get_cached_data():
    if not cache.get("cached_response"):
        print("Cache Miss")
        cache.set("cached_response", "Heavy computation result", 60)
    return cache.get("cached_response")

# Simulate long task using threading
def simulate_slow_task():
    def task():
        time.sleep(5)
        print("Slow task completed")
    threading.Thread(target=task).start()
