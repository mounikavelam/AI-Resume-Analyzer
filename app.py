import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

from utils.pdf_reader import extract_text
from utils.text_cleaner import clean_text
from utils.skill_matcher import extract_skills
from utils.similarity import calculate_similarity
from utils.ats_calculator import calculate_ats_score

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide"
)

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<h1 style='text-align:center;'>
🚀 AI Resume Analyzer
</h1>

<p style='text-align:center;font-size:20px;'>
Smart ATS Resume Scanner
</p>

<hr>
""", unsafe_allow_html=True)

# ==========================================
# INPUTS
# ==========================================

uploaded_resume = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "💼 Paste Job Description"
)

# ==========================================
# MAIN LOGIC
# ==========================================

if uploaded_resume and job_description:

    resume_text = extract_text(uploaded_resume)

    with st.expander("📄 View Extracted Resume Text"):
        st.write(resume_text)

    cleaned_resume = clean_text(
        resume_text
    )

    cleaned_jd = clean_text(
        job_description
    )

    # --------------------------------------
    # SKILL EXTRACTION
    # --------------------------------------

    resume_skills = extract_skills(
        cleaned_resume
    )

    jd_skills = extract_skills(
        cleaned_jd
    )

    # --------------------------------------
    # ATS SCORE
    # --------------------------------------

    ats_score = calculate_ats_score(
        resume_skills,
        jd_skills
    )

    similarity_score = calculate_similarity(
        cleaned_resume,
        cleaned_jd
    )

    final_score = round(
        (ats_score * 0.7)
        +
        (similarity_score * 0.3),
        2
    )

    # --------------------------------------
    # ATS METER
    # --------------------------------------

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=final_score,
        title={'text': "ATS Score"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "green"}
        }
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------
    # STATUS
    # --------------------------------------

    if final_score >= 80:

        st.success(
            f"🟢 Excellent Match ({final_score}%)"
        )

    elif final_score >= 60:

        st.warning(
            f"🟡 Good Match ({final_score}%)"
        )

    else:

        st.error(
            f"🔴 Low Match ({final_score}%)"
        )

    # --------------------------------------
    # SCORE BREAKDOWN
    # --------------------------------------

    st.subheader(
        "📊 Score Breakdown"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Skill Match",
        f"{ats_score}%"
    )

    col2.metric(
        "NLP Similarity",
        f"{similarity_score}%"
    )

    col3.metric(
        "Final ATS Score",
        f"{final_score}%"
    )

    # --------------------------------------
    # PROGRESS BAR
    # --------------------------------------

    st.subheader(
        "🎯 Skill Match Percentage"
    )

    st.progress(
        int(ats_score)
    )

    st.write(
        f"{ats_score}%"
    )

    # --------------------------------------
    # MATCHED & MISSING
    # --------------------------------------

    matched = []

    missing = []

    for skill in jd_skills:

        if skill in resume_skills:

            matched.append(skill)

        else:

            missing.append(skill)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "✅ Matched Skills"
        )

        if matched:

            for skill in matched:

                st.write(
                    "✔",
                    skill
                )

        else:

            st.write(
                "No skills matched"
            )

    with col2:

        st.subheader(
            "❌ Missing Skills"
        )

        if missing:

            for skill in missing:

                st.write(
                    "❌",
                    skill
                )

        else:

            st.success(
                "No missing skills"
            )

    # --------------------------------------
    # RECOMMENDATIONS
    # --------------------------------------

    if missing:

        st.subheader(
            "💡 Recommendations"
        )

        st.write(
            "Consider learning these skills:"
        )

        for skill in missing:

            st.write(
                "📌",
                skill
            )

    # --------------------------------------
    # PIE CHART
    # --------------------------------------

    st.subheader(
        "🥧 Skill Match Analysis"
    )

    pie_data = {
        "Category": ["Matched", "Missing"],
        "Count": [len(matched), len(missing)]
    }

    fig = px.pie(
        pie_data,
        values="Count",
        names="Category",
        title="Matched vs Missing Skills"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------
    # RESUME STRENGTHS
    # --------------------------------------

    st.subheader(
        "💪 Resume Strengths"
    )

    if resume_skills:

        cols = st.columns(3)

        for i, skill in enumerate(resume_skills):

            with cols[i % 3]:

                st.success(skill)

    # --------------------------------------
    # RESUME OVERVIEW
    # --------------------------------------

    st.subheader(
        "📋 Resume Overview"
    )

    if len(resume_skills) > 0:

        st.write(
            f"""
Candidate possesses skills in
{', '.join(resume_skills)}.

Resume contains
{len(resume_skills)}
technical skills.
"""
        )

    # --------------------------------------
    # STATISTICS
    # --------------------------------------

    st.subheader(
        "📈 Statistics"
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Resume Skills",
        len(resume_skills)
    )

    c2.metric(
        "JD Skills",
        len(jd_skills)
    )

    c3.metric(
        "Matched",
        len(matched)
    )

    c4.metric(
        "Missing",
        len(missing)
    )

    # --------------------------------------
    # DOWNLOAD REPORT
    # --------------------------------------

    report = f"""
AI RESUME ANALYZER REPORT

ATS SCORE:
{final_score}%

SKILL MATCH:
{ats_score}%

NLP SIMILARITY:
{similarity_score}%

MATCHED SKILLS:
{', '.join(matched)}

MISSING SKILLS:
{', '.join(missing)}

RECOMMENDATIONS:
{', '.join(missing)}
"""

    st.download_button(
        label="📥 Download ATS Report",
        data=report,
        file_name="ATS_Report.txt",
        mime="text/plain"
    )