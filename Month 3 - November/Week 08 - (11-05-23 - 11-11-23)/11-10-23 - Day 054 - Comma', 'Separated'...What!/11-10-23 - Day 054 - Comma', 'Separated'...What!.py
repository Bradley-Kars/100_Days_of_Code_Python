import csv

def calculate_total(file_path):
  total = 0.0
  try:
    with open(file_path) as file:
      reader = csv.DictReader(file)
      for row in reader:
        try:
          total += float(row["Quantity"]) * float(row["Cost"])
        except (ValueError, KeyError):
          print("Error: Invalid data in the CSV file.")
  except FileNotFoundError:
    print("Error: CSV file not found.")
  return total

def main():
  file_path = "Day54Totals.csv"
  total = calculate_total(file_path)
  formatted_total = "{:,.2f}".format(total)
  print(f"Total: ${formatted_total}")

if __name__ == "__main__":
  main()