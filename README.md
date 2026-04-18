## 📊 Science Based Targets – Data Processing Project
# 📌 Project Name
---
**Science Based Targets Data Pipeline**

- 📖 Description

* This project focuses on cleaning and merging data files downloaded from the Science Based Targets Initiative (SBTi) Target Dashboard.
* 
* The dashboard provides two separate datasets:
* 
* Companies data
* Targets data

This script:

1. Cleans both datasets by removing unnecessary columns/data
2. Processes and standardizes the structure
3. Merges them into a single, analysis-ready file
4. 
5. The final output is saved as:
6. sciencebasedtargets_data.xlsx

---

## 🌐 Data Source

* Download the datasets manually from:
👉 https://sciencebasedtargets.org/target-dashboard

---

## ⚙️ Setup Instructions

1. Download Data Files
   * Visit the Target Dashboard link above
   * Download both datasets:
   * Companies dataset
   * Targets dataset
   * Place the downloaded Excel files into the project folder
   
2. Update File Names

##### Open the script:

* filemergeanddataclean.py

Update the file names if needed:

      * company_df = pd.read_excel("companies-excel.xlsx")
      * targets_df = pd.read_excel("targets-excel.xlsx")
      * Make sure these match your downloaded file names.

3. Run the Script

   * Execute the script:
   * python filemergeanddataclean.py

---

## 📦 Output  

### After running the script, a merged and cleaned dataset will be generated:
sciencebasedtargets_data.xlsx

🧹 Data Processing Steps 

* The script performs the following operations:
* Removes irrelevant/unwanted columns
* Cleans missing or inconsistent data
* Standardizes column formats
* Merges company and target datasets
---

## 🛠️ Requirements  
* Make sure you have the following installed:
* pip install pandas openpyxl
---

✅ Notes
Ensure the downloaded files are in Excel format (.xlsx)
File names must match those used in the script
Update the script if the dashboard file format changes