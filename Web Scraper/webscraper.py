import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url, tag, class_name, attributes):
    try:
        # Send a request to the website and get the HTML content
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        html_content = response.content

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the data you need
        data = []
        for item in soup.find_all(tag, class_=class_name):
            extracted_data = {attr: item[attr] for attr in attributes if item.has_attr(attr)}
            extracted_data['text'] = item.get_text(strip=True)
            data.append(extracted_data)

        # Convert the data into a DataFrame
        df = pd.DataFrame(data)

        # Save the DataFrame to a CSV file
        csv_file = 'output.csv'
        df.to_csv(csv_file, index=False)

        print(f"Data has been scraped and saved to {csv_file}")
        return csv_file

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = 'https://books.toscrape.com'
tag = 'article'
class_name = 'product_pod'
attributes = ['href', 'title']

scrape_website(url, tag, class_name, attributes)
