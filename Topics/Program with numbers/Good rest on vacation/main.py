days = int(input())
food = int(input())
flight = int(input())
one_night = int(input())
nights = days - 1
print((nights * one_night) + (days * food) + (flight * 2))
