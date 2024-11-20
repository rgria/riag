# Import necessary libraries
import tweepy
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Twitter API credentials (replace with your own keys)
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Function to fetch tweets
def fetch_tweets(keyword, count=100):
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en", tweet_mode='extended').items(count)
    data = [[tweet.created_at, tweet.user.screen_name, tweet.full_text] for tweet in tweets]
    return pd.DataFrame(data, columns=['Timestamp', 'Username', 'Tweet'])

# Fetch tweets for Kamala Harris and Donald Trump
kamala_tweets = fetch_tweets("Kamala Harris", 500)
trump_tweets = fetch_tweets("Donald Trump", 500)

# Function to clean tweets
def clean_tweet(tweet):
    stop_words = set(stopwords.words('english'))
    tweet = re.sub(r"http\S+|www\S+|https\S+", "", tweet)  # Remove URLs
    tweet = re.sub(r'\@\w+|\#', "", tweet)  # Remove mentions and hashtags
    tweet = re.sub(r"[^a-zA-Z ]", "", tweet)  # Remove special characters
    tweet = tweet.lower()  # Convert to lowercase
    tweet = " ".join([word for word in tweet.split() if word not in stop_words])  # Remove stopwords
    return tweet

# Apply cleaning function to tweets
kamala_tweets['Cleaned_Tweet'] = kamala_tweets['Tweet'].apply(clean_tweet)
trump_tweets['Cleaned_Tweet'] = trump_tweets['Tweet'].apply(clean_tweet)

# Perform sentiment analysis using VADER
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(tweet):
    score = analyzer.polarity_scores(tweet)
    if score['compound'] > 0.05:
        return 'Positive'
    elif score['compound'] < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

kamala_tweets['Sentiment'] = kamala_tweets['Cleaned_Tweet'].apply(analyze_sentiment)
trump_tweets['Sentiment'] = trump_tweets['Cleaned_Tweet'].apply(analyze_sentiment)

# Save to CSV
kamala_tweets.to_csv("kamala_tweets.csv", index=False)
trump_tweets.to_csv("trump_tweets.csv", index=False)

# Function to plot sentiment distribution
def plot_sentiment_distribution(data, title):
    sentiment_counts = data['Sentiment'].value_counts()
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="coolwarm")
    plt.title(title)
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Tweets")
    plt.show()

# Plot sentiment distributions
plot_sentiment_distribution(kamala_tweets, "Sentiment Distribution for Kamala Harris")
plot_sentiment_distribution(trump_tweets, "Sentiment Distribution for Donald Trump")

# Function to generate word clouds
def generate_wordcloud(data, sentiment, title):
    text = " ".join(data[data['Sentiment'] == sentiment]['Cleaned_Tweet'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()

# Generate word clouds for positive tweets
generate_wordcloud(kamala_tweets, "Positive", "Positive Tweets about Kamala Harris")
generate_wordcloud(trump_tweets, "Positive", "Positive Tweets about Donald Trump")
twitter_sentiment_analysis.py

