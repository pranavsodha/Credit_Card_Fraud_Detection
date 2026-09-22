import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

BASE_DIR = Path(__file__).resolve().parent

# 1. Load the dataset (replace with your file path)
print("Loading data...")
df = pd.read_csv(BASE_DIR / "creditcard.csv")

# 2. Separate features and target (assuming 'Class' is the fraud indicator)
X = df.drop(columns=['Class'])
y = df['Class']

# 3. Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 4. Train a fast baseline model
print("Training the model...")
model = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# 5. Save the trained model and test data for real-time simulation
print("Saving model and test data...")
joblib.dump(model, BASE_DIR / "fraud_model.pkl")
X_test.head(100).to_csv(BASE_DIR / "simulation_stream.csv", index=False)
print("Setup complete!")