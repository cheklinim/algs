def my_decor(func):
    def wrapper():
        import timeit
        code_to_test = """
        func()
        """
        elapsed_time = timeit.timeit(code_to_test, number=100)/100
        print(elapsed_time)
    return wrapper



#@my_decor
def simple_function():
    print("simple_function() started")

import inspect
print(inspect.getsource(simple_function)[1:])


