from utils import timeit
import time

##### Helper Functions ###########
@timeit
def function_helper_one():
    time.sleep(0.1)  # Simulate processing time

@timeit
def function_helper_two():
    time.sleep(0.2)  # Simulate processing time


###################################

@timeit
def function_a():
    time.sleep(0.2)  # Simulate processing time
    function_helper_one()
    function_helper_two()


