from utils import timeit
from module_a import function_a
from module_b import function_b

@timeit
def main_function():
    function_a()
    function_b()
