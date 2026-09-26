# 🛴 ßolt Operations & Customer Support Analytics Dashboard

An interactive performance dashboard built with Python, Streamlit, and Plotly Express to monitor real-time operational efficiency, customer satisfaction (CSAT), and market distribution across Bolt customer support tickets.

---

## 📊 Business Problem & Features

This tool enables operations managers and support leads to identify operational bottlenecks and performance trends.

- **Dynamic Data Filtering:** Filter datasets by Market Language, Communication Channel, Priority Level, and Customer Tier.
- **Executive Metrics:** High-level overview displaying Total Tickets, Average CSAT Score, and Average Resolution Time.
- **Interactive Visualizations:**
  - **Sunburst Chart:** Multi-level volume breakdown by custom grouping and customer tier.
  - **Grouped Histograms:** Average metric distribution across ticket categories and volume breakdown by channel.
- **Raw Data Inspector:** Interactive table view for granular data analysis.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Data Manipulation:** Pandas
- **Visualization:** Plotly Express
- **Dashboard Framework:** Streamlit
- **IDE:** PyCharm

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR-GITHUB-USERNAME/Bolt-Operations-Dashboard.git](https://github.com/YOUR-GITHUB-USERNAME/Bolt-Operations-Dashboard.git)
   cd ßolt-Operations-Dashboard
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Streamlit app:**
   ```bash
   streamlit run test_streamlite.py
   ```