# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# def Compression(text): 
#     compressdata = ''
#     i = 0
#     while i < len(text):
#         count = 1
#         while i + 1 < len(text) and text[i] == text[i + 1]:
#             count += 1
#             i += 1
#         compressdata += str(count) + text[i]
#         i += 1
#     return compressdata


# def Recovery(text): 
#     datarecovery = ''
#     i = 0
#     while i < len(text):
#         datarecovery += str(text[i+1]) * int(text[i])
#         i+=2
#     return datarecovery


# with open('Text1.txt', 'r') as t1:
#     t1 = t1.read()

# with open('Text2.txt', 'w+') as t2:
#     t2.write(Compression(t1))
#     t2.seek(0) 
#     t2 = t2.read()

# with open('Text3.txt', 'w') as t3:
#     t3.write(Recovery(t2))

def rle_encode(data): 
    encoding = '' 
    prev_char = '' 
    count = 1 
    if not data: return '' 
    for char in data: 
        if char != prev_char: 
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            count += 1 
    else: 
        encoding += str(count) + prev_char 
        return encoding

def rle_decode(data): 
    decode = '' 
    count = '' 
    for char in data: 
        if char.isdigit():
            count += char 
        else: 
            decode += char * int(count) 
            count = '' 
    return decode

with open('Text1.txt', 'r') as t1:
    t1 = t1.read()

with open('Text2.txt', 'w+') as t2:
    t2.write(rle_encode(t1))
    t2.seek(0) 
    t2 = t2.read()

with open('Text3.txt', 'w') as t3:
    t3.write(rle_decode(t2))