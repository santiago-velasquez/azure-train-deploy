import pandas as pd
import joblib
import argparse
import os
from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder



if __name__ == "__main__":
    print('Iniciando')
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_path',
        type=str,
        default='.',
        help='Path to the training data'
    )

    args = parser.parse_args()
    print("===== DATA =====")
    print("DATA PATH: " + args.data_path)
    print("LIST FILES IN DATA PATH...")
    print(os.listdir(args.data_path))
    print("================")



    df = pd.read_csv(f'{args.data_path}/cleanData.csv', index_col=[0])
    print('Cargado el archivo correctamente')

    cat_features = ['race', 'gender', 'discharge_disposition_id', 'admission_source_id',
                    'medical_specialty', 'diag_1', 'diag_2', 'diag_3', 'max_glu_serum',
                    'A1Cresult', 'metformin', 'glimepiride', 'glipizide', 'glyburide',
                    'pioglitazone', 'rosiglitazone', 'insulin', 'change', 'diabetesMed']

    num_features = ['age', 'time_in_hospital', 'num_medications', 'number_outpatient',
                    'number_emergency', 'number_inpatient', 'requests_1', 'requests_10']

    y = ['readmitted']

    X = cat_features + num_features

    X_train, X_test, y_train, y_test = train_test_split(df[X], df[y], test_size=0.30, random_state=27)

    numeric_transformer = Pipeline(steps = [
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', MinMaxScaler())])

    categorical_transformer = Pipeline(steps = [
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers = [
            ('num', numeric_transformer, num_features),
            ('cat', categorical_transformer, cat_features)])

    rf1 = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', RandomForestClassifier())])
    rf1.fit(X_train,y_train)
    joblib.dump(rf1, 'outputs/rf1.pkl')
    print('Finished training. Model saved.')