import streamlit as st
import google.generativeai as genai
import time
from dotenv import load_dotenv
import os 

load_dotenv()
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)



def get_career_roadmap(skills, role):
    # model = genai.GenerativeModel("gemini-pro")
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
    Given the following skills: {skills}, and the desired role: {role},
    provide a detailed career roadmap including suggestions, required improvements, and learning resources.
    """
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
# st.set_page_config(page_title="Career Roadmap Generator", layout="wide")

# st.set_page_config(
#     page_title='Queries Assistance',
#     layout='wide',
#     initial_sidebar_state='collapsed'
# )

# Custom CSS for a Modern UI
st.markdown(
    """
    <style>
        body {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: 'Inter', sans-serif;
        }
        .main-container {
            max-width: 900px;
            margin: auto;
            padding: 50px;
            background: #161b22;
            border-radius: 15px;
            box-shadow: 0px 6px 20px rgba(255, 255, 255, 0.1);
        }
        h1 {
            text-align: center;
            color: #58a6ff;
            font-size: 40px;
            font-weight: bold;
        }
        .input-box {
            padding: 20px;
            background: #21262d;
            border-radius: 10px;
            border: 2px solid #30363d;
            font-size: 22px;
        }
        .stButton>button {
            background-color: #238636;
            color: white;
            border-radius: 10px;
            padding: 15px;
            font-size: 20px;
            font-weight: bold;
            width: 100%;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #2ea043;
        }
        .roadmap-box {
            padding: 30px;
            background: #30363d;
            color: #c9d1d9;
            border-radius: 12px;
            font-size: 22px;
            line-height: 2;
            text-align: left;
            margin-top: 25px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# UI Layout
st.title(" Career Path Assistance")

skills = st.text_area("Enter your current skills " )
role = st.text_input("Enter your desired role:")

if st.button("Generate Roadmap"):
    if skills and role:
        with st.spinner("Generating roadmap..."):
            time.sleep(2)
            roadmap = get_career_roadmap(skills, role)
            st.subheader("Your Career Roadmap")
            st.markdown(f"<div class='roadmap-box'>{roadmap}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter both skills and desired role.")

st.markdown("</div>", unsafe_allow_html=True)
