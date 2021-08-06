x = int(input("Enter the seconds :"))
seconds = x % 60
minutes = x // 60

hours = minutes // 60
minutes = minutes % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")
