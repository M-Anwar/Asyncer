# Asyncer
Python Asynchronous Function Execution using AscyncIO

![alt text](res/asyncer_main.gif "Logo Title Text 1")

## Install
```
pip install git+git://github.com/M-Anwar/Asyncer.git#egg=asyncer
```

## Usage
Asyncer exposes one main function `asyncRun`. This function take an iterable of data, a function to run for each element and optional arguments.

```python
def asyncRun(data, function, workers=10, showProgress=False):
    """
    param data: [Iterable]     -> Iterable of tuples, which are arguments to your function
    param function: [Function] -> The function to execute for each element in data 
                                  (should accept the same number of parameters as the length of 
                                  each tuple in data )
    param workers: [Integer]   -> [DEFAULT 10] The number of worker threads to use 
    param showProgress: [Bool] -> [DAFAULT False] To show progress or not (requires tqdm)
    return: [List]             -> A list of return values from running function on each element of data.
    """
```

**Example Usage**

Below is a simple program showing the use of `asyncRun`

```Python
import asyncer
import time

def long_task(input):
    time.sleep(0.5)
    return input * 2

result = asyncer.asyncRun([1]*100, long_task, workers = 10, showProgress=True)
print("The result is: {}".format(result))
```