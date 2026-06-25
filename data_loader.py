import pandas as pa
import time
def load_data(path):
    chunksize = 100000
    print("started to read")
    reader = pa.read_csv(path ,encoding="utf-8",chunksize=chunksize ,on_bad_lines="warn" , header=None)
    return reader

        

