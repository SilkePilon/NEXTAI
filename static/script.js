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
function change() {



    // Set the width of the progress bars based on the ratings

    const diepgangValue = '{{ diepgang }}';
    const diepgangElement = document.getElementById("Diepgang");
    diepgangElement.style.width = `${diepgangValue}0%`;

    const OriginaliteitValue = '{{ Originaliteit }}';
    const OriginaliteitElement = document.getElementById("Originaliteit");
    OriginaliteitElement.style.width = `${OriginaliteitValue}0%`;

    const InzichtelijkheidValue = '{{ Inzichtelijkheid }}';
    const InzichtelijkheidElement = document.getElementById("Inzichtelijkheid");
    InzichtelijkheidElement.style.width = `${InzichtelijkheidValue}0%`;



};
const button = document.getElementById('check');
// button.addEventListener('click', window.location.href = "/send");