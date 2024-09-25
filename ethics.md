# Ethical Considerations for Data Collection and Sentiment Analysis

This project involves the collection and analysis of publicly available data about public companies, specifically their stock performance and related news articles, using APIs and web scraping. The following ethical considerations outline how the data is handled responsibly and transparently, in alignment with ethical data collection practices.

## Purpose of Data Collection

The purpose of this project is to analyze sentiment about public companies based on news article titles and stock market data. The goal is to demonstrate how sentiment analysis and data collection can be applied for educational purposes, research, and practical insights into stock market behavior. The data is not intended for commercial use and does not involve the storage of personal data.

Initially, the idea was to perform sentiment analysis on the **full content** of the news articles. However, this approach was reconsidered due to the potential violation of intellectual property rights and terms of service of news providers. As a result, the project was modified to focus solely on the **titles of the articles**, which are considered publicly available metadata and are generally not subject to the same restrictions.

## Data Sources and APIs Used

The data for this project is collected from several trusted sources:

- **Yahoo Finance** for stock data: The project retrieves publicly available stock data for companies, including stock price changes.
  - Website: [https://finance.yahoo.com/](https://finance.yahoo.com/)
  
- **NewsAPI** for news articles: The project fetches news article titles related to public companies using the NewsAPI service, which provides access to publicly available news content metadata.
  - API Documentation: [https://newsapi.org/](https://newsapi.org/)

- **BeautifulSoup** for web scraping: Web scraping is performed using `BeautifulSoup` to extract stock-related data from public websites like Yahoo Finance.
  - Library: [https://www.crummy.com/software/BeautifulSoup/](https://www.crummy.com/software/BeautifulSoup/)

## Ethical Web Scraping and API Use

### Responsible Use of APIs
This project adheres to the guidelines provided by the APIs used. In particular, the project complies with the terms of service and usage limits of NewsAPI, ensuring that API rate limits are respected and that data usage aligns with their intended purpose (educational and research applications).

### Web Scraping Practices
The web scraping component of this project focuses on publicly accessible, non-restricted pages. The following principles are upheld to ensure ethical scraping:

- **Rate Limiting**: The project ensures that scraping is performed responsibly, with minimal requests made to avoid placing excessive load on Yahoo Finance’s servers.
- **Respecting `robots.txt`**: The project honors the rules outlined in the `robots.txt` files of websites. Pages restricted by `robots.txt` are not scraped.
- **No Scraping of Restricted Content**: The project only scrapes publicly available data and does not attempt to access password-protected, paywalled, or otherwise restricted content.
- **Legal Compliance**: The project follows the terms of service of Yahoo Finance and other data sources used. If any data source prohibits scraping, the project would immediately cease scraping activities for that source.

### Data Handling and Privacy

- **No Personal Identifiable Information (PII)**: This project does not collect or process any personal user data. The data collected relates solely to public company information, stock data, and **news article titles**, all of which are publicly available.
- **Data Security**: Should any future development involve the collection of sensitive or proprietary data, appropriate measures will be implemented to ensure secure storage and handling. As of now, no private or sensitive data is collected.
- **Exclusion of Sensitive Data from Version Control**: Any data that may be collected for the purpose of analysis will be excluded from version control by adding it to `.gitignore` to prevent public exposure. This ensures that no unnecessary data is made publicly available on GitHub.

## Data Usage and Limitations

- **Educational and Research Use**: The data collected and analyzed through this project is used for educational and research purposes only. The sentiment analysis is intended to demonstrate the integration of web scraping, APIs, and natural language processing techniques. No commercial use of the data is involved.
- **Avoiding Violations of Terms of Service**: While the initial approach considered performing sentiment analysis on the full content of news articles, this was avoided to ensure compliance with the terms of service and ethical guidelines related to intellectual property rights of news content providers. Only article titles, which are considered metadata, are used in the sentiment analysis.

This project aims to balance the technical capabilities of data collection with ethical responsibility and respect for the rights of data owners. All activities are conducted with transparency, minimal disruption, and compliance with legal and ethical guidelines.
