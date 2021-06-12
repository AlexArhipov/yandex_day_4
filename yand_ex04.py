def ex01():
    len = int(raw_input())
    MyDictinary = {}
    st = 10
    for i in range(len):
        st = raw_input().split(' ')
        MyDictinary[st[1]] = st[0]
        MyDictinary[st[0]] = st[1]
    find = raw_input()
    print MyDictinary.get(find)

def ex02():
    f = open("input.txt", "r")
    data = f.read().split()
    f.close()
    MyDictinary = {}
    for i in data:
        if i not in MyDictinary:
            MyDictinary[i] = 0
            print 0,
        else:
            MyDictinary[i] += 1
            print MyDictinary[i],
def ex03():
    f = open("input.txt", "r")
    data = f.read().split()
    f.close()
    MyDictinary = {}
    Sp_max = []
    maxs = 0
    for i in data:
        if i not in MyDictinary:
            MyDictinary[i] = -1
        MyDictinary[i] += 1
        if MyDictinary[i] >= maxs:
            maxs = MyDictinary[i]
    for i in MyDictinary:
        if MyDictinary[i] == maxs:
            Sp_max.append(i)
    print min(Sp_max)

def ex04():
    f = open("input.txt", "r")
    data = f.readline()
    sl = int(data) + 1
    kyes = {}
    data = f.readline().split()
    for i in range(1, sl):
        kyes[i] = int(data[i - 1])
    ex = int(f.readline())
    data = list(f.readline().split())
    f.close()
    for i in data:
        if int(i) in kyes:
            kyes[int(i)] -= 1
    for i in range(1, sl):
        if int(kyes[i]) >= 0:
            print "NO"
        else:
            print "YES"

def ex05():
    MyDictinary = {}
    len = int(raw_input())
    for i in range(len):
        data = raw_input().split()
        if data[0] not in MyDictinary:
            MyDictinary[data[0]] = data[1]
        elif int(MyDictinary[data[0]]) < int(data[1]):
            MyDictinary[data[0]] = data[1]
    sums = 0
    for i in MyDictinary:
        sums += int(MyDictinary[i])
    print sums

def ex06():
    f = open("input.txt", "r")
    MyDictinary = {}
    while True:
        data = f.readline().split()
        if not data:
            break
        if data[0] not in MyDictinary:
            MyDictinary[data[0]] = {data[1]: int(data[2])}
        elif data[1] not in MyDictinary[data[0]]:
            MyDictinary[data[0]][data[1]] = int(data[2])
        else:
            MyDictinary[data[0]][data[1]] += int(data[2])
    for i in sorted(MyDictinary.keys()):
        print i + ":"
        for j in sorted(MyDictinary[i].keys()):
            print j, MyDictinary[i][j]
    f.close()

def ex07():
    f = open("input.txt", "r")
    MyDictinary = {}
    while True:
        data = f.readline().split()
        if not data:
            break
        if data[0] == "DEPOSIT":
            if data[1] not in MyDictinary:
                MyDictinary[data[1]] = int(0)
            MyDictinary[data[1]] += int(data[2])
        elif data[0] == "WITHDRAW":
            if data[1] not in MyDictinary:
                MyDictinary[data[1]] = int(0)
            MyDictinary[data[1]] -= int(data[2])
        elif data[0] == "BALANCE":
            if data[1] not in MyDictinary:
                print "ERROR"
            else:
                print MyDictinary[data[1]]
        elif data[0] == "TRANSFER":
            if data[1] not in MyDictinary:
                MyDictinary[data[1]] = int(0)
            if data[2] not in MyDictinary:
                MyDictinary[data[2]] = int(0)
            MyDictinary[data[1]] -= int(data[3])
            MyDictinary[data[2]] += int(data[3])
        elif data[0] == "INCOME":
            for i in MyDictinary:
                if MyDictinary[i] > 0:
                    MyDictinary[i] += int((MyDictinary[i] // 100 + 0.01 * (MyDictinary[i] % 100)) * int(data[1]))
    f.close()

def ex08():
    f = open("input.txt", "r")
    data = f.readline()
    sl = int(data)
    word = {}
    for i in range(sl):
        data = f.readline().replace('\n', '')
        if data.lower() not in word:
            word[data.lower()] = {data: 1}
        elif data not in word[data.lower()]:
            word[data.lower()][data] = 1
    data = list(f.readline().split())
    osh = len(data)
    for i in data:
        if (sum([c.isupper() for c in i])) == 1:
            if i.lower() in word:
                if i in word[i.lower()]:
                    osh -= 1
            else:
                osh -= 1
    print osh
    f.close()
