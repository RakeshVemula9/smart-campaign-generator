# 🧠 Smart Customer Segmentation Web App

This is an interactive Streamlit application that allows businesses to upload customer data, apply clustering techniques (like K-Means), visualize the results, and ask questions about customer segments via a built-in assistant.

---

## 📌 Features

- 📁 Upload CSV data (e.g., Mall_Customers.csv)
- 🧼 Preprocessing with Label Encoding & Standard Scaling
- 📉 Elbow method to determine optimal number of clusters
- 📊 Cluster visualization using PCA
- 🔍 Explore customer segments in detail
- 💬 Built-in natural language query assistant for segment insights
- 💾 Download clustered data
- 🕘 Chat history of your assistant queries

---

## 🛠 Tech Stack

- Python
- Streamlit
- scikit-learn
- Pandas
- Matplotlib & Seaborn
- PCA for dimensionality reduction
- KMeans for clustering

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smart-customer-segmentation.git
cd smart-customer-segmentation
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3. Run the App
bash
Copy
Edit
streamlit run app.py
📂 Sample Dataset Format
Make sure your CSV includes at least the following columns:

csv
Copy
Edit
CustomerID,Gender,Age,Annual Income (k$),Spending Score (1-100)
1,Male,19,15,39
2,Male,21,15,81
...
🧠 How It Works
Upload a dataset.

App preprocesses and standardizes the relevant features.

View the Elbow curve to find the ideal number of clusters.

Visualize clusters in 2D (via PCA).

Explore specific clusters and their average characteristics.

Ask questions like:

"Average income in cluster 2"

"How many customers in cluster 4?"

"Average age in cluster 1"

Download your segmented dataset with cluster labels.

