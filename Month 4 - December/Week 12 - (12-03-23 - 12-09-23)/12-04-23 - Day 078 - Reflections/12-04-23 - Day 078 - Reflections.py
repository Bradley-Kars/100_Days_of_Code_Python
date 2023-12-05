from replit import db
from flask import Flask, render_template

def populate_db():
  db[77] = {
    'url': 'https://github.com/Bradley-Kars/100_Days_of_Code_Python/tree/main/Month%204%20-%20December/Week%2012%20-%20(12-03-23%20-%2012-09-23)/12-03-23%20-%20Day%20077%20-%20Slim%20Down', 
    'ref': 'Deployed my first site using code with variables.'

  }
  db[76] = {
    'url': 'https://github.com/Bradley-Kars/100_Days_of_Code_Python/tree/main/Month%204%20-%20December/Week%2011%20-%20(12-01-23%20-%2012-02-23)/12-02-23%20-%20Day%20076%20-%20Flask', 
    'ref': 'Learned about flask and how to host more adnvaced sites in python.'
  }
  db[75] = {
    'url': 'https://github.com/Bradley-Kars/100_Days_of_Code_Python/tree/main/Month%204%20-%20December/Week%2011%20-%20(12-01-23%20-%2012-02-23)/12-01-23%20-%20Day%20075%20-%20Link%20tree', 
    'ref': 'Created a Link sharing page with links to my socials.'
  }

app = Flask(__name__)
"""
@app.route('/<pageNumber>')
def index(pageNumber):

  return f"This is page {pageNumber}"
"""

@app.route('/<pagenumber>')
def index(
  pagenumber,
  href=None, 
  reflection=None
):

    data = db[pagenumber]

    return render_template(
      'reflection.html', 
      pagenumber=pagenumber, 
      href=data.get('url'), 
      reflection=data.get('ref')
    )

populate_db()
app.run(host='0.0.0.0', port=81, debug=True)