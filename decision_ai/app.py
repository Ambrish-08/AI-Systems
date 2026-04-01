import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Decision AI", page_icon="🧠")

st.title("🧠 AI Decision System")
st.subheader("Real-Time Drone / Vehicle Decision Intelligence")

# 🔑 API KEY INPUT
api_key = st.text_input("Enter your OpenAI API Key", type="password")

client = None
if api_key:
    client = OpenAI(api_key=api_key)

situation = st.text_area(
    "Enter Situation",
    placeholder="Obstacle detected ahead, battery at 15%, GPS signal weak"
)

def get_ai_decision(user_input):
    prompt = f"""
You are an intelligent control system for a drone or autonomous vehicle.

Analyze the situation and respond in this format:

Risk Level:
Recommended Action:
Reason:

Situation: {user_input}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

if st.button("Analyze with AI"):
    if not api_key:
        st.warning("Enter API key first")
    elif not situation.strip():
        st.warning("Enter a situation")
    else:
        result = get_ai_decision(situation)

        st.markdown("### AI Output")
        st.write(result)

        st.markdown("### System Thinking")
        st.write(
            "This simulates a decision layer in an intelligent system, "
            "where AI processes environmental inputs and suggests optimal actions."
        )
