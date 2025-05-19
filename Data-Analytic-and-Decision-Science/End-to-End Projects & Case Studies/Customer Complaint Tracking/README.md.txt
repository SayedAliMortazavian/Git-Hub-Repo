# Customer Complaint Tracking Report — Bank of America
This project focuses on analyzing customer complaints by calculating key performance indicators (KPIs), visualizing weekly complaint trends, and delivering a polished, interactive report to support data-driven decision-making. 

## Financial Consumer Complaints
Consumer complaints on financial products & services for Bank of America from 2017 to 2023, including the dates the complaint was submitted to the CFPB and then sent to the company, the product and issue mentioned in the complaint, and the company's response.

## Recommended Analysis
### 1. Do consumer complaints show any seasonal patterns?
### 2. Which products present the most complaints? What are its most common issues?
### 3. How are complaints typically resolved?
### 4. Can you learn anything from the complaints with untimely responses?


## Objectives
### Objective 1: Calculate Top-Level KPIs
To begin, I classified complaints into Open and Closed statuses based on the company’s response. Complaints marked as “In progress” were flagged as Open, while all others were considered Closed. This categorization helps prioritize ongoing issues.

Next, I created a Week Start column aligning each complaint’s date to the corresponding Monday, enabling consistent weekly analysis. I also extracted the Year, Month, and Day of Week components from these dates to facilitate time-based breakdowns. To improve readability, months were formatted as text abbreviations (e.g., Jan, Feb).

### Objective 2: Visualize Weekly Trends
Building on the KPIs, I generated a PivotTable showing counts of Open and Closed complaints by week, including grand totals for a comprehensive overview.

For better presentation and user experience:
The KPIs were arranged in a single row with a clear label “Complaints:”
The report title “Consumer Complaints Tracking” was added and formatted for emphasis
An interactive timeline filter based on the Week Start date was inserted to allow dynamic filtering of data over time
To visualize trends effectively, I created a stacked column chart displaying the weekly distribution of complaints by status.

### Objective 3: Finalize and Polish the Report
The final step was enhancing the report’s usability and appearance. I:
Expanded the PivotTable to show complaint counts by Status across Year, Month, and Day, providing detailed temporal insights
Connected the stacked column chart to the timeline filter for seamless interactivity
Adjusted the chart to place the Open complaints column at the baseline for clearer trend comparison
Applied consistent color coding matching the KPIs to serve as the chart’s legend
Added formatting and alignment refinements to create a professional, polished dashboard ready for stakeholder review

## Summary:
This project demonstrates a practical approach to transforming raw complaint data into actionable insights through calculated KPIs, dynamic filtering, and clear visualizations — all essential elements for effective business intelligence in customer service management.

