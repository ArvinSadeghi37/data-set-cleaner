import pandas as pa
import time
def load_data(path):
    chunksize = 100000
    print("started to read")
    zaman = time.time()
    reader = pa.read_csv(path ,encoding="utf-8",chunksize=chunksize ,on_bad_lines="warn" , header=None)
    print(f"read file in {time.time() - zaman} seconds")
    return reader

        

