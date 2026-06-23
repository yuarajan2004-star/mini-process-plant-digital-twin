import pandas as pd

FILE = "/home/yuarajan_s/Mini_Process_Plant_DT/09_AI_Model/Dataset/plant_historian.csv"

df = pd.read_csv(FILE)

print("\nDATASET INFO\n")

print(df.info())

print("\nFIRST 5 ROWS\n")

print(df.head())

print("\nSTATISTICS\n")

print(df.describe())
