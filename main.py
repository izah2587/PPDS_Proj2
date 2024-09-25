from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from newsapi import NewsApiClient
from textblob import TextBlob
import csv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Get the API keys from the .env file
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
MARKET_STACK_API_KEY = os.getenv('MARKET_STACK_API_KEY')

# Initialize the NewsApiClient with the API key from .env
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

# Function to fetch the stock symbol
def get_stock_symbol(company_name):
    # Use the MarketStack API key from the .env file
    url = f"http://api.marketstack.com/v1/tickers?search={company_name}&access_key={MARKET_STACK_API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    # Extract and return stock symbol from the response data
    return data['data'][0]['symbol'] if 'data' in data and data['data'] else None

# Function to scrape stock change percentage
def scrape_stock_change(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract and return stock change percentage
    stock_change = soup.find('fin-streamer', {'data-field': 'regularMarketChangePercent'}).text
    return stock_change

# Function to fetch top 20 articles related to the company using stock symbol to refine the search
def get_company_articles(company_name, symbol):
    query = f'"{company_name}" AND "{symbol}"'
    articles = newsapi.get_everything(q=query, language='en', sort_by='relevancy', page_size=20)
    return articles['articles']

# Function to perform sentiment analysis on the article title
def analyze_sentiment(title):
    blob = TextBlob(title)
    return blob.sentiment.polarity

# Function to write results to a CSV file
def write_to_csv(company_name, symbol, stock_change, average_sentiment):
    current_date = datetime.now().strftime('%Y-%m-%d')
    csv_file = 'company_sentiment.csv'
    file_exists = os.path.isfile(csv_file)

    with open(csv_file, mode='a', newline='') as file:
        fieldnames = ['company_name', 'company_symbol', 'date', 'stock_change', 'sentiment_score']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header if the file is new
        if not file_exists:
            writer.writeheader()

        # Write the company data to the CSV
        writer.writerow({
            'company_name': company_name,
            'company_symbol': symbol,
            'date': current_date,
            'stock_change': stock_change,
            'sentiment_score': average_sentiment
        })

# Get user input for the company name
company_name = input("Enter the name of a public company: ")

# Get and display the stock change for the given company
symbol = get_stock_symbol(company_name)
if symbol:
    stock_change = scrape_stock_change(symbol)
else:
    print(f"Could not retrieve stock symbol for {company_name}")
    stock_change = "N/A"  # Assign a placeholder if the stock symbol is not found

# Fetch and analyze sentiment of the top 20 articles for the company
articles = get_company_articles(company_name, symbol)

total_sentiment = 0  # Variable to store the cumulative sentiment score

for article in articles:
    title = article['title']
    sentiment_score = analyze_sentiment(title)
    total_sentiment += sentiment_score  # Accumulate sentiment scores for final average

# Calculate the average sentiment score for the company
average_sentiment = total_sentiment / len(articles) if articles else 0

# Print the final sentiment score for the company
print(f"\nOverall Sentiment Score for {company_name}: {average_sentiment:.2f}")

# Write the overall sentiment score to the CSV file
write_to_csv(company_name, symbol, stock_change, average_sentiment)
