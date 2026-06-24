from textblob import TextBlob
import pandas as pd

# Read the dataset
df = pd.read_csv("reviews.csv")

# Function to find sentiment
def get_sentiment(review):
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["Review"].apply(get_sentiment)

# Display the result
print("Customer Reviews with Sentiment")
print(df)

# Count sentiments
print("\nSentiment Count")
print(df["Sentiment"].value_counts())

# Save output
df.to_csv("sentiment_output.csv", index=False)

print("\nProject Completed Successfully!")