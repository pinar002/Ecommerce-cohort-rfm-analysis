import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

load_dotenv()
db_password = os.getenv('DB_PASSWORD')

# DB connection
engine = create_engine(f'postgresql://postgres:{db_password}@localhost:5432/postgres')

def run_pipeline():
    print("Connecting to db...")
    
    sql_query = """
    WITH rfm_base AS (
        SELECT 
            "Customer ID",
            MAX(CAST("InvoiceDate" AS TIMESTAMP)) as last_purchase_date,
            COUNT(DISTINCT "Invoice") as frequency,
            SUM(CAST("Quantity" AS NUMERIC) * CAST("Price" AS NUMERIC)) as monetary
        FROM online_retail_ii
        WHERE "Customer ID" IS NOT NULL 
          AND "Customer ID" != ''
          AND "Invoice" NOT LIKE 'C%%'
          AND CAST("Quantity" AS NUMERIC) > 0
        GROUP BY "Customer ID"
    )
    SELECT 
        "Customer ID",
        EXTRACT(DAY FROM (
            (SELECT MAX(CAST("InvoiceDate" AS TIMESTAMP)) FROM online_retail_ii) - last_purchase_date
        )) AS recency,
        frequency,
        monetary
    FROM rfm_base;
    """
    
    df_rfm = pd.read_sql(sql_query, engine)
    print(f"Extracted data for {len(df_rfm)} customers.")

    print("Scaling features for ML...")
    features = df_rfm[['recency', 'frequency', 'monetary']]
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    print("Running elbow method...")
    wcss = []
    max_clusters = 10
    
    for i in range(1, max_clusters + 1):
        kmeans_test = KMeans(n_clusters=i, random_state=42)
        kmeans_test.fit(features_scaled)
        wcss.append(kmeans_test.inertia_)

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, max_clusters + 1), wcss, marker='o', linestyle='--')
    plt.title('Elbow method for optimal k value')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('WCSS (Inertia)')
    plt.grid(True)
    plt.savefig('images/elbow_graph.png')
    print("Elbow graph saved as elbow_graph.png")

    print("Applying ML (K-Means) model...")

    kmeans_final = KMeans(n_clusters=3, random_state=42)
    df_rfm['cluster'] = kmeans_final.fit_predict(features_scaled)

    print("Exporting results...")
    df_rfm.to_csv('data/ml_rfm_results.csv', index=False)
    print("Finish")

if __name__ == "__main__":
    run_pipeline()