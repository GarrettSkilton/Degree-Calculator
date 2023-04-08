C_F = input('Type C or F for Celcius or Fahrenheit (will be converting FROM whichever you select): ')
C_F = C_F.lower()
if C_F == 'c':
    celc = input('Insert temperature in Celcius: ')  # Initial input

    try:  # To detect if the inputted character is a number
        celc = int(celc)
    except:
        print('INVALID INPUT. MUST RESTART NOW :(')
        quit()

    while celc == '':  # To detect if no characters are inputted
        farh = input('Insert temperature in Celcius: ')

    fahr = (celc * 1.8) + 32  # Actual calculation

    print(f'{celc} degrees Celius to Fahrenheit is: {fahr} degrees Fahrenheit')  # Printing results


elif C_F == 'f':
    farh = input('Insert temperature in Fahrenheit: ')

    try:
        farh = int(farh)
    except:
        print('INVALID INPUT. MUST RESTART NOW :(')
        quit()

    while farh == '':
        farh = input('Insert temperature in Fahrenheit: ')

    celc = (farh - 32) * 0.5556

    print(f'{farh} degrees Farenheit to Celcius is: {celc} degrees Celcius')


else:
    print('Invalid Input, RESTART...')
    quit()