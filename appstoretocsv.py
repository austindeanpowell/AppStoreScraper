from app_store_scraper import AppStore
import pandas as pd
import csv

# Define the app (Co-Star example)
co_star = AppStore(country="us", 
                   #Can chage sort.NEWEST with other functions to analyze
                   sort=Sort.NEWEST,
                   app_name="co-star-personalized-astrology",
                   # Within the App URL from Browser the app_id will be the last 10 digits within the URL
                   app_id=1264782561)

# Fetch reviews (limit to 50)
co_star.review(how_many=50)

# Convert to DataFrame
df = pd.DataFrame(co_star.reviews)

# Save to CSV
df.to_csv("co_star_reviews.csv", index=False, encoding="utf-8")

#Will save locally into VSCODE or device when code Runs. Spotlight search on device if unable to find
print("✅ Data saved as co_star_reviews.csv")
