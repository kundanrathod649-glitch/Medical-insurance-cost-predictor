# 🏥 Medical Insurance Cost Predictor

A Machine Learning web application that predicts medical insurance charges based on customer information using **Linear Regression** and **Streamlit**.

The application takes user inputs such as age, gender, BMI, number of children, smoking status, and region to estimate medical insurance costs.

## 🚀 Project Overview

The goal of this project is to build a regression model that estimates medical insurance expenses from demographic and lifestyle-related features. The trained model is integrated into a Streamlit web application to make predictions interactive and easy to use.

## ✨ Features

* **Linear Regression:** Predicts medical insurance charges using a supervised machine learning model.
* **Interactive web interface:** Built with Streamlit.
* **Customer information inputs:** Age, gender, BMI, number of children, smoking status, and region.
* **Categorical data preprocessing:** Uses One-Hot Encoding and Ordinal Encoding.
* **Model evaluation:** Evaluates performance using MAE, MSE, RMSE, and R² score.
* **Model persistence:** Saves the trained machine learning pipeline as a `.pkl` file using Joblib.
* **Real-time predictions:** Displays the estimated insurance cost in US dollars.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook

## 📂 Project Structure

```text
Medical-Insurance-Cost-Predictor/
│
├── app.py
├── linear_regression_model.ipynb
├── medical_insurance.csv
├── regression_model.pkl
├── requirements.txt
└── README.md
```

**File descriptions:**

* `app.py` — Streamlit application for collecting inputs and predicting insurance costs.
* `linear_regression_model.ipynb` — Notebook for data analysis, preprocessing, model training, and evaluation.
* `medical_insurance.csv` — Dataset used to train and evaluate the model.
* `regression_model.pkl` — Serialized preprocessing and Linear Regression pipeline.
* `requirements.txt` — Python dependencies required to run the project.
* `README.md` — Project documentation.

*Note: The dataset and trained model file must be available in the project directory when running the application. Generate `regression_model.pkl` by running the notebook if it is not already available.*

## ⚙️ Machine Learning Workflow

1. **Data loading:** Load the medical insurance dataset using Pandas.
2. **Exploratory Data Analysis (EDA):** Examine data distributions, categorical features, and relationships between variables.
3. **Feature selection:** Use age, sex, BMI, children, smoker, and region as input features. The target variable is `charges`.
4. **Train-test split:** Split the dataset into training and testing sets using an 80:20 ratio.
5. **Data preprocessing:** Apply One-Hot Encoding to gender and region, and Ordinal Encoding to smoking status.
6. **Model training:** Train a Linear Regression model within a scikit-learn pipeline.
7. **Model evaluation:** Calculate MAE, MSE, RMSE, and R² score on the test data.
8. **Model serialization:** Save the complete trained pipeline using Joblib.
9. **Deployment:** Load the saved pipeline into Streamlit and generate predictions from user inputs.

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Replace `YOUR_USERNAME` and `YOUR_REPOSITORY` with your GitHub username and repository name.

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
```

Activate it on macOS or Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

Create a `requirements.txt` file with the following contents:

```text
streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
jupyter
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run the Project

### Step 1: Train and save the model

Open the Jupyter Notebook:

```bash
jupyter notebook linear_regression_model.ipynb
```

Run the notebook cells to train the model, evaluate its performance, and generate `regression_model.pkl`.

Make sure the dataset path in the notebook points to the location of `medical_insurance.csv` on your computer.

### Step 2: Launch the Streamlit application

Ensure that `app.py` and `regression_model.pkl` are in the same directory, then execute:

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open that URL in your browser.

### Step 3: Predict medical insurance costs

1. Enter the customer's age.
2. Select gender.
3. Enter BMI.
4. Select the number of children.
5. Select smoking status.
6. Select the geographical region.
7. Click **Predict Cost**.

The application will display the predicted medical insurance cost in US dollars.

## 📊 Model Evaluation

The model is evaluated using the following regression metrics:

| Metric   | Description                                                          |
| -------- | -------------------------------------------------------------------- |
| MAE      | Mean Absolute Error; average absolute prediction error.              |
| MSE      | Mean Squared Error; average squared prediction error.                |
| RMSE     | Root Mean Squared Error; error measured in the target's units.       |
| R² Score | Measures how much variation in the target is explained by the model. |

The actual evaluation scores are printed when the notebook is executed. They should be added here after running the notebook rather than assuming specific performance values.

## 🔮 Future Improvements

* Deploy the application to Streamlit Community Cloud.
* Compare Linear Regression with Random Forest and other regression algorithms.
* Improve feature engineering and model evaluation.
* Add visualizations of predicted insurance costs.
* Improve input validation and error handling.
* Add a model performance summary to the web interface.

## 👨‍💻 Author

**Kundan Rathod**

GitHub: ([https://github.com/YOUR_USERNAME](https://github.com/kundanrathod649-glitch))

---

⭐ If you find this project useful, consider giving the repository a star!
