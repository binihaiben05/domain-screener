# Personal Housing Project
## Project Overview
Australia has been a popular place for property investment in the past decades. With more and more and more people have fully vaccinated for the COVID-19 and the rising expectation of re-opening the border, the real estate market in Australia starts regaining people’s attention. More and more investors are willing to purchase the property in Australia. In this project, this project aims to analyze the historical data of the Australian properties in the past 2 decades. At the end of this project, based on the evidence from the data analysis, we will develop the solution for investors with certain amount of budget to find suburbs that are most suitable for investment. 



### Key Tools Used in This Project
* Python
* SQL
* Tableau
* PowerBI
* Jupyter notebook
* Docker

## Data Source

The housing data is scrapped from [Domain](https://www.domain.com.au/?mode=sold) website

## Data Profile

The data covers the information of sold-properties from 2000 to July 2021. The dataset has 862714 rows and 15 columns.

### Sample Data

| listing_id | suburb      | sold_date    | sold_type | property_type | is_rural      | price           | beds | baths | parking | land_size | address_lat | address_lng   | address_street       | rn       | 
|----------|-------------|---------------|----------|-------|-----------------|----------------|----------------------|----------------|-----------|------------|---------------|--------|-----------|-----------|
| 2004017953    | cremorne-nsw-2090 | 31 Oct 2010 | auction     |  House  | 1.0 | 1250000 | 3.0 | 15.0        | 2.0  | 85.0 | -33.8208771       | 151.231964         | 88 Macpherson St  | 1 |
| 2004113258    | killara-nsw-2071 | 22 Oct 2003 | private treaty     |  House  | 1.0 | 1445000 | 4.0 | 2.0  | 2.0  | 562.0 | -37.84444       | 145.120941         | 153 Station Street  | 1 |
| 2004234169    | mascot-nsw-2020 | 17 Mar 2011 | private treaty     |  ApartmentUnitFlat  | 1.0 | 445000 | 1.0 | 1.0        | 1.0  | | -33.9207039       | 151.189316        | 42/635 Gardeners Road  | 1 |

* **note**: the sample data can be found in the properties_clean.csv in the [domain_scanner.zip](https://github.com/GuoshuaiWang/housing_project/blob/master/domain_screener.zip)

## Code Instruction
### Step 1: download file
* bigtable.sql
* distance_to_CBD.ipynb
* properties_cleaned.csv
* table_by perperty_type.ipynb
* tocsv.py
* utils.py

### Step 2: data scrapping (optional)
The **utils.py** file is used for reading, writting, and downloading JSON file from the website. This file is imported into the **tocsv.py** file for data scrapping. We can run the following code in the terminal to transfer the JSON file into the csv file for the analysis purpose.
```
directory/domain_scanner/tocsv.py > properties_cleaned.csv
```
The result of data scrapping is already included in the zip file, and the file name is **properties_cleanned.csv**.

### Step 3: data filtering
This step is to fine-tune the dataset into a samller dataset for analysis purpose. For doing this, we can run the SQL code of the **bigtable.sql** file to generate a new dataset. This new dataset removes observations that we do not need, sets the budget constrain, and  keeps the refined information for analysis. The new dataset can be used for finding median price for each suburb, housing price comparison with previous year, affordability analysis, and data visulization using data visulization tools (Tableau and PowerBI). 

### Step 4: Distance to CBD calculation
Since the distance of a property to CBD is a very important factor that investors consider, in this step, we use the dataset generated in the previous step and run the code of **distance_to_CBD.ipynb** to add the distance of each suburb to the CBD to its corresponding state. 

### Step 5: Generate csv files based on property type
In the final step, we can run the table_by_property_type.ipynb to generate several csv files based on different property type and number of bedrooms. Specifically, there are 6 csv files will be generated, and they are
* 1 bed apartment
* 2 beds apartment
* 3 beds apartment
* 2 beds house
* 3 beds house
* 4 beds house
* 5 beds house

The purpose of this step is to generate csv files for people who have minimal knowledge about EXCEL to look up properties based on their individual needs.

## Analytical Report
The final analytical report can be found domian_screener_report.pdf
This report contains all the detailed processes about this project, which includes 
* problem statement
* data source
* data profilling
* assumptions 
* persona analysis
* data visulization
