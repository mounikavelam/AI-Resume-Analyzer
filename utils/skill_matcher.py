import pandas as pd

def extract_skills(text):

    # Load skills database
    skills_df = pd.read_csv("models/skills.csv")

    # Convert text to lowercase
    text = str(text).lower()

    found_skills = []

    # Check every skill from CSV
    for skill in skills_df["skill"]:

        skill = str(skill).strip().lower()

        if skill in text:
            found_skills.append(skill)

    # Remove duplicates
    found_skills = list(set(found_skills))

    return sorted(found_skills)