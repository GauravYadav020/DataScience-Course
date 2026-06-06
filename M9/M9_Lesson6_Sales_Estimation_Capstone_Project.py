# ============================================================
# M9 Lesson 6 – Sales Estimation Capstone Project
# ============================================================
# This capstone project combines all M9 skills: data entry,
# functions, validation, charts, and pivot tables into one
# complete real-world sales estimation spreadsheet.
# ============================================================


# ----------------------------
# Activity 1: Build the Sales Data Sheet
# ----------------------------
# Goal: Set up a structured and validated sales data entry sheet.
# Summary: Students will create a complete sales sheet with proper
#          headers, data validation, and auto-calculated fields.

# Task:
# - Create a sheet named "Sales Data" with columns:
#   Order ID | Date | Product | Category | Units Sold | Unit Price | Total Revenue
# - Add Data Validation:
#   → Units Sold: Number only, greater than 0
#   → Category: Dropdown (Electronics, Clothing, Food, Other)
# - In "Total Revenue" column, use formula: =Units Sold * Unit Price
# - Enter at least 15 rows of sample data across different categories


# ----------------------------
# Activity 2: Build the Summary Dashboard
# ----------------------------
# Goal: Create a summary sheet with key metrics and a visual chart.
# Summary: Students will use functions and a chart to build a simple
#          dashboard that shows total, average, and top sales insights.

# Task:
# - Create a new sheet named "Dashboard"
# - Use SUMIF to calculate total revenue per category
# - Use AVERAGEIF to find average revenue per category
# - Use LARGE function to find Top 3 revenue values
# - Insert a Bar Chart showing Revenue by Category
# - Add a title: "Sales Performance Dashboard – M9 Project"


# ----------------------------
# Activity 3: Add Pivot Table and Final Insights
# ----------------------------
# Goal: Use a Pivot Table to finalize analysis and present findings.
# Summary: Students will create a Pivot Table summarizing sales by
#          Product and Category, then write a short insight summary.

# Task:
# - Insert a Pivot Table from your "Sales Data" sheet on a new sheet
# - Set Rows = Product, Columns = Category, Values = SUM of Total Revenue
# - Apply Conditional Formatting: highlight revenue above average in green
# - In a text box or comment, write 3 business insights from your data:
#   Insight 1: Best performing category is ___
#   Insight 2: Lowest selling product is ___
#   Insight 3: Recommended action for next month is ___
# - This completed file is your M9 Capstone Submission!
