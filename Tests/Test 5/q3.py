# Program to sort Employee List Based on salary

def sort_salary(data):
    data.sort(key = lambda x : x[2])
    return data

Data = [
    [101, "Seema", 45000],
    [340, "Rajani", 13000],
    [210, "Suresh", 14000],
    [320, "Suresh", 35000]
]

sorted_data = sort_salary(Data)

print("Employee data sorted by salary: ")
for emp in sorted_data:
    print(emp)