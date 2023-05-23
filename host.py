from flask import Flask, render_template, request
import requests,urllib
import urllib.parse
import json,re
import you
app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/send')
def getapidata():
    # message = request.args.get("text")
    
    message= "Kies je techniek dan ga je tijdens de les op zoek naar creatieve oplossingen voor technische vraagstukken. We werken daarbij vaak samen met bedrijven en organisaties. Zo heeft de gemeente Ermelo ons gevraagd om een oplossing te bedenken voor de processierups. Je leert ook al iets over programmeren en 3D-ontwerpen. In ons pas vernieuwde technieklokaal word je uitgedaagd om met de nieuwste machines en apparatuur jouw ideeën werkelijkheid te laten worden."

    
    
    
    prompt = """je doel is om onderzoeken te beoordelen en feedback te geven. Gebruik altijd onderstaand puntensysteem. Volg de structuur van het voorbeeld.
Volg deze de regels:
-Je doet alle beoordelingsteksten voor de gebruiker.
-Je schrijft de tekst in de taal van de gebruiker
-Je doet alle beoordelingsteksten voor de gebruiker.
-u kunt tussen de 1 en 5 punten toekennen door gebruik te maken van het puntensysteem
-Je mag nooit punten geven in dit formaat: POINT/MAX_POINTS

Relevantie:
1 = Helemaal niet relevant
2 = Enigszins relevant
3 = Matig relevant
4 = Zeer relevant
5 = Zeer relevant

Nauwkeurigheid:
1 = Volledig onnauwkeurig
2 = Meestal onnauwkeurig
3 = Enigszins onnauwkeurig
4 = Meestal nauwkeurig
5 = Volledig nauwkeurig

Helderheid:
1 = Zeer onduidelijk
2 = Enigszins onduidelijk
3 = Neutraal
4 = Enigszins duidelijk
5 = Heel duidelijk

Volledigheid:
1 = Zeer onvolledig
2 = Enigszins onvolledig
3 = Neutraal
4 = Enigszins compleet
5 = Zeer compleet

objectiviteit:
1 = Volledig subjectief
2 = Meestal subjectief
3 = Neutraal
4 = Meestal objectief
5 = Volledig objectief

Belangrijkheid:
1 = Helemaal niet significant
2 = Enigszins significant
3 = Matig significant
4 = Zeer significant
5 = Zeer significant

Geschiktheid:
1 = Helemaal niet geschikt
2 = Enigszins ongeschikt
3 = Neutraal
4 = Enigszins geschikt
5 = Zeer geschikt

Example! - Stick to this JSON formatting exactly!
```json
{
  "Relevantie": "POINTS FOR Relevantie",
  "Relevantieinfo": "EXPLAIN WHY POINTS",
  "Nauwkeurigheid": "POINTS FOR Nauwkeurigheid",
  "Nauwkeurigheidinfo": "EXPLAIN WHY POINTS",
  "Duidelijkheid": "POINTS FOR Duidelijkheid",
  "Duidelijkheidinfo": "EXPLAIN WHY POINTS",
  "Volledigheid": "POINTS FOR Volledigheid",
  "Volledigheidinfo": "EXPLAIN WHY POINTS",
  "Objectiviteit": "POINTS FOR Objectiviteit",
  "Objectiviteitinfo": "EXPLAIN WHY POINTS",
  "Belangrijkheid": "POINTS FOR Belangrijkheid",
  "Belangrijkheidinfo": "EXPLAIN WHY POINTS",
  "Geschiktheid": "POINTS FOR Geschiktheid",
  "Geschiktheidinfo": "EXPLAIN WHY POINTS"
}
```
De gebruiker wil dat je de volgende tekst beoordeelt:""" + str(message)

# Relevantie: De relevantie-parameter meet de mate waarin het antwoord direct en toepasselijk is op de gestelde onderzoeksvraag. Een score van 1 betekent dat het antwoord helemaal niet relevant is, terwijl een score van 5 betekent dat het antwoord uiterst relevant is.
# Nauwkeurigheid: De nauwkeurigheid-parameter meet de mate waarin het antwoord feitelijk correct is. Een score van 1 betekent dat het antwoord volledig onnauwkeurig is, terwijl een score van 5 betekent dat het antwoord volledig nauwkeurig is.
# Duidelijkheid: De duidelijkheid-parameter meet de mate waarin het antwoord begrijpelijk en helder is geformuleerd. Een score van 1 betekent dat het antwoord zeer onduidelijk is, terwijl een score van 5 betekent dat het antwoord zeer duidelijk is.
# Volledigheid: De volledigheid-parameter meet de mate waarin het antwoord een volledig beeld geeft van het onderwerp. Een score van 1 betekent dat het antwoord zeer onvolledig is, terwijl een score van 5 betekent dat het antwoord zeer volledig is.
# Objectiviteit: De objectiviteit-parameter meet de mate waarin het antwoord feitelijk en onbevooroordeeld is. Een score van 1 betekent dat het antwoord volledig subjectief is, terwijl een score van 5 betekent dat het antwoord volledig objectief is.
# Belangrijkheid: De belangrijkheid-parameter meet de mate waarin het antwoord relevant is voor het begrijpen van het onderwerp en het beantwoorden van de onderzoeksvraag. Een score van 1 betekent dat het antwoord helemaal niet significant is, terwijl een score van 5 betekent dat het antwoord uiterst significant is.
# Geschiktheid: De geschiktheid-parameter meet de mate waarin het antwoord geschikt is voor de specifieke context van de onderzoeksvraag en het beoogde publiek. Een score van 1 betekent dat het antwoord zeer ongeschikt is, terwijl een score van 5 betekent dat het antwoord zeer geschikt is.

    prompt = urllib.parse.quote(prompt)
    
    url = f"https://api.betterapi.net/youchat?inputs={prompt}&key=site"
    jsonobj = requests.get(url).json() # load json form api
    response = jsonobj["generated_text"] # print message response
    
        
    data = re.split(r"\s(?=[{\[])", response)[-1]
    try:
        data = data.split("}", 1)[0]
        data = data + "}"
    except:
        pass
    print(data)
    with open("logs.txt", "w") as f:
        f.write(data)
    data = json.loads(data)
    print(data)
   
    

    # for line in data.split('\n'):
    #     if line.startswith('#Relevantie:'):
    #         Relevantie = line.replace('#Relevantie: ', '').strip()
    #         print(Relevantie)
    #     elif line.startswith('#Relevantieinfo:'):
    #         Relevantieinfo = line.replace('#Relevantieinfo: ', '').strip()
    #         print(Relevantieinfo)
    #     elif line.startswith('#Nauwkeurigheid:'):
    #         Nauwkeurigheid = line.replace('#Nauwkeurigheid: ', '').strip()
    #         print(Nauwkeurigheid)
    #     elif line.startswith('#Nauwkeurigheidinfo:'):
    #         Nauwkeurigheidinfo = line.replace('#Nauwkeurigheidinfo: ', '').strip()
    #         print(Nauwkeurigheidinfo)
    #     elif line.startswith('#Duidelijkheid:'):
    #         Duidelijkheid = line.replace('#Duidelijkheid: ', '').strip()
    #         print(Duidelijkheid)
    #     elif line.startswith('#Duidelijkheidinfo:'):
    #         Duidelijkheidinfo = line.replace('#Duidelijkheidinfo: ', '').strip()
    #         print(Duidelijkheidinfo)
    #     elif line.startswith('#Volledigheid:'):
    #         Volledigheid = line.replace('#Volledigheid: ', '').strip()
    #         print(Volledigheid)
    #     elif line.startswith('#Volledigheidinfo:'):
    #         Volledigheidinfo = line.replace('#Volledigheidinfo: ', '').strip()
    #         print(Volledigheidinfo)
    #     elif line.startswith('#Objectiviteit:'):
    #         Objectiviteit = line.replace('#Objectiviteit: ', '').strip()
    #         print(Objectiviteit)
    #     elif line.startswith('#Objectiviteitinfo:'):
    #         Objectiviteitinfo = line.replace('#Objectiviteitinfo: ', '').strip()
    #         print(Objectiviteitinfo)
    #     elif line.startswith('#Belangrijkheid:'):
    #         Belangrijkheid = line.replace('#Belangrijkheid: ', '').strip()
    #         print(Belangrijkheid)
    #     elif line.startswith('#Belangrijkheidinfo:'):
    #         Belangrijkheidinfo = line.replace('#Belangrijkheidinfo: ', '').strip()
    #         print(Belangrijkheidinfo)
    #     elif line.startswith('#Geschiktheid:'):
    #         Geschiktheid = line.replace('#Geschiktheid: ', '').strip()
    #         print(Geschiktheid)
    #     elif line.startswith('#Geschiktheidinfo:'):
    #         Geschiktheidinfo = line.replace('#Geschiktheidinfo: ', '').strip()
    #         print(Geschiktheidinfo)



        # elif line.startswith('#Content:'):
        #     content = line.replace('#Content:', '').strip()
        #     next_line = f.readline().strip()
        #     while next_line and not next_line.startswith('#'):
        #         content += '\n' + next_line
        #         next_line = f.readline().strip()
        #     continue
        
        
    
    
    return render_template("index.html", 
                       Relevantie=int(data['Relevantie']),
                       Relevantieinfo=data['Relevantieinfo'],
                       Nauwkeurigheid=int(data['Nauwkeurigheid']),
                       Nauwkeurigheidinfo=data['Nauwkeurigheidinfo'],
                       Duidelijkheid=int(data['Duidelijkheid']),
                       Duidelijkheidinfo=data['Duidelijkheidinfo'],
                       Volledigheid=int(data['Volledigheid']),
                       Volledigheidinfo=data['Volledigheidinfo'],
                       Objectiviteit=int(data['Objectiviteit']),
                       Objectiviteitinfo=data['Objectiviteitinfo'],
                       Belangrijkheid=int(data['Belangrijkheid']),
                       Belangrijkheidinfo=data['Belangrijkheidinfo'],
                       Geschiktheid=int(data['Geschiktheid']),
                       Geschiktheidinfo=data['Geschiktheidinfo'])


if __name__ == '__main__':
    app.run()
