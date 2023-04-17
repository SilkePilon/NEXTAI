from pychatgpt import Chat, Options

options = Options()

# [New] Pass Moderation. https://github.com/rawandahmad698/PyChatGPT/discussions/103
# options.pass_moderation = False

# [New] Enable, Disable logs
options.log = True

# Track conversation
options.track = True 


# Optionally, you can pass a file path to save the conversation
# They're created if they don't exist

# options.chat_log = "chat_log.txt"
# options.id_log = "id_log.txt"

# Create a Chat object
chat = Chat(email="silke2007minecraft@gmail.com", password="Landrover@01", options=options)
answer = chat.ask("How are you?")
print(answer)