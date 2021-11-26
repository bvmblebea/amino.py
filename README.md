# aminoboi
Library for https://aminoapps.com using service.narvii.com/api/v1

### Example
```python3
# login with input
import aminoboi
client = aminoboi.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.auth(email=email, password=password)
```
