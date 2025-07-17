Employee Salary Prediction App

This project is a machine learning web app built with **Streamlit** that predicts an employee's salary class (`<=50K` or `>50K`) based on key attributes such as age, education, occupation, weekly work hours, and work sector.

## 📌 Features
- Predicts income class in real time
- Clean and interactive user interface
- Built using Supervised Machine Learning Algorithm
- Built using a trained and serialized ML pipeline
- Inputs include:
  - Age
  - Education Level
  - Occupation
  - Hours worked per week
  - Workclass / Organization type

## 🔧 Tech Stack
- Python
- Scikit-learn (model and pipeline)
- Pandas
- Streamlit (web interface)
- Joblib (model serialization)

## 📁 Project Structure
```

├── app.py                  # Streamlit app interface
├── salary\_pipeline.pkl     # Pretrained ML model pipeline
├── Employee\_Salary\_Prediction.ipynb  # Model training notebook

````

## 🛠️ How to Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/employee-salary-prediction.git
   cd employee-salary-prediction
   ````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Launch the app:

   ```bash
   streamlit run app.py
   ```

## 📈 Model Overview

The model was trained on the Employee Income Dataset with features like:

* Age
* Education
* Occupation
* Hours-per-week
* Workclass

Preprocessing and model training were done in `Employee_Salary_Prediction.ipynb`, and the final pipeline was saved using `joblib`.

## 🙌 Contribution

Feel free to fork this repo, submit issues or pull requests. Feedback is welcome!
