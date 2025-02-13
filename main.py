import pandas as pd
from selenium import webdriver

file_path = input("path excel")

format_path = r"{}".format(file_path).replace('"', ' ')

df = pd.read_excel(r"C:\Users\name1\Downloads\raw_data_2025-02-13T00_41_08.xlsx", header=0)

filtered_df = df[df['price'] > 100]

link_column = df['product_link'].to_list();

for i in link_column:
  print(link_column[i])