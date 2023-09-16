import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    
    numeric_columns = data.select_dtypes(include=['number']).columns
    imputer = SimpleImputer(strategy='mean')
    data[numeric_columns] = imputer.fit_transform(data[numeric_columns])
    
    scaler = StandardScaler()
    numeric_features = ['Air Quality','Water Pollution','Deforestation'
                        ]  
    data[numeric_features] = scaler.fit_transform(data[numeric_features])
    
    
    return data
