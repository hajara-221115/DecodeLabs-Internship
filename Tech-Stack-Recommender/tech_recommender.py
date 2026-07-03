import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("raw_skills.csv")

print("\n=== Tech Stack Recommender ===")

# User input
skill1=input("Enter Skill 1: ")
skill2=input("Enter Skill 2: ")
skill3=input("Enter Skill 3: ")

user_skills=skill1+" "+skill2+" "+skill3

# Combine dataset skills with user input
all_skills=data["Skills"].tolist()

all_skills.append(user_skills)

# TF-IDF conversion
vectorizer=TfidfVectorizer()

tfidf_matrix=vectorizer.fit_transform(all_skills)

# Calculate similarity
similarity=cosine_similarity(
    tfidf_matrix[-1],
    tfidf_matrix[:-1]
)

# Add scores to dataframe
data["Similarity Score"]=similarity.flatten()

# Sort recommendations
recommendations=data.sort_values(
    by="Similarity Score",
    ascending=False
)

# Display top 3
print("\nTop 3 Recommended Career Paths:\n")

for index,row in recommendations.head(3).iterrows():

    print("Role:",row["Role"])
    print("Required Skills:",row["Skills"])
    print("Match Score:",round(row["Similarity Score"]*100,2),"%")
    print("-"*40)