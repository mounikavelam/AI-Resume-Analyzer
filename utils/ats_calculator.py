def calculate_ats_score(
    resume_skills,
    jd_skills
):

    if len(jd_skills) == 0:
        return 0

    matched = []

    for skill in jd_skills:

        if skill in resume_skills:
            matched.append(skill)

    score = (
        len(matched)
        /
        len(jd_skills)
    ) * 100

    return round(score, 2)