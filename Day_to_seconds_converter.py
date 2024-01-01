print('This program is used to calculate the number of seconds in days.'
      '\nHow to use this program: '
      'input the number of days and the program will generate the number of seconds in it.')


def convert_day_to_seconds(day):
    hours = day * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds


while True:
    print('Input the number of days:')
    total_seconds = convert_day_to_seconds(int(input()))
    print('the total number of seconds is: ', total_seconds)
    response = input('would you like to try another day? reply with y or n: ')
    if response == 'n':
        print('thanks for using this program')
        break
