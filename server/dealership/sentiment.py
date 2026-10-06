try:
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
except ImportError:
    analyzer = None

def analyze_sentiment(text):
    if not text:
        return 'neutral'
    
    text_lower = text.lower()
    
    if analyzer:
        scores = analyzer.polarity_scores(text)
        compound = scores['compound']
        if compound >= 0.05:
            return 'positive'
        elif compound <= -0.05:
            return 'negative'
        else:
            return 'neutral'
    else:
        # Fallback dictionary matching
        pos_words = ['fantastic', 'great', 'excellent', 'amazing', 'good', 'superb', 'awesome', 'love', 'happy', 'best', 'outstanding', 'wonderful']
        neg_words = ['bad', 'terrible', 'horrible', 'poor', 'slow', 'worst', 'disappointed', 'hate', 'rude', 'awful', 'overpriced']
        
        pos_count = sum(1 for w in pos_words if w in text_lower)
        neg_count = sum(1 for w in neg_words if w in text_lower)
        
        if pos_count > neg_count:
            return 'positive'
        elif neg_count > pos_count:
            return 'negative'
        return 'neutral'
