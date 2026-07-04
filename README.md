🍽️ Food Delivery Delay Analysis & Customer Satisfaction
📌 Project Overview

This project analyzes food delivery operations to identify the factors that contribute to delivery delays and their impact on customer satisfaction. The project follows a complete data analytics workflow—from raw data cleaning to SQL analysis and Power BI visualization.

The analysis helps answer business questions such as:

What causes delivery delays?
Which cities experience the most delayed orders?
Which vehicle type delivers the fastest?
How do weather and traffic conditions affect delivery time?
How can customer satisfaction be improved?
🎯 Problem Statement

Food delivery platforms often experience delays due to factors such as traffic, weather, distance, and multiple deliveries. These delays can negatively affect customer satisfaction and business performance.

The goal of this project is to analyze delivery data, identify the major causes of delays, and provide insights that can help improve delivery efficiency and customer experience.

🎯 Objectives
Clean and preprocess raw delivery data.
Analyze delivery performance using SQL.
Identify key factors affecting delivery time.
Measure customer satisfaction based on delivery duration.
Build an interactive dashboard for business insights.
🛠️ Tools & Technologies
Python (Pandas, NumPy, SQLAlchemy)
MySQL (SQL Queries)
Power BI
Git & GitHub
📂 Project Structure
Food-Delivery-Delay-Analysis/
│
├── data/
│   ├── Zomato Dataset 2.csv              # Raw Dataset
│   └── Cleaned_Zomato_Dataset.csv        # Cleaned Dataset
│
├── python/
│   └── Food_Delivary.py                  # Data Cleaning & Database Upload
│
├── sql/
│   └── food_delivery.sql                 # SQL Analysis Queries
│
├── dashboard/
│   └── food_delivery_dashboard.pbix      # Power BI Dashboard
│
└── README.md

📊 Project Workflow
1️⃣ Raw Dataset
Imported the original Zomato delivery dataset.
Checked for missing values and duplicate records.
Explored the dataset structure.
2️⃣ Data Cleaning (Python)

Performed the following preprocessing steps:

Converted column names to a standard format.
Handled missing values using:
Median
Mode
Group-wise median
Converted date and time columns.
Calculated delivery distance using the Haversine Formula.
Uploaded the cleaned dataset into a MySQL database.
3️⃣ Data Analysis (SQL)

Performed SQL analysis to answer business questions such as:

Average delivery time
Delayed orders
Fastest vehicle type
Effect of weather conditions
Customer satisfaction percentage
Delayed orders by city
Delivery partner performance
Festival vs Non-Festival analysis
4️⃣ Dashboard (Power BI)

Created an interactive dashboard including:

KPI Cards
Delivery Time Analysis
Customer Satisfaction
Weather Impact
Traffic Analysis
Vehicle Performance
City-wise Delay Analysis
Interactive Filters & Slicers
📈 Key Insights
Identified cities with the highest delivery delays.
Found the fastest delivery vehicle type.
Analyzed how weather and traffic influence delivery time.
Measured customer satisfaction using delivery time.
Compared delivery partner performance.
💡 Business Impact

The insights from this project can help delivery companies:

Reduce delivery delays
Improve route planning
Optimize delivery assignments
Increase customer satisfaction
Improve operational efficiency
