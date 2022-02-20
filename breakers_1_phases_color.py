print('')

try:

    def color_by_individual_or_by_panel():

        x = input("""Looking for wire color by individual breaker,
or the wires colors of all breakers in the whole panel?;\n
Enter "p" for panel or "i" for individual breake \n""").lower()

        color = [0, 'Black color for wire', 'Red color for wire']

        if x != 'p' and x != 'i':
            x = input('Only "p" or "i" \n')

        if x == 'p':  # p = panel
            def panel_breakers_number_color(color, number):
                return color, 'breaker # ', number
            number = int(
                input('Enter the total number of breakers on the panel \n'))
            # print('The colors for the lines of the breakers are; ')
            if number <= 0:
                print('No color for posicion "0" or lest')
            else:
                numbers = [*range(1, number + 1, 4)]
                print('The colors for the wires on the breakers are; \n')
                for number in numbers:
                    if number % 2 == 1:
                        number_impar_black = number

                        print(color[1], 'on breakers num ', number_impar_black, ' and ', number_impar_black + 1) #

                    numbers_impar_red = [*range(3, number + 4, 4)]
                    for number in numbers_impar_red:
                        if number % 2 == 1:
                            number_impar_red = number
                    print(color[2], 'on breakers num ',
                        number_impar_red, ' and ', number_impar_red+1)

            panel_breakers_number_color(color, number)

        elif x == 'i':  # i = individual
            def individual_breaker_number_phase_color(color, number):
                return color, 'breaker #', number
            number = int(input('Enter breaker number '))
            b = 'The wire color is black for breaker # '
            r = 'The wire color is red for breaker # '

            if number <= 0:
                print(
                    'No color for posicion "0" or lest')
            elif number % 2 == 1:
                number_impar_black = number
                if number in [*range(1, number + 1, 4)]:
                    print(b, number_impar_black)
                else:
                    print(r, number)
            elif number % 2 == 0:
                number_par_black = number
                if number in [*range(2, number + 1, 4)]:
                    print(b, number_par_black)
                else:
                    print(r, number_par_black)

            individual_breaker_number_phase_color(color, number)

    color_by_individual_or_by_panel()


except ValueError:
    print('Only integers number')
except NameError:
    print('Only integers number')
print('')
print('End of the breakers_1_phases_color Script')
