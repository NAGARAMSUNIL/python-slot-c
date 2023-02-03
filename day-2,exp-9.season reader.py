month=input("input the month:")
day=int(input("input the day"))

if month in ('january'or'jan','february'or'feb','march'or'mar'):
    season='winter'
elif month in ('april'or'apr','may','june'or'jun'):
    season='spring'
elif month in ('july'or'jul','august'or'aug','september'or'sep'):
    season='summer'
else:
    season='autumn'

if (month=='march'or'mar')and (day>19):
    season='spring'
elif (month=='june'or'jun')and (day>20):
    season='summer'
elif (month=='september'or'sep')and(day>21):
    season='autumn'
elif (month=='december'or'dec')and(day>20):
    season='winter'

print("season is",season)
