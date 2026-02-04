import pandas as pd

# Load dataset
data = pd.read_csv("students.csv")

# Calculate total and percentage
data["Total"] = data[["Maths", "Science", "English"]].sum(axis=1)
data["Percentage"] = data["Total"] / 3

# Assign grade
def grade(p):
    if p >= 80:
        return "A"
    elif p >= 60:
        return "B"
    elif p >= 40:
        return "C"
    else:
        return "Fail"

data["Grade"] = data["Percentage"].apply(grade)

print(data)
