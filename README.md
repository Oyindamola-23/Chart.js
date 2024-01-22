# Sales Summary Dashboard

This Python code is designed to create a simple web-based sales summary dashboard using Flask. The dashboard includes charts displaying monthly, quarterly, and yearly sales and quantity summaries based on provided data.

## Getting Started

1. Clone the repository or download the code files.

```bash
git clone https://github.com/your-username/your-repo.git
```

2. Install the required dependencies.

```bash
pip install -r requirements.txt
```

3. Update the file path and summary folder name in the `__main__` block.

```python
file_path = 'path/to/your/data.csv'
summary_folder = 'your_summary_folder'
```

## Prerequisites

- Python 3.x
- Flask
- pandas

## Usage

1. Run the script to generate sales summaries and start the Flask web application.

```bash
python your_script.py
```

2. Open a web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the sales summary dashboard.

3. The `/get_data` endpoint provides the necessary data in JSON format for chart rendering.

## Data Preprocessing

The code includes a `load_and_preprocess_data` function that reads a CSV file (`dabarobjects_data.csv` by default) and preprocesses the data. Ensure your data file is correctly formatted.

## Summary Generation

The `generate_sales_summary` function processes the preprocessed data and generates monthly, quarterly, and yearly sales and quantity summaries. The results are saved in CSV files within the specified summary folder.

## Web Dashboard

- Access the main dashboard at the root URL ([http://127.0.0.1:5000/](http://127.0.0.1:5000/)).
- The `/get_data` endpoint provides the necessary data for the dashboard charts.

## Authors

- Kelani Sidikat Oyindamola
- Email: kelanisidikat883@gmail.com

Feel free to contact the author with any questions or concerns.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Flask
- pandas
- Chart.js (used for rendering charts in the dashboard)
