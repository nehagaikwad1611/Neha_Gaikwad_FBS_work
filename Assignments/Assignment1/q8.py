days = int(input('Enter total number of days :'))

years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7

print(f'Number of years:{years}')
print(f'Number of weeks:{weeks}')
print(f'Number of days:{remaining_days}')