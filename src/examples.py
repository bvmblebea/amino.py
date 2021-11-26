# login
import aminoboi
client = aminoboi.Client()
client.auth(email="email", password="password")

# login with input
import aminoboi
client = aminoboi.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.auth(email=email, password=password)

