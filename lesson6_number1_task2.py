# list of negative and positive words.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Function to tally positive and negative words in reviews

def sentiment_tally(reviews):
    positive_count = 0
    negative_count = 0

    for review in reviews:
        words = review.lower().split()
        positive_count += sum(word in positive_words for word in words)
        negative_count += sum(word in negative_words for word in words)

    return positive_count, negative_count


reviews = [ "This product is really good. I'm impressed with its quality.", 
           "The performance of this product is excellent. Highly recommended!", 
           "I had a bad experience with this product. It didn't meet my expectations.", 
           "Poor quality product. Wouldn't recommend it to anyone.", 
           "The product was average. Nothing extraordinary about it."
]

# Tallying sentiment words in reviews

positive_count, negative_count = sentiment_tally(reviews)
print("Total Positive Words:", positive_count)
print("Total Negative Words:", negative_count)