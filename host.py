from flask import Flask, render_template, request
import requests,urllib
import urllib.parse
import json,re
app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/send')
def getapidata():
    # message = request.args.get("text")
    
    message= "Kies je techniek dan ga je tijdens de les op zoek naar creatieve oplossingen voor technische vraagstukken. We werken daarbij vaak samen met bedrijven en organisaties. Zo heeft de gemeente Ermelo ons gevraagd om een oplossing te bedenken voor de processierups. Je leert ook al iets over programmeren en 3D-ontwerpen. In ons pas vernieuwde technieklokaal word je uitgedaagd om met de nieuwste machines en apparatuur jouw ideeën werkelijkheid te laten worden."

    
    
    
    prompt = f"""Your goal is to rate and give featback on research. Always use the points system below. Follow the structure of the example.
Notice
Follow there rules:
-You do all the rating text for the user.
-You shall write the text in the language of the user
-You do all the rating text for the user.
-you can awward points between 1 - 5 use the points system
-You shall never give points in this format: POINT/MAX_POINTS

Relevance:
1 = Not relevant at all
2 = Somewhat relevant
3 = Moderately relevant
4 = Very relevant
5 = Extremely relevant

Accuracy:
1 = Completely inaccurate
2 = Mostly inaccurate
3 = Somewhat inaccurate
4 = Mostly accurate
5 = Completely accurate

Clarity:
1 = Very unclear
2 = Somewhat unclear
3 = Neutral
4 = Somewhat clear
5 = Very clear

Completeness:
1 = Very incomplete
2 = Somewhat incomplete
3 = Neutral
4 = Somewhat complete
5 = Very complete

Objectivity:
1 = Completely subjective
2 = Mostly subjective
3 = Neutral
4 = Mostly objective
5 = Completely objective

Importance:
1 = Not significant at all
2 = Somewhat significant
3 = Moderately significant
4 = Very significant
5 = Extremely significant

Suitability:
1 = Not suitable at all
2 = Somewhat unsuitable
3 = Neutral
4 = Somewhat suitable
5 = Very suitable

Example! - Stick to this formatting exactly!
#Relevantie: POINTS FOR Relevantie
#Relevantieinfo: EXPLAIN WHY POINTS
#Nauwkeurigheid: POINTS FOR Nauwkeurigheid
#Nauwkeurigheidinfo: EXPLAIN WHY POINTS
#Duidelijkheid: POINTS FOR Duidelijkheid
#Duidelijkheidinfo: EXPLAIN WHY POINTS
#Volledigheid: POINTS FOR Volledigheid
#Volledigheidinfo: EXPLAIN WHY POINTS
#Objectiviteit: POINTS FOR Objectiviteit
#Objectiviteitinfo: EXPLAIN WHY POINTS
#Belangrijkheid: POINTS FOR Belangrijkheid
#Belangrijkheidinfo: EXPLAIN WHY POINTS
#Geschiktheid: POINTS FOR Geschiktheid
#Geschiktheidinfo: EXPLAIN WHY POINTS
The user wants you to rate the following text: {message}"""

# Relevantie: De relevantie-parameter meet de mate waarin het antwoord direct en toepasselijk is op de gestelde onderzoeksvraag. Een score van 1 betekent dat het antwoord helemaal niet relevant is, terwijl een score van 5 betekent dat het antwoord uiterst relevant is.
# Nauwkeurigheid: De nauwkeurigheid-parameter meet de mate waarin het antwoord feitelijk correct is. Een score van 1 betekent dat het antwoord volledig onnauwkeurig is, terwijl een score van 5 betekent dat het antwoord volledig nauwkeurig is.
# Duidelijkheid: De duidelijkheid-parameter meet de mate waarin het antwoord begrijpelijk en helder is geformuleerd. Een score van 1 betekent dat het antwoord zeer onduidelijk is, terwijl een score van 5 betekent dat het antwoord zeer duidelijk is.
# Volledigheid: De volledigheid-parameter meet de mate waarin het antwoord een volledig beeld geeft van het onderwerp. Een score van 1 betekent dat het antwoord zeer onvolledig is, terwijl een score van 5 betekent dat het antwoord zeer volledig is.
# Objectiviteit: De objectiviteit-parameter meet de mate waarin het antwoord feitelijk en onbevooroordeeld is. Een score van 1 betekent dat het antwoord volledig subjectief is, terwijl een score van 5 betekent dat het antwoord volledig objectief is.
# Belangrijkheid: De belangrijkheid-parameter meet de mate waarin het antwoord relevant is voor het begrijpen van het onderwerp en het beantwoorden van de onderzoeksvraag. Een score van 1 betekent dat het antwoord helemaal niet significant is, terwijl een score van 5 betekent dat het antwoord uiterst significant is.
# Geschiktheid: De geschiktheid-parameter meet de mate waarin het antwoord geschikt is voor de specifieke context van de onderzoeksvraag en het beoogde publiek. Een score van 1 betekent dat het antwoord zeer ongeschikt is, terwijl een score van 5 betekent dat het antwoord zeer geschikt is.

    prompt = urllib.parse.quote(prompt)
    
    # print(prompt)


    headers = {
        'Content-Type': 'application/json',
    }


    json_data = {
        'cmd': 'request.get',
        'url': f'https://you.com/api/streamingSearch?q=replay%20in%20the%20input%20message%20language:{message}' +'&page=1&count=10&safeSearch=Moderate&onShoppingPage=false&mkt=&responseFilter=WebPages,Translations,TimeZone,Computation,RelatedSearches&domain=youchat&queryTraceId=2f917965-2e6f-427d-822c-a4dba2d744d9&chat=%5B%7B%22question%22%3A%22Your%20goal%20is%20to%20rate%20and%20give%20featback%20on%20research.%20Always%20use%20the%20points%20system%20below.%20Follow%20the%20structure%20of%20the%20example.%5CnNotice%5CnFollow%20there%20rules%3A%5Cn-You%20do%20all%20the%20rating%20text%20for%20the%20user.%5Cn-You%20shall%20write%20the%20text%20in%20the%20language%20of%20the%20user%5Cn-You%20do%20all%20the%20rating%20text%20for%20the%20user.%5Cn-you%20can%20awward%20points%20between%201%20-%205%20use%20the%20points%20system%5Cn-You%20shall%20never%20give%20points%20in%20this%20format%3A%20POINT%2FMAX_POINTS%5Cn%5CnRelevantie%3A%201%20%3D%20Helemaal%20niet%20relevant%202%20%3D%20Enigszins%20relevant%203%20%3D%20Matig%20relevant%204%20%3D%20Zeer%20relevant%205%20%3D%20Uiterst%20relevant%5CnNauwkeurigheid%3A%201%20%3D%20Volledig%20onnauwkeurig%202%20%3D%20Meestal%20onnauwkeurig%203%20%3D%20Enigszins%20onnauwkeurig%204%20%3D%20Meestal%20nauwkeurig%205%20%3D%20Volledig%20nauwkeurig%5CnDuidelijkheid%3A%201%20%3D%20Zeer%20onduidelijk%202%20%3D%20Enigszins%20onduidelijk%203%20%3D%20Neutraal%204%20%3D%20Enigszins%20duidelijk%205%20%3D%20Zeer%20duidelijk%5CnVolledigheid%3A%201%20%3D%20Zeer%20onvolledig%202%20%3D%20Enigszins%20onvolledig%203%20%3D%20Neutraal%204%20%3D%20Enigszins%20volledig%205%20%3D%20Zeer%20volledig%5CnObjectiviteit%3A%201%20%3D%20Volledig%20subjectief%202%20%3D%20Grotendeels%20subjectief%203%20%3D%20Neutraal%204%20%3D%20Grotendeels%20objectief%205%20%3D%20Volledig%20objectief%5CnBelangrijkheid%3A%201%20%3D%20Helemaal%20niet%20significant%202%20%3D%20Enigszins%20significant%203%20%3D%20Matig%20significant%204%20%3D%20Zeer%20significant%205%20%3D%20Uiterst%20significant%5CnGeschiktheid%3A%201%20%3D%20Zeer%20ongeschikt%202%20%3D%20Enigszins%20ongeschikt%203%20%3D%20Neutraal%204%20%3D%20Enigszins%20geschikt%205%20%3D%20Zeer%20geschikt%5Cn%5CnExample!%20-%20Stick%20to%20this%20formatting%20exactly!%5Cn%23Relevantie%3A%20POINTS%20FOR%20Relevantie%5Cn%23Relevantieinfo%3A%20EXPLAIN%20WHY%20POINTS%5Cn%23Nauwkeurigheid%3A%20POINTS%20FOR%20Nauwkeurigheid%5Cn%23Nauwkeurigheidinfo%3A%20EXPLAIN%20WHY%20POINTS%5Cn%23Duidelijkheid%3A%20POINTS%20FOR%20Duidelijkheid%5Cn%23Duidelijkheidinfo%3A%20EXPLAIN%20WHY%20POINTS%5Cn%23Volledigheid%3A%20POINTS%20FOR%20Volledigheid%5Cn%23Volledigheidinfo%3A%20EXPLAIN%20WHY%20POINTS%5Cn%23Objectiviteit%3A%20POINTS%20FOR%20Objectiviteit%5Cn%23Objectiviteitinfo%3A%20EXPLAIN%20WHY%20POINTS%5Cn%23Belangrijkheid%3A%20POINTS%20FOR%20Belangrijkheid%5Cn%23Belangrijkheidinfo%3A%20EXPLAIN%20WHY%20POINTS%5Cn%23Geschiktheid%3A%20POINTS%20FOR%20Geschiktheid%5Cn%23Geschiktheidinfo%3A%20EXPLAIN%20WHY%20POINTS%5CnThe%20user%20wants%20you%20to%20rate%20the%20all%20the%20new%20message%20below%20and%20use%20the%20format%20for%20the%20replay.replay%20in%20the%20input%20message%20languageuse%22%2C%22answer%22%3A%22I%20apologize%2C%20but%20I%20am%20not%20quite%20sure%20what%20%5C%22new%20message%5C%22%20you%20are%20referring%20to%20for%20me%20to%20rate.%20Could%20you%20please%20provide%20me%20with%20more%20information%20so%20that%20I%20can%20accurately%20respond%20to%20your%20request%3F%20Thank%20you.%22%7D%5D&chatId=2f917965-2e6f-427d-822c-a4dba2d744d9',
        'maxTimeout': 600000,
    }


    response = requests.post('http://192.168.2.151:8191/v1', headers=headers, json=json_data).json()
    response = str(response['solution']['response']).replace('<html><head><meta name="color-scheme" content="light dark"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">', '').split("\n")
    # print(data)
    output = ""
    for line in response:
        if line:
            
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key == "data":
                if value == "I'm Mr. Meeseeks. Look at me.":
                    break
                data = json.loads(value)
                if "youChatToken" in data:
                    output += data["youChatToken"]

        out = str(re.sub(r"\[.+?\]\(.+?\)", "", output)).lstrip()
        data = str(out)
   
    

    for line in data.split('\n'):
        if line.startswith('#Relevantie:'):
            Relevantie = line.replace('#Relevantie: ', '').strip()
            print(Relevantie)
        elif line.startswith('#Relevantieinfo:'):
            Relevantieinfo = line.replace('#Relevantieinfo: ', '').strip()
            print(Relevantieinfo)
        elif line.startswith('#Nauwkeurigheid:'):
            Nauwkeurigheid = line.replace('#Nauwkeurigheid: ', '').strip()
            print(Nauwkeurigheid)
        elif line.startswith('#Nauwkeurigheidinfo:'):
            Nauwkeurigheidinfo = line.replace('#Nauwkeurigheidinfo: ', '').strip()
            print(Nauwkeurigheidinfo)
        elif line.startswith('#Duidelijkheid:'):
            Duidelijkheid = line.replace('#Duidelijkheid: ', '').strip()
            print(Duidelijkheid)
        elif line.startswith('#Duidelijkheidinfo:'):
            Duidelijkheidinfo = line.replace('#Duidelijkheidinfo: ', '').strip()
            print(Duidelijkheidinfo)
        elif line.startswith('#Volledigheid:'):
            Volledigheid = line.replace('#Volledigheid: ', '').strip()
            print(Volledigheid)
        elif line.startswith('#Volledigheidinfo:'):
            Volledigheidinfo = line.replace('#Volledigheidinfo: ', '').strip()
            print(Volledigheidinfo)
        elif line.startswith('#Objectiviteit:'):
            Objectiviteit = line.replace('#Objectiviteit: ', '').strip()
            print(Objectiviteit)
        elif line.startswith('#Objectiviteitinfo:'):
            Objectiviteitinfo = line.replace('#Objectiviteitinfo: ', '').strip()
            print(Objectiviteitinfo)
        elif line.startswith('#Belangrijkheid:'):
            Belangrijkheid = line.replace('#Belangrijkheid: ', '').strip()
            print(Belangrijkheid)
        elif line.startswith('#Belangrijkheidinfo:'):
            Belangrijkheidinfo = line.replace('#Belangrijkheidinfo: ', '').strip()
            print(Belangrijkheidinfo)
        elif line.startswith('#Geschiktheid:'):
            Geschiktheid = line.replace('#Geschiktheid: ', '').strip()
            print(Geschiktheid)
        elif line.startswith('#Geschiktheidinfo:'):
            Geschiktheidinfo = line.replace('#Geschiktheidinfo: ', '').strip()
            print(Geschiktheidinfo)



        # elif line.startswith('#Content:'):
        #     content = line.replace('#Content:', '').strip()
        #     next_line = f.readline().strip()
        #     while next_line and not next_line.startswith('#'):
        #         content += '\n' + next_line
        #         next_line = f.readline().strip()
        #     continue
        
        
    
    
    return render_template("index.html", 
                       Relevantie=int(Relevantie),
                       Relevantieinfo=Relevantieinfo,
                       Nauwkeurigheid=int(Nauwkeurigheid),
                       Nauwkeurigheidinfo=Nauwkeurigheidinfo,
                       Duidelijkheid=int(Duidelijkheid),
                       Duidelijkheidinfo=Duidelijkheidinfo,
                       Volledigheid=int(Volledigheid),
                       Volledigheidinfo=Volledigheidinfo,
                       Objectiviteit=int(Objectiviteit),
                       Objectiviteitinfo=Objectiviteitinfo,
                       Belangrijkheid=int(Belangrijkheid),
                       Belangrijkheidinfo=Belangrijkheidinfo,
                       Geschiktheid=int(Geschiktheid),
                       Geschiktheidinfo=Geschiktheidinfo)


if __name__ == '__main__':
    app.run()
