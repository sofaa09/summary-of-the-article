import requests

user_input = input('enter article URL: ')
language = input('write the language in which you would like the summary of the article: ')
user_input+=f'write a summary of this article. write me what exactly it is about. write this in {language} language.'

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": user_input}],
    "temperature": 0.7
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "code",
}

response = requests.post('https://api.openai.com/v1/chat/completions',
                         headers=headers, json=data)

response_json = response.json()

print(response_json['choices'][0]['message']['content'])
