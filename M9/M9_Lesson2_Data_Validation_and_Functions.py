# ============================================================
# M9 Lesson 2 – Data Validation and Functions (Drive link = "https://drive.google.com/drive/folders/1KNZiYJaS2SICGy6VkJpFqTnrMpg9m7Ii?usp=drive_link")
# ============================================================
# Data Validation controls what users can enter in a cell.
# Functions are built-in formulas that perform calculations automatically.
# ============================================================


# ----------------------------
# Activity 1: Apply Data Validation
# ----------------------------
# Goal: Restrict cell input using Data Validation rules.
# Summary: Students will set rules so that only specific values
#          or data types can be entered in selected cells.

# Task:
# - Select cells B2:B10
# - Go to Data > Data Validation
# - Set criteria: "Number" between 1 and 100
# - Try entering a number outside this range and observe the warning
# - Also try creating a Dropdown list in Column C (e.g., Pass, Fail)


# ----------------------------
# Activity 2: Use Basic Functions
# ----------------------------
# Goal: Learn and apply common Google Sheets functions.
# Summary: Students will practice using SUM, AVERAGE, MAX, and MIN
#          functions on a sample dataset.

# Task:
# - Enter the following scores in B2:B6 → 70, 85, 90, 60, 75
# - In B7, use =SUM(B2:B6) to get total
# - In B8, use =AVERAGE(B2:B6) to get average
# - In B9, use =MAX(B2:B6) to find highest score
# - In B10, use =MIN(B2:B6) to find lowest score


# ----------------------------
# Activity 3: Use IF Function
# ----------------------------
# Goal: Apply conditional logic using the IF function.
# Summary: Students will use the IF function to automatically
#          label results as "Pass" or "Fail" based on a score condition.

# Task:
# - In Column C (next to scores), write an IF formula:
#   =IF(B2>=70, "Pass", "Fail")
# - Drag the formula down for all rows
# - Change a score below 70 and verify the result updates automatically
# - Try nested IF: =IF(B2>=90,"A", IF(B2>=70,"B","C"))
