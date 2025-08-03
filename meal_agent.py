import streamlit as st
import openai
from openai import OpenAI
import os
import datetime
from dotenv import load_dotenv

# Load env and set up Groq
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Validate API key
if not groq_api_key:
    st.error("❌ GROQ_API_KEY not found in environment variables. Please add it to your .env file.")
    st.stop()

# Initialize OpenAI client for Groq
client = OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1"
)

# Get today's name
today = datetime.datetime.now().strftime("%A")

st.set_page_config(page_title="🍽️ Ghar Ka Rasoi – Smart Meal Agent", layout="centered")
st.title("🍽️ Ghar Ka Rasoi – Daily Meal Planner for Your Cook")
st.markdown("Plan delicious, customized meals in Hinglish for your cook based on your preferences.")

# -------------------------------
# ✍️ Form to Collect Daily Inputs
# -------------------------------
with st.form("meal_form"):
    st.subheader("📋 Meal Preferences")

    day = st.selectbox("📅 Plan meals for", ["Today", "Tomorrow", "Custom"])
    if day == "Custom":
        custom_day = st.text_input("Enter day name (e.g. Friday):")
        target_day = custom_day if custom_day.strip() else today
    elif day == "Tomorrow":
        target_day = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%A")
    else:
        target_day = today

    diet = st.selectbox("🥗 Diet Preference", ["Vegetarian", "Vegetarian + Eggs"])
    people = st.slider("👨‍👩‍👧‍👦 Number of People", 1, 6, 3)
    tone = st.selectbox("🍽️ Meal Style", ["Light", "Balanced", "Indulgent"])
    variety = st.radio("🔁 Meal Rotation", ["Daily variety", "Repeat weekly"])
    notes = st.text_input("📝 Any special request? (e.g. light dinner, no paneer)")

    generate = st.form_submit_button("🧠 Suggest Meals")

# -------------------------------
# 🧠 Prompt Generator
# -------------------------------
def build_prompt(day, diet, people, tone, variety, notes):
    return f"""
You are a helpful Indian home meal assistant for planning meals for a cook.

Please suggest 3 meals for {people} people for {day} — breakfast, lunch, and dinner.

Rules:
- Diet: {diet}
- Meal style: {tone.lower()}
- Rotation: {variety.lower()}
- Keep dinner light and avoid heavy fried items late evening.
- Notes: {notes or 'None'}

Respond in simple Hinglish so the home cook can easily understand and follow. Use only common Indian ingredients and avoid repeating dishes from recent days. Try 1 new dish on weekends.

Format your response as:
**Breakfast:**
• [meal name and description]

**Lunch:**
• [meal name and description]

**Dinner:**
• [meal name and description]
"""

# -------------------------------
# 🔁 Generate Meals via LLM
# -------------------------------
if generate:
    with st.spinner("Cooking up ideas..."):
        try:
            prompt = build_prompt(target_day, diet, people, tone, variety, notes)
            
            # Use a currently available model for Groq
            response = client.chat.completions.create(
                model="llama3-8b-8192",  # Currently available model for Groq
                messages=[
                    {"role": "system", "content": "You are a friendly meal planner for Indian homes. Always respond in Hinglish."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            meals = response.choices[0].message.content
            st.success(f"🍛 Meal Plan for {target_day}")
            st.markdown("### 🍽️ Your Meals:")
            st.markdown(meals)
            
            # Add download functionality
            st.download_button(
                "📥 Download Meal Plan", 
                data=meals, 
                file_name=f"meal_plan_{target_day.lower()}.txt",
                mime="text/plain"
            )
            
        except Exception as e:
            if "authentication" in str(e).lower() or "api_key" in str(e).lower():
                st.error("❌ Authentication failed. Please check your GROQ_API_KEY in the .env file.")
            elif "rate" in str(e).lower() or "limit" in str(e).lower():
                st.error("❌ Rate limit exceeded. Please try again in a few minutes.")
            else:
                st.error(f"❌ Error: {e}")
                st.info("💡 Make sure your GROQ_API_KEY is correctly set in the .env file")

# -------------------------------
# 📚 Instructions
# -------------------------------
with st.expander("ℹ️ How to use this app"):
    st.markdown("""
    1. **Set up your API key**: Add your Groq API key to the `.env` file
    2. **Choose your preferences**: Select diet, number of people, and meal style
    3. **Get meal suggestions**: Click 'Suggest Meals' to generate a plan
    4. **Download**: Save your meal plan for your cook
    
    **Tips:**
    - Use 'Custom' day for specific planning
    - Add special requests in the notes section
    - Choose 'Light' for dinner to avoid heavy meals late at night
    """)

# -------------------------------
# 🔧 API Status
# -------------------------------
with st.sidebar:
    st.subheader("🔧 API Status")
    if groq_api_key:
        st.success("✅ API Key Configured")
    else:
        st.error("❌ API Key Missing")
    
    st.subheader("📊 Usage")
    st.info(f"Planning for: {target_day}")
    st.info(f"People: {people}")
    st.info(f"Diet: {diet}")
