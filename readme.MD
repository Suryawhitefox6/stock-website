# Interactive Stock Data Downloader

This project allows users to fetch stock data for Nifty 50 stocks using the Yahoo Finance API. The frontend is designed with an interactive UI where users can input the stock ticker symbol and a date range to retrieve stock data. The backend is built using Flask and communicates with the Yahoo Finance API to fetch and display stock data.

## Deployed Website

You can access the live version of the application at:

[https://nifty50-data-downloader.onrender.com/](https://nifty50-data-downloader.onrender.com/)

## Features

- **User Input**: Users can input a stock ticker symbol, select a date range, and request data.
- **Interactive Table**: Once the data is fetched, it is displayed in an interactive table showing the stock's open, high, low, close, and volume for each date.
- **Data Download**: Users can download the stock data as a CSV file.
- **Responsive Design**: The application is fully responsive and works well on both desktop and mobile devices.
- **Gradient Background**: The app features a visually appealing gradient background that changes over time.

## Installation and Setup

### Prerequisites

- Python 3.6+
- Flask
- yFinance (for downloading stock data)

### Steps to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/stock-data-downloader.git
   cd stock-data-downloader

2. Install dependencies:
pip install -r requirements.txt
3. Run the Flask application:
   python app.py
4. Open your browser and navigate to http://127.0.0.1:5000/ to view the app.

###Backend Configuration

The backend is built using Flask and communicates with the Yahoo Finance API through the yfinance Python library. It listens for POST requests from the frontend and fetches the stock data for the given ticker and date range.

###Frontend Overview
HTML: The frontend is built with simple HTML forms and uses Bootstrap for styling.
CSS: A custom CSS stylesheet is used to add a gradient background and animations.
JavaScript/jQuery: Used for handling form submission and dynamically displaying the stock data. It also handles the download functionality.
API Endpoint
POST /: Receives the ticker symbol, start date, and end date from the frontend, fetches the stock data from Yahoo Finance using yfinance, and returns the data as a JSON response.
###Dependencies
Flask – A lightweight Python web framework.
yfinance – Python library to fetch stock data from Yahoo Finance.
Bootstrap – For responsive design.
jQuery – For handling AJAX requests.

###Usage
-Navigate to the deployed website at https://nifty50-data-downloader.onrender.com/.
-Enter a stock ticker symbol (e.g., ZEEL).
-Select the start and end dates.
-Click the "Fetch Data" button to retrieve the stock data.
-The data will be displayed in a table. You can toggle the visibility of the table by clicking the "Toggle Data View" button.
-To download the data, click the "Download Data" button, which will generate a CSV file.

###Acknowledgements
The data is fetched using the yfinance library, which provides easy access to historical stock data from Yahoo Finance.
The frontend uses Bootstrap for responsive design and jQuery for handling AJAX requests.
