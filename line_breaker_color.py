
def line_breaker_color():
    phases = input(
'''Looking for line breaker color.
Is your system single-phase or three-phase?
For one-phase enter 1, for three-phase enter 3\n''')
    if phases == '1':
        import breakers_1_phases_color
    if phases == '3':
        import breakers_3_phases_color
line_breaker_color()    
