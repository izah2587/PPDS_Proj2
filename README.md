# Public Company Sentiment Analysis Tool

## Project Summary

This project is a Python-based tool designed to gather stock data and perform sentiment analysis on news articles related to public companies. The program retrieves stock performance data from Yahoo Finance and news article titles from NewsAPI, providing users with a simple command-line interface to interact with. The tool then calculates an overall sentiment score based on the news articles and stores the results, including the company’s stock change and sentiment score, in a CSV file.

The goal of the project is to demonstrate the integration of web scraping, API usage, and sentiment analysis in a way that is both educational and practical for analyzing media sentiment and stock market behavior.

## Methods to Gather Data

The project utilizes the following key methods and libraries to gather and process data:

### 1. **Stock Data via Web Scraping (requests and BeautifulSoup)**
   - The `requests` library is used to send an HTTP GET request to Yahoo Finance to retrieve stock data.
   - The `BeautifulSoup` library from `bs4` parses the retrieved HTML content to extract the stock percentage change for the specified company. The stock change data is found within specific HTML elements, which are located using CSS selectors and attributes.

### 2. **News Articles via NewsAPI**
   - The `NewsAPI` is used to fetch news articles related to the selected public company. It retrieves the titles of the top 20 news articles and processes them for further sentiment analysis. This ensures that the data collected is up-to-date and relevant to the company’s current performance.

### 3. **Sentiment Analysis (TextBlob)**
   - The `TextBlob` library is employed to perform sentiment analysis on the article titles. Each title’s polarity score (ranging from -1 for negative sentiment to 1 for positive sentiment) is calculated. The average sentiment score across all article titles is then computed to give an overall sentiment for the company.

### 4. **Data Storage in CSV**
   - The results, including the company name, symbol, stock change, and sentiment score, are written to a CSV file (`company_sentiment.csv`). This allows users to keep track of historical sentiment scores and stock changes for different companies.

## Usage

The tool provides a simple command-line interface where users can input the name of a public company, and the program automatically retrieves the relevant stock data and news articles. The results, including the company’s stock change and overall sentiment score, are displayed to the user and saved in the CSV file for future reference.

### Running the Project

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
