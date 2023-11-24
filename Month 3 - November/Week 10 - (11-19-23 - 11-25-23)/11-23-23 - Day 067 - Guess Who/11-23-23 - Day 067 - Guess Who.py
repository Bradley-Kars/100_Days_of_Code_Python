import tkinter as tk
from PIL import Image, ImageTk

class GuessWhoApp:
  def __init__(self, master):
    self.master = master
    self.master.title("Guess Who?")
    self.master.geometry("400x400")

    self.label = tk.Label(text="Guess Who?")
    self.label.pack()

    self.text = tk.Text(self.master, height=1, width=30)
    self.text.pack()

    self.button = tk.Button(text="Find", command=self.show_image)
    self.button.pack()

    self.canvas = tk.Canvas(self.master, width=400, height=380)
    self.canvas.pack()

    self.images = {
      "mo": ImageTk.PhotoImage(Image.open("guessWho/mo.jpg")),
      "charlotte": ImageTk.PhotoImage(Image.open("guessWho/charlotte.jpg")),
      "gerald": ImageTk.PhotoImage(Image.open("guessWho/gerald.jpg")),
      "katie": ImageTk.PhotoImage(Image.open("guessWho/katie.jpg"))
    }

    self.container = self.canvas.create_image(150, 1, image=self.images["mo"])

  def show_image(self):
      person = self.text.get("1.0", "end").lower().strip()

      if person in self.images:
          self.canvas.itemconfig(self.container, image=self.images[person])
      else:
          self.label["text"] = "Unable to find this user"

def main():
  root = tk.Tk()
  app = GuessWhoApp(root)
  root.mainloop()

if __name__ == "__main__":
  main()