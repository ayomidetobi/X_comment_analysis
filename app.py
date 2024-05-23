from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from pymongo import MongoClient
# URL to open
web = "https://x.com/search?q=wema%20bank&src=typed_query&f=top"

# Path to chromedriver executable
path = "C:/Users/HP/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=path)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service)
driver.get(web)
driver.maximize_window()

# Function to extract tweet data
def get_tweet(element):
    try:
        user = element.find_element(By.XPATH, ".//span[contains(text(), '@')]").text
        text = element.find_element(By.XPATH, ".//div[@lang]").text
        tweet_data = [user, text]
    except:
        tweet_data = ['user', 'text']
    return tweet_data

# Initialize data storage
user_data = []
text_data = []
tweet_ids = set()
scrolling = True

while scrolling:
    tweets = WebDriverWait(driver, 2000).until(
        EC.presence_of_all_elements_located((By.XPATH, "//article[@role='article']"))
    )
    print(len(tweets))
    for tweet in tweets[-15:]:  # Adjust the number based on how many tweets you want to capture per scroll
        tweet_list = get_tweet(tweet)
        tweet_id = ''.join(tweet_list)
        if tweet_id not in tweet_ids:
            tweet_ids.add(tweet_id)
            user_data.append(tweet_list[0])
            text_data.append(" ".join(tweet_list[1].split()))

    # Get the initial scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(2)
        # Calculate new scroll height and compare it with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # Check if new content is loaded
            scrolling = False
            break
        else:
            last_height = new_height
            break

# Quit the driver
driver.quit()

# Save the extracted tweets to a CSV file
df_tweets = pd.DataFrame({'user': user_data, 'text': text_data})
df_tweets.to_csv('tweets_pagination.csv', index=False)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['twitter_data']  # Database name
collection = db['tweets']  # Collection name

# Convert DataFrame to dictionary format suitable for MongoDB
data_dict = df_tweets.to_dict("records")

# Insert data into MongoDB collection
collection.insert_many(data_dict)

# Print a confirmation message
print(f"Data has been successfully inserted into MongoDB.")

print(df_tweets)
