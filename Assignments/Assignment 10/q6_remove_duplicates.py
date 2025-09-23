def remove_element(list, value):
    if value in list:
        list.remove(value)
        print(f"{value} removed successfully.")
    else:
        print("{value} not found in the list.")
    return list

list = [12,24,48,36,60,72]
print(list)

value = int(input("Enter value to remove from the list: "))
print(remove_element(list, value))


