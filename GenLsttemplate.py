# переформатрировть список по пноввому шаблону
names = ['Alice', 'Bob', 'Marry', 'Joe', 'Hilary', 'Stevia', 'Dylan', 'Kevin', 'Darvin']
# Генератор списка для создания нового списка
formated_names = [f"My name is {name}" for name in names]
print(formated_names)
