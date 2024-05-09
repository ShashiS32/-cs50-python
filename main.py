
#remobes any space between the name and treats the name like a title

name = input("What is your name? ").title().strip()


#split users name into first and last anme

first , last  = name.split()



print(f"Hi {first }")

