CREATE DATABASE delay_time;
USE delay_time;

SELECT *
FROM zomato LIMIT 5;

-- Q1. What is the average delivery time for all orders?
SELECT type_of_order,AVG(`time_taken_(min)`) as avg_time
FROM zomato
GROUP BY type_of_order
ORDER BY avg_time DESC;

-- Q2. How many orders were delayed (e.g., above a certain threshold like 45 minutes)?
SELECT COUNT(*) AS total_delayed_orders
FROM zomato
WHERE `time_taken_(min)` > 45;

-- Q3. Which city has the highest average delivery time?
SELECT city,AVG(`time_taken_(min)`) as avg_time_min
FROM zomato
GROUP BY city
ORDER BY avg_time_min DESC;

-- Q4. What is the customer satisfaction percentage 
-- (based on delivery time categories like ≤30 min, 31–45 min, >45 min)?

SELECT 
CASE 
	WHEN `time_taken_(min)`<=30 THEN "Satisfied"
    WHEN `time_taken_(min)` BETWEEN 31 AND 45 THEN "Neutral"
    ELSE "DisSatisfied"
    END as customer_satisfaction,
COUNT(*) as total_orders,
ROUND(COUNT(*)*100/(SELECT COUNT(*) FROM zomato),2) as percentage
FROM zomato
GROUP BY customer_satisfaction;

-- Q5. Which delivery partner has the highest average delivery time?
    
SELECT delivery_person_id,AVG(`time_taken_(min)`) as avg_time
from zomato
group by delivery_person_id
ORDER BY avg_time DESC LIMIT 5;

-- Q6. Is there a difference in average delivery time between festival and non-festival days?
SELECT festival,AVG(`time_taken_(min)`) as avg_time
from zomato
group by festival;

-- Q7. What is the total number of delayed orders by weather condition?
SELECT
    Weather_conditions,
    COUNT(*) AS delayed_orders
FROM zomato
WHERE `time_taken_(min)` > 45
GROUP BY weather_conditions
ORDER BY delayed_orders DESC;

-- Q8. Which vehicle type delivers the fastest on average?
SELECT
    type_of_vehicle,
    AVG(`time_taken_(min)`) AS avg_delivery_time
FROM zomato
GROUP BY type_of_vehicle
ORDER BY avg_delivery_time ASC;
-- Q9. What percentage of orders are satisfied (≤30 minutes) by each delivery partner?
SELECT
    delivery_person_id,
    ROUND(
        SUM(CASE WHEN `time_taken_(min)` <= 30 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS satisfaction_percentage
FROM zomato
GROUP BY delivery_person_id
ORDER BY satisfaction_percentage DESC;

-- Q10. Rank cities by total number of delayed orders to see which needs the most improvement.
SELECT
    city,
    COUNT(*) AS delayed_orders,
    RANK() OVER (ORDER BY COUNT(*) DESC) AS city_rank
FROM zomato
WHERE `time_taken_(min)` > 45
GROUP BY city;