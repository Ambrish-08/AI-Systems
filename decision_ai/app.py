import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Decision AI", page_icon="🧠", layout="centered")

st.title("🧠 Decision AI Assistant")
st.subheader("AI-powered Drone / Vehicle Real-Time Decision Support")

st.write(
    "Enter a real-world situation. The AI will analyze the risk level and suggest the best action."
)

api_key = st.text_input("OpenAI API Key", type="password")

situation = st.text_area(
    "Situation Input",
    placeholder="Example: Smoke coming from engine bay, battery unstable, vehicle losing control.",
    height=140
)

def get_ai_decision(user_input: str, key: str) -> str:
    client = OpenAI(api_key=key)

    system_prompt = """
You are an AI safety decision system for drones, vehicles, and autonomous machines.

Your task:
1. Read the situation carefully.
2. Infer the actual level of danger, even if the wording is indirect.
3. Respond in this exact format:

Risk Level: <Low / Medium / High / Critical>
Recommended Action: <one clear action>
Reason: <short explanation>

Important:
- Fire, smoke, overheating, engine failure, brake failure, crash risk, or loss of control should usually be treated as High or Critical.
- Weak signal, low battery, and obstacle combinations should raise severity.
- Focus on safety-first decision making.
- Be concise and practical.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Situation: {user_input}"}
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content

if st.button("Analyze Situation"):
    if not situation.strip():
        st.warning("Please enter a situation first.")
    elif not api_key.strip():
        st.warning("Please enter your OpenAI API key.")
    else:
        try:
            result = get_ai_decision(situation, api_key)

            st.markdown("### AI Result")
            st.write(result)

            st.markdown("### System Thinking")
            st.write(
                "This version uses an LLM-based reasoning layer to interpret open-ended operational scenarios "
                "and recommend safety-focused actions."
            )

        except Exception as e:
            st.error(f"Error: {e}")
