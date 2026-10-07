"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:the name of a retail brand and the numbers of stores to equip
# 2. Process:convert the number of stores into an integer and add 1 for the pilot store we test first
# 3. Out: a sentence summarising the deployment to plan
# 4. My two fields, and what I would do with them: at ADEIZ, we deploy our unified commerce platform in retail chains. 
# Before a rpoject i need the brand name and how many stores are concerned, to plan the deployment and the teams needed.

# Check it yourself:
# empty line: ValueError: invalid literal for int() with base 10: ''
# space: ValueError: invalid literal for int() with base 10: ' '
# text ("dix"): ValueError: invalid literal for int() with base 10: 'text'
# the program crashes because int() can only convert text that contains digits

# Your code below
brand = input("Enter the retail brand name: ")
stores = int(input("Number of stores to equip: "))
total = stores + 1  # Add 1 for the pilot store
print(f"ADEIZ deployment for {brand}: with {total} stores.")
