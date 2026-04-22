# Sentiment Analysis Model Report

## Objective

The goal of this project is to build a sentiment analysis model that classifies user reviews as either **positive (1)** or **negative/neutral (0)** based on their textual content.

---

## Dataset Overview

- Total reviews: **490**
- Features:
  - `review_text` (raw text input)
  - `rating` (1–5 scale)
  - `date` datetime
- Target transformation:
  - Ratings ≥ 4 → Positive (1)
  - Ratings ≤ 3 → Negative/Neutral (0)

The dataset shows a relatively balanced distribution between positive and negative reviews, with slightly more negative samples in the test set.

---

## Methodology

### 1. Text Preprocessing
- Converted text to lowercase
- Removed noise and unnecessary characters (if applied)
- Prepared text for vectorization

### 2. Feature Extraction
- Used **TF-IDF (Term Frequency–Inverse Document Frequency)**
- Limited to top features for efficiency and noise reduction
- Converted text into numerical feature vectors for modeling

### 3. Model Selection
- Logistic Regression was used as the classification model due to its strong performance on high-dimensional sparse text data.

---

## Model Performance

### Evaluation Metrics:

- **Accuracy:** 0.796 (~80%)

### Classification Report:

- Class 0 (Negative/Neutral):
  - Precision: 0.79
  - Recall: 0.92
  - F1-score: 0.85

- Class 1 (Positive):
  - Precision: 0.81
  - Recall: 0.59
  - F1-score: 0.69

---

## Key Insights

- The model achieves strong overall performance with approximately **80% accuracy**.
- It performs better at identifying **negative reviews**, with high recall (0.92), meaning most negative reviews are correctly detected.
- Performance on **positive reviews is weaker in recall (0.59)**, indicating that the model misses a portion of positive sentiments.
- This imbalance suggests that negative reviews contain stronger and more distinguishable linguistic signals (e.g., “crash”, “bug”, “slow”).

---

## Interpretation

The model demonstrates a slight bias toward predicting negative sentiment. This is likely due to:
- Stronger emotional language in negative reviews
- Imbalanced feature representation in text data
- Subtle or less explicit wording in positive reviews

Despite this, Logistic Regression with TF-IDF provides a strong and interpretable baseline for sentiment classification.

---

## Next Steps

- Try alternative models such as Naive Bayes or Linear SVM
- Improve recall for positive sentiment class
