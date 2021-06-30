# Save the input in this variable
ticket = input()
a = int(ticket[0])
b = int(ticket[1])
c = int(ticket[2])
d = int(ticket[3])
e = int(ticket[4])
f = int(ticket[5])

# Add up the digits for each half
half1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
half2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
