import streamlit as st
from datetime import datetime

# Configure the page
st.set_page_config(
    page_title="Cybersecurity Dashboard",
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

    /* Section Styling */
    .section {
        padding: 40px;
        max-width: 1200px;
        margin: 0 auto;
        color: white;
        background-color: #2c2c2c;
        border-radius: 10px;
        margin-bottom: 30px;
    }

    .section h2 {
        color: #00ff00;
        font-size: 30px;
    }

    .lesson-content, .quiz-content {
        color: #cccccc;
        font-size: 18px;
        margin-bottom: 20px;
    }

    .question {
        color: #ffffff;
    }

    .quiz-option {
        color: #cccccc;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# HERO SECTION
hero_html = """
<div class="hero">
    <h1>Welcome to the Cybersecurity Dashboard</h1>
    <p>Stay up to date with daily lessons and quizzes to strengthen your cybersecurity skills.</p>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# DAILY LESSON SECTION
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("📝 Daily Lesson")
lesson_content = """
ADD CHAT GPT STUFF 
"""
st.markdown(lesson_content, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# QUIZ SECTION
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("❓ Quiz: Test Your Knowledge")

# Define quiz questions and answers
'''quiz_questions = [
    {
        "question": "What is Phishing?",
        "options": [
            "A type of fishing",
            "A cyber attack aimed at stealing sensitive information",
            "A way to prevent malware",
            "None of the above"
        ],
        "correct_answer": "A cyber attack aimed at stealing sensitive information"
    },
    {
        "question": "Which of the following is a red flag in a phishing email?",
        "options": [
            "It has a professional tone",
            "It includes a generic greeting",
            "It has an unusual URL",
            "It asks for personal details"
        ],
        "correct_answer": "It has an unusual URL"
    }
]

# Display quiz questions
for i, quiz in enumerate(quiz_questions):
    st.markdown(f"### Question {i + 1}: {quiz['question']}")
    for option in quiz['options']:
        st.radio(f"{quiz['question']}", quiz['options'], key=f"question_{i + 1}")
'''
st.markdown('</div>', unsafe_allow_html=True)

# Footer section
st.markdown("""
    <footer style="color: #cccccc; text-align: center; padding: 20px;">
        <p>Made with ❤️ by SecureLingo | &copy; 2025</p>
    </footer>
""", unsafe_allow_html=True)
