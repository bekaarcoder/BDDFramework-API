import requests

url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
file = {'file': open("C:\\Users\\shash\\Pictures\\user_img.png", 'rb')}

response = requests.post(url, files=file)
print(response.status_code)
print(response.json())
