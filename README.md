# Sentiment Analysis of Strava App Reviews

## Overview
This project implements a fine-grained sentiment analysis pipeline for user reviews of the Strava mobile application. Inspired by research from Guzman & Maalej (2014), the goal is to move beyond traditional document-level sentiment classification and instead extract feature-level insights from user feedback.

The system identifies specific app features (e.g., subscription, workouts, Garmin integration) and determines the sentiment expressed toward each feature, enabling more actionable product insights.

---

## Dataset

The dataset consists of **490 Strava app reviews** collected from the Apple App Store using the public RSS feed API.

- Source: Apple iTunes Customer Reviews RSS Feed  
- App ID: `426826309` (Strava)  
- Fields: `review`, `rating`, `date`  

Example API endpoint:
https://itunes.apple.com/rss/customerreviews/page=1/id=426826309/sortBy=mostRecent/json

The data was programmatically extracted using Python and stored locally as:
[data/strava_reviews.csv](https://github.com/geoffreycloud/ios-app-review-insights/blob/master/data/strava_reviews.csv)


---

## Pipeline

The NLP pipeline consists of the following stages:

1. **Text Preprocessing**
   - Lowercasing
   - Removal of punctuation and noise
   - Tokenization using spaCy
   - Stopword and irrelevant term filtering

2. **Feature Extraction (Aspect Mining)**
   - Noun phrase extraction using spaCy
   - Filtering of generic terms (e.g., "app", "this")
   - Normalization of similar features:
     - "my subscription" --> "subscription"
     - "premium", "paywall" --> grouped conceptually

3. **Sentiment Analysis**
   - VADER sentiment scoring (range: -1 to 1)
   - Sentence-level sentiment computation

4. **Aspect-Sentiment Linking**
   - Assign sentence sentiment to features appearing in that sentence

5. **Aggregation**
   - Feature frequency
   - Average sentiment
   - Sentiment variance

---

## Results

### Feature-Level Insights

| Feature        | Count | Avg Sentiment |
|---------------|------:|--------------:|
| runs          | 8     | 0.641         |
| workouts      | 7     | 0.559         |
| data          | 8     | 0.419         |
| subscription  | 16    | -0.083        |
| premium       | 10    | -0.022        |
| garmin        | 10    | -0.109        |

**Key Insight:**
- Fitness features (runs, workouts) --> strongly positive sentiment  
- Monetization features (subscription, premium) --> negative sentiment  
- Integration features (Garmin) --> inconsistent (high variance)

---

## Baseline Model

A traditional sentiment classifier was implemented for comparison:

- **Model:** Logistic Regression  
- **Features:** TF-IDF  
- **Accuracy:** 0.80  

### Performance:

Precision (Negative): 0.79
Recall (Negative): 0.92

Precision (Positive): 0.81
Recall (Positive): 0.59

### Top Positive Words:
- love, great, best, awesome, run

### Top Negative Words:
- subscription, paywall, support, feature, watch

---

## Limitations

While the baseline model performs well for overall sentiment classification, it fails to provide actionable insights because:

- It assigns only one label per review  
- It cannot distinguish sentiment across multiple features  
- It lacks contextual understanding of feature-specific issues  

This reinforces the importance of fine-grained sentiment analysis.

---

## 📚 References

- Guzman, E., Maalej, W. (2014). *How Do Users Like This Feature?* IEEE Intelligent Systems  
- Haddi, E., Liu, X., Shi, Y. (2013). *The Role of Text Pre-processing in Sentiment Analysis*  
- Pagano, D., Maalej, W. (2013). *User Feedback in the AppStore*  

---

## Future Improvements

- Dependency parsing for better aspect-sentiment linking  
- Transformer-based models (e.g., BERT)  
- Larger dataset for improved generalization  
- Clustering features into higher-level categories  
