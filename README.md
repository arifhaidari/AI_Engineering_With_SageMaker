# AI Engineering with SageMaker

This repository showcases the development of **production-ready AI solutions** using **AWS SageMaker**. It provides step-by-step examples of deploying machine learning models and services on SageMaker, covering various real-world use cases.

The goal is to demonstrate how to leverage **AWS services** effectively for **scalable** and **robust AI applications**, without relying on local environments. All experiments and processes are conducted within **SageMaker Studio Classic** and documented here for reference.

---

## 🌟 **Projects in this Repository**

### 1. **News Categorizer**

A machine learning project that classifies news articles into categories such as **Business**, **Technology**, **Entertainment**, and **Health**. The goal is to build a **text classification pipeline** and deploy it using AWS SageMaker, enabling real-time predictions.

#### **Features**:

- **Context-Aware Categorization**: The model analyzes news headlines and predicts the corresponding category.
- **Scalable Deployment**: The trained model is deployed as an endpoint on AWS SageMaker for real-time inference.

#### **Dataset**:

The dataset is sourced from the [UCI News Aggregator Dataset](https://archive.ics.uci.edu/dataset/359/news+aggregator). It contains references to news pages collected from an aggregator between March and August 2014. The dataset is tab-delimited and includes columns such as `ID`, `TITLE`, `URL`, `PUBLISHER`, `CATEGORY`, `STORY`, `HOSTNAME`, and `TIMESTAMP`.

#### **Data Statistics**:

- **Total Records**: 422,937 news pages.
- **Categories**:
  - Business: 152,746
  - Science & Technology: 108,465
  - Entertainment: 45,615
  - Health: 115,920

#### **Preprocessing**:

- **Text Cleaning**: Removed duplicates, handled missing values, and standardized text.
- **Feature Engineering**: Used **TF-IDF vectorization** to transform news headlines.
- **Label Encoding**: Encoded categorical labels for compatibility with machine learning models.

---

## 🚀 **Modeling and Deployment**

### **Models Used**:

1. **Multinomial Naive Bayes (MultinomialNB)**:
   - Lightweight and efficient for text classification.
   - Suitable for sparse datasets like TF-IDF-transformed text.
2. **Multiclass LSTM** (Future Work):
   - Planned to improve performance using deep learning.
   - Leverages sequence information in text for more nuanced predictions.

### **Training and Deployment**:

- **Training**:
  - The `train.py` script preprocesses the data, trains the Naive Bayes model, and saves it along with the TF-IDF vectorizer.
  - The training job is executed on SageMaker using the **SKLearn Estimator**.
- **Deployment**:
  - The trained model is deployed to an **ML.m5.large** instance as a SageMaker endpoint for real-time predictions.

---

## 🛠 **Technologies and Tools**:

- **AWS SageMaker**: For training, deploying, and managing models.
- **S3**: For data storage and retrieval.
- **Scikit-learn**: For machine learning modeling.
- **Pandas**: For data manipulation and preprocessing.
- **Joblib**: For model serialization.
- **TF-IDF**: For text vectorization and feature extraction.

---

## 🔧 **How to Run This Project Locally**:

> Note: All processes are designed for cloud deployment on AWS. However, you can replicate the steps locally if needed.

### Step 1: Clone the repository

```bash
git clone https://github.com/arifhaidari/AI-Engineering-SageMaker.git
cd AI-Engineering-SageMaker
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Prepare the dataset

Upload the dataset to an accessible S3 bucket or modify the script to point to a local file.

### Step 4: Run training locally (optional)

```bash
python train.py
```

---

## 🔑 **Key Takeaways**:

- **Production-Ready Pipelines**: The project emphasizes creating scalable, production-ready pipelines with minimal local setup.
- **Cloud-Native Approach**: All workflows are cloud-first, leveraging SageMaker’s managed services.
- **Modular Design**: Scripts are modular and designed to be easily extendable.

---

## 📈 **Future Enhancements**:

- Integration with **Hugging Face models** for advanced NLP.
- Experimentation with deep learning models like **LSTM** and **Transformers**.
- Enhanced data augmentation and preprocessing techniques.

---

## 📄 **License**:

This project is licensed under the [MIT License](LICENSE).

---

## 📬 **Contact**:

For any questions or suggestions, feel free to reach out.
Contributions are welcome!
