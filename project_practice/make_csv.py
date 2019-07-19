students = {
    'asdf1' : {
        '순번' : '01',
        '이름' : '김성훈'
    },
    'asdf2' : {
        '순번' : '02',
        '이름' : '김은정'
    }
}

# with open('a.csv', 'w', encoding='utf-8') as f:
#     f.wirte('nember, name\n')
#     for number, name in student.items():
#         f.write('{number}, {name}\n')
import csv
with open('c.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['순번', '이름']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in students.values():
        csv_writer.writerow(item)