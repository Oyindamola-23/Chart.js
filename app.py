import os
import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sales_chart.html')

@app.route('/get_data')
def get_data():
    # Replace this with the logic to get your cleaned data
    month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Actual sales data for different summaries
    sales_summary_monthly = [425, 437, 313, 651, 259, 207, 187, 417, 422, 874, 11213, 17250, 16213, 251, 27180, 13277, 142, 439, 393, 265, 338, 240, 165, 106, 245, 347, 293, 202, 155, 309, 327, 306, 274, 265, 264, 145, 49, 3, 18, 8, 10]
    sales_summary_quarterly = [1175, 1117, 1026, 29337, 43644, 13858, 996, 511, 885, 666, 907, 674, 49, 3, 36]
    sales_summary_yearly = [32655, 59009, 3132, 88]

    # Actual quantity data for different summaries
    quantity_summary_monthly = [0.003614351, 0.005138563, 0.003905661, 0.003763533, 0.003709707, 0.001844792, 0.002466289, 0.004609542, 0.003314104, 0.029059618,
                                1.039461166, 1.868383395, 1.728546713, 0.003176367, 3.392237857, 0.862422264, 0.001481868, 0.005558304, 0.010169632, 0.017614115,
                                0.009220642, 0.0052152, 0.001657004, 0.002687995, 0.004683432, 0.004744569, 0.002955254, 0.002559557, 0.002414396, 0.002623863, 0.005433869,
                                0.003670921, 0.003430498, 0.003204695, 0.000466076, 5.67E-05, 1.69E-06, 0.001398494, 0.000470618, 0.000312609]
    quantity_summary_quarterly = [0.012658575, 0.009318033, 0.010389936, 2.93690418, 5.123960937, 0.869462436, 0.016092846, 0.012115996, 0.007929207, 0.011728653,
                                   0.007101268, 5.67E-05, 1.69E-06, 0.002181721]
    quantity_summary_yearly = [2.969270723, 0.038875124, 0.002240071]

    # Additional labels for quarterly and yearly summaries
    quarter_labels = ['Q1', 'Q2', 'Q3', 'Q4']
    year_labels = [2019, 2020, 2021, 2022]

    return jsonify(
        month_labels=month_labels,
        quarter_labels=quarter_labels,
        year_labels=year_labels,
        sales_summary_monthly=sales_summary_monthly,
        sales_summary_quarterly=sales_summary_quarterly,
        sales_summary_yearly=sales_summary_yearly,
        quantity_summary_monthly=quantity_summary_monthly,
        quantity_summary_quarterly=quantity_summary_quarterly,
        quantity_summary_yearly=quantity_summary_yearly
    )

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['date of sales'], dayfirst=True)
    selected_columns = ['productId', 'price in kobo', 'total sales', 'date of sales', 'storeId', 'Price in Naira']
    df = df[selected_columns].dropna()
    return df

def generate_sales_summary(df, summary_folder):
    df['year'] = df['date of sales'].dt.year
    df['quarter'] = df['date of sales'].dt.quarter
    df['month'] = df['date of sales'].dt.month
    df['quantity'] = df['total sales'] / df['price in kobo']  # Assuming 'price in kobo' represents price per unit

    sales_summary_monthly = df.groupby(['year', 'month'])[['total sales']].sum().reset_index()
    quantity_summary_monthly = df.groupby(['year', 'month'])[['quantity']].sum().reset_index()

    sales_summary_quarterly = df.groupby(['year', 'quarter'])[['total sales']].sum().reset_index()
    quantity_summary_quarterly = df.groupby(['year', 'quarter'])[['quantity']].sum().reset_index()

    sales_summary_yearly = df.groupby(['year'])[['total sales']].sum().reset_index()
    quantity_summary_yearly = df.groupby(['year'])[['quantity']].sum().reset_index()

    sales_summary_monthly.to_csv(f'{summary_folder}/sales_summary_monthly.csv', index=False)
    quantity_summary_monthly.to_csv(f'{summary_folder}/quantity_summary_monthly.csv', index=False)

    sales_summary_quarterly.to_csv(f'{summary_folder}/sales_summary_quarterly.csv', index=False)
    quantity_summary_quarterly.to_csv(f'{summary_folder}/quantity_summary_quarterly.csv', index=False)

    sales_summary_yearly.to_csv(f'{summary_folder}/sales_summary_yearly.csv', index=False)
    quantity_summary_yearly.to_csv(f'{summary_folder}/quantity_summary_yearly.csv', index=False)

if __name__ == "__main__":
    file_path = 'dabarobjects_data.csv'  # Update with the correct file path
    summary_folder = 'sales_summary'  # Update with the desired summary folder name
    df = load_and_preprocess_data(file_path)
    generate_sales_summary(df, summary_folder)
    print("Code execution completed.")
    print("Current working directory:", os.getcwd())  # Print current working directory
    print("File path:", os.path.abspath(__file__))  # Print absolute path of the script
    app.run(debug=True)
