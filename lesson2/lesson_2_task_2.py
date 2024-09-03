def is_year_leap(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return print('Год ' + str(n) + ': True')
    else:
        return print('Год ' + str(n) + ': False')
    
year_to_check = int (input("Введи год для проверки: ")) 

is_year_leap(year_to_check)