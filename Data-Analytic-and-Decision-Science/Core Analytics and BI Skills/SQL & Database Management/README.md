# Maven Movies SQL Business Intelligence Project

## Project Overview

This project simulates a business intelligence audit for a fictional DVD rental company called **Maven Movies**. The objective is to support strategic business decisions by answering 16 key business questions using SQL. These questions cover operational, customer, and financial aspects of the company, using SQL to extract insights from a relational database.

The use case resembles a real-world scenario where a company is preparing for a potential **merger, acquisition, internal audit**, or **performance review** — and stakeholders such as **investors, analysts, and management** demand hard evidence and KPIs derived from the company’s data infrastructure.

---

## Dataset Description

The database consists of multiple normalized tables representing the operations of a DVD rental business. Key tables include:

- `staff`: Employee information.
- `store`: Store location and management.
- `inventory`: Individual DVDs and their availability.
- `customer`: Basic information on customers.
- `rental`: Rentals made by customers.
- `payment`: Financial transactions from rentals.
- `film`: Films in inventory.
- `category`: Film categories (e.g., Comedy, Action).
- `actor`: Actors in each film.
- `film_actor`: Relationship table between `film` and `actor`.
- `investor` and `advisor`: Stakeholder data.

---

## SQL Techniques Used

The following SQL techniques were used across the queries:

- `JOIN` operations (INNER JOIN, LEFT JOIN) to combine relational data
- `GROUP BY`, `COUNT()`, `SUM()`, `AVG()` for aggregations
- `CASE` statements for conditional output
- `UNION` to merge different data sources
- `ORDER BY` for sorting KPIs
- Filtering with `WHERE` clauses (e.g., filtering active customers)
- Use of `DISTINCT` to eliminate duplicates

These techniques reflect real-world SQL use in business analytics, reporting, and dashboard creation.

---

## 📊 Business Questions & SQL Solutions

Below are the 16 business intelligence questions, along with the SQL logic, purpose, and the business impact of each.

---

### 1. Retrieve the full names and store locations of all staff members.

- **Tables Used**: `staff`, `store`
- **SQL Skills**: JOIN
- **Business Use**: HR and workforce planning — helps determine staffing per location.
- **Insight**: Understand employee distribution and management responsibility across stores.

---

### 2. Count the number of inventory items in each store.

- **Tables Used**: `store`, `inventory`
- **SQL Skills**: JOIN, COUNT(), GROUP BY
- **Business Use**: Inventory valuation and logistics planning.
- **Insight**: Which store has more physical assets; supports reallocation or auditing.

---

### 3. Calculate the number of films available in each category.

- **Tables Used**: `category`, `film_category`
- **SQL Skills**: JOIN, GROUP BY, COUNT()
- **Business Use**: Content strategy.
- **Insight**: Helps marketing focus on categories with high or low volume.

---

### 4. Identify the top 5 most rented movies.

- **Tables Used**: `film`, `inventory`, `rental`
- **SQL Skills**: JOIN, GROUP BY, COUNT(), ORDER BY
- **Business Use**: Revenue optimization.
- **Insight**: These films are your cash cows — worth promoting or keeping in stock.

---

### 5. Find the customers who have rented more than 30 movies.

- **Tables Used**: `customer`, `rental`
- **SQL Skills**: JOIN, GROUP BY, HAVING
- **Business Use**: Customer segmentation.
- **Insight**: Identify VIPs for retention, upselling, and loyalty programs.

---

### 6. Total payment collected from each customer.

- **Tables Used**: `customer`, `payment`
- **SQL Skills**: JOIN, SUM(), GROUP BY
- **Business Use**: Revenue analysis and Customer Lifetime Value (CLTV).
- **Insight**: Supports targeted marketing or premium customer programs.

---

### 7. Average rental duration for each film.

- **Tables Used**: `rental`, `inventory`, `film`
- **SQL Skills**: JOIN, DATE_DIFF or TIMESTAMP logic, GROUP BY, AVG()
- **Business Use**: Operational insights.
- **Insight**: High average duration may suggest long-term interest or lack of availability.

---

### 8. Identify inactive customers.

- **Tables Used**: `customer`
- **SQL Skills**: WHERE clause (`active = 0`)
- **Business Use**: Churn analysis.
- **Insight**: Helps in re-engagement campaigns or pruning CRM database.

---

### 9. Determine the most active customers per store.

- **Tables Used**: `rental`, `customer`, `store`
- **SQL Skills**: JOIN, GROUP BY, COUNT(), ORDER BY, LIMIT
- **Business Use**: Store-level performance metrics.
- **Insight**: Identify local influencers and customer behavior by location.

---

### 10. Identify staff members with the highest number of rentals processed.

- **Tables Used**: `staff`, `rental`
- **SQL Skills**: JOIN, GROUP BY, COUNT(), ORDER BY
- **Business Use**: HR performance review.
- **Insight**: Reward high-performing employees or investigate workload distribution.

---

### 11. Calculate revenue generated by each staff member.

- **Tables Used**: `staff`, `payment`
- **SQL Skills**: JOIN, SUM(), GROUP BY
- **Business Use**: Sales team performance.
- **Insight**: Support bonus calculations or optimize staff scheduling.

---

### 12. Find the film with the highest replacement cost in each category.

- **Tables Used**: `film`, `category`, `film_category`
- **SQL Skills**: JOIN, MAX(), GROUP BY
- **Business Use**: Asset risk management.
- **Insight**: High replacement costs signal critical assets or costly licensing deals.

---

### 13. Determine the number of films in stock by category and store.

- **Tables Used**: `inventory`, `film_category`, `category`, `store`
- **SQL Skills**: Multiple JOINs, GROUP BY, COUNT()
- **Business Use**: Inventory optimization.
- **Insight**: Supports demand forecasting and restocking decisions.

---

### 14. Identify the most rented film in each store.

- **Tables Used**: `rental`, `inventory`, `film`, `store`
- **SQL Skills**: JOINs, GROUP BY, COUNT(), RANK or ROW_NUMBER (or subqueries)
- **Business Use**: Store-specific marketing.
- **Insight**: Tailor local campaigns based on top preferences.

---

### 15. List advisors and investors in a single unified list.

- **Tables Used**: `advisor`, `investor`
- **SQL Skills**: UNION
- **Business Use**: Stakeholder management.
- **Insight**: Useful for board reporting or outreach strategies.

---

### 16. Count of actors who have received awards.

- **Tables Used**: `actor`
- **SQL Skills**: CASE WHEN, COUNT()
- **Business Use**: Content valuation and brand perception.
- **Insight**: Helps assess the quality of content inventory based on celebrity appeal.

---

## Business Use Cases Summary

This project showcases how SQL enables:
- Strategic customer segmentation
- Revenue analytics & financial oversight
- Staff performance evaluation
- Content portfolio management
- Inventory control & logistics planning
- Stakeholder consolidation & transparency

These insights replicate how **BI teams** operate in media, retail, or e-commerce platforms — enabling **data-driven decisions** across multiple departments.

---

### 📝 Final Note

This README is designed not just to present 16 disconnected queries, but to narrate a **complete data story**. It simulates how a **BI Analyst would present findings to stakeholders** — focusing not just on what SQL did, but why it matters in a business context.

