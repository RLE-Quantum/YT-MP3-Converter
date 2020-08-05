import youtube_dl
from tkinter import *
import os

root = Tk()
root.title('Youtube-MP3 Converter')
root.geometry('600x600+350+60')

label = Label(root, text="Youtube to MP3 Converter")
label.pack()

url = Entry(root)
url.pack()
url.get()


def download():
    ydl_opts = {
        "format": "bestaudio"
    }

    youtube = youtube_dl.YoutubeDL(ydl_opts)
    try :
        youtube.download([url.get()])
    except youtube_dl.utils.DownloadError:
        print("Invalid URL")
        return

    all_files = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f))]

    for file_path in all_files:
        if file_path.endswith(".webm"):

            file_path_in = os.path.join(r'.', file_path)
            file_path_out = file_path_in.replace("webm", "mp3")
            os.system(rf""".\ffmpeg.exe -i "{file_path_in}" -vn -ab 128k -ar 44100 -y "{file_path_out}" """)

            break

download = Button(root, text="Download", command=download)
download.pack()

root.mainloop()