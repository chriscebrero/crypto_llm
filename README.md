# Cryptocurrency Data Summary Project

This project provides a Jupyter Notebook that fetches recent cryptocurrency data, processes it using the CoinGecko API, and generates a concise summary using a language model from Hugging Face's `transformers` library. The notebook features an interactive UI created with `ipywidgets` for selecting a cryptocurrency symbol, fetching data, and displaying a summary along with recent prices.

[OPEN THE PROJECT ON COLAB](https://colab.research.google.com/github/chriscebrero/crypto_llm/blob/master/cryptocurrency_summary.ipynb)

## Project Overview

The main goals of this project are to:
1. Fetch recent cryptocurrency price data for a given cryptocurrency symbol using the [CoinGecko API](https://www.coingecko.com/en/api).
2. Use a language model to generate a natural-language summary of recent price trends.
3. Present the summary and recent data in a user-friendly interface within the Jupyter Notebook.

## Features

- **User Input**: Enter a cryptocurrency symbol (e.g., `bitcoin`, `ethereum`) to fetch data.
- **Summary Generation**: Generates a report (pre-summary) and summary of recent cryptocurrency price trends using Facebook Bart-Large-CNN summarization model.
- **Data Display**: Displays recent price data in a tabular format.

## Requirements

To run this notebook, you need the following Python packages:

```plaintext
ipywidgets==7.7.1
pandas<2.2.0  # As cudf requires pandas <2.2
numpy<2.0.0  # As many dependencies are incompatible with numpy 2.0.2
gensim<4.4.0
langchain<0.3.5  # To stay compatible with numpy<2.0
matplotlib<3.8.0
tf-keras<2.17.0  # tf-keras requires tensorflow<2.18
tensorflow<2.18
torch==2.5.0  # Compatible with torchaudio and torchvision
torchvision==0.20.0+cu121  # Compatible with torch 2.5.0 and CUDA 12
torchaudio==2.5.0+cu121
yfinance==0.2.48
transformers==4.31.0
```

## Setup Instructions (Google Colab)
1. Run the scripts at the top to make sure all dependencies are included, and being able to access the helper functions

## Setup Instructions (Locally)
1. Clone the repository
`git clone <repository_url>`

2. Install Dependencies
- Navigate to the directory and run `pip install -r requirements.txt`

3. Run the notebook (open cryptocurrency_summary.ipynb)

## Usage Instructions
1. Launch the notebook
2. Enter a cryptocurrency symbol (i.e. bitcoin, ethereum)
3. Click thee Fetch & Summarize button to retrieve recent data
4. View output
5. Notebook should display the report of the crypto prices, a summary, and a table showing the latest daily prices.

