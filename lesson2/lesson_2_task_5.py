def month_to_season(month):
    if month in [12, 1, 2] :
        return 'Winter'
    elif month in [3,4,5]:
        return 'Spring'
    elif month in [6,7,8] :
        return 'Summer'
    elif month in [9,10,11]:
        return 'Аutumn'
    else:
        return ' укажите правильный месяц '
    
print (month_to_season (2)) 
print (month_to_season(4))   
print (month_to_season(12))
print (month_to_season(6))  