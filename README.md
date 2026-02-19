## Project Description
This project is a personal study. I built this project to understand automating a data science pipeline from start to finish. 
The main goal is to segment customers for an e-commerce platform using RFM (Recency, Frequency, Monetary) technique. This project also uses K-Means Clustering algorithm that connects to a database and runs automatically.

During this project i learnt:
- PostgreSQL database 
- K-Means algorithm 
- Using "Elbow Method" to find the best number of clusters mathematically
- Basics of MLOps by containerizing the application with Docker.
- Automating scripts using Linux Cron Jobs.

Based on the results customers are divided into 3 groups:
1. Champions: Customers who shops often and spends lots of money.
2. Active Regulars: Customers who are active and shops frequently but spends average amounts.
3. Churned: Customers who have not visited the store for a long time

## Visualization and Results
<img width="1093" height="874" alt="Dashboard " src="https://github.com/user-attachments/assets/11bc4e75-6134-4aab-9a59-d62492749a69" />
Cohort retention matrix shows how many customers continue to shop over months.
RFM Distribution is for understandşng the Recency and Monetary values of customers.
ML Cluster Map shows 3 different customer segments found by K-Means algorithm

## Dashboard Link
https://public.tableau.com/views/E-CommerceRFMandCohortAnalysis/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

## Tech Stack
- PostgreSQL, SQL
- Python (Pandas, Scikit-Learn, Matplotlib)
- Docker
- Tableau Public

## Dataset
https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci?resource=download

## How to Run the Project
1. Clone this repository to your local machine.
2. Create a .env file and add your DB_PASSWORD.
3. Use the following commands for Docker:
   ```bash
   docker build -t rfm-pipeline .
   docker run --network host rfm-pipeline
