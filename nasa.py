import requests
from tkinter import *
from io import BytesIO
from PIL import ImageTk, Image

API = 'NhgK0tSVbVyFeToxhQbMRoDObeY1ZOBd5aMQiIxN'
URL = 'https://api.nasa.gov/planetary/apod'


def show_picture(url, title):
    window = Tk()
    window.title('picture of the day')
    window.geometry('800x600')

    response = requests.get(url)
    img_data = response.content

    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    pict_of_day = Label(window, image=img)
    pict_of_day.place(x=0, y=0, relwidth=1, relheight=1)

    text = Label(window, text=title, font=("Arial Bold", 15))
    text.grid(column=0, row=0)

    window.mainloop()


def get_picture_of_the_day(url):
    params = {'api_key': API}
    response = requests.get(url, params=params)

    data = response.json()
    picture_url = data['url']
    title = data['title']
    show_picture(picture_url, title)


get_picture_of_the_day(URL)
