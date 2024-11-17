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

