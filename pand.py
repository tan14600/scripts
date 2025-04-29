import pandas as pd

# Sample messy data
data = {
    "transaction_id": [101, 102, 103, 104, 105, 105],
    "merchant": ["Amazon", "Walmart", "Amazon", "Target", "Walmart", "Walmart"],
    "amount": [50, None, 75, 100, None, None],  # Missing values
    "status": ["SUCCESS", "FAILED", "SUCCESS", "FAILED", "FAILED", "FAILED"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# 1️⃣ Remove duplicates
df = df.drop_duplicates()

# 2️⃣ Fill missing values in 'amount' with the column's median
df['amount'] = df['amount'].fillna(df['amount'].median())

# 3️⃣ Convert all text columns to lowercase for consistency
df['merchant'] = df['merchant'].str.lower()
df['status'] = df['status'].str.lower()

# Print cleaned data
print("✅ Cleaned Data:\n", df)