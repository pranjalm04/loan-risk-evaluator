# loan-risk-evaluator
A machine learning project to evaluate loan application risks using EDA, feature engineering, and models like Random Forest. Tracks results with MLflow and DagsHub. Deployed with FastAPI (backend) and Streamlit (frontend) for real-time predictions.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Results Tracking](#results-tracking)
- [Metrics and Observations](#metrics-and-observations)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Overview
This project predicts the risk associated with loan applications using two datasets. Key steps include:
- Exploratory Data Analysis (EDA).
- Data Cleaning and Preprocessing.
- Addressing class imbalance using SMOTE.
- Feature Engineering.
- Model Training and Testing.
- Results logging with MLflow and integration with DagsHub.

---

## Features
- Comprehensive EDA to understand data distributions and correlations.
- Data cleaning to handle missing values and outliers.
- Balancing classes using SMOTE to enhance model performance.
- Dropping features with high correlations to avoid overfitting.
- Feature selection using XGBoost by calculating feature importance.
- Training multiple machine learning models (Logistic Regression, Random Forest, Ridge Classifier).
- Detailed model evaluation metrics.
- Results and artifacts tracking using MLflow and DagsHub.

---

## Technologies Used
- Python
- MLflow
- DagsHub
- SQLite
- Scikit-learn
- Pandas, NumPy, Matplotlib, Plotly
- FastAPI
- Streamlit

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- Pipenv or Virtualenv (optional)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/loan-risk-evaluation.git
   cd loan-risk-evaluation
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up SQLite database:
   ```bash
   sqlite3 loan.db < schema.sql
   ```

4. Initialize DagsHub repository:
   ```bash
   dvc init
   dagshub init --mlflow
   ```

---

## Usage

1. Load the datasets:
   - `loan_applications.csv`
   - `credit_features.csv`

2. Run the Jupyter Notebook for:
   - EDA
   - Data Cleaning and Preprocessing
   - Feature Engineering
   - Model Training and Evaluation

3. Log results to MLflow and push them to DagsHub:
   ```bash
   mlflow run .
   ```

---

## Results Tracking
- **MLflow**: Tracks model metrics, parameters, and artifacts.
- **DagsHub**: Stores experiment results and datasets for reproducibility. The metrics of the models are compared on DagsHub for detailed analysis and visualization.

---

## Metrics and Observations
- Features with high correlations are dropped to avoid model overfitting.
- Feature selection is performed using XGBoost to calculate feature importance.

### Model Performance Metrics
#### Random Forest Classifier
- **Accuracy**: 0.99
- **Precision**: 0.99
- **Recall**: 1.00
- **F1_score**: 0.99
- **ROC_AUC**: 0.99

### Key Observation
After addressing data imbalances, the Random Forest model outperforms other models, making it the best choice for deployment.

---

## Deployment
The selected Random Forest Classifier model is deployed as follows:
- **Backend**: Hosted using FastAPI to serve predictions.
- **Frontend**: A basic interface developed using Streamlit to query the model for predictions about whether the loan application is safe or not.

![Loan Application Risk Prediction Workflow](image_path_here)

---

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add feature-name'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License.

---

## Contact
For any questions or feedback, please contact:
- **Name**: Your Name
- **Email**: [your.email@example.com](mailto:your.email@example.com)
- **GitHub**: [https://github.com/yourusername](https://github.com/yourusername)
