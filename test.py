
import jwt

data = {
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}

# 加密 py3加密后是字节型数据
encoded = jwt.encode(data, 'secret', algorithm='HS256')
print(encoded.encode())
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.
# eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.
# DzMJlzRbt6kdh1Kbbqv8SA8QsddwfSoM1bqw41tQY2k

encoded='eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxIiwiZXhwIjoxNjQyNDkzMTg3LCJ1c2VyIjp7ImlkIjoxLCJhY2NvdW50IjoiYWRtaW4iLCJuYW1lIjoiYWRtaW4iLCJhdmF0YXIiOiJodHRwczovL2tleXRlc3Qub3NzLWNuLXpoYW5namlha291LmFsaXl1bmNzLmNvbS91cGxvYWQvcHQvcGljX3VzZXJfcGhvdG8vMjAyMC8wNC8xNy9mNjM5MjczYmY1Nzg0OTc3OWZhZDEyNmMzYTQ1OTUwY182MjEtNTY4LmpwZyIsImNsaWVudFNvdXJjZSI6MSwicGVybWlzc2lvbnMiOm51bGwsInJvbGVJZHMiOlsxXSwiYXBwSWQiOm51bGwsInN0b3JlSWQiOm51bGwsInVzZXJUeXBlSWQiOm51bGwsInN1cHBsaWVySWQiOm51bGwsInhjeE9wZW5pZCI6bnVsbCwid3hPcGVuSWQiOm51bGwsInBsYXRmb3JtIjoxLCJwbGFjZUlkIjpudWxsLCJwcm9kdWN0IjpudWxsfSwiaWF0IjoxNjQyNDA2Nzg3fQ.ixzIJq50FvEjrB4JA3BjKvSz3wUctQkJA3rYZ4CTFgSAQzZxOo3QNwZTv2IyiBMaIWCBA11HDaYNK0fjmqglTg'
print(jwt.decode(encoded, 'secret', algorithms=['HS512']))
# {'sub': '1234567890', 'name': 'John Doe', 'iat': 1516239022}