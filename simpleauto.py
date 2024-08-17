import random
from datetime import datetime

# List of inspirational quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt"
]

# Generate a random quote
quote_of_the_day = random.choice(quotes)

# Get current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Create content for README
content = f"# Quote of the Day\n\n**Date:** {current_date}\n\n{quote_of_the_day}"

# Write content to README.md
with open("README.md", "w") as file:
    file.write(content)

print("README.md updated successfully!")
