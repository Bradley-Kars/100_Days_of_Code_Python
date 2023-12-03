from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  page = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Home - Bradley Kars</title>
  <style>
    body {
      background-color: #1e1e1e;
      color: #ecf0f1;
      font-family: Tahoma, sans-serif;
      margin: 0;
    }

    .container {
      display: flex;
      justify-content: space-around;
      align-items: center;
      flex-wrap: wrap;
      padding: 20px;
      box-sizing: border-box;
    }

    .button {
      padding: 10px;
      margin: 10px;
      border-radius: 5px;
      text-align: center;
      background-color: #333;
      color: #fff;
      text-decoration: none;
      font-weight: bold;
      transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
    }

    .button:hover {
      background-color: #4caf50;
      color: #000;
    }
  </style>
</head>

<body>

  <div class="container">
    <a href="/linktree" class="button">Linktree</a>
    <a href="/portfolio" class="button">Portfolio</a>
  </div>

  <script src="https://replit.com/public/js/replit-badge.js" theme="dark" defer></script>
</body>

</html>"""
  return page

@app.route('/portfolio')
def portfolio():
  page = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>My Portfolio</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
  <style>
    body {
      background-color: #1e1e1e;
      color: #ffffff;
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    h1 {
      color: #a45bf5;
    }

    ol {
      list-style: none;
      padding: 0;
    }

    li {
      margin-bottom: 20px;
      overflow: hidden;
      background-color: #363636;
      border-radius: 10px;
      padding: 15px;
    }

    a {
      color: #8a2be2;
      float: left;
      margin-right: 10px;
    }

    a:hover {
      color: #39ff14;
    }

    img {
      border: none;
      border-radius: 0;
    }

    p {
      margin-top: 10px;
    }

  </style>
</head>

<body>
  <h1>Bradley Kars<br>Portfolio</h1>

  <ol>
    <li>
      <h2>Day 72 - Secret Diary 2.0</h2>
      <a href='https://github.com/Bradley-Kars/100_Days_of_Code_Python/blob/main/Month%203%20-%20November/Week%2011%20-%20(11-26-23%20-%2011-30-23)/11-28-23%20-%20Day%20072%20-%20Secret%20Diary%202.0.py'>
        <img src='https://play-lh.googleusercontent.com/-OxVM3IlQm2XPpUzgOhwfzBrmnmogB5ISHQ_irEiXRGToh51QCTRu9_2jaD5mOv1Aw8' width='75px'>
      </a>
      <p>Stores user credentials in the Replit database, using hashed and salted passwords.</p>
      <p>Stores the user's diary entries in the same database, using the timestamp as the key, while allowing the user to view the entries in order.</p>
    </li>
    <li>
      <h2>Day 66 - This is getting GUI</h2>
      <a href='https://github.com/Bradley-Kars/100_Days_of_Code_Python/blob/main/Month%203%20-%20November/Week%2010%20-%20(11-19-23%20-%2011-25-23)/11-22-23%20-%20Day%20066%20-%20This%20is%20getting%20GUI.py'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/GNOME_Calculator_icon_2021.svg/640px-GNOME_Calculator_icon_2021.svg.png' width='75px'>
      </a>
      <p>A simple but functional GUI calculator. No bells and whistles or scientific functions, but a solid calculator nonetheless.</p>
    </li>
    <li>
      <h2>Day 60 - The Magic of Time</h2>
      <a href='https://github.com/Bradley-Kars/100_Days_of_Code_Python/blob/main/Month%203%20-%20November/Week%2009%20-%20(11-12-23%20-%2011-18-23)/11-16-23%20-%20Day%20060%20-%20The%20Magic%20of%20Time.py'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/X-office-calendar.svg/2048px-X-office-calendar.svg.png' width='75px'>
      </a>
      <p>This is a simple program that takes an event date from the user and informs them of the time until or the time since said event.</p>
    </li>
    <li>
      <h2>Day 59 - Palindrome</h2>
      <a href='https://github.com/Bradley-Kars/100_Days_of_Code_Python/blob/main/Month%203%20-%20November/Week%2009%20-%20(11-12-23%20-%2011-18-23)/11-15-23%20-%20Day%20059%20-%20Palindrome.py'>
        <img src='https://easydrawingguides.com/wp-content/uploads/2020/08/Racecar-Step-10.png' width='75px'>
      </a>
      <p>A simple but functional palindrome detector that works on both single words and full sentences.</p>
    </li>
    <li>
      <h2>Day 42 - MokeBeast</h2>
      <a href='https://github.com/Bradley-Kars/100_Days_of_Code_Python/blob/main/Month%202%20-%20October/Week%2007%20-%20(10-29-23%20-%2010-31-23)/10-29-23%20-%20Day%20042%20-%20MokeBeast.py'>
        <img src='https://reel2media.com/wp-content/uploads/2021/05/Asset-2@4x.png' width='75px'>
      </a>
      <p>A fun new game and not at all a rip-off of a giant multinational franchise that took the world by storm in the '90s.</p>
    </li>
  </ol>

  <script src="{{ url_for('static', filename='script.js') }}"></script>
  <script src="https://replit.com/public/js/replit-badge.js" theme="dark" defer></script>
</body>

</html>"""
  return page

@app.route('/linktree')
def linktree():
  page = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Bradley Kars</title>
  <style>
    body {
      background-color: #1e1e1e;
      color: #ecf0f1;
      font-family: Tahoma, sans-serif;
      margin: 0;
    }

    .container {
      display: flex;
      justify-content: space-around;
      align-items: center;
      flex-wrap: wrap;
      padding: 20px;
      box-sizing: border-box;
    }

    .person,
    .socials,
    .resume {
      flex: 0 0 75%;
      padding: 20px;
      margin: 10px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
      text-align: center;
      background-color: #333;
    }

    .person img {
      border-radius: 10px;
      width: 100%;
    }

    h1 {
      margin-bottom: 10px;
    }

    h2,
    .resume p,
    .socials li {
      color: #ffffff;
    }

    a {
      text-decoration: none;
      font-weight: bold;
      transition: color 0.3s ease-in-out;
      color: #fff;
    }

    a:hover {
      color: #4caf50;
    }

    .socials ul,
    .resume ul {
      list-style-type: none;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
    }
  </style>
</head>

<body>

  <div class="container">
    <section class='person' itemscope itemtype="http://schema.org/Person">
      <img src='https://i.imgur.com/IlpAYV0.jpg' width='400px'>
      <div>
        <h1>
          <span itemprop="givenName">Bradley</span>
          <span itemprop="familyName">Kars</span>
        </h1>
        <p>IT Help Desk Support Specialist | Cybersecurity Enthusiast | Game Dev Hobbyist</p>
      </div>
    </section>

    <section class='socials'>
      <h2>Socials</h2>
      <ul>
        <li><a href='https://www.linkedin.com/in/bradley-kars/'>LinkedIn</a></li>
        <li><a href='https://www.instagram.com/bradley_kars/'>Instagram</a></li>
        <li><a href='https://github.com/Bradley-Kars/' target='_blank'>GitHub</a></li>
      </ul>
    </section>

    <section class='resume'>
      <h2>Resume</h2>
      <p>Check out my resume: <a href='https://bradley-kars.github.io/' target='_blank'>Resume</a></p>
    </section>
  </div>

  <script src="script.js"></script>
  <script src="https://replit.com/public/js/replit-badge.js" theme="dark" defer></script>
</body>

</html>
"""
  return page


app.run(host='0.0.0.0', port=81)