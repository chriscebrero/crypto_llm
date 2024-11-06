from transformers import pipeline
from datetime import datetime

# Initialize the Hugging Face summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_crypto_info(data):
    formatted_data = ". ".join(
        [
            f"On {datetime.strptime(date, '%Y-%m-%d').strftime('%A, %B %d, %Y')}, "
            f"the price of the cryptocurrency was ${info['Price']:.2f}"
            for date, info in data  # Iterate in the order provided (most recent first)
        ]
    ) + "."
    return formatted_data

def generate_crypto_summary(data):
    # Assuming 'data' is sorted with the most recent date first
    # formatted_data = ". ".join(
    #     [
    #         f"On {datetime.strptime(date, '%Y-%m-%d').strftime('%A, %B %d, %Y')}, "
    #         f"the price of the cryptocurrency was ${info['Price']:.2f}"
    #         for date, info in data  # Iterate in the order provided (most recent first)
    #     ]
    # ) + "."
    formatted_data = generate_crypto_info(data)

    # Use the summarizer on the formatted text
    print("Formatted data for summarization:", formatted_data)
    summary = summarizer(
    formatted_data, 
    max_length=100, 
    min_length=50, 
    do_sample=True, 
    temperature=0.7, 
    top_k=50
    )
    return summary[0]["summary_text"]
