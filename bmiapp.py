import datetime
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel


def save():
    time = datetime.now()
    bmiresult = str(bmi_)
    age2 = str(age)

    with open('records.txt','a') as file:
        file.write(str(time) + '\n' + 'Age = ' + age2 + '\n' + 'BMI = ' + bmiresult + '\n' + 'Range = ' + type + '\n' + '----------' + '\n')
        messagebox.showinfo('Confirmation','Results stored successfully')
        result.destroy()
        info.destroy()

def bmi():
    h = float(height_entry.get())
    height = float(h*h)
    weight = float(weight_entry.get())

    global bmi_, type, result    
    
    bmi_ = (weight/height)

    if bmi_ < 18.5:
        type = 'Underweight'
    if  (bmi_ > 18.5 and bmi_ <= 24.9):
        type = 'Healthy Weight'
    if (bmi_ > 25 and bmi_ <= 29.9):
        type = 'Overweight'
    if bmi_ > 30:
        type = 'Obese'

    result = Toplevel()
    result.geometry('250x120')
    result.minsize(250, 120)
    result.maxsize(250, 120)
    result.title('BMI Calculator')

    result_label = tk.Label(
        result,
        text='Your BMI',
        font=('Arial',20,'bold'),
        width=20
    )
    result_label.grid(
        row=1,
        column=1,
        columnspan=2,
        padx=2,
        pady=2
    )

    bmi_label = tk.Label(
        result,
        text='BMI =',
        font=('Arial',15)
    )
    bmi_label.grid(
        row=2,column=1
    )

    bmi_result = tk.Label(
        result,
        text=f'{bmi_:.2f}',
        font=('Arial',15)
    )
    bmi_result.grid(
        row=2,
        column=2
    )

    range_label = tk.Label(
        result,
        text='Range =',
        font=('Arial',15)
    )
    range_label.grid(
        row=3,
        column=1
    )
    
    range_result = tk.Label(
        result,
        text=type,
        font=('Arial',15)
    )
    range_result.grid(
        row=3,
        column=2
    )

    save_button = tk.Button(
        result,
        text='Save',
        command=save,
        width=20
    )
    save_button.grid(
        row=4,
        column=1,
        columnspan=2
    )


def infopage():
    global height_entry, weight_entry, info

    info = Toplevel()
    info.title('BMI Calculator')
    info.geometry('280x150')
    info.minsize(280, 150)

    info_label = tk.Label(
        info,
        text='Personal Information',
        font=('Arial',20,'bold'),
        width=20
    )
    info_label.grid(
        row=1,
        column=1,
        columnspan=2,
        padx=2,
        pady=2
    )

    height_label = tk.Label(
        info,
        text='Height (m)',
        font=('Arial',15)
    )
    height_label.grid(
        row=2,
        column=1
    )

    height_entry = tk.Entry(info)
    height_entry.grid(
        row=2,
        column=2
    )

    weight_label = tk.Label(
        info,
        text='Weight (kg)',
        font=('Arial',15)
    )
    weight_label.grid(
        row=3,
        column=1
    )

    weight_entry = tk.Entry(info)
    weight_entry.grid(
        row=3,
        column=2
    )

    submit_button = tk.Button(
        info,
        text='Submit',
        command=bmi,    
        width=20      
    )
    submit_button.grid(
        row=5,
        column=1,
        columnspan=2
    )

    exit_button = tk.Button(
        info,
        text='Back',
        command=info.destroy,
        width=20
    )
    exit_button.grid(
        row=6,
        column=1,
        columnspan=2
    )

    agecheck.destroy()

def ageverify():
    global age
    age = int(age_entry.get())

    if age >= 18:
        infopage()
    elif age < 18:
        messagebox.showinfo('info','Program is for people aged 18 and over')
        agecheck.destroy()
        root.destroy()

def aged():
    global age_entry, agecheck

    agecheck = Toplevel()
    agecheck.title('BMI Calculator')
    agecheck.geometry('230x100')
    agecheck.minsize(230, 60)
    agecheck.maxsize(230, 60)

    age_label = tk.Label(
        agecheck,
        text='Age',
        font=('Arial',15)
    )
    age_label.grid(
        row=1,
        column=1
    )

    age_entry = tk.Entry(
        agecheck,
    )
    age_entry.grid(
        row=1,
        column=2
    )

    submit_button = tk.Button(
        agecheck,
        text='Submit',
        command=ageverify,
        width=20
    )
    submit_button.grid(
        row=2,
        column=1,
        columnspan=2,
    )

root = tk.Tk()
root.title('BMI Calculator')
root.geometry('245x90')
root.minsize(245,90)
root.maxsize(245,90)

root_label = tk.Label(
    root,
    text = 'BMI Calculator',
    font = ('Arial',20),
    width = 20
)
root_label.grid(
    row=1,
    column=1,
    columnspan=2,
    padx=0,
    pady=0
)

measure_button = tk.Button(
    root,
    text='Measure BMI',
    command=aged,
    width=20
)
measure_button.grid(
    row=2,
    column=1,
    columnspan=2,
    padx=0,
    pady=0
)

exit_button = tk.Button(
    root,
    text='Exit',
    command=root.destroy,
    width=20
)
exit_button.grid(
    row=3,
    column=1,
    columnspan=2,
    padx=0,
    pady=0
)

root.mainloop()