import time



def run_for_five_sec(cookie):
    timeout= time.time() + 5
    while True:
        if time.time()> timeout:
            break
        cookie.click()
        # time.sleep(0.0001)