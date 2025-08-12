# ✈️ MLOps - Flight Customer Satisfaction

This project is an end-to-end **MLOps pipeline** for predicting customer satisfaction using a machine learning model trained on flight-related customer data.

The pipeline incorporates:
- **Data versioning with DVC**
- **Model tracking with MLflow**
- **Model serving with Flask**
- **Experiment visualization with TensorBoard**
- **Data ingestion using SQL**

---

## 🔧 Tech Stack

| Component       | Tool/Library            |
|----------------|--------------------------|
| Data Ingestion | SQL (e.g., SQLite/MySQL) |
| Version Control| Git + DVC                |
| Model Tracking | MLflow                   |
| Experiment Logging | TensorBoard         |
| Backend Serving | Flask API               |
| ML Model       | Scikit-learn / XGBoost   |

---

## 📁 Project Structure

```
.
├── data/                   # Raw & processed data tracked via DVC
├── dvc.yaml                # DVC pipeline stages
├── params.yaml             # Model/config parameters
├── src/                    # All source code modules
│   ├── data_ingestion/     # SQL-based data loader
│   ├── components/         # Data transformation, model training, evaluation
│   ├── pipeline/           # DVC pipeline logic
│   ├── utils/              # Utility functions
├── templates/              # HTML for Flask frontend (if any)
├── static/                 # Static files for Flask app
├── app.py                  # Flask API for serving predictions
├── requirements.txt
├── mlruns/                 # MLflow artifacts
├── logs/                   # TensorBoard logs
├── notebooks/              # Jupyter notebooks for EDA/testing
└── README.md
```

---

## 🚀 How to Run the Project

### 1. Clone and Set Up Environment

```bash
git clone https://github.com/codewithkaran-21/mlops-fligt-customer-satisfaction.git
cd mlops-fligt-customer-satisfaction
pip install -r requirements.txt
```

### 2. Configure DVC and Pull Data

```bash
dvc pull
```

### 3. Run DVC Pipeline

```bash
dvc repro
```

### 4. Track Experiments with MLflow

MLflow autologs during training. Launch the UI with:

```bash
mlflow ui
```

### 5. Visualize with TensorBoard

```bash
tensorboard --logdir=logs/
```

### 6. Serve Model with Flask

```bash
python app.py
```

Visit: `http://localhost:5000`

---

## ✅ Features

- 📦 Modular code: ingestion, transformation, training, and evaluation are cleanly separated
- 🔁 Reproducibility: data and model artifacts are versioned via DVC
- 📊 Experiment tracking: MLflow logs hyperparameters, metrics, and artifacts
- 🔎 Monitoring: TensorBoard shows real-time loss/accuracy graphs
- 🌐 API: Flask serves the trained model for real-world usage

---

## 📌 To-Do / Enhancements

- [ ] Add Docker support
- [ ] CI/CD pipeline with GitHub Actions
- [ ] Cloud deployment (e.g., Azure, GCP, or AWS)
- [ ] Add unit tests

---

## 🙋‍♂️ Author

**Karan Singh**  
[GitHub Profile](https://github.com/codewithkaran-21)

---

## 📄 License

This project is licensed under the MIT License.