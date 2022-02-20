print('')
try:
    def line_color_by_individual_breaker_or_by_panel():
        x = input("""Looking for wire color by individual breaker,
or the wires color of all breakers in the whole panel?;\n
Enter only one of the two,
"p" for panel or "i" for individual breker; \n""").lower()

        panel_voltage = int(input('What is the system voltage?\n'))

        if panel_voltage <= 240:
            color = [0, 'Black Phase A ', 'Red Phase B  ', 'Blue Phase C ']

        if panel_voltage > 240:
            color = [0, 'Brown Phase A ', 'Oregen Phase B ', 'Yellow Phase C ']

        if x != 'p' and x != 'i':
                input('Only "p" or "i"\n')

        elif x == 'p':

            def panel_breakers_number_color(color, number):
                return color, number

            number = int(
                input('Enter the total number of breakers on the panel\n'))
            print('The wire colors by phase on the breakers are;\n')
            if number == 0:
                print('No color posicion for breaker num ', number)
            for number in range(1, number + 1):
                if number == 0:
                    print('No color posicion for breaker num ', number)
                elif (number % 6 == 1):
                    print(color[1], 'for breakers num ', number, 'and', number+1)
                elif (number % 6 == 3):
                    print(color[2], 'for breakers num ', number,'and', number+1)
                elif (number % 6 == 0):
                    print(color[3], 'for breakers num ', number - 1, 'and', number)
            panel_breakers_number_color(color, number)

        elif x == 'i':

            def individual_breaker_number_phase_color(color, number):
                return color, 'breaker #', number

            number = int(input('Enter the breaker number\n'))
            print('The wire color of the breake must be ; ')

            if number == 0:
                print('No color posicion for ', 'for breaker num ', number)
            elif (number % 6 == 1) or (number % 6 == 2):
                print(color[1], 'for breaker num ', number)

            elif (number % 6 == 3) or (number % 6 == 4):
                print(color[2], 'for breaker num ', number)

            elif (number % 6 == 0) or ((number % 6 == 5)):
                print(color[3], 'for breaker num ', number)

            individual_breaker_number_phase_color(color, number)

    line_color_by_individual_breaker_or_by_panel()
except ValueError:
    print('Only integers number')
except NameError:
    print('Only integers number')
print('')
print('End of the breakers_3_phases_color Script')
