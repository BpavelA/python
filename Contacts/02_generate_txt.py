# Инструкция: 
# 1) Скопировать информацию из Навигатора в файл 01_contacts_for_import.txt
# 2) Запустить скрипт
# 3) Скопировать текст из 01_contacts_for_import.txt в Книга для импорта.csv
# 4) Открыть файл в Notepad++. преобразовать в UTF-8 (при необходимости, проверить, внизу тип кодировки), сохранить и импортировать в Google


ls = []

header = 'First Name,Middle Name,Last Name,Phonetic First Name,Phonetic Middle Name,Phonetic Last Name,Name Prefix,Name Suffix,Nickname,File As,Organization Name,Organization Title,Organization Department,Birthday,Notes,Photo,Labels,E-mail 1 - Label,E-mail 1 - Value,Phone 1 - Label,Phone 1 - Value'

with open('Python/Contacts/01_contacts_for_import.txt', 'r', encoding='utf8') as i_file:
 res = i_file.readlines()
 for person in res:
  ls.append(person.split(','))

 with open('Python/Contacts/03_contacts_for_google.txt', 'w', encoding='utf8') as o_file:
   o_file.write(f'{header}\n')

 for c in ls:
  entry = f'{c[1]},{c[2].strip()},{c[0]},,,,,,,,,,,,{c[5].strip()},,,,{c[3].strip()},,{c[4].strip()}'
  with open('Python/Contacts/03_contacts_for_google.txt', 'a', encoding='utf8') as o_file:
   o_file.write(f'{entry.strip()}\n')

