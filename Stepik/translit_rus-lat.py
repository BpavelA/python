#  преобразование типа: Фамилия Имя Отчество - > familia.i.o 

abc = {
        'а': 'a',  'б': 'b',  'в': 'v',  'г': 'g',  'д': 'd',  'е': 'e',  'ё': 'e',
        'ж': 'zh',  'з': 'z',  'и': 'i',  'й': 'y',  'к': 'k',  'л': 'l',  'м': 'm',
        'н': 'n',  'о': 'o',  'п': 'p', 'р': 'r',  'с': 's',  'т': 't',  'у': 'u',
        'ф': 'f',  'х': 'kh',  'ц': 'ts',  'ч': 'ch',  'ш': 'sh',  'щ': 'sch',  'ъ': '',
        'ь': '',  'ы': 'y',  'э': 'e',  'ю': 'yu',  'я': 'ya', '.': '.'}

names = []
for name in input().split(','):
    names.append(f'{name.split()[0].lower()}.{name.split()[1][0].lower()}')

for name in names:
    translit = ''
    for letter in name:
        translit += abc[letter]
    print(f'INSERT INTO oc_accounts (email, user_id, lower_user_id, display_name, quota, backend, home, state) VALUES ("borodenkov@list.ru", "{translit}", "{translit}", "{translit}", "100 MB", "OC\\\\User\\\\Database", "/mnt/data/files/{translit}", 1);')
    print(f'INSERT INTO oc_users (uid) VALUES ("{translit}");')
    print(f'INSERT INTO oc_group_user (gid, uid) VALUES ("ИК_58", "{translit}");')