import csv
ls = []

with open('Python/Contacts/contacts_for_import.txt', 'r', encoding='utf8') as i_file:
 res = i_file.readlines()
 for person in res:
  ls.append(person.split(','))
  
 a =  ' '
 b = ' '
 
 for c in ls:
  # entry = f'{c[1]},{c[2].strip()},{c[0]},,,,,,,,,,,,,,{c[5].strip()},,,,{c[3].strip()},,,{c[4].strip()}'
  with open('Python/Contacts/contacts_for_google.csv', 'a', encoding='utf-8') as o_file:
   
   file_writer = csv.writer(o_file, delimiter=',', lineterminator='\r')
   file_writer.writerow([c[1],c[2].strip(),c[0],' ', ' ',c[5].strip(),c[3].strip(),c[4].strip()])

