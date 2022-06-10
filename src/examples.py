# login
import amino
client = amino.Client()
client.login(email="", password="")

# login with input
import amino
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)

