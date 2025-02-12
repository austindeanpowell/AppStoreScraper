from app_store_scraper import AppStore
import pandas as pd
import csv

# Define the app (Co-Star example)
co_star = AppStore(country="us", 
                   sort=Sort.NEWEST,
                   app_name="co-star-personalized-astrology", 
                   app_id=1264782561)

# Fetch reviews (limit to 50)
co_star.review(how_many=50)

# Convert to DataFrame
df = pd.DataFrame(co_star.reviews)

# Save to CSV
df.to_csv("co_star_reviews.csv", index=False, encoding="utf-8")

print("✅ Data saved as co_star_reviews.csv")
