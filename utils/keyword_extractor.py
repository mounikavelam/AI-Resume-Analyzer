import pandas as pd


def extract_keywords(text):

    text = text.lower()

    skills_df = pd.read_csv("models/skills.csv")

    skills_list = skills_df["skill"].dropna().str.lower().tolist()

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))