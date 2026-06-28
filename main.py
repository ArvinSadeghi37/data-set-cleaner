from data_loader import load_data
from analyzer import analyze_data
from cleaner import cleanizer
from tqdm import tqdm 
import pandas
reader = load_data("twitter_sample_tweets.csv")
#print(analyze_data(reader))


for chunk in tqdm(reader, total=80, desc="Processing Chunks"):
    data = cleanizer(chunk)


for i in data:
    print(i)
    