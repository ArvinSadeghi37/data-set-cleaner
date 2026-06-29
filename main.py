from data_loader import load_data
from analyzer import analyze_data
from cleaner import cleanizer
from normalizer import normalizator
from tqdm import tqdm 
import pandas
reader = load_data("twitter_sample_tweets.csv")
#print(analyze_data(reader))


for chunk in tqdm(reader, total=80, desc="Processing Chunks"):
    data = cleanizer(chunk)
    data = normalizator(data)
    data = data.to_frame()
    data.to_csv("cleaned_data_main.csv",mode="a", index=False ,  header=False)
print("cleaning data finished succesfully")
        
    

    