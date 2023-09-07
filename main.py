import openllm
client = openllm.client.HTTPClient('https://localhost:3000')

while True:
    question = input('$ ')
    response = client.query(question)
    print(response)

