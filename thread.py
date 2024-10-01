# multi_threading.py
import threading

class Counter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            local_copy = self.value
            local_copy += 1
            self.value = local_copy

def worker(counter, iterations):
    for _ in range(iterations):
        counter.increment()

# Usage
counter = Counter()
threads = []

for _ in range(5):
    thread = threading.Thread(target=worker, args=(counter, 100000))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter.value}")
