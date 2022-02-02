
f = open('user.csv')
for u in f.readlines():
    name, id = u.strip().split(',')
    print(f'insert into student (studentName, pwd) values("{id}","888888");');