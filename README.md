## Project Description
This project is a personal study. I built this project to understand automating a data science pipeline from start to finish. 
The main goal is to segment customers for an e-commerce platform using RFM (Recency, Frequency, Monetary) technique. This project also uses K-Means Clustering algorithm that connects to a database and runs automatically.

During this project i learnt:
- PostgreSQL database 
- K-Means algorithm 
- Using "Elbow Method" to find the best number of clusters mathematically
- Basics of MLOps by containerizing the application with Docker.
- Automating scripts using Linux Cron Jobs.

## Visualization and Results
<img width="1093" height="874" alt="Dashboard " src="https://github.com/user-attachments/assets/11bc4e75-6134-4aab-9a59-d62492749a69" />
- Customer Segmentation Tree Map (Sheet 1): This sheet shows the distribution of different customer segments based on their RFM scores as a Tree Map. I used the data/rfm_results.csv file which contains the segment names for every customer. This map helps to see which segment is the largest.
  
- RFM Distribution (Sheet 2): This visualization shows how customers behave in the dataset. I used the calculated metrics from the data/rfm_results.csv file to create a chart that compares Customer Segments with their Monetary values. This analysis helps to see the financial profile of each segment. For example it shows if the company relies on a small group of high spending customers.
  
- Cohort Analysis (Sheet 3): This sheet shows how different groups (cohorts) stay active over a 12 month period. I created a grid that shows the number of active customers for each month starting from their first purchase date. I used the data from data/cohort_results.csv. This table helps to identify specific months where customer loyalty was higher or lower.
  
- K-Means Cluster Map (Sheet 4): This sheet shows how customers are grouped based on their spending. I used the data/ml_rfm_results.csv file. I applied a Logarithmic Scale to both axes in Tableau to handle the large range of values and make the clusters easier to see. I used the "Cluster" field for identifying the three main groups: High Value Champions, Active Regulars, and Churned. This map provides a clear visualization of how the algorithm groups similar customers for better targeted marketing strategies.


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
