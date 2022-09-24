# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Пока абвЗемля Земля еще вертится, пока еще ярок абв свет, Господи, дай же ты каждому, чего у него абвгдежз нет'

def del_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = del_words(text)
print(text)