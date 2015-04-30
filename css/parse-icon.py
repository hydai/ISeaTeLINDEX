
f = open('icon.txt')
s = f.read()
s = s.split('\n')

for ss in s:
    ss = ss.split(':')[0]
    ss = ss[1:]
    print '<span class="fa '+ss+'"></span>'
