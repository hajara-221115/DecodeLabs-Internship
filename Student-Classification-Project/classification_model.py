import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load dataset
data = pd.read_csv("student_data.csv")

print("\nDataset:")
print(data.head())

# Step 2: Features and target variable
X = data[["Hours_Studied", "Attendance", "Assignments"]]
y = data["Result"]

# Convert Pass/Fail into numerical values
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Step 3: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Size:", len(X_train))
print("Testing Data Size:", len(X_test))

# Step 4: Train classification model
model = DecisionTreeClassifier()

model.fit(X_train, y_train)

# Step 5: Predictions
predictions = model.predict(X_test)

# Step 6: Evaluate model
accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:", accuracy*100,"%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Step 7: Test custom input
hours = float(input("\nEnter study hours: "))
attendance = float(input("Enter attendance percentage: "))
assignments = float(input("Enter completed assignments: "))

new_student = pd.DataFrame({
    "Hours_Studied": [hours],
    "Attendance": [attendance],
    "Assignments": [assignments]
})

prediction = model.predict(new_student)

result = encoder.inverse_transform(prediction)

print("\nPrediction:", result[0])
