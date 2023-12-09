from flask import Flask

app = Flask(__name__)

def translate_text(language, text):
    translations = {
        'english':' Strange women lying in ponds distributing swords is no basis for a system of government. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony.',
        'mandarin-chinese': '奇怪的女人躺在池塘里分发剑，这不能成为政府体系的基础。最高行政权力源于群众的授权，而不是某种荒谬的水中仪式。',
        'hindi': 'तालाब में पड़ी विद्वेषी महिलाएँ तलवारें बाँटती हैं एक सरकारी तंत्र के लिए कोई आधार नहीं हैं। सर्वोच्च कार्यकारी शक्ति जनसमूह की मंडली से, किसी विषामकारी जलसंस्कार से नहीं उत्पन्न होती है।',
        'spanish': 'Mujeres extrañas que yacen en estanques distribuyendo espadas no son la base para un sistema de gobierno. El poder ejecutivo supremo emana de un mandato de las masas, no de alguna ceremonia acuática ridícula.',
        'french': 'Des femmes étranges gisant dans des étangs distribuant des épées ne constituent pas la base d\'un système de gouvernement. Le pouvoir exécutif suprême découle d\'un mandat des masses, non d\'une cérémonie aquatique ridicule.',
        'arabic': 'النساء الغريبات اللواتي يستلقين في البرك توزع السيوف ليسوا أساسًا لنظام حكومي. السلطة التنفيذية العليا تنبع من تفويض الجماهير، وليس من حفل مائي هزلي.',
        'bengali': 'পুকুরে শোকীয় মহিলা কয়েকটি কাটার বিতরণ করছে তা কোনো সরকারি ব্যবস্থার জন্য কোন ভিত্তি হয় না। সুপ্রীম নির্বাচনী ক্ষমতা জনসমূহের মণ্ডেট থেকে উত্পন্ন, কোনও হাস্যরস জলসংস্কার থেকে নয়।',
        'russian': 'Странные женщины, лежащие в прудах и раздающие мечи, не являются основой для системы управления. Высшая исполнительная власть происходит от мандата масс, а не от какой-то фарсовой акватической церемонии.',
        'portuguese': 'Mulheres estranhas deitadas em lagoas distribuindo espadas não são a base para um sistema de governo. O poder executivo supremo deriva de um mandato das massas, não de alguma cerimônia aquática ridícula.',
        'indonesian': 'Wanita aneh yang berbaring di kolam membagikan pedang bukan dasar bagi sistem pemerintahan. Kekuasaan eksekutif tertinggi berasal dari mandat dari massa, bukan dari suatu upacara air yang konyol.',
    }

    return translations.get(language, translations['english'])

@app.route('/language')
def default_language():
    default_text = translate_text('english', '')
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                background-color: #1a1a1a; /* Dark background color */
                color: #ffffff; /* Text color */
                font-family: Arial, sans-serif;
            }}

            .card {{
                background-color: #333; /* Card background color */
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                max-width: 600px;
                margin: auto;
                margin-top: 50px;
                text-align: center;
            }}

            p {{
                font-weight: bold;
                text-align: center;
            }}
        </style>
        <title>Translation App</title>
    </head>
    <body>
        <div class="card">
            <p>{default_text}</p>
        </div>
    </body>
    </html>
    """

@app.route('/language/<lang>')
def custom_language(lang):
    custom_text = translate_text(lang, '')
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                background-color: #1a1a1a; /* Dark background color */
                color: #ffffff; /* Text color */
                font-family: Arial, sans-serif;
            }}

            .card {{
                background-color: #333; /* Card background color */
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0
              : 4px 8px rgba(0, 0, 0, 0.1);
                  max-width: 600px;
                  margin: auto;
                  margin-top: 50px;
                  text-align: center;
              }}

              p {{
                  font-weight: bold;
                  text-align: center;
              }}
          </style>
          <title>Translation App</title>
      </head>
      <body>
          <div class="card">
              <p>{custom_text}</p>
          </div>
      </body>
      </html>
      """

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)