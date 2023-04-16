import requests

message= "Python is a high-level programming language that has rapidly become one of the most popular languages in the world. Its simple syntax, powerful capabilities, and extensive libraries make it a great language to learn for beginners and an essential tool for experienced developers. In this blog post, we will explore some of the key features and benefits of Python. One of the defining features of Python is its simplicity. Python code is easy to read and write, thanks to its simple syntax and consistent formatting. As a result, developers can quickly write programs that are easy to understand and maintain, without getting bogged down in the details of the language. This ease of use also makes Python an ideal language for beginners who are just starting to develop their programming skills."

input_format = f"""
Your goal is to rate and give featback on research made by kids for school. You only answer with the json text. Follow the structure of the example. Always use the points sysem.
Folow there rules/info:
- You do all the rating text for the user.
- You can award points between 1 - 10 using the points system.
- Always reply in the inputted text language.
- Never reply with plain text, always use the json example below.
- dont use newlines
- never format the json other than shown below
points system:
1 = very low
10 = very high
1 = bad
10 = good

rate the text based on:
Originaliteit: het onderzoek moet origineel zijn en een nieuw perspectief bieden op het onderwerp. max points: 10
Diepgang: het onderzoek moet voldoende diepgang hebben om de onderzoeksvragen te beantwoorden. max points: 10
Inzichtelijkheid: het onderzoek moet begrijpelijk zijn voor de doelgroep en de resultaten moeten duidelijk worden gepresenteerd. max points: 10



Example! - Stick to this formatting exactly!"""+ "\n{'Originaliteit': 'POINTS FOR Originaliteit', 'Diepgang': 'POINTS FOR Diepgang', 'Inzichtelijkheid': 'POINTS FOR Inzichtelijkheid', 'Originaliteit': 'explain Originaliteit here', 'Diepgang': 'explain Diepgang here', 'Inzichtelijkheid': 'explain Inzichtelijkheid here'}" + f"The user wants you to review/rate this text: {message}"
    
    
url = f"https://api.betterapi.net/youdotcom/chat?message={input_format}&key=site"
json = requests.get(url).json() # load json form api
print(json["message"]) # print message response