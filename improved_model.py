import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ----------------------
# Load dataset
# ----------------------
df = pd.read_csv("ai_student_impact_dataset.csv")

# ----------------------
# Data preparation (encoding)
# ----------------------
df_encoded = pd.get_dummies(df, drop_first=True)

# ----------------------
# Features & target
# ----------------------
X = df_encoded.drop(columns=["Post_Semester_GPA"])
y = df_encoded["Post_Semester_GPA"]

# ----------------------
# Train-test split
# ----------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------
# Improved Model (Random Forest)
# ----------------------
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ----------------------
# Predictions
# ----------------------
y_pred = model.predict(X_test)

# ----------------------
# Evaluation
# ----------------------
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Improved Model Results")
print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)