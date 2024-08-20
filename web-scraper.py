import pandas as pd
import time
import requests
from bs4 import BeautifulSoup
import fake_useragent

user_agent = fake_useragent.UserAgent()

product_names = []
prices = []
descriptions = []
reviews = []

for page_num in range(2, 12):
    url = "https://www.flipkart.com/search?q=smart+phones+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(page_num)
    
    # New User-Agent for each request
    headers = {'User-Agent': user_agent.random}
    
    r = requests.get(url, headers=headers)
    print(r)
    
    # Adding a delay of 2 seconds between requests
    time.sleep(2)

    soup = BeautifulSoup(r.text, "lxml")


    # Finding the desired container elements
    boxes = soup.find_all('div', class_="DOjaWF gdgoEp")  # Assuming multiple containers per page

    for box in boxes:
        # Extracting product names
        names = box.find_all("div", class_="KzDlHZ")
        for name in names:
            product_names.append(name.text.strip())  
        
        print(product_names)

        # Extracting prices
        prices_container = box.find("div", class_="Nx9bqj _4b5DiR")  # Assuming a single price container
        if prices_container:
            price = prices_container.text.strip()
            prices.append(price)
        else:
            prices.append("NA")  # Handling missing price with a placeholder
        
        print(prices)

        # Extracting  descriptions 
        descriptions_container = box.find("ul", class_="G4BRas")  
        if descriptions_container:
            description = descriptions_container.text.strip()
            descriptions.append(description)
        else:
            descriptions.append("NA")  # Handling missing description with a placeholder

        print(description)

        # Extracting reviews 
        reviews_container = box.find("div", class_="XQDdHH")  
        if reviews_container:
            review = reviews_container.text.strip()
            reviews.append(review)
        else:
            reviews.append("NA")  # Handling missing review with a placeholder

        print(reviews)

# Creating the DataFrame 
data_frame = pd.DataFrame({
    "Product Name": product_names,
    "Price": prices,
    "Description": descriptions,
    "Reviews": reviews
})

print(data_frame)

data_frame.to_csv("Flipkart_Web_Scraped_Data_of_mobiles_under_50000", index=False)  # Avoiding index column