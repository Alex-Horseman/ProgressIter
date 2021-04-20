
import sys 
sys.path.append('./')

from src.ProgressIter import Progressbar as PB
import time

def some_work(some_data):
    time.sleep(0.0001)

some_iterable_dataset = range(322)

start_time = time.time()
PB.global_on(True)
PB.global_time_on(True)
PB.global_bar_len(5)
pb = PB(some_iterable_dataset)
for data in pb:
    some_work(data)

from src.ProgressIter import Progressbar as PB2
pb = PB2(some_iterable_dataset)
for data in pb:
    some_work(data)