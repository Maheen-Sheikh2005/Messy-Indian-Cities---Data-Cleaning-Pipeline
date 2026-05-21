# 🏙️ Messy Indian Cities - Data Cleaning Pipeline

## 📌 Project Overview
This project takes a highly messy, human-entered dataset of Indian cities and transforms it into a clean, standardized format using a mix of **Python (Pandas)** and **Microsoft Excel shortcuts**. 

Data entered by humans often has typos, weird spacing, and random abbreviations. This project builds a reliable pipeline to fix those errors automatically.

---

## 🏗️ Step 1: How the Messy Data Was Generated
To simulate a real-world corporate scenario where users type whatever they want into a form, a script was used to generate 101 rows of messy data. It deliberately introduced common human errors into a list of 15 major Indian cities:
* **Extra Spaces:** `  Mumbai ` or `Delhi  `
* **Random Capitalization:** `bAnGaLoRe` or `kolkataaa`
* **Spelling Typos:** `Ahmdabad`, `Hyderbad`, or `Bhopl`
* **City Codes & Nicknames:** `BLR`, `CCU`, `DL`, or `Pink City`
* **Missing Fields:** Blank rows showing up as `NaN` (Not a Number)

---

## 🧼 Step 2: How We Cleaned It
Instead of fixing all 101 rows manually, we engineered a smart, hybrid workflow that combines Python's processing power with Excel's speed:

### 1. Removing Extra Spaces and Fixing Case (Python)
We used Python to strip away accidental leading/trailing spaces and forced every word into proper "Title Case" (where only the first letter is capitalized). This instantly grouped similar typos together.

### 2. The Alphabetical Sorting Shortcut (Python)
We extracted only the *unique* city variations and sorted them alphabetically. This forced typos like *Ahmadabad* and *Amdavad* to sit right next to each other, making them easy to spot.

### 3. The Excel "Code Generator" Trick (Excel)
Instead of typing a massive dictionary in Python, we pasted the unique messy list into Excel. 
* We dragged down the correct spellings in Column B.
* We used an Excel formula `=A3 & ":" & CHAR(39) & B3 & CHAR(39) & ","` to automatically write the Python dictionary code for us!

### 4. Mapping & Handling Missing Data (Python)
We pasted that Excel-generated dictionary straight back into VS Code using `.map()`. Finally, we caught all the blank data gaps and safely filled them with the label `'Not Given'` using `.fillna()`.

---

## 📈 Final Results
* **Before:** 56 unique, chaotic variations and typos spread across 101 rows.
* **After:** 15 perfectly standardized master categories + 1 clear `'Not Given'` category for missing data.
* **Output:** The pristine data is automatically exported to a clean file called `perfectly_cleaned_indian_cities.csv`.

---

## 🛠️ Tech Stack Used
* **Language:** Python 3
* **Libraries:** Pandas
* **Tools:** VS Code, Microsoft Excel

