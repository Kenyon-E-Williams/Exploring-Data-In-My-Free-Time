#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 23:56:42 2022

@author: kwill
"""

import pandas as pd
breasts=pd.read_csv("/Users/kwill/Downloads/chick-fil-a-nutrition.csv",index_col=0)
Sodium=(int(15)/int(100))
Calories=int(2000)/int(100)
Saturated=int(1300)/int(100)
Cholesterol=int(3000)/int(100)
Fiber=int(29)/int(100)
Sugar=int(34)/int(100)
Protein=int(113)/int(100)
#Important to note here ^ that i divided by 100 to get into terms of percentage after below is calculated
breasts[" Percent of reccommended Sodium Intake (MG) "]=(breasts["Sodium (MG)"]/((Sodium)))
breasts["Percent of reccommended Daily Calories"]=(breasts["Calories"]/(Calories))
breasts["Percent of reccommended Daily Saturated Fats (G)"]=(breasts["Sat. Fat (G)"]/(Saturated))
breasts["Percent of reccommended Daily Cholesterol (MG)"]=(breasts["Cholesterol (MG)"]/(Cholesterol))
breasts["Percent of reccommended Daily Fiber (G)"]=(breasts["Fiber (G)"]/(Fiber))
breasts["Percent of reccommended Daily Sugar (G)"]=(breasts["Sugar (G)"]/(Sugar))
breasts["Percent of reccommended Daily Protien (G)"]=(breasts["Protein (G)"]/(Protein))
print(breasts)

##Look into web scraping online menu for menu and pricing items 
##Basing this off of AMA, Mayo Clinic and UCSF Reccomendeded intake values 
##Cal=AMA,Sat Fat= AMA,Cholesterol= UCSF,Carbs= Mayo Clinic, Fiber= Mayo Clinic,Sugar= AMA,Protein=Mayo Clinic

## So now that you have your nutrional database set up the flow is as follows
## DB1 --> Web Scrape --> Save to seperate CVS --> merge them on index row (same amount of nutrition facts as same amount of prices on the menu * important to remember nutrition DB doesnt include drinks other than Doctor Pepper and Coca-Cola
#Final Step Will be analysis, what is the most reasonably priced and healthy item on Chik-Fil-A Menu (maybe top 5?)
