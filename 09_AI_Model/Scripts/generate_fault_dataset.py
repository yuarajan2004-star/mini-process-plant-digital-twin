import pandas as pd
import random

rows = []

# NORMAL
for _ in range(1000):

    rows.append([
        round(random.uniform(0.90,1.10),2),
        round(random.uniform(100,120),2),
        round(random.uniform(25,32),2),
        0
    ])

# LOW PRESSURE
for _ in range(1000):

    rows.append([
        round(random.uniform(0.60,0.84),2),
        round(random.uniform(100,120),2),
        round(random.uniform(25,32),2),
        1
    ])

# HIGH PRESSURE
for _ in range(1000):

    rows.append([
        round(random.uniform(1.16,1.40),2),
        round(random.uniform(100,120),2),
        round(random.uniform(25,32),2),
        2
    ])

# LOW FLOW
for _ in range(1000):

    rows.append([
        round(random.uniform(0.90,1.10),2),
        round(random.uniform(50,94),2),
        round(random.uniform(25,32),2),
        3
    ])

# HIGH TEMPERATURE
for _ in range(1000):

    rows.append([
        round(random.uniform(0.90,1.10),2),
        round(random.uniform(100,120),2),
        round(random.uniform(33,40),2),
        4
    ])

# COMBINED FAULT
for _ in range(1000):

    rows.append([
        round(random.uniform(0.60,0.84),2),
        round(random.uniform(50,94),2),
        round(random.uniform(33,40),2),
        5
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "PT101",
        "FT101",
        "TT101",
        "Fault_Code"
    ]
)

df.to_csv(
    "/home/yuarajan_s/Mini_Process_Plant_DT/09_AI_Model/Dataset/Fault_Data/fault_dataset.csv",
    index=False
)

print(df.head())

print("\nRows:", len(df))
