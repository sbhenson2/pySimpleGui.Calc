import PySimpleGUI as sg
import math

total = '0'
firstNumber = '0'
operation = ''
trig_mode = False
sg.theme('DarkGreen')

# All the stuff inside your window.
layout = [
    [sg.Text('0', font=('Arial 20'), size=(18, 1), justification='r', key='-NUMBERS-')],
    [sg.Button('%', size=(8, 4)), sg.Button('CE', size=(8, 4)), sg.Button('C', size=(8, 4)), sg.Button('Back', size=(8, 4))],
    [sg.Button('2nd', size=(8, 4), button_color=('white', 'blue'))] +
    [sg.Button('sin(x)', key='-SIN-', size=(8, 4)), sg.Button('cos(x)', size=(8, 4)), sg.Button('tan(x)', size=(8, 4))],
    [sg.Button('1/x', size=(8, 4)), sg.Button('x^2', size=(8, 4)), sg.Button('sqrt(x)', size=(8, 4)), sg.Button('/', size=(8, 4))],
    [sg.Button('7', size=(8, 4)), sg.Button('8', size=(8, 4)), sg.Button('9', size=(8, 4)), sg.Button('*', size=(8, 4))],
    [sg.Button('4', size=(8, 4)), sg.Button('5', size=(8, 4)), sg.Button('6', size=(8, 4)), sg.Button('-', size=(8, 4))],
    [sg.Button('1', size=(8, 4)), sg.Button('2', size=(8, 4)), sg.Button('3', size=(8, 4)), sg.Button('+', size=(8, 4))],
    [sg.Button('+/-', size=(8, 4)), sg.Button('0', size=(8, 4)), sg.Button('.', size=(8, 4)), sg.Button('=', size=(8, 4))]
]

# Create the Window
window = sg.Window('My Calculator', layout, element_padding=(1, 1))

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:    # if user closes window or clicks cancel
        break
    elif event in '0123456789':
        if total == '0' or total == '' or operation == '=':
            total = event
        else:
            total += event
        window['-NUMBERS-'].update(total)
    elif event == 'Back':
        if len(total) <= 1:
            total = '0'
        else:
            total = total[:-1]
        window['-NUMBERS-'].update(total)
    elif event == 'C':
        total = '0'
    elif event == '%':
        total = str(float(total) / 100)
    elif event == '1/x':
        total = str(1 / float(total))
    elif event == 'x^2':
        total = str(float(total) ** 2)
    elif event == 'sqrt(x)':
        total = str(math.sqrt(float(total)))
    elif event in ['sin(x)', 'cos(x)', 'tan(x)']:
        if trig_mode:
            event = 'arc' + event
        total = str(eval('math.' + event.replace('(x)', '(' + total + ')')))
    elif event in ['arcsin(x)', 'arccos(x)', 'arctan(x)']:
        total = str(eval('math.' + event.replace('(x)', '(' + total + ')')))
    elif event == '2nd':
        trig_mode = not trig_mode
        new_texts = {
            'sin(x)': 'arcsin(x)' if trig_mode else 'sin(x)',
            'cos(x)': 'arccos(x)' if trig_mode else 'cos(x)',
            'tan(x)': 'arctan(x)' if trig_mode else 'tan(x)'
        }
        window['2nd'].update(button_color=('white', 'blue') if trig_mode else ('white', 'green'))
        for key, value in new_texts.items():
            window[key].update(value)

    elif event in '+-/*':
        operation = event
        firstNumber = total
        total = '0'
    elif event == '=':
        if operation == '*':
            total = str(float(firstNumber) * float(total))
        operation = '='
    total = total[:8]
    window['-NUMBERS-'].update(total)

window.close()