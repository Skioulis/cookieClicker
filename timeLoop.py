import time


def run_for_some_time(cookie):
    for i in range(200):
        cookie.click()
        time.sleep(0.0001)