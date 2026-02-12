# Facilities-Asset-Management-Analytics
This project simulates a real world asset management system using synthetic data, PostgreSQL, and SQL analysis. It showcases data generation, relational modeling, and business insights, ideal for portfolio presentation.


📌 Project Workflow

1. Synthetic Data Generation
- Used Python + Faker in Visual Studio Code to generate realistic asset and maintenance data.
- Saved datasets as CSV files:
  - assets.csv
  - maintenance_logs.csv

2. Database Setup
- Created a PostgreSQL database: facilities_db
- Designed two tables:
- assets: stores asset details
- maintenance_logs: tracks maintenance history
- Imported CSVs using COPY command in pgAdmin 4

3. Relational Modeling
- Linked maintenance_logs.asset_id to assets.asset_id via foreign key
- Created an ER diagram using dbdiagram.io

4. SQL Analysis
- Wrote and saved queries in queries.sql
- Explored asset value, maintenance cost, issue types, and technician performance


🧩 ER Diagram

<img width="774" height="376" alt="ER Diagram" src="https://github.com/user-attachments/assets/2499af47-9186-4dee-a702-9ee397491852" />


📊 Key Analyst Questions

Q1: What is the total asset value by location?

sql
SELECT location, SUM(cost) AS total_asset_value
FROM assets
GROUP BY location
ORDER BY total_asset_value DESC;

<img width="756" height="320" alt="image" src="https://github.com/user-attachments/assets/cecad43e-15b7-4076-a35d-8a2280388ac3" />


#Q2: Which asset categories are most expensive overall?

SELECT category, SUM(cost) AS total_category_cost
FROM assets
GROUP BY category
ORDER BY total_category_cost DESC;

<img width="763" height="377" alt="image" src="https://github.com/user-attachments/assets/008ec085-7916-4aa4-91e6-0b743ca2f04d" />


#Q3: Which assets have the highest maintenance cost?

SELECT a.asset_name, a.category, SUM(m.cost) AS total_maintenance_cost
FROM assets a
JOIN maintenance_logs m ON a.asset_id = m.asset_id
GROUP BY a.asset_name, a.category
ORDER BY total_maintenance_cost DESC
LIMIT 5;

<img width="975" height="318" alt="image" src="https://github.com/user-attachments/assets/78881450-2e8b-416d-b4b2-3352bfc6bd61" />


#Q4: What are the most common maintenance issue types?

SELECT issue_type, COUNT(*) AS issue_count
FROM maintenance_logs
GROUP BY issue_type
ORDER BY issue_count DESC;

<img width="975" height="318" alt="image" src="https://github.com/user-attachments/assets/9d2214f6-9761-4ac4-b8fe-280ccca7b89e" />


#Q5: Which technicians handled the most maintenance tasks?

SELECT technician, COUNT(*) AS task_count
FROM maintenance_logs
GROUP BY technician
ORDER BY task_count DESC
LIMIT 5;

<img width="975" height="318" alt="image" src="https://github.com/user-attachments/assets/84ac4200-376e-4c18-8efb-82b0f7731995" />


#Q6: What is the average maintenance cost per issue type?

SELECT issue_type, ROUND(AVG(cost), 2) AS avg_cost
FROM maintenance_logs
GROUP BY issue_type
ORDER BY avg_cost DESC;

<img width="636" height="317" alt="image" src="https://github.com/user-attachments/assets/24bc4e26-0724-4fdc-b010-a0f97e461cfb" />


#Q7: Join assets with maintenance logs for full history

SELECT a.asset_name, a.category, a.location, m.maintenance_date, m.technician, m.cost, m.issue_type
FROM assets a
JOIN maintenance_logs m ON a.asset_id = m.asset_id
ORDER BY m.maintenance_date DESC
LIMIT 10;

<img width="965" height="275" alt="image" src="https://github.com/user-attachments/assets/31c1e776-bd6d-4be8-8037-6a451bc1bb66" />

🧪 Tools Used
- Python + Faker (data generation)
- PostgreSQL 18
- pgAdmin 4
- Visual Studio Code
- dbdiagram.io (ER diagram)
