# 🏦 Streamlit Banking System

A modern, interactive banking web application built with **Python** and **Streamlit**. This app replaces the traditional command-line interface with a user-friendly GUI (Graphical User Interface), allowing users to perform banking operations with button clicks and visual feedback.

## 🌟 Key Features

This application uses `st.session_state` to store data temporarily, making it function like a real bank during the session.

* **➕ Open Account:** Create a new account with an auto-generated Account Number and PIN.
* **💰 Check Balance:** Securely view available funds using authentication.
* **💸 Deposit & Withdraw:** Add or remove funds instantly with real-time balance updates.
* **🔄 Fund Transfer:** Transfer money between two accounts (Validates both Sender and Beneficiary).
* **🔐 Security Features:**
    * **Change PIN:** Users can update their security PIN.
    * **Close Account:** Option to delete an account permanently.
* **📂 Admin View:** 'Show All Accounts' feature to view the database (for testing purposes).

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Framework:** [Streamlit](https://streamlit.io/) (For Web UI)
* **Logic:** List of Dictionaries & Nested Loops for data handling.

## 🚀 How to Run Locally

1.  **Install Python** (if not installed).
2.  **Install Streamlit** using pip:
    ```bash
    pip install streamlit
    ```
3.  **Clone this repository**:
    ```bash
    git clone [https://github.com/YourUsername/Streamlit-Banking-App.git](https://github.com/YourUsername/Streamlit-Banking-App.git)
    ```
4.  **Run the App**:
    Instead of `python bank.py`, use the following command:
    ```bash
    streamlit run bank.py
    ```
5.  The app will automatically open in your web browser at `http://localhost:8501`.


## 📂 Project Structure
├── bank.py # Main application file ├── README.md # Documentation └── requirements.txt # Dependencies streamlit

## 👤 Author

**[kasaam ali]**
* Built with ❤️ using Python & Streamlit
