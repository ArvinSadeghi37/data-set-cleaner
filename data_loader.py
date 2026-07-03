import pandas as pa
def load_data(path):
    chunksize = 200000
    print("started to read")
    reader = pa.read_csv(path ,encoding="utf-8",chunksize=chunksize ,on_bad_lines="warn" , header=None)
    return reader

        

