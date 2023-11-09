from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import json

def perform_forecast(data):
    df = pd.DataFrame(data)
    df['ds'] = pd.to_datetime(df['ds'])
    df = df.set_index('ds')

    df['month'] = df.index.month

    model = LinearRegression()

    X = np.array(df['month']).reshape(-1, 1)
    y = df['y']
    model.fit(X, y)

    future_months = np.array(range(13, 25)).reshape(-1, 1)
    predicted_sales = model.predict(future_months)

    predicted_sales_array = []

    for i, sales in enumerate(predicted_sales, 1):
        predicted_sales_array.append({'ds': f'2023-{i:02d}-01', 'y': round(sales, 2)})

    json_output = json.dumps(predicted_sales_array, indent=2)
    return json_output

sales_data_json = input()
sales_data = json.loads(sales_data_json)
forecast_result = perform_forecast(sales_data)
print(forecast_result)