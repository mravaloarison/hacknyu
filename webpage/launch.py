import streamlit as st
import streamlit.components.v1 as components
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB (update the connection string, db name, and collection as needed)
client = MongoClient('mongodb+srv://dzheng4m:cGqGXWHSHFQRxSRZ@cluster0.06nr7.mongodb.net/')
database = client['SecurityFilterDb']
users_collection = database["users"]

# Configure the page
st.set_page_config(
    page_title="SecureLingo",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #1a1a1a;
    }
    
    /* Navigation bar styling */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        background-color: #2c2c2c;
        margin: -6rem -4rem 2rem -4rem;
    }
    
    .logo {
        color: #00ff00;
        font-size: 24px;
        font-weight: bold;
    }
    
    .nav-buttons {
        display: flex;
        gap: 20px;
    }
    
    .login-btn {
        background-color: transparent;
        border: 2px solid #00ff00;
        color: #00ff00;
        padding: 10px 25px;
        border-radius: 25px;
        cursor: pointer;
        font-weight: bold;
    }
    
    .signup-btn {
        background-color: #00ff00;
        border: none;
        color: #1a1a1a;
        padding: 12px 25px;
        border-radius: 25px;
        cursor: pointer;
        font-weight: bold;
    }
    
    /* Hero section styling */
    .hero {
        text-align: center;
        padding: 80px 20px;
        max-width: 1200px;
        margin: 0 auto;
        color: white;
    }
    
    .hero h1 {
        font-size: 48px;
        margin-bottom: 20px;
        color: #00ff00;
    }
    
    .hero p {
        font-size: 20px;
        color: #cccccc;
        margin-bottom: 40px;
        line-height: 1.6;
    }
    
    /* Feature cards styling */
    .features {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 30px;
        padding: 40px;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .feature-card {
        background-color: #2c2c2c;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
    }
    
    .feature-icon {
        font-size: 40px;
        color: #00ff00;
    }
    
    .feature-card h3 {
        color: #00ff00;
        margin: 20px 0;
    }
    
    .feature-card p {
        color: #cccccc;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for form visibility
if 'show_login' not in st.session_state:
    st.session_state.show_login = False
if 'show_signup' not in st.session_state:
    st.session_state.show_signup = False

# Functions to toggle form visibility
def toggle_login():
    st.session_state.show_login = not st.session_state.show_login
    st.session_state.show_signup = False  # Hide signup form when toggling login

def toggle_signup():
    st.session_state.show_signup = not st.session_state.show_signup
    st.session_state.show_login = False  # Hide login form when toggling signup

# Define the navbar function (displayed in the sidebar)
def navbar():
    st.sidebar.markdown("<h1 style='font-size: 40px; color: #00ff00;'>SecureLingo</h1>", unsafe_allow_html=True)
    
    # "Log In" button logic
    if st.sidebar.button("Log In"):
        toggle_login()
    
    # "Sign Up" button logic
    if st.sidebar.button("Sign Up"):
        toggle_signup()

# Call the navbar function
navbar()

# LOGIN FORM
if st.session_state.show_login:
    with st.sidebar:
        st.subheader("Login")
        login_email = st.text_input("Email", key="login_email")
        login_password = st.text_input("Password", type="password", key="login_password")
        if st.button("Submit", key="login_submit"):
            # Validate email: must end with @gmail.com and be longer than 6 characters
            if not login_email.endswith("@gmail.com") or len(login_email) <= 6:
                st.warning("Please enter a valid @gmail.com email address longer than 6 characters.")
            else:
                # Query the database for the user
                user = users_collection.find_one({"email": login_email})
                if not user:
                    st.error("User not found. Please sign up.")
                elif user["password"] != login_password:
                    st.error("Incorrect password.")
                else:
                    st.success("Logged In!")
                    st.session_state.show_login = False


# SIGN-UP FORM
if st.session_state.show_signup:
    with st.sidebar:
        st.subheader("Create Account")
        signup_email = st.text_input("Email", key="signup_email")
        signup_password = st.text_input("Password", type="password", key="signup_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm")
        if st.button("Submit", key="signup_submit"):
            # Validate email: must end with @gmail.com and be longer than 6 characters
            if not signup_email.endswith("@gmail.com") or len(signup_email) <= 6:
                st.warning("Please enter a valid @gmail.com email address longer than 6 characters.")
            elif signup_password != confirm_password:
                st.warning("Passwords do not match")
            else:
                # Check if the email already exists in the database
                existing_user = users_collection.find_one({"email": signup_email})
                if existing_user:
                    st.warning("An account with this email already exists. Please log in.")
                else:
                    # Insert the new user document into MongoDB
                    users_collection.insert_one({"email": signup_email, "password": signup_password})
                    st.success("Account Created!")
                    st.session_state.show_signup = False

# HERO SECTION
hero_html = """
<div class="hero">
    <h1>Learn Cybersecurity The Fun Way</h1>
    <p>Master essential cybersecurity skills through interactive lessons, real-world scenarios, and daily practice. 
    Join millions of learners protecting themselves and their organizations online.</p>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# FEATURES SECTION
features_html = """
<div class="features">
    <div class="feature-card">
        <div class="feature-icon">🛡️</div>
        <h3>Interactive Lessons</h3>
        <p>Learn through hands-on exercises and real-world scenarios</p>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <h3>Daily Practice</h3>
        <p>Build your security skills with bite-sized daily lessons</p>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📈</div>
        <h3>Track Progress</h3>
        <p>Monitor your learning journey with detailed analytics</p>
    </div>
</div>
"""
st.markdown(features_html, unsafe_allow_html=True)
