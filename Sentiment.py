from textblob import TextBlob

text = "This is a good project"
analysis = TextBlob(text)

print(analysis.sentiment)