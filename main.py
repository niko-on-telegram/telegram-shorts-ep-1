import requests

updates_response = requests.get("https://api.telegram.org/bot6117837715:AAEbBH1KW9vnfqHgXxb6e4E1D5aYQBiqgKA/getUpdates")
print(updates_response.json())

sendmessage_response = requests.get("https://api.telegram.org/bot6117837715:AAEbBH1KW9vnfqHgXxb6e4E1D5aYQBiqgKA/sendMessage?chat_id=5626154366&text=Hello")
