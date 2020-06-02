try:
    def line_color_by_individual_breaker_or_by_panel():
        x = input("""Looking for line phase color by individual breaker
or the line phase color of all breakers in the whole panel?
Enter only one of the two,
"p" for panel or "i" for individual \n""").lower()

        panel_voltage = int(input('What is the system voltage?\n'))

        if panel_voltage <= 240:
            color = [0, 'Phase A black', 'Phase B red  ', 'Phase C blue ']

        if panel_voltage > 240:
            color = [0, 'Phase A brown ', 'Phase B orage ', 'Phase C yellow']

        if x != 'p' and x != 'i':
                input('Only "p" or "i"\n')

        elif x == 'p':

            def panel_breakers_number_color(color, number):
                return color, number

            number = int(
                input('Enter the total number of breakers on the panel\n'))
            print('The colors for the line in phase on the breakers are;\n')
            if number == 0:
                print('No color posicion for breaker num ', number)



            for number in range(1, number + 1):

                if number == 0:
                    print('No color posicion for breaker num ', number)
                elif (number % 6 == 1):
                    print(color[1], 'for breaker num ', number, 'and', number+1)
                elif (number % 6 == 3):
                    print(color[2], 'for breaker num ', number,'and', number+1)
                elif (number % 6 == 0):
                    print(color[3], 'for breaker num ', number - 1, 'and', number)
                    
            panel_breakers_number_color(color, number)

        elif x == 'i':


            def individual_breaker_number_phase_color(color, number):
                return color, 'breaker #', number

            number = int(input('Enter the breaker number\n'))
            print('The color for the phase of the breaker is; ')

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
