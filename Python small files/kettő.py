import random

while True:
    try:
        x = int(input('Adj meg egy számot a nehézség beálítására! '))
    except Exception:
        print('Nem helyes számot adtál meg!')
        continue
    if x <= 0:
        print('Nem adhatsz meg minusz számot')
        continue
    else:
        break


random_number = random.randint(0, int(x))

print(random_number)

#
# while True:
#     try:
#         x = int(input('Fasz: '))
#     except Exception:
#         print('Nem számot adtál meg!')
#         continue
#     if x <= 0:
#         print('Fo')
#         continue
#     else:
#         print('done')
#         break
