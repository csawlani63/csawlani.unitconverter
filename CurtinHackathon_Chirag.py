'''
Author: Chirag Sawlani
Date: 11/6/2020

This is a Universal Unit Converter.
Converts between units of Mass, Length, Speed, Temperature, Currency and Date as mentioned in the case study.
The program has a user-friendly GUI Interface coupled with input/output boxes that updates the converted value automatically as the input is being typed.
Doesnt require the push of a 'convert' button.
GUI Interface was built using the built in tkinter module.

Each section of the program was implemented into a function or module as seen.
The program begins with the start() function being called and so starts up the program when the program function is called and the gui window is created.
When a number is entered or the unit is changed, the function conversiontype() is called to update the converted value depending on the change.
Then conversiontype calls a function depending on the type of conversion such as the function Mass() is called if the type of conversion is Mass.
This works with all types of conversions.
The program keeps running until the Exit button is clicked which when clicked, calls the built in function exit() and exits the program.
'''

import tkinter as tk 
from tkinter import ttk

#---------------START FUNCTION OF THE PROGRAM----------------##
def start():
    global x, y, z, background_color, options, conversion_type, window
    window = tk.Tk()
    conversion_type = 'Mass'
    if conversion_type=='Mass':
        background_color = '#C866CD'
        x = 2.205
        y = 14
        z = 6.35
        options = ('Kilograms','Pounds','Stone')
    program()
#--------------MAIN CALCULATION FUNCTIONS-------------------##
#--------------FUNCTION TO CHECK FOR LEAP YEAR--------------##
def leap_year():
    global month, days
    if month != 1 and combobox1.get() == 'Gregorian Calendar':
        days = days + 1
    if value[8:10] == '00':
        if int(value[6:10])%400 == 0:
            z = 29
        else:
            z = 28
    else:
        if int(value[6:10])% 4 == 0:
            if int(value[6:10]) % 100 != 0:
                z = 29
            else:
                z = 28
        else:
            z = 28
            
#--------------FUNCTION TO CALL OTHER FUNCTIONS FOR CALCULATION OF CONVERTED VALUE--------------##
def main_conversions(*args):
    global value, answer, entry_box1, entry_box2
    entry_box2['state'] = 'normal'
    entry_box2.delete(0,tk.END)   
    if entry_box1.get() == '':
        value = 0
    else:
        if conversion_type == 'Date':
            value = entry_box1.get()
        else:
            value = int(entry_box1.get())
    if conversion_type == 'Mass':
        Mass()
    elif conversion_type == 'Length':
        combobox2['state'] = 'disabled'
        Length()
    elif conversion_type == 'Speed':
        Speed()
    elif conversion_type == 'Temperature':
        Temperature()
    elif conversion_type == 'Currency':
        Currency()
    elif conversion_type == 'Date':
        Date()
    entry_box2.insert(0,answer)
    entry_box2['state'] = 'readonly'
    
#--------------FUNCTION TO DO MASS CONVERSIONS--------------##
def Mass():
    global answer
    if combobox1.get() == 'Kilograms' and combobox2.get() == 'Pounds':
        answer = (value * x)
    elif combobox1.get() == 'Pounds' and combobox2.get() == 'Kilograms':
        answer = (value / x)
    elif combobox1.get() == 'Stone' and combobox2.get() == 'Pounds':
        answer = (value * y)
    elif combobox1.get() == 'Pounds' and combobox2.get() == 'Stone':
        answer = (value / y)
    elif combobox1.get() == 'Stone' and combobox2.get() == 'Kilograms':
        answer = (value * z)
    elif combobox1.get() == 'Kilograms' and combobox2.get() == 'Stone':
        answer = (value / z)
    elif combobox1.get() == combobox2.get():
        answer = value
        
#--------------FUNCTION TO DO LENGTH CONVERSIONS--------------##
def Length():
    global answer
    if combobox1.get() == 'Inches':
        combobox2.current(1)
        answer = (value * x)
    elif combobox1.get() == 'Centimetres':
        combobox2.current(0)
        answer = (value / x)      # combobox2.current() is used to set the unit that the value entered should be converted to depending on the unit to convert from
    elif combobox1.get() == 'Yards':
        combobox2.current(3)
        answer = (value / y)      # this was done to meet the specific conversions between units of length as asked in the case study
    elif combobox1.get() == 'Metres':
        combobox2.current(2)
        answer = (value * y)      # and not conversions such as between inch and miles as they were not asked for nor specified in the case study
    elif combobox1.get() == 'Miles':
        combobox2.current(5)
        answer = (value * z)
    elif combobox1.get() == 'Kilometres':
        combobox2.current(4)
        answer = (value / z)
        
#--------------FUNCTION TO DO CONVERSIONS OF SPEED--------------##
def Speed():
    global answer
    if combobox1.get() == 'Miles per hour' and combobox2.get() == 'Kilometres per hour':
        answer = (value * x)
    elif combobox1.get() == 'Kilometres per hour' and combobox2.get() == 'Miles per hour':
        answer = (value / x)
    elif combobox1.get() == 'Knots' and combobox2.get() == 'Miles per hour':
        answer = (value * y)
    elif combobox1.get() == 'Miles per hour' and combobox2.get() == 'Knots':
        answer = (value / y)
    elif combobox1.get() == 'Knots' and combobox2.get() == 'Kilometres per hour':
        answer = (value * z)
    elif combobox1.get() == 'Kilometres per hour' and combobox2.get() == 'Knots':
        answer = (value / z)
    elif combobox1.get() == combobox2.get():
        answer = value
        
#--------------FUNCTION TO DO CONVERSION OF TEMPERATURE--------------##
def Temperature():
    global answer
    if combobox1.get() == 'Fahrenheit' and combobox2.get() == 'Celsius':
        answer = ((value - x) * y)
    elif combobox1.get() == 'Celsius' and combobox2.get() == 'Fahrenheit':
        answer = ((value + x) / y)
    elif combobox1.get() == 'Kelvin' and combobox2.get() == 'Fahrenheit':
        answer = (((value - z) / y) + x)
    elif combobox1.get() == 'Fahrenheit' and combobox2.get() == 'Kelvin':
        answer = (((value - x) * y) + z)
    elif combobox1.get() == 'Kelvin' and combobox2.get() == 'Celsius':
        answer = (value - z)
    elif combobox1.get() == 'Celsius' and combobox2.get() == 'Kelvin':
        answer = (value + z)
    elif combobox1.get() == combobox2.get():
        answer = value
        
#--------------FUNCTION TO DO CONVERSION OF CURRENCY--------------##
def Currency():
    global answer
    if combobox1.get() == 'AED' and combobox2.get() == 'USD':
        answer = (value * x)
    elif combobox1.get() == 'USD' and combobox2.get() == 'AED':
        answer = (value / x)
    elif combobox1.get() == 'GBP' and combobox2.get() == 'USD':
        answer = (value * y)
    elif combobox1.get() == 'USD' and combobox2.get() == 'GBP':
        answer = (value / y)
    elif combobox1.get() == 'AED' and combobox2.get() == 'GBP':
        answer = (value * z)
    elif combobox1.get() == 'GBP' and combobox2.get() == 'AED':
        answer = (value / z)
    elif combobox1.get() == combobox2.get():
        answer = value
        
#--------------FUNCTION TO CONVERT GREGORIAN CALENDAR TO JULIAN AND VICE VERSA--------------##
def Date():
    global answer, value, month, days, year
    value = str(value)
    if combobox1.get() == 'Gregorian Calendar' and combobox2.get() == 'Julian Calendar':
        if len(value) == 10:
            month = int(value[3] + value[4])
            day1 = int(value[0] + value[1])
            if month in months_31 and day1 > x or months_30 and day1 > y:
                answer = 0
            else:
                year = int(value[6:10])
                century = int(value[6] + value[7])
                days = (century - 2 - (century / 4))
                days = int(value[0] + value[1]) - days
                leap_year()
                #--------------CODE TO MAKE CHANGES IF DAYS IS GREATER THAN 31 OR 30---------##
                if month in months_31 and days < 1:
                    days = days + x
                    month = month - 1
                    year = value[6:10]
                elif month in months_30 and days < 1:
                    days = days + y
                    month = month - 1
                    year = value[6:10]
                elif month in [2] and days < 1:
                    days = days + z
                    month = month - 1
                    year = value[6:10]
                if int(month) < 1:
                    year = int(value[6:10])
                    year = year-1
                    month = 12
                answer = str(int(days)) + '/' + str(month) + '/' + str(year)
        else:
            answer = 0
            
    elif combobox1.get() == 'Julian Calendar' and combobox2.get() == 'Gregorian Calendar':
        if len(value) == 10:
            month = int(value[3] + value[4])
            day1 = int(value[0] + value[1])
            if month in months_31 and day1 > x or months_30 and day1 > y:
                answer = 0
            else:
                year = int(value[6:10])
                century = int(value[6] + value[7])
                days = (century - 2 - (century / 4))
                days = int(value[0] + value[1]) + days
                leap_year()
                #--------------CODE TO MAKE CHANGES IF DAYS IS GREATER THAN 31 OR 30---------##
                if month in months_31 and days > x:
                    days = days - x
                    month = month + 1
                elif month in months_30 and days > y:
                    days = days - y
                    month = month + 1
                elif month in [2] and days > z:
                    days = days - z
                    month = month + 1
                answer = str(int(days)) + '/' + str(month) + '/' + str(value[6:10])
        else:
            answer = 0
    elif combobox1.get() == combobox2.get():
        answer = value
    
#---------------FUNCTION TO SET VALUES FOR CONSTANTS DEPENDING ON CONVERSION TYPE CHOSEN------------##
def conversiontype(*args):
    global x, y, z, background_color, options, conversion_type, conversions
    conversion_type = conversions.get()
    if conversion_type=='Mass':
        background_color = '#C866CD'
        x = 2.205
        y = 14
        z = 6.35
        options = ('Kilograms','Pounds','Stone')
    if conversion_type=='Length':
        background_color = '#50BCB9'
        x = 2.54
        y = 1.094
        z = 1.609
        options = ('Inches','Centimetres','Yards','Metres','Miles','Kilometres')
    if conversion_type=='Speed':
        background_color = '#50BC55'
        x = 1.609
        y = 1.151
        z = 1.852
        options = ('Miles per hour','Kilometres per hour','Knots')
    if conversion_type=='Temperature':
        background_color = '#9D0CF5'
        x = 32
        y = (5/9)
        z = 273.15
        options = ('Fahrenheit','Celsius','Kelvin')
    if conversion_type=='Currency':
        background_color = '#ff605e'
        x = 0.27
        y = 1.27
        z = 0.21
        options = ('AED','USD','GBP')
    if conversion_type=='Date':
        background_color = '#F5AB0C'
        x = 31
        y = 30
        z = 29
        options = ('Gregorian Calendar','Julian Calendar')
    program()

#-----------------MAIN PROGRAM FUNCTION FOR THE GUI------------------------##
def program():
    global x, y, z, background_color, options, conversion_type, window, conversions
    global answer, combobox1, combobox2, entry_box1, entry_box2, months_31, months_30
    window.destroy()
    window=tk.Tk() # creates the window
    window.geometry('550x400')
    window.resizable(False, False)
    window.title('Universal Unit Converter')
    #--------------LAYOUT AND DESIGN OF THE WINDOW-------------------------##
    frame1 = tk.Frame(window, width = 550, height = 200, bg = background_color) # splitting the window into two halves
    frame2 = tk.Frame(window, width = 550, height = 200, bg = '#F3EFF3')
    
    title = tk.Label(window, text = 'Universal Unit', width = 12, font = 'Verdana 11 bold', bg = background_color)
    title.place(x=5,y=5)
    title2 = tk.Label(window, text = 'Converter :)', width = 12, font = 'Verdana 11 bold', bg = background_color)
    title2.place(x=5,y=25)

    content1 = tk.StringVar()
    content2 = tk.StringVar()
    content3 = tk.StringVar()
    content4 = tk.StringVar()
    months_31 = [1,3,5,7,8,10,12]
    months_30 = [4,6,9,11]
    dropdown=('Mass','Length','Speed','Temperature','Currency','Date')

    if conversion_type == 'Date':
        formatting = tk.Label(master = frame1, text = 'DD/MM/YYYY Format', bg = background_color, relief = 'flat', fg = 'black', font = 'Verdana 11')
        formatting.place(x=330, y=130)
        formatting2 = tk.Label(master = frame2, text = 'DD/MM/YYYY Format', bg = '#F3EFF3', relief = 'flat', fg = 'black', font = 'Verdana 11')
        formatting2.place(x=330, y=80)
        
    entry_box1 = tk.Entry(master = frame1, textvariable = content1, font = 'Helvetica 18 bold', bg = background_color, fg = '#F3EFF3', relief = 'flat', justify = 'center')
    entry_box1.place(x=25, y=100)  # creates input box for values 
    entry_box1.insert(0,0)
    entry1_label = tk.Label(master = frame1, text = '‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾', relief = 'flat', bg = background_color, fg = '#F3EFF3').place(x=91, y=130)
    content1.trace('w',main_conversions)

    entry_box2 = tk.Entry(master = frame2, state = 'readonly', font = 'Helvetica 18 bold', readonlybackground = '#F3EFF3', bg = '#F3EFF3', fg = background_color, relief = 'flat', justify = 'center')
    entry_box2.place(x=25, y=50) # creates output box for the converted value
    entry2_label = tk.Label(master = frame2, text = '‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾', relief = 'flat', bg = '#F3EFF3', fg = background_color).place(x=91, y=80)

    conversions = ttk.Combobox(master = frame1, state='readonly', width = 15, height = 15, values = dropdown, textvariable = content2, font = 'Verdana 10')
    for choice in dropdown:
        if choice == conversion_type:         
            default = dropdown.index(choice) # creates a dropdown list for type of conversion
    conversions.current(default)
    conversions.place(x=200,y=10)
    content2.trace('w',conversiontype)
    
    combostyle = ttk.Style()
    combostyle.theme_create('combostyle', parent = 'alt', settings = {'TCombobox':{'configure':{'foreground':'black', 'relief':'flat', 'fieldbackground':'white', 'background':'white'}}})
    combostyle.theme_use('combostyle') # creates design to use for dropdown list
    
    combobox1 = ttk.Combobox(master=frame1, state='readonly', width = 17, height = 25, values = options, textvariable = content3, font = 'Verdana 14')
    combobox1.current(0)
    content3.trace('w',main_conversions)    # creates a dropdown list for unit to convert from
    combobox1.place(x=300, y=105)

    combobox2 = ttk.Combobox(master=frame2, state='readonly', width = 17, height = 25, values = options, textvariable = content4, font = 'Verdana 14')
    combobox2.current(1)
    content4.trace('w',main_conversions)    # creates a dropdown list for unit to convert to
    combobox2.place(x=300, y=55)

    Exit = tk.Button(master=frame2, text='Exit', command=exit, bg='#F3EFF3', fg='black', width = 15, relief = 'raised')
    Exit.place(x=360, y=140)    # creates exit button

    frame1.pack(fill = tk.BOTH, expand = True)
    frame2.pack(fill = tk.BOTH, expand = True)

    window.mainloop()

start()
