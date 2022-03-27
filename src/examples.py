# login
import amino
client = amino.Client()
client.auth(email="", password="")

# login with input
import amino
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.auth(email=email, password=password)

