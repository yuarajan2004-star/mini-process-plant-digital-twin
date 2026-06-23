import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)

FILE = "/home/yuarajan_s/Mini_Process_Plant_DT/09_AI_Model/Dataset/Fault_Data/fault_dataset.csv"

df = pd.read_csv(FILE)

X = df[
    [
        "PT101",
        "FT101",
        "TT101"
    ]
]

y = df["Fault_Code"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nMODEL ACCURACY\n")
print(accuracy)

print("\nCONFUSION MATRIX\n")
print(confusion_matrix(
    y_test,
    predictions
))

print("\nCLASSIFICATION REPORT\n")
print(classification_report(
    y_test,
    predictions
))

joblib.dump(
    model,
    "/home/yuarajan_s/Mini_Process_Plant_DT/09_AI_Model/Models/fault_classifier.pkl"
)

print("\nMODEL SAVED\n")
