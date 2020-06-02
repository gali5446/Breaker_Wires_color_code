def panel_breakers_number_color(color, number):
    return color, 'breaker # ', number


color = ''
number = 12  # int(input('Enter the total number of breakers on the panel '))
# print('The colors for the lines of the breakers are; ')
for number in range(1, number + 1):
    if number <= 0:
        print('No color for posicion that')
numbers = [*range(1, number + 1, 4)]
for number in numbers:
    if number % 2 == 1:
        number_impar_black = number
        return_black = f'Black for line on breaker num ',number_impar_black, 'and',number_impar_black + 1
    print(return_black)
    
    numbers_impar_red = [*range(3, number + 4, 4)]
    for number in numbers_impar_red:
        if number % 2 == 1:
            number_impar_red = number
            return_red = f'Red   for line on breaker num ',number_impar_red, 'and', number_impar_red+1
        
    print(return_red)

            

panel_breakers_number_color(color, number)
