hh = int(input("Enter hours: "))
mm = int(input("Enter minutes: "))
ss = int(input("Enter seconds: "))

hh_ss = (hh * 3600)
mm_ss = (mm* 60)

total_seconds = (hh_ss + mm_ss + ss)

print(f'Total seconds: {total_seconds}')
