# Minimum number of notes

def min_notes(amount):
    D = [2000,1000, 500, 200, 100, 50, 20, 10, 5]
    notes_count = {}

    for note in D:
        if amount >= note:
            count = amount // note
            notes_count[note] = count
            amount %= note

    print("Minimun number of notes needed: ")
    for note,count in notes_count.items():
        print(f"{note}: {count}")

amount = int(input("Enter the amount: "))
min_notes(amount)