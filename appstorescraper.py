from app_store_scraper import AppStore
import json

# Define the app (Co-Star example)
co_star = AppStore(country="us", 
                   app_name="co-star-personalized-astrology",
                   app_id=1264782561)

# Fetch reviews (limit to 50)
co_star.review(how_many=50)

# Convert reviews to JSON format
reviews_json = json.dumps(co_star.reviews, indent=4, sort_keys=True, default=str)

# Print the result
print(reviews_json)
