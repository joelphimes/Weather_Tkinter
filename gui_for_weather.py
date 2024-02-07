# https://docs.python.org/3/library/tkinter.ttk.html
import tkinter as ttk
# https://docs.python.org/3/library/re.html
import re
# https://docs.python.org/3/library/subprocess.html
import subprocess

# need to use .call with older version of python on this Mac. Would update to "run" for later versions.
def run_shell_command():
    subprocess.call(["./get_weather.sh"], shell=True)

# open in read only, read into variable, use re to to find matches in variable.
# take first string from list and replace quotes / make first letter upper case.
# set variable temp (string var from tk) to 'a'.
def get_temps():
        with open('weather.txt', 'r') as f:
            d = f.read()
            m = re.findall(r'"temperature":[0-9][0-9]', d)
            a = m[0].replace('"', '').title()
            temp.set(a)

# run shell script (curl) for weather. 
run_shell_command()

# create instance of tk.       
app = ttk.Tk()
# set title of application.
app.title("Temperature in Severn, Maryland")

# need variable from get temps. 
temp = ttk.StringVar()
# label for contents of the application, placed in the center of the window. 
temp_label = ttk.Label(app, textvariable=temp, justify="center", anchor='center')
# pack to complete the proccess. 
temp_label.pack()

# button for application.
# command will excute get temps function.
extract_button = ttk.Button(app, text="Fetch Temp", command=get_temps)
# pack to complete the proccess.
extract_button.pack()

# variables for application box geometey, this is a convuleted pain in the ass for like no reason. 
w = 300 
h = 60
ws = app.winfo_screenwidth() 
hs = app.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the postion and size of text box.
app.geometry('%dx%d+%d+%d' % (w, h, x, y))

# mainloop to start the program.
app.mainloop()