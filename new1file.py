# modules
from tkinter import *
import calsal

# tkinter object 
ws = Tk()
ws.title('PythonGuides - PaySlip Generator')
ws.geometry('400x300')

f = 'sans-serif, 12'

# functions
def clearbtn():
    emp_name.delete(0, 'end')
    rph.delete(0, 'end')
    duty.delete(0, 'end')
    s3_contrib.delete(0, 'end')
    phealth.delete(0, 'end')
    hloan.delete(0, 'end')


def main():
    ename = emp_name.get()
    r = rph.get()
    d = duty.get()
    contri = s3_contrib.get()
    ph = phealth.get()
    hl = hloan.get()

    r = float(r)
    d = float(d) 
    contri = float(contri)
    ph = float(ph)
    hl = float(hl)

    gross_sal = r * d
    tax = gross_sal * 0.1
    total_deduction = contri + ph + hl + tax
    net_sal = gross_sal - total_deduction
    # calling function
    calsal.payslip(ename, d, r, gross_sal, contri, ph, hl, tax, total_deduction, net_sal, ws, f)
    
Label(
    ws,
    text="EMPLOYEE PAYSLIP",
    font=('sans-serif, 14'),
    relief=SOLID,
    padx=10,
    pady=5
).pack()

# frame widget
mainframe = Frame(ws, padx=5, pady=5)
mainframe.pack(expand=True)

# label widget
Label(
    mainframe,
    text='Employee Name',
    font=f
    ).grid(row=2, column=0, sticky='e')

Label(
    mainframe,
    text='Rate per hour',
    font=f
    ).grid(row=3, column=0, sticky='e')

Label(
    mainframe,
    text='Duty (No. of hours)',
    font=f
    ).grid(row=4, column=0, sticky='e')

Label(
    mainframe,
    text='SSS Contribution',
    font=f
    ).grid(row=5, column=0, sticky='e')

Label(
    mainframe,
    text='PhilHealth',
    font=f
    ).grid(row=6, column=0, sticky='e')

Label(
    mainframe,
    text='House loan',
    font=f
    ).grid(row=7, column=0, sticky='e')


# Entry widgets
emp_name = Entry(mainframe, font=f)
rph = Entry(mainframe, font=f)
duty = Entry(mainframe, font=f)
s3_contrib = Entry(mainframe, font=f)
phealth = Entry(mainframe, font=f)
hloan = Entry(mainframe, font=f)

# geometry method - Grid
emp_name.grid(row=2, column=1, padx=5)
rph.grid(row=3, column=1, padx=5, sticky='w')
duty.grid(row=4, column=1, padx=5, sticky='w')
s3_contrib.grid(row=5, column=1, padx=5, sticky='w')
phealth.grid(row=6, column=1, padx=5, sticky='w')
hloan.grid(row=7, column=1, padx=5, sticky='w')

# default values in the entry widget
emp_name.insert('0', 'Noel B. Atazar')
rph.insert('0', 150)
duty.insert('0', 9)
s3_contrib.insert('0', 200)
phealth.insert('0', 150)
hloan.insert('0', 100)

# frame for buttons
frame = Frame(mainframe)
frame.grid(row=8, columnspan=3, pady=(30, 0))

# button widget
Button(
    frame,
    text='Calculate',
    width=10,
    command=main,
    font=f,
    bg='#91BF2C'
).pack(side=LEFT, expand=True, padx=(0, 5))

Button(
    frame,
    text='Clear',
    width=5,
    font=f,
    bg='#E6D92A',
    command=clearbtn
).pack(side=LEFT, expand=True, padx=(0, 5))

Button(
    frame,
    text='Exit',
    width=5, 
    font=f,
    bg='#FF614F',
    command=lambda:ws.destroy()
).pack(side=LEFT, expand=True, padx=(0, 5))

# infinite loop
ws.mainloop()
