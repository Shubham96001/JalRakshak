import pandas as pd
import numpy as np
from sklearn import svm
import os


data_path = os.path.join('data', 'sample.csv')

def train_svm_model():
    try:
        df = pd.read_csv(data_path)
        
        # Features: pH, Turbidity, Dissolved Oxygen (DO) [cite: 78, 79]
        X = df[['pH', 'Turbidity', 'DO']]
        # Target: 1 for Safe, 0 for Polluted 
        y = df['Target']

        # 2. Initialize SVM Classifier 
        # We use a linear kernel for efficiency on Raspberry Pi 
        clf = svm.SVC(kernel='linear', probability=True)
        clf.fit(X, y)
        
        print("✅ SVM Model trained successfully on JalRakshak dataset.")
        return clf
    except FileNotFoundError:
        print("🚨 Error: Training data not found. Please add sample_water_data.csv to /data.")
        return None

# 3. Prediction Function for the API/UI 
def predict_quality(model, ph, turbidity, do):
    if model:
        prediction = model.predict([[ph, turbidity, do]])
        status = "Safe" if prediction[0] == 1 else "Polluted"
        return status
    return "Unknown"

# model initialization from the name jal rkashak 
jal_rakshak_brain = train_svm_model()

if __name__ == "__main__":
    # prediction of the data to test model functionality
    test_result = predict_quality(jal_rakshak_brain, 7.2, 1.5, 8.0)
    print(f"Test Analysis: {test_result}")
