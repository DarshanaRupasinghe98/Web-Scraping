import os
from bs4 import BeautifulSoup
import pandas as pd

# empty lists for item names and prices
item_names = []
price_list = []

# directory path where HTML files are located
dir_path = r'C:\Users\ACER\Downloads\Webpages'


# Loop through each HTML file in the directory
for file_name in os.listdir(dir_path):
    # Check if file is an HTML file
    if file_name.endswith('.html'):
        # Open file
        with open(os.path.join(dir_path, file_name), 'r') as file:
            # Parse HTML using BeautifulSoup
            soup = BeautifulSoup(file, 'html.parser')
            
            # Find all product names and prices
            product_names = soup.select('span.w_V_DM')
            product_prices = soup.select('div[data-automation-id="product-price"]')
            
            # Append item names and prices to respective lists
            for name, price in zip(product_names, product_prices):
                item_names.append(name.text.strip())
                price_list.append(price.text.strip())

# pandas DataFrame with the item names and prices
df = pd.DataFrame({'Product_Name': item_names, 'Price': price_list})

# Export DataFrame to Excel file
excel_file_path = r"E:\3rd year\2nd Semester\IS 3005 - Statistics in Practice I\IS3005_ExtractedData.xlsx"
df.to_excel(excel_file_path, index=False)




