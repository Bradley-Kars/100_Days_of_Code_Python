import tkinter as tk

class VisualNovel(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Visual Novel")
    self.geometry("400x400")

    image_paths = ["visualNovel/1.png", "visualNovel/3.png", "visualNovel/2.png", "visualNovel/4.png", "visualNovel/5.png", "visualNovel/6.png"]
    self.images = [tk.PhotoImage(file=path).subsample(4) for path in image_paths]

    self.canvas = tk.Canvas(self, width=300, height=200)
    self.canvas.pack()
    self.container = self.canvas.create_image(150, 150, image=self.images[0])

    self.story = "You meet a woman on the way to a Replit meetup IRL"
    self.story_label = tk.Label(text=self.story)
    self.story_label.pack()

    self.button = tk.Button(text="Ask her how she codes?", command=self.ask_how_she_codes)
    self.button.pack()

    self.button2 = tk.Button(text="Tell her about Replit", command=self.tell_about_replit)
    self.button2.pack()

    self.button3 = tk.Button(text="She says 'I use a local editor'", command=self.say_local_editor)
    self.button4 = tk.Button(text="She says 'I use Replit'", command=self.say_replit)

    self.button5 = tk.Button(text="You say 'I use Replit too'", command=self.say_replit_too)
    self.button6 = tk.Button(text="You say 'I'm actually going through 100 days of code right now'", command=self.celebrate_win)

    self.restart_button = tk.Button(text="Restart", command=self.restart)

  def configure_buttons(self, *buttons):
    for btn in buttons:
      btn.pack_forget()
    self.restart_button.pack()

  def ask_how_she_codes(self):
    self.canvas.itemconfig(self.container, image=self.images[1])
    self.story = "She tries to pull out her laptop and drops it on the floor"
    self.story_label["text"] = self.story
    self.configure_buttons(self.button, self.button2)

  def tell_about_replit(self):
    self.canvas.itemconfig(self.container, image=self.images[2])
    self.story = "Why I use Replit of course, like every sane individual!"
    self.story_label["text"] = self.story
    self.configure_buttons(self.button5, self.button6)

  def say_local_editor(self):
    self.canvas.itemconfig(self.container, image=self.images[5])
    self.story = "She spends two hours loading up a code editor\nand getting it working, you wait politely"
    self.story_label["text"] = self.story
    self.restart_button.pack()

  def say_replit(self):
    self.canvas.itemconfig(self.container, image=self.images[4])
    self.story = "You both celebrate using the best\n coding platform on your way to the meetup"
    self.story_label["text"] = self.story
    self.restart_button.pack()

  def say_replit_too(self):
    self.canvas.itemconfig(self.container, image=self.images[3])
    self.story = "She tells you all about 100 days of code!"
    self.story_label["text"] = self.story
    self.configure_buttons(self.button5, self.button6)

  def celebrate_win(self):
    self.canvas.itemconfig(self.container, image=self.images[4])
    self.story = "You both celebrate using the best\n coding platform on your way to the meetup\nand talk about 100 days of code"
    self.story_label["text"] = self.story
    self.configure_buttons(self.button5, self.button6)

  def restart(self):
    self.canvas.itemconfig(self.container, image=self.images[0])
    self.story = "You meet a woman on the way to a Replit meetup IRL"
    self.story_label["text"] = self.story
    self.restart_button.pack_forget()
    self.button.pack()
    self.button2.pack()

if __name__ == "__main__":
  app = VisualNovel()
  app.mainloop()