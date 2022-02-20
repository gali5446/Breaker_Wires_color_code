""""Solo deside si es monofasico o trifasico para luego importar la correspondiente funcion"""
print('')
def line_breaker_color():
    phases = input(
        '''Looking for wires color by breaker number?
Is your system single-phase or three-phase?\n
For one-phase enter 1, for three-phase enter 3\n''')
    if phases  <='0':
        print('wrong number of faces')
    elif phases == '2':
        print('wrong number of faces')
    elif phases >= '4':
        print('wrong number of faces')
    elif phases == '1':
        import breakers_1_phases_color  # noqa F401
    else:
        phases == '3'
        import breakers_3_phases_color  # noqa F401
    #elif print('Wrong number of faces!'):
line_breaker_color()
print('')
print('End of the line_breaker_color Script')
