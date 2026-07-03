import pandas as pa
import re
def analyze_data(data ,  text_line):
    print("working for a report of data...")
    total_rows = 0
    empty_rows = 0
    max_line = 0 
    min_line = 1500000000000
    link_count = 0
    retweet_count = 0
    
    for chunk in data:
        #count all lines and empty lines
        total_rows += len(chunk[text_line])
        empty_rows += (chunk[text_line].str.strip()== "").sum()
        #count line sizes
        lenth = chunk[text_line].astype(str).str.len()
        biggest_line = lenth.max()
        smallest_line = lenth.min()
        max_line = max(biggest_line , max_line)
        
        
        min_line = min(smallest_line , min_line)

        #count linked lines
        link_count += chunk[text_line].str.contains(r"https?://|www\.", na=False).sum()

    return {"total_tweets" : total_rows ,
            "empty_tweets" : empty_rows ,
            "biggest_tweet": max_line   ,
            "smallest_tweet": min_line   , 
            "linked_twittes": link_count
            }
