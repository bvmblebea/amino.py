# amino.py
Library for https://aminoapps.com using https://service.narvii.com/api/v1

### Example
```python3
# login with input
import amino
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.auth(email=email, password=password)
```
