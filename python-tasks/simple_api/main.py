#_______________________________Built simple APIs using FastAPI_________________________________

""" 
API : Application Programming Interface
     It is the way to connect / communicate two different services on the internet.

    Database---> Web Server---> API---> Internet---> Web Application
    Database-----------------API-------------------- Web Server
"""

#_________________________________________FASTAPI________________________________________
"""
🚀 What is FastAPI?
FastAPI is a modern, high-performance Python web framework used to build APIs (Application Programming Interfaces).

🏆 Why use FastAPI?
-Very fast (like Node.js or Go!)
-Easy to learn
-Automatic docs with Swagger UI
-Built on top of Starlette (for web) and Pydantic (for data validation)
"""

from fastapi import FastAPI
import random

app = FastAPI()

# WE will built two simple GET endpoints

# - side_hustles
# - money_quotes

side_hustles = [
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom-designed products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "Youtube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!",
    "App Development - Create mobile and web applications for buisnesses!"
]

money_quotes = [
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "An investment in knowledge pays the best interest. - Benjamin Franklin",
    "Never spend your money before you have earned it. - Thomas Jefferson",
    "Time is more valuable than money. You can get more money, but you cannot get more time. - Jim Rohn",
    "Do not save what is left after spending, but spend what is left after saving. - Warren Buffett",
    "The stock market is filled with individuals who know the price of everything, but the value of nothing. - Philip Fisher",
    "Formal education will make you a living; self-education will make you a fortune. - Jim Rohn",
    "Wealth consists not in having great possessions, but in having few wants. - Epictetus",
    "If you live for having it all, what you have is never enough. - Vicki Robin",
    "Opportunity is missed by most people because it is dressed in overalls and looks like work. - Thomas Edison",
    "It’s not your salary that makes you rich, it’s your spending habits. - Charles A. Jaffe"
]

# @ is decorator in python

@app.get("/side_hustles")
def get_side_hustle(apiKey : str):
    """Returns a random side hustle idea"""
    if apiKey != "1234567890":
        return {"error" : "Invalid Api Key"}

    return {"side_hustle" : random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes(apiKey : str):
    """Returns a random money quote"""
    if apiKey != "1234567890":
        return {"error" : "Invalid Api Key"}

    return {"money_quote" : random.choice(money_quotes)}

# Swagger : It is a way to write API documentation (auto-generated docs)