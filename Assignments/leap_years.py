
leapcount = 0

start_year = int(input())

for year in range(start_year, 2025):
    if(year % 4 == 0):
      print ("This Is Leap Year", year)
      leapcount+=1
    else:
       print("its Not Leap Yeay", year)
print(f"Total Leap Years From {start_year} to 2024 is {leapcount}")