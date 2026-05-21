import pandas as pd

df = pd.read_csv("C:/Users/HP Laptop/Documents/python data cleaning/messy_indian_cities.csv")
# print (df.head())

# Removes duplicate rows 
df_cleaned = df.drop_duplicates()
# print(df.isnull().sum())

# to clean the unncessary space and to change the text into title case 
df['City'] = df['City'].str.strip().str.title()

# to find the unique values in the city column 
sorted_unique_cities = sorted(df['City'].dropna().unique())
# print(sorted_unique_cities)

corrections ={
 'Ahmadabad':'Ahmedabad',
 'Ahmdabad':'Ahmedabad',
 'Amd':'Ahmedabad',
 'Ahmedabad':'Ahmedabad',
 'Amdavad':'Ahmedabad',
 'Bambai':'Mumbai',
 'Bangalore':'Bengaluru',
 'Banglore':'Bengaluru',
 'Begaluru':'Bengaluru',
 'Bengaluru':'Bengaluru',
 'Bhopal':'Bhopal',
 'Bhopl':'Bhopal',
 'Blr':'Bengaluru',
 'Bombay':'Mumbai',
 'Calcutta':'Kolkata',
 'Ccu':'Kolkata',
 'Chenai':'Chennai',
 'Chennai':'Chennai',
 'Delhi':'Delhi',
 'Delhy':'Delhi',
 'Delli':'Delhi',
 'Dilli':'Delhi',
 'Dl':'Delhi',
 'Hyd':'Hyderabad',
 'Hyderabad':'Hyderabad',
 'Hyderbad':'Hyderabad',
 'Hydrabad':'Hyderabad',
 'Indor':'Indore',
 'Indore':'Indore',
 'Jaipur':'Jaipur',
 'Jaypur':'Jaipur',
 'Kolkaata':'Kolkata',
 'Kolkata':'Kolkata',
 'Kolkataaa':'Kolkata',
 'Lakhnow':'Lucknow',
 'Lko':'Lucknow',
 'Lucknow':'Lucknow',
 'Luknow':'Lucknow',
 'Maa':'Chennai',
 'Madras':'Chennai',
 'Mumai':'Mumbai',
 'Mumb.':'Mumbai',
 'Mumbay':'Mumbai',
 'Nagpoor':'Nagpur',
 'Nagpr':'Nagpur',
 'Nagpur':'Nagpur',
 'New Delhi':'Delhi',
 'Ngp':'Nagpur',
 'Patna':'Patna',
 'Patnaa':'Patna',
 'Pink City':'Jaipur',
 'Poona':'Pune',
 'Pune':'Pune',
 'Thana':'Thane',
 'Thane':'Thane',

}

#  Map the corrections dictionary to the City column
df['City']= df['City'].map(corrections)

#  Check the results! Let's print out the unique values of our cleaned column
# print("--- CLEANED UNIQUE CITIES ---")
# print(df['City_Cleaned'].dropna().unique())

# Fill all the missing (NaN) values with 'Not Given'
df['City']= df['City'].fillna('Not Given')

# Save the final cleaned data to a new file
df.to_csv('perfectly_cleaned_indian_cities.csv', index=False)
print("\n🎉 Success! Saved your clean data to 'perfectly_cleaned_indian_cities.csv'")