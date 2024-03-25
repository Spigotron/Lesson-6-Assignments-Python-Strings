# Task 1

def categorize(review):
    keywords = ["average", "Average", "Bad", "Excellent", "Poor", "Good", "bad", "excellent", "good", "poor"]
    for keyword in keywords:
        if keyword in review:
            review = review.replace(keyword, keyword.upper())
    return review

reviews = ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."]

for review in reviews:
    highlighted_review = categorize(review)
    print(highlighted_review)

# Task 2

def tally(review):
    positive = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    positive_count = 0
    negative_count = 0
    words = review.lower().split()
    for word in words:
        if word in positive:
            positive_count += 1
        elif word in negative:
            negative_count += 1
    return positive_count, negative_count

reviews = ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."]

for review in reviews:
    positive_count, negative_count = tally(review)
    
    print(f"In this review - {review} - there are this many positive words: {positive_count}.")
    print(f"In this review - {review} - there are this many negative words: {negative_count}.")

# Task 3

hobbit = ("The Hobbit is set in Middle-earth and follows home-loving Bilbo Baggins, the hobbit of the title, who joins the wizard Gandalf and the thirteen dwarves of Thorin's Company, on a quest to reclaim the dwarves' home and treasure from the greedy, fire-breathing dragon Smaug.")

def summarize(hobbit):
    words = hobbit.split()
    summary = " ".join(words[:30])
    summary += "..."
    print(summary)

summarize(hobbit)