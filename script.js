document.addEventListener('DOMContentLoaded', function() {
    var modeSwitch = document.querySelector('.mode-switch');

    modeSwitch.addEventListener('click', function() {
        document.documentElement.classList.toggle('dark');
        modeSwitch.classList.toggle('active');
    });

    var listView = document.querySelector('.list-view');
    var gridView = document.querySelector('.grid-view');
    var projectsList = document.querySelector('.project-boxes');

    listView.addEventListener('click', function() {
        gridView.classList.remove('active');
        listView.classList.add('active');
        projectsList.classList.remove('jsGridView');
        projectsList.classList.add('jsListView');
    });

    gridView.addEventListener('click', function() {
        gridView.classList.add('active');
        listView.classList.remove('active');
        projectsList.classList.remove('jsListView');
        projectsList.classList.add('jsGridView');
    });

    document.querySelector('.messages-btn').addEventListener('click', function() {
        document.querySelector('.messages-section').classList.add('show');
    });

    document.querySelector('.messages-close').addEventListener('click', function() {
        document.querySelector('.messages-section').classList.remove('show');
    });
});

// Define the input format
function sendtoapi() {
    let message = `Python is a high-level programming language that has rapidly become one of the most popular languages in the world. Its simple syntax, powerful capabilities, and extensive libraries make it a great language to learn for beginners and an essential tool for experienced developers. In this blog post, we will explore some of the key features and benefits of Python.

    One of the defining features of Python is its simplicity. Python code is easy to read and write, thanks to its simple syntax and consistent formatting. As a result, developers can quickly write programs that are easy to understand and maintain, without getting bogged down in the details of the language. This ease of use also makes Python an ideal language for beginners who are just starting to develop their programming skills.`
    let inputFormat = `
      Your goal is to rate and give feedback on research. You only answer with the json text. Follow the structure of the example. Always use the points system.
      Follow these rules/info:
      - You do all the rating text for the user.
      - You can award points between 1 - 10 using the points system.
      - Always reply in the inputted text language.
      - YOU MUST STICK TO THE FORMAT.
      - DONT USE \n or make new lines
      Points system:
      1 = very low
      10 = very high
      1 = bad
      10 = good

      Rate the text based on:
      Originaliteit: het onderzoek moet origineel zijn en een nieuw perspectief bieden op het onderwerp. max points: 10
      Diepgang: het onderzoek moet voldoende diepgang hebben om de onderzoeksvragen te beantwoorden. max points: 10
      Inzichtelijkheid: het onderzoek moet begrijpelijk zijn voor de doelgroep en de resultaten moeten duidelijk worden gepresenteerd. max points: 10

      Example! Stick to this formatting exactly!
      ###Originaliteitpoints | POINTS FOR Originaliteit
      ###Originaliteitexplain | explain Originaliteit here
      ###Diepgangpoints | POINTS FOR Diepgang
      ###Diepgangexplain | explain Diepgang here
      ###Inzichtelijkheidpoints | POINTS FOR Inzichtelijkheid
      ###Inzichtelijkheidexplain | explain Inzichtelijkheid here
      
      The user wants you to review/rate this text: ` + message;

    // Send the request to the API
    let url = `https://api.betterapi.net/youdotcom/chat?message=${encodeURIComponent(inputFormat)}&key=site`;
    fetch(url)
        .then(response => response.text())
        .then(json => {


            // Set the width of the progress bars based on the ratings

            const diepgangValue = json.split("###Diepgangpoints");
            const diepgang = Array.from(diepgangValue)[0];
            const diepgangElement = document.getElementById("Diepgang");
            diepgangElement.style.width = `${diepgang}0%`;

            const OriginaliteitValue = json.split('Originaliteitpoints | ');
            const Originaliteit = Array.from(OriginaliteitValue)[0];
            const OriginaliteitElement = document.getElementById("Originaliteit");
            OriginaliteitElement.style.width = `${Originaliteit}0%`;

            const InzichtelijkheidValue = json.split('###Inzichtelijkheidpoints');
            const Inzichtelijkheid = Array.from(InzichtelijkheidValue)[0];
            const InzichtelijkheidElement = document.getElementById("Inzichtelijkheid");
            InzichtelijkheidElement.style.width = `${Inzichtelijkheid}0%`;

            console.log(diepgang)
            console.log(Originaliteit)
            console.log(Inzichtelijkheid)

        });
};
const button = document.getElementById('check');
button.addEventListener('click', sendtoapi);