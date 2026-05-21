import pandas as pd
import numpy as np
import random

# Seed for consistency
np.random.seed(2026)
random.seed(2026)

# 15 Target Indian Cities with ~50 total messy variations
city_chaos = {
    'Mumbai': ['Mumbai', 'mumbai', 'MUMBAI', '  Mumbai  ', 'Bambai', 'Bombay', 'mumbay', 'Mumb.', 'Mumai'],
    'Delhi': ['Delhi', 'delhi', 'DELHI', ' New Delhi', 'delhy', 'Dilli', 'DL', 'delhi ', 'Delli'],
    'Bengaluru': ['Bengaluru', 'begaluru', 'Bangalore', 'bangalore', 'BLR', 'bengaluru', 'Banglore', '  BANGALORE  '],
    'Kolkata': ['Kolkata', 'kolkata', 'Calcutta', 'calcutta', 'Kolkata ', 'kolkaata', 'CCU', 'Kolkataaa'],
    'Chennai': ['Chennai', 'chennai', 'Madras', 'madras', 'Chenai', 'CHENNAI  ', 'MAA'],
    'Hyderabad': ['Hyderabad', 'hyderabad', 'HYD', 'hydrabad', 'Hyderbad', ' hyd', 'Hyderabad '],
    'Pune': ['Pune', 'pune', 'PUNE', ' poona', 'Poona', 'pune ', 'Pune  '],
    'Ahmedabad': ['Ahmedabad', 'ahmedabad', 'Amdavad', 'amdavad', 'Ahmadabad', 'AMD', 'ahmdabad'],
    'Jaipur': ['Jaipur', 'jaipur', 'JAIPUR', 'Jaypur', ' Pink City', 'jaipur '],
    'Lucknow': ['Lucknow', 'lucknow', 'LKO', 'luknow', 'Lucknow ', 'Lakhnow'],
    'Nagpur': ['Nagpur', 'nagpur', 'NAGPUR', 'nagpur ', ' Nagpoor', 'Nagpr', 'NGP'],
    'Indore': ['Indore', 'indore', 'INDORE', 'indor', 'Indore '],
    'Thane': ['Thane', 'thane', 'Thana', 'thane ', 'THANE'],
    'Bhopal': ['Bhopal', 'bhopal', 'BHOPAL', 'bhopal ', 'Bhopl'],
    'Patna': ['Patna', 'patna', 'PATNA', 'patna ', 'Patnaa']
}

# Flatten the dictionary to create a giant pool of messy inputs
all_messy_variants = [variant for variants in city_chaos.values() for variant in variants]

names = ['Rohan', 'Pooja', 'Aditya', 'Anjali', 'Arjun', 'Meera', 'Yash', 'Kiran', 'Siddharth', 'Tanvi']
surnames = ['Sharma', 'Joshi', 'Patil', 'Nair', 'Mehta', 'Das', 'Singh', 'Kulkarni', 'Reddy', 'Mishra']

# Generate 1,000 rows
data = {
    'Lead_ID': range(5001, 6001),
    'Customer_Name': [f"{random.choice(names)} {random.choice(surnames)}" for _ in range(1000)],
    'City': [random.choice(all_messy_variants) if random.random() > 0.04 else np.nan for _ in range(1000)],
    'Pincode': [random.randint(110001, 850001) for _ in range(1000)]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('messy_indian_cities.csv', index=False)

print("🔥 Challenge Generated! Saved as 'messy_indian_cities.csv'")
print("Rows: 1,000 | Target Cities: 15 | Messy Variations: Over 50+")