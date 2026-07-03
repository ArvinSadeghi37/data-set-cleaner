import pandas as pa
import hazm 
import re


def cleanizer(chunk):
    
    link_pattern = re.compile(r"(https?://\S+|www\.\S+)")
    emoji_pattern = re.compile(
    r'[\U00010000-\U0010ffff]' 
    r'|[\u2300-\u2BFF]'          
    r'|[\u200d\ufe0f]')        
    hashtag_icon_pattern = re.compile(r"#")
    hashtag_endoftweet_pattern = re.compile(r"(\s#\w+)*$")
    retweet_patter = re.compile(r"^RT\s:\s")
    
    #detect and delete empty lines 
    chunk = chunk.dropna()
       
    # detect and delete duplicate lines
    chunk = chunk.drop_duplicates()

    # detect and delete links
    chunk[1] = chunk[1].str.replace(link_pattern , "" ,  regex=True)

    # detect and delete emojis
    chunk[1] = chunk[1].str.replace(emoji_pattern , "" , regex=True)
    
    # hashtags 
    chunk[1] = chunk[1].str.replace(hashtag_endoftweet_pattern , "" ,  regex=True)
    chunk[1] = chunk[1].str.replace(hashtag_icon_pattern , "" ,  regex=True)

    # delete retweet re : 
    chunk[1] = chunk[1].str.replace(retweet_patter , "" ,  regex=True)
    
    #clean unlikely charachters
    chunk[1] = chunk[1].str.replace(r'[\u200e\u200f\u202a-\u202e\u2066-\u2069]', '', regex=True)

    #clean lines which newly got empty
    chunk = chunk.dropna()
    chunk[1] = chunk[1].str.replace("\n", " ", regex=False)
    
    return chunk[1]
