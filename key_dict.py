# задача заменить ключи secret и last_name на новые в списке 
user = {
    "name": "Alex",
    "password": "secret_password_123",
    "last_name": "Smith",
    "age": 30,
}

# Переименовываем password в secret
user["secret"] = user.pop("password")

# Переименовываем last_name в surname
user["surname"] = user.pop("last_name")

print(user)
