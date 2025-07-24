# 💹 SIP ROI Simulator

A simple yet powerful Streamlit web app that helps users simulate returns from a **Systematic Investment Plan (SIP)** using various parameters like monthly investment, duration, expected return rate, and investment frequency.

🌐 Live App: [SIP ROI Calculator](https://sip-roi-calculator.streamlit.app/)

---

## 📊 Features

- Interactive interface built with **Streamlit**
- Customizable inputs:  
  - Monthly investment amount  
  - Expected annual return (%)  
  - Investment duration (in years)  
  - Frequency (Monthly or Quarterly)
- Visualizations powered by **Plotly**
  - Investment Growth over Time (Line Chart)
  - Investment vs Gain breakdown (Pie Chart)
- Real-time calculation of:
  - Total Invested Amount
  - Final Corpus Value
  - Total Gain
- Optimized for desktop and mobile view


---

## 🧠 How It Works

The app calculates SIP growth using compound interest principles for periodic investments.

It computes investment for each period and compounds it accordingly. The final corpus and gain are then visualized to help users understand long-term wealth creation via SIP.

---

## 🛠 Tech Stack

- 🐍 Python 3.11+
- 📊 [Plotly](https://plotly.com/python/) for visualization
- 📈 [Pandas](https://pandas.pydata.org/) for data manipulation
- 🌐 [Streamlit](https://streamlit.io/) for app deployment

---

## 🚀 How to Run Locally

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/sip-roi-simulator.git
   cd sip-roi-simulator
