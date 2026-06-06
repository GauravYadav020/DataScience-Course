# ============================================================
# M9 Lesson 3 – Level Up the Google Sheets (Drive link = "https://drive.google.com/drive/folders/1KNZiYJaS2SICGy6VkJpFqTnrMpg9m7Ii?usp=drive_link")
# ============================================================
# This lesson covers advanced features like VLOOKUP, conditional
# formatting, and named ranges to make Sheets more powerful.
# ============================================================


# ----------------------------
# Activity 1: Conditional Formatting
# ----------------------------
# Goal: Visually highlight data based on conditions automatically.
# Summary: Students will apply color rules to cells so that data
#          meeting certain criteria is automatically highlighted.

# Task:
# - Select your score column (B2:B10)
# - Go to Format > Conditional Formatting
# - Add rule: If value is less than 70 → Red background
# - Add rule: If value is greater than or equal to 90 → Green background
# - Observe how the sheet updates colors automatically


# ----------------------------
# Activity 2: VLOOKUP Function
# ----------------------------
# Goal: Search and retrieve data from a table using VLOOKUP.
# Summary: Students will use VLOOKUP to automatically find and
#          display information from a separate data table.

# Task:
# - Create a table in Sheet2 with: Student ID, Name, Grade
#   (IDs: 101, 102, 103 | Names: Alice, Bob, Charlie | Grades: A, B, A)
# - In Sheet1, type a Student ID in cell A1
# - In B1, write: =VLOOKUP(A1, Sheet2!A:C, 2, FALSE) to get the Name
# - In C1, write: =VLOOKUP(A1, Sheet2!A:C, 3, FALSE) to get the Grade
# - Test with different IDs


# ----------------------------
# Activity 3: Named Ranges
# ----------------------------
# Goal: Simplify formulas using named ranges for readability.
# Summary: Students will assign names to cell ranges so formulas
#          become easier to read and manage.

# Task:
# - Select your scores range B2:B10
# - Go to Data > Named Ranges
# - Name it "StudentScores"
# - Now rewrite your SUM formula as: =SUM(StudentScores)
# - Compare readability with the original =SUM(B2:B10)
# - Create one more named range called "StudentNames" for column A
