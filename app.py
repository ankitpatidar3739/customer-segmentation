import streamlit as st
import matplotlib.pyplot as plt
from predict import predict_customer

# Page config
st.set_page_config(page_title="Customer Segmentation", layout="centered")

# ---------- ADVANCED CSS ----------
st.markdown("""
<style>

/* ---------- BACKGROUND ANIMATION ---------- */
body {
    background: linear-gradient(-45deg, #0f172a, #1e293b, #020617, #1e1b4b);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
    color: white;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ---------- FLOATING PARTICLES ---------- */
body::before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    background-image: radial-gradient(circle, rgba(255,255,255,0.08) 1px, transparent 1px);
    background-size: 50px 50px;
    animation: moveParticles 60s linear infinite;
    z-index: -1;
}

@keyframes moveParticles {
    from {transform: translate(0,0);}
    to {transform: translate(-500px,-500px);}
}

/* ---------- GLASS CARD ---------- */
.card {
    padding: 25px;
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(14px);
    box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px) scale(1.01);
}

/* ---------- ANIMATED TITLE ---------- */
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    background: linear-gradient(90deg, #6366f1, #8b5cf6, #22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from {text-shadow: 0 0 10px #6366f1;}
    to {text-shadow: 0 0 20px #22d3ee;}
}

/* ---------- SUBTITLE ---------- */
.subtitle {
    text-align: center;
    opacity: 0.8;
    margin-bottom: 20px;
}

/* ---------- BUTTON ---------- */
.stButton > button {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
}

/* ---------- METRICS ---------- */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.05);
    padding: 15px;
    border-radius: 12px;
}

/* ---------- SIDEBAR ---------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #1e293b);
}

</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.title("🚀 About This App")
st.sidebar.write("""
🔥 Built using:
- RFM Analysis  
- K-Means Clustering  

💡 Smart AI-driven segmentation
""")

# ---------- TITLE ----------
st.markdown('<div class="title">🔥 Customer Segmentation AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Turn Data into Smart Business Decisions</div>', unsafe_allow_html=True)

st.divider()

# ---------- INPUT CARD ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📥 Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    recency = st.number_input("🕒 Recency (days)", min_value=0)

with col2:
    frequency = st.number_input("🔁 Frequency", min_value=0)

monetary = st.number_input("💰 Monetary Value", min_value=0.0)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- INFO ----------
st.markdown("""
<div class="card">
📊 <b>How it works:</b><br>
Recency → Last purchase<br>
Frequency → Purchase count<br>
Monetary → Total spend<br><br>

</div>
""", unsafe_allow_html=True)

# ---------- PREDICTION ----------
if st.button("🚀 Analyze Customer"):

    cluster, segment = predict_customer(recency, frequency, monetary)

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(f"<h2 style='text-align:center;'>🎯 {segment}</h2>", unsafe_allow_html=True)
    st.success(f"Cluster: {cluster}")

    st.markdown('</div>', unsafe_allow_html=True)

    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("🕒 Recency", recency)
    col2.metric("🔁 Frequency", frequency)
    col3.metric("💰 Monetary", monetary)

    # Insights
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if "Loyal" in segment:
        st.success("🔥 Retain with loyalty rewards & exclusive offers")

    elif "High Value" in segment:
        st.success("💎 Provide premium services & VIP benefits")

    elif "At Risk" in segment:
        st.error("⚠️ Re-engage with discounts & personalized campaigns")

    elif "New" in segment:
        st.info("🆕 Offer onboarding deals & first-time benefits")

    else:
        st.info("👤 Maintain engagement with regular updates")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- VISUAL ----------
if st.button("📊 Show Position"):

    fig, ax = plt.subplots()
    ax.scatter(recency, monetary, s=150)

    ax.set_xlabel("Recency")
    ax.set_ylabel("Monetary")
    ax.set_title("Customer Position")

    st.pyplot(fig)