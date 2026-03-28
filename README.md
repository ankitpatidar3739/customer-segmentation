# customer-segmentation
🚀 Customer Segmentation AI (SaaS Dashboard)

An end-to-end Machine Learning project that segments customers using RFM Analysis + K-Means Clustering and provides real-time predictions through an interactive Streamlit dashboard.

🌐 Live Demo

👉(https://customer-segmentation-fpizeaizyhdrtywvaupjpw.streamlit.app/)

📌 Features
🔍 Customer segmentation using RFM (Recency, Frequency, Monetary)
🤖 K-Means clustering model for grouping customers
🎯 Real-time prediction system
📊 Interactive dashboard (Streamlit UI)
💡 Business insights & recommendations for each segment
🎨 Modern SaaS-style UI with animations
🧠 Tech Stack

Frontend: Streamlit
Machine Learning: Scikit-learn (KMeans)
Data Processing: Pandas, NumPy
Visualization: Matplotlib
Model Storage: Joblib (.pkl files)


📊 How It Works
Customer data is transformed into RFM features:
Recency → Last purchase time
Frequency → Number of purchases
Monetary → Total spending
K-Means clustering is applied to segment customers.
The trained model is used to:
Predict customer segment
Provide business recommendations
🎯 Customer Segments
💎 High Value Customers
🔥 Loyal Customers
🟡 Potential Customers
⚠️ At Risk Customers
🆕 New Customers
📸 Screenshots

<img width="2156" height="1326" alt="image" src="https://github.com/user-attachments/assets/f0a315ed-a9cf-4ab5-ab70-06b2a51244b4" />


⚙️ Installation (Run Locally)
git clone https://github.com/your-username/customer-segmentation.git
cd customer-segmentation
pip install -r requirements.txt
streamlit run app.py
📁 Project Structure
customer-segmentation/
│
├── app.py                # Streamlit app
├── predict.py            # Prediction logic
├── kmeans_model.pkl      # Trained model
├── scaler.pkl            # Feature scaler
├── requirements.txt      # Dependencies
└── README.md             # Documentation
🚀 Deployment

This app is deployed using Streamlit Cloud:

Connected with GitHub repository
Auto-deployed on every push

⚠️ Notes
Model version compatibility warnings may occur due to sklearn version differences.
For production use, retrain the model using the latest library versions.
