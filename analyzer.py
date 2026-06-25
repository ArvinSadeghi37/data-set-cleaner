import pandas as pa
import re
def analyze_data(data):
    print("working for a report of data...")
    total_rows = 0
    empty_rows = 0
    max_line = 0 
    min_line = 0
    short_twittes = 0
    link_count = 0
    retweet_count = 0
    
    for chunk in data:
        total_rows += len(chunk)
        empty_rows += (chunk[1].str.strip()== "").sum()

        lenth = chunk[1].astype(str).str.len()
        biggest_line = lenth.max()
        smallest_line = lenth.min()
        
        max_line = max(biggest_line , max_line)
        min_line = min(smallest_line , min_line)

        short_twittes += (lenth < 5 ).sum()

        link_count += chunk[1].str.contains(r"https?://|www\.", na=False).sum()
    return {"total_rows" : total_rows ,
            "empty_rows" : empty_rows ,
            "biggest_row": max_line   ,
            "smallest_row": min_line   , 
            "linked_twittes": link_count
            }