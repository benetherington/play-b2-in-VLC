from backblazeb2 import BackBlazeB2
import os
from Tkinter import *
import tkFont
from private import *

b2 = BackBlazeB2(B2_ACCOUNT, B2_APPLICATION_KEY)

master = Tk()
list_frame = Frame()
list_frame.grid()

def open_vlc(event, file_ID):
    file_URL = "https://" +B2_SERVER+ ".backblazeb2.com/b2api/v1/b2_download_file_by_id?fileId=" + file_ID
    os.system("/Applications/VLC.app/Contents/MacOS/VLC " + file_URL)

def delete_warning(event, file_name, file_ID):
    warning.place(relx=0.5, rely=0.5, anchor=CENTER)
    big_obnoxious.grid(row=0, columnspan=2)
    Label(warning, text="Are you sure you want to delete this file?").grid(row=1, columnspan=2)
    Label(warning, text=file_name).grid(row=2, columnspan=2)
    button_okay.grid(row=3, column=1, sticky=E)
    button_cancel.grid(row=3, column=0, sticky=W)
    button_okay.bind("<Button-1>", lambda event, file_ID=file_ID, file_name=file_name: delete_me(event, file_name, file_ID))

def delete_me(event, file_name, file_ID):
    warning.place_forget()
    list_frame.destroy()

    os.system("b2 delete-file-version " + file_name + ' ' + file_ID)

    global list_frame
    list_frame = Frame()
    list_frame.grid()
    generate_file_list()

def generate_file_list():
    grid_row = 0
    for file in b2.list_file_names(bucket_name='media4ana')['files']:
        
        episode = Label(list_frame, text=file["fileName"], fg='blue')
        f = tkFont.Font(episode, episode.cget("font"))
        f.configure(underline = True)
        episode.configure(font=f)
        delete = Button(list_frame, text="delete")

        episode.grid(row=grid_row, column=0)
        delete.grid(row=grid_row, column=1)

        episode.bind("<Button-1>", lambda event, file_ID=file['fileId']: open_vlc(event, file_ID))
        delete.bind("<Button-1>", lambda event, file_ID=file['fileId'], file_name=file['fileName']: delete_warning(event, file_name, file_ID))

        grid_row += 1

warning = Frame(bg='white', bd=1, relief='ridge')
big_obnoxious = Label(warning, text="WARNING, ANALIESE, WARNING", font=("Courier", 20), fg='red')
button_okay = Button(warning, text="okay")
button_cancel = Button(warning, text="cancel", command= lambda: warning.place_forget())

generate_file_list()

mainloop()