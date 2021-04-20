from ProgressIter import Progressbar as PB
import time


def some_work(some_data):
    time.sleep(0.001)


some_iterable_dataset = range(1289)

start_time = time.time()
pb = PB(some_iterable_dataset,time_on=True)
for data in pb:
    # some_work(data)
    # if data < 3:
    pb.show_message('ahahahahahahahah'*10)