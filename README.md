# 📈 Interactive Data Analyzer App

Welcome to the Interactive Data Analyzer\! This is a powerful web application built with **Streamlit** that allows you to upload, clean, filter, and visualize your datasets—all without writing a single line of code.

This tool is perfect for data analysts, students, and anyone curious to find insights in their data quickly.

-----

## 🚀 What My App Does

This application transforms your raw data files (CSV or Excel) into an interactive dashboard. You can:

  * **Upload** your dataset.
  * Instantly **preview** the data and see a statistical summary.
  * Apply multiple **dynamic filters** across your data.
  * Create beautiful, interactive **visualizations** with Plotly.
  * **Download** your newly filtered data for further use.

-----

## 🎯 Key Features

Based on the `index.py` file, this app is packed with the following features:

### 1\. 📁 Flexible Data Upload

  * **CSV and Excel Support:** Easily upload your data in either `.csv` or `.xlsx` format.
  * **Robust Reading:** The app correctly handles different file types, using `pandas` for CSVs and `openpyxl` for Excel files.

### 2\. 📋 Instant Data Overview

  * **Data Preview:** Immediately see the first few rows of your dataset in a clean dataframe.
  * **Shape Display:** Instantly know the size of your data with a (row, column) count.
  * **Statistical Summary:** Get a full statistical breakdown (`.describe()`) of all numerical columns (count, mean, std, min, max, etc.).

### 3\. 🔍 Powerful Dynamic Filtering

This is the core of the app\! All filters are neatly organized in the sidebar and update the data in real-time.

  * **Categorical Filtering:** Automatically finds all text/category columns and lets you `multi-select` which values to include.
  * **Numerical Filtering:** Automatically finds all number columns and provides an interactive `slider` to select a min/max range.
  * **Date Filtering:** Automatically detects date columns and provides a `date range` selector.

### 4\. 🎨 Interactive Visualizations

Create custom, publication-ready charts using **Plotly Express**.

  * **Multiple Chart Types:** Choose from:
      * Bar Chart
      * Line Chart
      * Scatter Plot
      * Pie Chart
      * Histogram
  * **Dynamic Axis Selection:** You choose what goes on the X-axis, Y-axis, and even the Color dimension.
  * **Filtered Plots:** All visualizations automatically update based on the filters you've applied.

### 5\. 📥 Data Export

  * **Download Original Data:** Get a copy of your uploaded file in `.xlsx` format.
  * **Download Filtered Data:** After cleaning and filtering, you can download the *resulting dataset* as a new Excel file, ready for your reports.

-----

## 💻 Tech Stack

  * **Streamlit:** For the core web application and interactive widgets.
  * **Pandas:** For all data manipulation and analysis.
  * **Plotly Express:** For creating rich, interactive visualizations.
  * **Openpyxl:** To provide support for reading and writing Excel files.

-----

## 🚀 How to Run Locally

Want to run this app on your own machine?

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Savant261/Data-Analyzer-app.git
    cd Data-Analyzer-app
    ```

2.  **Install the dependencies:**
    (It's highly recommended to use a [virtual environment](https://docs.python.org/3/tutorial/venv.html) first\!)

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app:**

    ```bash
    streamlit run index.py
    ```

4.  Open your browser and go to `http://localhost:8501`.

-----

## 🤝 Contributing

Contributions, issues, and feature requests are welcome\! Feel free to check the [issues page](https://www.google.com/search?q=https://github.com/Savant261/Data-Analyzer-app/issues).
