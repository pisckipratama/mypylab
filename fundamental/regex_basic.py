import re

string = "'I AM NOT YELLING', she said. Though we knew it to not be true."

new = re.sub('[A-Z]', '', string)  # menghilangkan huruf kapital
print(new)

new = re.sub('[a-z]', '', string)  # menghilangkan huruf kecil
print(new)

new = re.sub('[.,\']', '', string)  # menghilangkan simbol titik dan koma
print(new)

new = re.sub('[.,\'a-zA-Z]', '', string)  # Menghilangkan simbol titik koma dan huruf kecil maupun besar
print(new, '<- ini new')

new = re.sub('[.,\'A-Z+" "]', '', string)  # meghilangkan simbol titik koma dan huruf besar beserta spasi
print(new)

string = string + "6 298 - 345"
new = re.sub('[^0-9]', '', string)  # menghilangkan semua huruf dan spasi juga simbol
print(new)

new = re.sub('[^., \'a-z]', '', string)
print(new)