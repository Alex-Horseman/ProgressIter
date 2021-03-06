# ProgressIter <kbd>v0.4.0</kbd>

Discription
-------------

This is a simple wrapper of any Iterator or Iterable and print the progressbar string during a for loop.

Like this:

    [######################################1                                                             ]38%(123/322)[15.80ms/1.94s/3.14s]some extra information

Usage
--------------

### Class instantiation

    Progressbar(
        iter
        length=0,
        on=None,
        time_on=None,
        bar_len=None
    )
    
<kbd>iter</kbd> is the Iterator or the Iterable object you want to iterate in a for loop.

<kbd>length</kbd> (Optional) The total length of iter. Only use if the iter object has no attribute \_\_len__. If the length was set wrong, the printing string of progressbar may act wrong.

<kbd>on</kbd> (Optional) If it is set to False, nothing will be print. The progressbar will act the same as the iterable object.

<kbd>time_on</kbd> (Optional) If it is set to True, time of each step will be calculated and the average time, total time and rest time will be printed.

<kbd>bar_len</kbd> (Optional) Length of the bar string. Default 100.

### Methods

    show_message(str)

<kbd>str</kbd> Some extra information you want to print after the string of progressbar. When this method is called, the information will not be print immediately. When the iterable object goes to the next step, this information will be print.

    global_on(on:bool)

<kbd>on</kbd> It set the default value of optional parameter *on* for all instantiation.

    global_time_on(on:bool)

<kbd>on</kbd> It set the default value of optional parameter *time_on* for all instantiation.

    global_bar_len(length:int)

<kbd>length</kbd> It set the default value of optional parameter *bar_len* for all instantiation.

Example
--------------

    from ProgressIter import Progressbar as PB
    import time

    def some_work(some_data):
        time.sleep(0.001)

    some_iterable_dataset = range(10289)

    start_time = time.time()
    pb = PB(some_iterable_dataset, on=True)
    for data in pb:
        some_work(data)
        pb.show_message('this data = %d' % data)

