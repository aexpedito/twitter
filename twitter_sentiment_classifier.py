from textblob import TextBlob


def sentiment_classifier(text):
    classification = TextBlob(text)
    result = "Neutral"

    if classification.sentiment.polarity < -0.2:
        if classification.sentiment.subjectivity > 0.5:
            result = "Negative"
        else:
            result = "Neutral"
    if classification.sentiment.polarity > 0.2:
        if classification.sentiment.subjectivity > 0.5:
            result = "Positive"
        else:
            result = "Neutral"


    return  result
