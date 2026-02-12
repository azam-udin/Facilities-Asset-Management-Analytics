from faker import Faker
import pandas as pd
import random

fake = Faker()

#Define Categories

asset_types = ["Air Conditioner", "Generator", "Elevator", "Pump", "Lighting System"]
statuses = ["Active", "Retired", "Under Maintenance"]

#Generate 200 assets

assets = []
for i in range(1, 201):
    assets.append({
        "asset_id": i,
        "type": random.choice(asset_types),
        "location": f"Building {random.choice(['A','B','C','D'])}",
        "purchase_date": fake.date_between(start_date='-10y', end_date='today'),
        "cost": round(random.uniform(5000, 50000), 2),
        "status": random.choice(statuses)
    })

#Save to CSV

df_assets = pd.DataFrame(assets)
df_assets.to_csv("assets.csv", index=False)
print("✅ Assets dataset created: assets.csv")

#Generate 500 maintenance records

maintenance_logs = []
for i in range(1, 501):
    maintenance_logs.append({
        "log_id": i,
        "asset_id": random.randint(1, 200),  # FK to Assets

        "technician": fake.name(),
        "date": fake.date_between(start_date='-5y', end_date='today'),
        "cost": round(random.uniform(100, 5000), 2),
        "issue_type": random.choice(["Electrical", "Mechanical", "Software", "Routine"])
    })

# Save to CSV

df_logs = pd.DataFrame(maintenance_logs)
df_logs.to_csv("maintenance_logs.csv", index=False)
print("✅ Maintenance logs dataset created: maintenance_logs.csv")
