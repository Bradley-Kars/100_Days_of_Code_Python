import csv
import os

file_path = "100MostStreamedSongs.csv"

try:
  with open(file_path) as file:
    reader = csv.DictReader(file)
    for row in reader:
      artist = row["Artist(s)"].title()
      print(artist)
      if not os.path.exists(artist):
        os.mkdir(artist)
      song = row["Song"]
      print(song)
      path = os.path.join(artist, song)
      try:
        with open(path, "w") as f:
          pass
      except IOError as e:
        print(f"Error creating file {path}: {e}")

except FileNotFoundError:
  print(f"Error: File '{file_path}' not found.")

except Exception as e:
  print(f"An unexpected error occurred: {e}")