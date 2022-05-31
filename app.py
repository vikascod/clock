from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    pm = time.strftime('%p')
    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')

    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_pm.config(text=pm)

    lab_date.config(text=date)
    lab_mon.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)


    lab_hr.after(200, date_time)

clock = Tk()
clock.title('Digital Clock')
clock.geometry('1000x500')
clock.config(bg='blue')

lab_hr = Label(clock, text='00', font=('Time New Roman', 60, 'bold'), bg='red', foreground='black')
lab_hr.place(x=120, y=40, height=100, width=100)
lab_hr_txt = Label(clock, text='Hour', font=('Time New Roman', 30, 'bold'), bg='red', foreground='black')
lab_hr_txt.place(x=120, y=180, height=40, width=100)

lab_min = Label(clock, text='00', font=('Time New Roman', 60, 'bold'), bg='red', foreground='black')
lab_min.place(x=340, y=40, height=100, width=100)
lab_min_txt = Label(clock, text='Min', font=('Time New Roman', 30, 'bold'), bg='red', foreground='black')
lab_min_txt.place(x=340, y=180, height=40, width=100)

lab_sec = Label(clock, text='00', font=('Time New Roman', 60, 'bold'), bg='red', foreground='black')
lab_sec.place(x=560, y=40, height=100, width=100)
lab_sec_txt = Label(clock, text='Sec', font=('Time New Roman', 30, 'bold'), bg='red', foreground='black')
lab_sec_txt.place(x=560, y=180, height=40, width=100)

lab_pm = Label(clock, text='00', font=('Time New Roman', 50, 'bold'), bg='red', foreground='black')
lab_pm.place(x=780, y=40, height=100, width=100)
lab_pm_txt = Label(clock, text='PM/AM', font=('Time New Roman', 20, 'bold'), bg='red', foreground='black')
lab_pm_txt.place(x=780, y=180, height=40, width=100)



lab_date = Label(clock, text='00', font=('Time New Roman', 60, 'bold'), bg='red', foreground='black')
lab_date.place(x=120, y=270, height=100, width=100)
lab_date_txt = Label(clock, text='Date', font=('Time New Roman', 20, 'bold'), bg='red', foreground='black')
lab_date_txt.place(x=120, y=400, height=40, width=100)

lab_mon = Label(clock, text='00', font=('Time New Roman', 60, 'bold'), bg='red', foreground='black')
lab_mon.place(x=340, y=270, height=100, width=100)
lab_mon_txt = Label(clock, text='Month', font=('Time New Roman', 20, 'bold'), bg='red', foreground='black')
lab_mon_txt.place(x=340, y=400, height=40, width=100)

lab_year = Label(clock, text='00', font=('Time New Roman', 60, 'bold'), bg='red', foreground='black')
lab_year.place(x=560, y=270, height=100, width=100)
lab_year_txt = Label(clock, text='Year', font=('Time New Roman', 20, 'bold'), bg='red', foreground='black')
lab_year_txt.place(x=560, y=400, height=40, width=100)

lab_day = Label(clock, text='00', font=('Time New Roman', 50, 'bold'), bg='red', foreground='black')
lab_day.place(x=780, y=270, height=100, width=100)
lab_day_txt = Label(clock, text='Day', font=('Time New Roman', 20, 'bold'), bg='red', foreground='black')
lab_day_txt.place(x=780, y=400, height=40, width=100)





date_time()

clock.mainloop()