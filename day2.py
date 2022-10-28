#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Assignment 2
# Greeting
print("Welcome to the tip calculator.")

# Variable 1
bill_total = input("What was the total bill? $")
# Convert to float
bill_total_float = float(bill_total)

# Variable 2
desired_tip = input("What percentage tip would you like to give? ")
# Convert to int + change input to 1.xx format for ease of calculating tip (12% = 1.12)
desired_tip_integer = (float(desired_tip) * 0.01) + 1

# Variable 3
guest_count = input("How many people to split the bill? ")
# Convert to int
guest_count_integer = int(guest_count)

# Final bill calculation
final_bill = ((bill_total_float * desired_tip_integer) / guest_count_integer)

# Print statement
print(f'Each person should pay: ${final_bill:.2f}')
