import openllm
client = openllm.client.HTTPClient('https://localhost:3000')

# def question():
#     question = input('$ ')
#     response = client.query(question)
#     print(response)
# while True:
#     question()

response = client.query('Hello, tell me a joke')
print(response)