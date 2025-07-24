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
## 🧪 Example Output

For example, if a user invests:

- 💸 ₹5000 per month  
- ⏳ for 10 years  
- 📈 with an expected annual return of 12%  
- 📅 and selects a **Monthly** investment frequency  

Then the simulator will compute:

- 📦 **Final Corpus**: ₹11,61,695.38  
- 💰 **Total Invested**: ₹6,00,000  
- 📈 **Total Gain**: ₹5,61,695.38  

These results are visualized using interactive charts to help users understand the power of compounding over time.

---

## 👨‍💻 Author

Built with ❤️ by [Rohit Kumar Yadav](https://www.linkedin.com/in/rohit-kumar-yadav-b97360194/)

I'm currently working on [100 Days of Finance Data Science Projects](https://github.com/rohit2255), where I build impactful, real-world projects every day related to finance and data science.

---

## 🛠 Tech Stack

- 🐍 Python 3.11+
- 📊 [Plotly](https://plotly.com/python/) for visualization
- 📈 [Pandas](https://pandas.pydata.org/) for data manipulation
- 🌐 [Streamlit](https://streamlit.io/) for app deployment

---

## 🪪 License

This project is licensed under the **MIT License**.

You are free to:

- ✅ Use it for personal/commercial purposes  
- 🛠️ Modify and distribute  
- 🙌 Attribute when sharing is appreciated but not mandatory

See the `LICENSE` file for more details.

---

## 🚀 How to Run Locally

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/sip-roi-simulator.git
   cd sip-roi-simulator
