import asyncio
import concurrent.futures
from threading import Lock

try:
    get_ipython()   
    from tqdm import tqdm_notebook as tqdm
except Exception as e:  
    try: 
        from tqdm import tqdm as tqdm
    except Exception as e:
        print("Asyncer: No tqdm install found, no progress will be shown")

print("Hello World")
def prog_wrapper(func, pbar=None, mutex = None, *args):    
    result = func(*args)
    if pbar:        
        mutex.acquire()
        pbar.update(1)
        mutex.release()
    return result  

def asyncRun(data, function, workers=10, showProgress=False):

    pbar = tqdm(total=len(data)) if showProgress else None
    mutex = Lock()
    async def runAll():                        
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            loop = asyncio.get_event_loop()
            futures = [
                loop.run_in_executor(
                    executor, 
                    prog_wrapper,
                    function,
                    pbar,
                    mutex,
                    *(in_val,) if type(in_val)!=tuple else in_val
                )
                for in_val in data
            ]       
           
            response =  await asyncio.gather(*futures)                   
            return response
    
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(runAll())     
    if pbar: pbar.close()
    return result