# Parse a URL query string to get query parameters in Python

from urllib.parse import urlparse, parse_qs

url = 'https://bobbyhadz.com/store?page=10&limit=15&price=ASC'
parse_result = urlparse(url)

# 👇️ "page=10&limit=15&price=ASC"
print(parse_result)

dict_result = parse_qs(parse_result.query)

# 👇️ {'page': ['10'], 'limit': ['15'], 'price': ['ASC']}
print(dict_result)

print(dict_result['page'][0])  # 👉️ '10'
print(dict_result['price'][0])  # 👉️ 'ASC'