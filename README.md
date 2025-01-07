# cs1026a-project2
# What Does this Project Do

This project involves analyzing and visualizing flight-related data using two Python scripts (analysis.py and main.py) and multiple CSV files containing flight information (flights.csv, flights_extra_1.csv, flights_extra_2.csv). The goal is to process these datasets, derive insights, and present them visually.

Script: analysis.py
What This Script Does
The analysis.py script is responsible for performing data preprocessing, analysis, and computation of statistics or metrics from the flight data.

Features
Data Cleaning and Transformation:

Handles missing or inconsistent data in the provided CSV files.
Formats data into usable structures for analysis.
Key Metrics Calculation:

Computes statistics such as:
Total flights.
Average delays.
Busiest airports/routes.
Data Aggregation:

Groups and summarizes data based on specific columns, such as airports, airlines, or routes.
Modular Design:

Contains reusable functions for performing common operations like filtering, grouping, and calculating statistics.

The main.py script serves as the primary interface for the project, integrating user inputs, data analysis (via analysis.py), and visualization.

Features
User Interaction:

Allows users to specify input files (flights.csv, flights_extra_1.csv, flights_extra_2.csv) or choose operations to perform on the data.
Integration with analysis.py:

Utilizes functions from analysis.py for data processing and analysis.
Visualization:

Generates visual insights using charts and graphs (e.g., bar charts for delays, pie charts for route popularity) with libraries like matplotlib or seaborn.
Report Generation:

Outputs summaries of key metrics and saves visualizations as images or displays them interactively.

CSV Files:
flights.csv:

The primary dataset containing flight details.
flights_extra_1.csv & flights_extra_2.csv:

Additional datasets providing supplementary information (e.g., extended routes, historical data).


Technologies/Libraries Used:
Language: Python
Libraries:
pandas: For data manipulation and analysis.
numpy: For numerical computations.
matplotlib/seaborn: For visualizations.

Skills Demonstrated:
Data Analysis: Cleaning, processing, and statistical computations.
Visualization: Creating insightful graphs and charts.
Integration: Combining multiple datasets for comprehensive analysis.
Modular Programming: Separating concerns into analysis.py and main.py.
