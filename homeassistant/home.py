import requests

url = "https://localhost:8123/api/error/all"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI4YjRiZWI2ZTYzMWU0N2M5OWRkNWFiZGNhNDcyZGMzZiIsImlhdCI6MTY4NDMzMjI2NiwiZXhwIjoxOTk5NjkyMjY2fQ.VJJwmxcDYQEKdAs54Y3OgOIn-BG2ENlKUPN1Tkq2Los",
}
response = requests.request("GET", url, headers=headers)

print(response.text)