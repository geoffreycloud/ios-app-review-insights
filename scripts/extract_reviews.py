import requests
from requests.exceptions import HTTPError
import pandas as pd


def extract():
    """
    Extracts reviews of the Strava app from the Apple App Store RSS feed and returns a DataFrame.

    Returns:
        pd.DataFrame: A DataFrame containing the reviews, ratings, and dates of the reviews.
    """
    all_reviews = []
    try:
        # CustomerReviews RSS page depth is limited to 10
        for page in range(1, 11):  

        # API endpoint for fetching reviews of the Strava app on the Apple App Store
            url = f"https://itunes.apple.com/rss/customerreviews/page={page}/id=426826309/sortBy=mostRecent/json"
            
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful
            
            if response.status_code != 200:
                break
            
            data = response.json()
            
            if 'entry' not in data['feed']:
                break
            
            for entry in data['feed']['entry'][1:]:
                review = entry['content']['label']
                rating = int(entry['im:rating']['label'])
                date = entry['updated']['label']
                
                all_reviews.append({
                    "review": review,
                    "rating": rating,
                    "date": date
                })

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    df = pd.DataFrame(all_reviews).drop_duplicates()

    return df

def load(df, file_path):
    """
    Loads the DataFrame into a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to be saved.
        file_path (str): The path where the CSV file will be saved.
    """
    df.to_csv(file_path, index=False)

if __name__ == "__main__":

    df = extract()
    load(df, "data/strava_reviews.csv")