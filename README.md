# SGX3 Flask Project

This repository contains two distinct Flask applications developed for the SGX3 project. Each application serves a different purpose, demonstrating basic Flask routing and data analysis capabilities with Pandas.

## `app.py`

### Overview

`app.py` is a simple Flask application that demonstrates fundamental routing concepts. It provides basic "Hello World" responses and personalized greetings based on URL parameters.

### Features

*   **Root Route (`/`)**: Returns a classic "Hello, world!" message.
*   **Personalized Greeting Route (`/<name>`)**: Takes a name as a URL parameter and returns a personalized greeting (e.g., `/John` would return "Hello, John!").
*   **SGXers Route (`/sgx3`)**: Returns a specific greeting for "SGXers".

### How to Run

To run this application, ensure you have Flask installed (`pip install Flask`). Navigate to the `sgx3-project` directory and execute the following command:

```bash
python app.py
```

The application will run on `http://0.0.0.0:8002`. You can access it via your web browser or `curl`:

*   `http://localhost:8002/`
*   `http://localhost:8002/YourName`
*   `http://localhost:8002/sgx3`

## `app-charlie-routes_warmup.py`

### Overview

`app-charlie-routes_warmup.py` is a Flask application designed for analyzing Austin traffic data. It leverages the Pandas library to load and provide various insights into a CSV dataset (`atxtraffic.csv`). This application demonstrates how to expose data analysis functionalities through a web API.

### Features

*   **Data Loading**: Automatically loads `atxtraffic.csv` into a Pandas DataFrame upon startup.
*   **Root Route (`/`)**: Returns the first 10 rows of the traffic data as a JSON array.
*   **Head Route (`/head?count=<num>`)**: Returns the first `<num>` rows of the traffic data. For example, `/head?count=5` would return the first 5 rows.
*   **Shape Route (`/shape`)**: Returns the dimensions (rows and columns) of the DataFrame.
*   **Columns Route (`/columns`)**: Returns a list of all column names in the DataFrame.
*   **Info Route (`/info`)**: Returns a string containing the DataFrame's `info()` output, which includes data types and non-null counts for each column.
*   **Summary Route (`/summary`)**: Provides a comprehensive summary of the DataFrame, including shape, columns, data types, null counts, and descriptive statistics for all columns.
*   **Describe Route (`/describe`)**: Returns descriptive statistics for all columns in the DataFrame.

### Data Requirement

This application requires a CSV file named `atxtraffic.csv` to be present in the same directory as the script. Without this file, the application will not function correctly.

### How to Run

To run this application, ensure you have Flask and Pandas installed (`pip install Flask pandas`). Also, make sure `atxtraffic.csv` is in the same directory. Navigate to the `sgx3-project` directory and execute the following command:

```bash
python app-charlie-routes_warmup.py
```

The application will run on `http://0.0.0.0:8076`. You can access its endpoints via your web browser or `curl`:

*   `http://localhost:8076/`
*   `http://localhost:8076/head?count=5`
*   `http://localhost:8076/shape`
*   `http://localhost:8076/columns`
*   `http://localhost:8076/info`
*   `http://localhost:8076/summary`
*   `http://localhost:8076/describe`

---

**Author**: Manus AI


