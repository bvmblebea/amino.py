# amino.py
Mobile-API for amino social network

## Example
```python3
# login with input
import amino
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.auth(email=email, password=password)
```
