from tkinter import *
from pytube import YouTube

root = Tk()
root.configure(bg = "#595858")
root.minsize(850, 500)
root.title("YouTube Video Downloader")

#==============================================================================
#==============================================================================

def avail():
    
    try:
        vid = YouTube(input1.get())
        return 1
        
    except Exception:
        warn = Label(root, text = "Incorrect URL !", bg = "#595858")
        warn.place(relx = 0.25, rely = 0.28)
        return 0


def audio_download():
    
    if avail() == 1:
        vid = YouTube(input1.get())
        audio = vid.streams.filter(only_audio = True).first()
        audio.download("Music")
        notif = Label(root, text = "Download completed !", bg = "#595858", fg = "white")
        notif.place(relx = 0.45, rely = 0.65)
    

def video_download():
    if avail() == 1:
        vid = YouTube(input1.get())
        video = vid.streams.filter(progressive = True).filter(resolution = ("360p")).first()
        video.download("Videos")
        notif = Label(root, text = "Download completed !", bg = "#595858", fg = "white")
        notif.place(relx = 0.45, rely = 0.65)
#==============================================================================
#==============================================================================


go = Button(root, text = "Go!", bg = "#3A7CFF", fg = "white", command = avail)
input1  = Entry(root)

audio   = Label(root, text = "AUDIO")
a_download = Button(root, text = "Download", bg = "#14B300", fg = "white", command = audio_download)
v_download = Button(root, text = "Download", bg = "#14B300", fg = "white", command = video_download)

video   = Label(root, text = "VIDEO")

#input1.insert(0, "Enter the link here...")
link = input1.get()

go.place(relx = 0.75, rely = 0.2, relheight = 0.07, relwidth = 0.08)
input1.place(relx = 0.25, rely = 0.2,relheight = 0.07, relwidth = 0.5)

audio.place(relx = 0.4, rely = 0.4, relheight = 0.08, relwidth = 0.1)
a_download.place(relx =0.55, rely = 0.4, relheight = 0.08, relwidth = 0.15)

video.place(relx = 0.4, rely = 0.5, relheight = 0.08, relwidth = 0.1)
v_download.place(relx =0.55, rely = 0.5, relheight = 0.08, relwidth = 0.15)

root.mainloop()