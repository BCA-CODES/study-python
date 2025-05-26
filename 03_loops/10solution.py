import time

attempts = 0
wait_time = 1
retries = 5

while attempts < retries:
        print("Attempts:", attempts + 1, "wait time:", wait_time)
        time.sleep(wait_time)
        wait_time *= 2
        attempts += 1
