# Python Snippet for Bill Calculator
bill_amount = int(input('Please enter the total bill amount: '))
number_in_party = int(input('Please enter the number in your party: '))
desired_tip_percentage = round(float(input('Please enter the desired tip percentage (for example, "20" for 20%): ')), 2)

tip = int(bill_amount * desired_tip_percentage / 100)
total = bill_amount + tip
total_each = total / number_in_party

print('A ' + str(desired_tip_percentage) + '% tip ' + '($' + str(tip) + ') was added to the bill, for a total of $' + str(total))
print('With ' + str(number_in_party) + ' in your party, each person must pay $' + str(total_each))