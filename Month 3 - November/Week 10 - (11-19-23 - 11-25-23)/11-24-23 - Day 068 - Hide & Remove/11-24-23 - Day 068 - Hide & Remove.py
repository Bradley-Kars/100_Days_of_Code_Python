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
    self.canvas = tk.Canvas(self.master, width=300, height=300)
    self.canvas.pack()
    self.images = {
        "mo": "guessWho/mo.jpg",
        "charlotte": "guessWho/charlotte.jpg",
        "gerald": "guessWho/gerald.jpg",
        "katie": "guessWho/katie.jpg"
    }
    self.img_ref = None

  def show_image(self):
    person = self.text.get("1.0", "end").lower().strip()
    if person in self.images:
      self.canvas.pack()
      img = Image.open(self.images[person])
      img = img.resize((300, 300), Image.LANCZOS)
      self.img_ref = ImageTk.PhotoImage(img)
      self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_ref)
      self.label["text"] = "Correct! Here's the image for " + person.capitalize()
    else:
      self.label["text"] = "Unable to find this user"
      self.canvas.pack_forget()

def main():
  root = tk.Tk()
  app = GuessWhoApp(root)
  root.mainloop()

if __name__ == "__main__":
  main()