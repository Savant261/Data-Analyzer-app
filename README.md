# 📈 Interactive Data Analyzer App

Welcome to the Interactive Data Analyzer\! This is a powerful web application built with **Streamlit** that allows you to upload, clean, filter, group, and visualize your datasets—all without writing a single line of code.

[**» View Live Demo**](https://data-analyzer-app-b5g8hci3xltt9cna9dgi85.streamlit.app/) 

This tool is perfect for data analysts, students, and anyone curious to find insights in their data quickly.


## 🚀 What My App Does

This application transforms your raw `.csv` data files into an interactive analysis dashboard. You can:

  * **Upload** your dataset.
  * Instantly **preview** the data and see a statistical summary.
  * Apply multiple **dynamic filters** across your data.
  * **Group and aggregate** your data by specific columns.
  * Find **correlations** and **detect outliers** automatically.
  * Create beautiful, interactive **visualizations** with Plotly.
  * **Download** your newly filtered data for further use.

-----

## 🎯 Key Features

This app is packed with the following features to make data analysis fast and easy:

### 1\. 📁 CSV Data Upload

  * **Easy Upload:** Quickly upload your data in `.csv` format using the simple file uploader.
  * **Robust Reading:** The app uses `pandas` to efficiently read and process your data.

### 2\. 📋 Instant Data Overview

  * **Data Preview:** Immediately see the first few rows of your dataset in a clean dataframe.
  * **Shape Display:** Instantly know the size of your data with a (row, column) count.
  * **Statistical Summary:** Get a full statistical breakdown (`.describe()`) of all numerical columns (count, mean, std, min, max, etc.).

### 3\. 🔍 Powerful Dynamic Filtering

All filters are neatly organized in the sidebar and update the data in real-time.

  * **Categorical Filtering:** Automatically finds all text/category columns and lets you `multi-select` which values to include.
  * **Numerical Filtering:** Automatically finds all number columns and provides an interactive `slider` to select a min/max range.
  * **Date Filtering:** Automatically detects date columns and provides a `date range` selector.

### 4\. 📊 Dynamic GroupBy Analysis

  * **Flexible Aggregation:** Instantly group your data by one or more columns (e.g., 'Region', 'Product Type').
  * **Summarize Data:** Perform common aggregations like `sum`, `mean`, `count`, or `median` on numerical columns to get summary statistics for each group.
  * **Visualize Groups:** Directly plot the results of your `groupby` operation using Bar, Line, or Pie charts to compare groups easily.

### 5\. 🧠 Advanced Data Analysis

  * **🔥 Heatmap Correlation:** Automatically generates a `seaborn` correlation matrix to show how different numerical variables relate to each other.
  * **👀 Outlier Detection:** Uses the **Interquartile Range (IQR)** method to automatically identify and visualize outliers in any numerical column you select.

### 6\. 🎨 Interactive Visualizations

Create custom, publication-ready charts using **Plotly Express**.

  * **Multiple Chart Types:** Choose from:
      * Bar Chart
      * Line Chart
      * Scatter Plot
      * Pie Chart
      * Histogram
  * **Dynamic Axis Selection:** You choose what goes on the X-axis, Y-axis, and even the Color dimension.
  * **Filtered Plots:** All visualizations automatically update based on the filters you've applied.

### 7\. 📥 Data Export

  * **Download Filtered Data:** After cleaning, filtering, and grouping, you can download the *resulting dataset* as a new `.csv` file, ready for your reports.

-----

## 💻 Tech Stack

  * **Streamlit:** For the core web application and interactive widgets.
  * **Pandas:** For all data manipulation, aggregation, and analysis.
  * **Plotly Express:** For creating rich, interactive visualizations.
  * **Seaborn:** For generating the beautiful correlation heatmap.

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
