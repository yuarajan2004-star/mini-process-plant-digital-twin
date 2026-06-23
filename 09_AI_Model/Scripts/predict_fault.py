import joblib
import pandas as pd

model = joblib.load(
    "/home/yuarajan_s/Mini_Process_Plant_DT/09_AI_Model/Models/fault_classifier.pkl"
)

sample = pd.DataFrame(
    [
        [0.72,70,37]
    ],
    columns=[
        "PT101",
        "FT101",
        "TT101"
    ]
)

prediction = model.predict(sample)

fault_map = {

    0:"NORMAL",

    1:"LOW PRESSURE",

    2:"HIGH PRESSURE",

    3:"LOW FLOW",

    4:"HIGH TEMPERATURE",

    5:"COMBINED FAULT"
}

print(
    "\nPrediction:",
    fault_map[
        prediction[0]
    ]
)
