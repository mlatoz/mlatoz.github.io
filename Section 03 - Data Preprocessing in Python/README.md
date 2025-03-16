# Data Preprocessing in Python

## Python Code
```python
  import pandas as pd
  import numpy as np
  from sklearn.preprocessing import StandardScaler, MinMaxScaler
  
  # 1. Handling Missing Values
  def handle_missing_values(df, strategy="mean", fill_value=None):
      """
      Handles missing values in a DataFrame.
      
      Parameters:
      df (pd.DataFrame): Input DataFrame
      strategy (str): "mean", "median", "mode", or "constant"
      fill_value: Used when strategy="constant"
      
      Returns:
      pd.DataFrame: DataFrame with missing values handled
      """
      if strategy == "mean":
          return df.fillna(df.mean())
      elif strategy == "median":
          return df.fillna(df.median())
      elif strategy == "mode":
          return df.fillna(df.mode().iloc[0])
      elif strategy == "constant":
          return df.fillna(fill_value)
      else:
          raise ValueError("Invalid strategy. Choose from 'mean', 'median', 'mode', 'constant'.")
  
  # 2. Scaling and Normalization
  def scale_data(df, method="standard"):
      """
      Scales numerical columns in a DataFrame.
      
      Parameters:
      df (pd.DataFrame): Input DataFrame
      method (str): "standard" for StandardScaler, "minmax" for MinMaxScaler
      
      Returns:
      pd.DataFrame: Scaled DataFrame
      """
      scaler = StandardScaler() if method == "standard" else MinMaxScaler()
      numeric_cols = df.select_dtypes(include=np.number).columns
      df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
      return df
  
  # 3. Parsing Dates
  def parse_dates(df, date_columns):
      """
      Converts specified columns to datetime format.
      
      Parameters:
      df (pd.DataFrame): Input DataFrame
      date_columns (list): List of column names to parse
      
      Returns:
      pd.DataFrame: DataFrame with parsed dates
      """
      for col in date_columns:
          df[col] = pd.to_datetime(df[col], errors='coerce')
      return df
  
  # 4. Handling Character Encodings
  def fix_encoding(file_path, encoding="utf-8"):
      """
      Reads a file with a specified encoding.
      
      Parameters:
      file_path (str): Path to the file
      encoding (str): Encoding type (e.g., 'utf-8', 'latin1', etc.)
      
      Returns:
      pd.DataFrame: DataFrame read from the file
      """
      return pd.read_csv(file_path, encoding=encoding, errors='replace')
  
  # 5. Handling Inconsistent Data Entry
  def standardize_column_values(df, column, mapping=None):
      """
      Standardizes column values to maintain consistency.
      
      Parameters:
      df (pd.DataFrame): Input DataFrame
      column (str): Column to standardize
      mapping (dict): Dictionary mapping inconsistent values to standard ones
      
      Returns:
      pd.DataFrame: DataFrame with standardized values
      """
      if mapping:
          df[column] = df[column].replace(mapping)
      df[column] = df[column].str.lower().str.strip()
      return df
```
<hr>

## Download Resources
* <a href="Data Preprocessing in Python.ipynb">Python Notebook Preview</a>|<a href="Data Preprocessing in Python.ipynb" download>Download</a>
* <a href="Data Preprocessing.py" download>Python Template Code</a>
* <a href="Data Preprocessing in Python.ipynb" download>Python Notebook</a>
* <a href="Data.csv" download>Dataset</a>
<hr>

<a href="../Section 02 - Part 01 - Data Preprocessing">«Previous</a> | <a href="../Section 04 - Data Preprocessing in R">Next»</a>
