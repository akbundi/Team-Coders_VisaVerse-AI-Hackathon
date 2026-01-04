import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8007"

st.set_page_config(
    page_title="AI Global Mobility Assistant",
    layout="centered"
)

st.title("🌍 AI Global Mobility Assistant")
st.write("Get visa and work permit guidance tailored to your situation.")

# ---------------- BASIC DETAILS ----------------
country = st.selectbox(
    "Destination Country",
    ["Germany", "Canada", "USA", "England", "Netherlands"]
)

nationality = st.text_input("Nationality")

# ---------------- PURPOSE ----------------
purpose = st.selectbox(
    "Purpose of Move",
    ["Job", "Study", "Freelance", "Dependent"]
)

# ---------------- JOB DETAILS ----------------
job_role = st.text_input("Job Role (if applicable)")

salary_range = st.selectbox(
    "Salary Range",
    [
        "Select",
        "Below €30,000",
        "€30,000 – €50,000",
        "€50,000 – €70,000",
        "Above €70,000"
    ]
)

# ---------------- SPONSORSHIP ----------------
employer_sponsorship = st.selectbox(
    "Employer Sponsorship Available?",
    ["Select", "Yes", "No"]
)

# ---------------- TIMELINE ----------------
timeline = st.selectbox(
    "Timeline",
    ["Urgent", "Flexible"]
)

# ---------------- VISA SUMMARY ----------------
st.subheader("🛂 Visa & Work Permit Summary")

if st.button("Get Visa Summary"):
    payload = {
        "country": country,
        "nationality": nationality,
        "purpose": purpose,
        "job_role": job_role,
        "salary_range": salary_range,
        "employer_sponsorship": employer_sponsorship,
        "timeline": timeline
    }

    res = requests.post(
        f"{BACKEND_URL}/visa/summary",
        json=payload
    )

    if res.status_code == 200:
        data = res.json()

        st.success(data["summary"])

        st.markdown("### 🔐 AI Confidence Score")
        st.progress(data["ai_confidence_score"])
        st.write(f"**Overall Confidence:** {int(data['ai_confidence_score'] * 100)}%")

        # ✅ Professional, clear disclaimer text
        st.caption(
            "This score reflects the clarity of the information provided and the "
            "consistency of the AI-generated guidance. It does not indicate visa "
            "approval or a legal decision."
        )

    else:
        st.error("Failed to generate visa summary")
        st.json(res.json())
