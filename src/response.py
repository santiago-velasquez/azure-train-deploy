import json
import numpy as np
import os
import joblib
import pandas as pd

def init():
    global model
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It's the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION).
    # For multiple models, it points to the folder containing all deployed models (./azureml-models).
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'rf1.pkl')
    model = joblib.load(model_path)

def run(raw_data):
    print()
    data = np.array(json.loads(raw_data)['data'])
    cols = ['race', 'gender', 'discharge_disposition_id',
       'admission_source_id', 'medical_specialty', 'diag_1', 'diag_2',
       'diag_3', 'max_glu_serum', 'A1Cresult', 'metformin', 'glimepiride',
       'glipizide', 'glyburide', 'pioglitazone', 'rosiglitazone',
       'insulin', 'change', 'diabetesMed', 'age', 'time_in_hospital',
       'num_medications', 'number_outpatient', 'number_emergency',
       'number_inpatient', 'requests_1', 'requests_10']
    df = pd.DataFrame(columns=cols)
    df.loc[0] = data

    # Make prediction.
    y_hat = model.predict(df)
    # You can return any data type as long as it's JSON-serializable.
    # setosa_clases = [0,1]
    # return the result back
    return json.dumps({"Binary Predicted Class": int(y_hat[0])})