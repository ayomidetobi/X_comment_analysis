# Twitter Sentiment Analysis Project

## Overview

This project uses Selenium to scrape tweets about a specific brand from Twitter to perform sentiment analysis on the collected data. The workflow includes logging into Twitter, navigating to the search page, extracting tweet data, saving it to a CSV file, and inserting it into a MongoDB database.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- ChromeDriver (compatible with your version of Chrome)
- Required Python libraries:
  - `selenium`
  - `pandas`
  - `pymongo`
  - `python-dotenv`

## Installation

1. **Install Python libraries:**

   You can install the required libraries using pip:

   ```bash
   pip install selenium pandas pymongo python-dotenv


### 2. Check Chrome Version

Open Google Chrome and navigate to `chrome://settings/help` to find your Chrome version. You'll need this version number to download the compatible ChromeDriver.

### 3. Download ChromeDriver

1. Go to the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/).
2. Find the version that matches your Chrome version and download the appropriate file for your operating system.
3. Download the ZIP file for Windows (e.g., `chromedriver_win32.zip`).

### 4. Extract and Install ChromeDriver


1. Extract the downloaded ZIP file. You will get a file named `chromedriver.exe`.
2. Place `chromedriver.exe` in a directory of your choice. For example, you might place it in:

   ```plaintext
   C:/Users/HP/Downloads/chromedriver-win64/

## 5. Configuration

### Update Login Credentials

Replace the placeholders for username and password in the script with your actual Twitter login credentials.

```python
username.send_keys("your_username")  # Replace with your actual Twitter username
password.send_keys("your_password")  # Replace with your actual Twitter password
```

## 6. Note on Security

Be cautious with hardcoding sensitive information such as login credentials. Consider using environment variables or configuration files for added security.

### Example Using Environment Variables

1. **Create a `.env` File**

   Create a file named `.env` in the same directory as your script with the following content:

   ```plaintext
   TWITTER_USERNAME=your_username
   TWITTER_PASSWORD=your_password
   ```
```python
load_dotenv()

# Get credentials from environment variables
username = os.getenv("TWITTER_USERNAME")
password = os.getenv("TWITTER_PASSWORD")
```
## 7. How to Run

### Save the Script

Save the provided Python script to a file, for example, `apps.py`.

### Run the Script

Execute the script using Python:

```bash
python apps.py
```

## The Script Performs the Following Actions

- **Logs into Twitter:** The script automates the login process using your Twitter credentials.
- **Navigates to the Specified Search Page:** Once logged in, the script navigates to the search page for the specified brand or keyword.
- **Extracts Tweets:** The script collects tweets from the search results, including user handles and tweet content.
- **Saves the Extracted Data to a CSV File:** The collected data is saved into a CSV file for further analysis.
- **Inserts the Data into a MongoDB Database:** The script connects to a MongoDB database and inserts the extracted tweet data.

