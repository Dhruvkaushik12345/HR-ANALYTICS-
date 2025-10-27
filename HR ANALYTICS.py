# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 13:18:52 2025

@author: DHRUV KAUSHIK
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Load the dataset
file_path = r"C:\Users\DELL\Desktop\data sets\HR\HRDataset_v14.csv"
df = pd.read_csv(file_path)

# --- 1. DATE CONVERSION AND FEATURE ENGINEERING ---

# Convert date columns to datetime objects
date_cols = ['DateofHire', 'DateofTermination', 'LastPerformanceReview_Date', 'DOB']
for col in date_cols:
    # Use errors='coerce' to turn unparseable dates into NaT (Not a Time)
    df[col] = pd.to_datetime(df[col], errors='coerce')


# ---2. Fill missing values logically ---
today = datetime.today()

df['DateofHire'] = df['DateofHire'].fillna(df['DateofHire'].median())
df['DateofTermination'] = df['DateofTermination'].fillna(today)
df['LastPerformanceReview_Date'] = df['LastPerformanceReview_Date'].fillna(today - timedelta(days=365))
df['DOB'] = df['DOB'].fillna(df['DOB'].median())

# Ensure consistent date format for Power BI
for col in date_cols:
    df[col] = df[col].dt.strftime('%Y-%m-%d')

# --- 3. Standardize Text Columns ---
df['Employee_Name'] = df['Employee_Name'].str.strip().str.title()
df['Position'] = df['Position'].str.strip().str.title()
df['Department'] = df['Department'].str.strip().str.title()

#  --- Standrize Text Column ---
df['TermReason'] = df['TermReason'].fillna('Active')

# --- 4. Create Flag for Voluntary Turnover ---
# This flag is a 1 or 0 and is the most important part for our dashboard.
# We focus on people who CHOSE to leave (not fired)

df['Voluntary Term Flag'] = np.where(df['TermReason'] == 'N/A-StillEmployed' , 1 , 0)

df['Employee_Name'] = df['Employee_Name'].str.replace(',' ,"")

df.to_csv(r"C:\Users\DELL\Desktop\data sets\HR\Cleaned HRDataset.csv", index = False)
print("\nfile is uploaded after all changes'Cleaned HRDataset.csv'")

























