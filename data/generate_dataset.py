import pandas as pd
import random

data = {
    'time': pd.date_range(start='2024-01-01', periods=1000, freq='T'),
    'cpu_usage': [random.randint(10, 100) for _ in range(1000)],
    'temperature': [random.uniform(20, 80) for _ in range(1000)]
}
df = pd.DataFrame(data)
df['is_anomaly'] = ((df['cpu_usage'] > 90) | (df['temperature'] > 75)).astype(int)  # Label anomalies
df.to_csv('data/system_health.csv', index=False)
print("Dataset created: system_health.csv")
