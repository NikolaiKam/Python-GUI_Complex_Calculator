import PySimpleGUI as sg
import cmath

def calculator(num1,action,num2):
    act={
        '+':num1+num2, '-':num1-num2, '*':num1*num2, '/':num1/num2, '**':num1**num2
    }
    return act[action]

sg.theme('Python')
layout=[
    [
        sg.InputText(key='-N1-',size=(8,2)),
        sg.Combo(('+','-','*','/','**'),key='-ACT-',size=(4,5)),
        sg.InputText(key='-N2-', size=(8,2)),
        sg.Text('=')
    ],

    [
        sg.Text('Output:'),
        sg.Text('0',key='-OUT-'),
        sg.Submit('Calculate')
    ]
]

window=sg.Window('Calculator', layout)

while True:
    try:
        event, values = window.read()
        if event==sg.WIN_CLOSED:
            break
        if event=='Calculate':
            if str(values['-N1-']).find('j')==-1 and str(values['-N2-']).find('j')==-1:
                
                if values['-N2-']=='0':
                    result='Cannot divide by zero'
                    window['-OUT-'].update(result)

                else:

                    result=calculator(
                    float(values['-N1-']), values['-ACT-'], float(values['-N2-'])
                    )

                    if  result==(result*10)//10 and values['-N1-']!='' and values['-N2-']!='' and values['-ACT-']!='':
                        window['-OUT-'].update(int(result))
                    else:
                        window['-OUT-'].update(result) 
            else:
                
                result=calculator(
                complex(values['-N1-']), values['-ACT-'], complex(values['-N2-'])
                )
                window['-OUT-'].update(result)
    except ValueError:
        window['-OUT-'].update('Enter a valid numbers!!!')
    except ZeroDivisionError:
        window['-OUT-'].update('Can`t divide by zero!!!')
    except KeyError:
        window['-OUT-'].update('Enter a valid action!!!')
    except:
        window['-OUT-'].update('Error!!!')
window.close()
    
