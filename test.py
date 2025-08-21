# test.py
import requests
import pandas as pd
from datetime import datetime

# Fetch the latest public events from GitHub
url = "https://api.github.com/events"
response = requests.get(url)

if response.status_code != 200:
    raise Exception(f"Failed to fetch data: {response.status_code}")

events = response.json()

# Normalize into a DataFrame
df = pd.json_normalize(events)

# Select only a few useful columns
df = df[["id", "type", "repo.name", "actor.login", "created_at"]]

# Create filename with timestamp
filename = f"github_events_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"

# Save to CSV
df.to_csv(filename, index=False)

print(f"Wrote {len(df)} events to {filename}")
