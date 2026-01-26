import re

text="Yesterday at 09:45:30, developer @Code_Master shared the build update on https://myapp.dev/status?id=200. The invoice was mailed to billing.team_2025@service.org. Trending topics include #AIWave and #FutureTech 🚀. The system processed a payment of 2.750 ETH (Tx: 0xAB91Ff2039D451A9cC72). API logs show: POST /api/v2/data/user_root_#77. Status response was {OK}. Bonjour! Comment ça va? (Hello! How are you?)."

hashtaags=re.findall(r"#\+",text)
mentions=re.findall(r"@\w+",text)
emails=re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b",text)
urls=re.findall(r"https?:/^S+",text)
dates=re.findall(r"\b\d{1,2}^d{1,2,}^d{4}\b",text)
tokens=re.findall(r"\b\w+\b",text)

print("Hashtags:",hashtaags)
print("Mentions:",mentions)
print("Emails:",emails)
print("URLs:",urls)
print("Dates:",dates)
print("Tokens:",tokens)
