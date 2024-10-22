def second_index(text, some_str):
  first_index = text.find(some_str) #знаходимо перший індекс появи підрядка
  if first_index == -1: #якщо підрядок не знайдений, то функція повертає none
      return None
  second_index = text.find(some_str, first_index + len(some_str)) #шукаємо друге входження вєе після прешого знайденого підрядка
  if second_index != -1: #якщо входження знайдено, то функція повертає його значення
      return second_index
  else: #якщо ні, то none
      return None

print(second_index("sims", "s"))
print(second_index("find the river", "e"))
print(second_index("hi", "h"))
print(second_index("Hello, hello", "lo"))