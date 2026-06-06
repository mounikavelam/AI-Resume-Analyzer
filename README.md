🚀 AI Resume Analyzer

📌 Overview

AI Resume Analyzer is a Streamlit-based web application that helps job seekers evaluate their resumes against a Job Description (JD). The system extracts skills from both the resume and job description, calculates an ATS (Applicant Tracking System) score, identifies matched and missing skills, and provides recommendations for improvement.

---

✨ Features

- 📄 Upload Resume (PDF)
- 💼 Analyze Job Description
- 🎯 ATS Score Calculation
- 🔍 Skill Extraction
- 🤝 Skill Matching
- 📊 NLP Similarity Analysis
- ✅ Matched Skills Detection
- ❌ Missing Skills Detection
- 💡 Skill Recommendations
- 🥧 Skill Match Visualization
- 📈 Resume Statistics Dashboard
- 📥 Download ATS Report

---

🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Scikit-learn
- NLP Techniques
- Regular Expressions (Regex)

---

📂 Project Structure

AI_RESUME_ANALYZER/
│
├── assets/
├── data/
├── models/
│   └── skills.csv
│
├── reports/
│
├── utils/
│   ├── ats_calculator.py
│   ├── pdf_reader.py
│   ├── similarity.py
│   ├── skill_matcher.py
│   └── text_cleaner.py
│
├── app.py
├── requirements.txt
└── README.md

---

⚙️ Installation

Clone Repository

git clone <repository-url>
cd AI_RESUME_ANALYZER

Install Dependencies

pip install -r requirements.txt

Run Application

streamlit run app.py

---

🚀 How It Works

1. Upload a resume in PDF format.
2. Paste a job description.
3. The system extracts text from the resume.
4. Skills are identified from both resume and JD.
5. ATS score and NLP similarity are calculated.
6. Matched and missing skills are displayed.
7. Recommendations are generated.
8. ATS report can be downloaded.

---

📊 Sample Output

- ATS Score
- Skill Match Percentage
- Matched Skills
- Missing Skills
- Resume Strengths
- Resume Statistics
- Recommendations

---

🔮 Future Enhancements

- PDF Report Generation
- AI-Based Resume Suggestions
- Resume Ranking System
- Multi-Resume Comparison
- Interview Question Generation
- LinkedIn Profile Analysis

---

👩‍💻 Author

Velam Mounika

B.Tech – Computer Science and Machine Learning

Dadi Institute of Engineering and Technology

Andhra Pradesh, India