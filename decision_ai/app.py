import streamlit as st

st.set_page_config(page_title="Decision AI", page_icon="🧠", layout="centered")

st.title("🧠 Decision AI Assistant")
st.subheader("Drone / Vehicle Real-Time Decision Support")

st.write(
    "Enter a real-world situation. The system will analyze the risk level and suggest the best action."
)

situation = st.text_area(
    "Situation Input",
    placeholder="Example: Obstacle detected ahead, battery at 15%, GPS signal weak.",
    height=140
)

def simple_decision_engine(user_input: str):
    text = user_input.lower()

    action = "Continue mission with caution."
    risk = "Low"
    reason = "No major threat indicators detected."

    if "battery" in text:
        if "10%" in text or "15%" in text or "low battery" in text:
            action = "Return to base immediately."
            risk = "High"
            reason = "Battery level is critically low for safe continuation."

    if "obstacle" in text or "collision" in text:
        action = "Slow down, avoid obstacle, and re-route if needed."
        risk = "Medium"
        reason = "Obstacle detected in path; navigation adjustment required."

    if "gps signal weak" in text or "signal weak" in text or "communication loss" in text:
        action = "Switch to safe mode and stabilize before continuing."
        risk = "High"
        reason = "Weak communication or navigation signal increases operational risk."

    if ("battery" in text and ("15%" in text or "10%" in text or "low battery" in text)
        and ("obstacle" in text or "collision" in text)):
        action = "Abort mission and return to base using safest available route."
        risk = "Critical"
        reason = "Low battery combined with obstacle risk makes continuation unsafe."

    if ("battery" in text and ("15%" in text or "10%" in text or "low battery" in text)
        and ("gps signal weak" in text or "signal weak" in text or "communication loss" in text)):
        action = "Land at the nearest safe location or return immediately if stable."
        risk = "Critical"
        reason = "Low battery and weak signal together create severe mission risk."

    return risk, action, reason

if st.button("Analyze Situation"):
    if not situation.strip():
        st.warning("Please enter a situation first.")
    else:
        risk, action, reason = simple_decision_engine(situation)

        st.markdown("### Result")
        st.write(f"**Risk Level:** {risk}")
        st.write(f"**Recommended Action:** {action}")
        st.write(f"**Reason:** {reason}")

        st.markdown("### System Thinking")
        st.write(
            "This simulates how an intelligent system can combine environmental input, "
            "operational constraints, and safety logic to support real-time decisions."
        )
