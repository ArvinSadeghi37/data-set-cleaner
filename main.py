from data_loader import load_data
from analyzer import analyze_data

reader = load_data("twitter_sample_tweets.csv")
print(analyze_data(reader))