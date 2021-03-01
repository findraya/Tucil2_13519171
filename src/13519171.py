# NIM   : 13519171
# Nama  : Fauzan Yubairi Indrayadi
# Topik : Tugas Kecil 2

# Kelas Kuliah untuk menyimpan nama matkul, semester, jumlah prerequisite, next matkul, dan list prerequisitenya
class Kuliah:
    def __init__(self, matkul=None):
        self.matkul = matkul
        self.sem = None
        self.preqcount = 0
        self.next = None
        self.preq = None

# Kelas Node untuk menyimpan list prerequisite
class Node:
    def __init__(self, matkul=None):
        self.matkul = matkul
        self.next = None

# Kelas LinkedList untuk menyimpan seluruh detail kuliah yang ada dalam bentuk linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    # Fungsi untuk menambahkan sebuah node ke linked list
    def add(self, kuliah=None):
        if self.head != None:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = kuliah
        else:
            self.head = kuliah
        self.count += 1

    # Fungsi untuk print semua matkul beserta prerequisitenya di awal sebelum sort
    def print(self):
        i = 1
        p = self.head
        print("Terdapat " + str(self.count) + " matkul")
        while p != None:
            print("Matkul " + str(i) + " = " + p.matkul)
            if p.preqcount != 0:
                print("Preq dari node " + str(i) + " ada sebanyak " + str(p.preqcount) + ":")
                pr = p.preq
                while pr != None:
                    print(pr.matkul)
                    pr = pr.next
            else:
                print("Matkul ini tidak memiliki preq")
            p = p.next
            i += 1

    # Fungsi untuk print semua matkul pada tiap semester
    def printSemester(self):
        for i in range(8):
            p = self.head
            count = 0
            while p != None:
                if p.sem == (i+1):
                    if count == 0:
                        print("\nSemester " + str(i+1) + " : " + p.matkul, end='')
                        count += 1
                    else:
                        print(", " + p.matkul, end='')
                p = p.next

def topsort(listkul):
    tsort = LinkedList()
    sem = 1
    while tsort.count != listkul.count:
        a = listkul.head
        arrCek = []
        # Memasukkan matkul yang tidak memiliki preq (dengan mengecek preqcount) ke linked list baru
        while a != None:
            if a.preqcount == 0:
                arrCek.append(a.matkul)
                s = Kuliah(a.matkul)
                s.sem = sem
                s.next = None
                tsort.add(s)
                a.preqcount -= 1
            a = a.next
        
        # Mengurangi preqcount dari listkuliah yang memiliki matkul dari preq = arrCek
        b = listkul.head
        while b != None:
            if b.preq != None:
                pre = b.preq
                while pre != None:
                    for i in range(len(arrCek)):
                        if pre.matkul == arrCek[i]:
                            b.preqcount -= 1
                    pre = pre.next
                pr.next = p
            b = b.next
        sem += 1
    return tsort # Mengembalikan linked list yg telah di-sort

# Membaca input dari file text
txt = input('Ketik nama file : ')
f = open('test/' + txt, "r")
lines = f.read()
l = lines.split('.\n')
f.close()

# Membuat list semua matkul yang ada
listkul = LinkedList()
for listkel in l:
    a = listkel.split(', ')
    k = Kuliah(a[0].replace('.',''))
    k.preqcount = len(a)-1
    # menambahkan preq pada suatu matkul
    for i in range(1, len(a)):
        p = Node(a[i].replace('.',''))
        if k.preq != None:
            pr = k.preq
            while pr.next != None:
                pr = pr.next
            pr.next = p
        else:
            k.preq = p
    # memasukkan k ke dalam linked list
    listkul.add(k)
    
listkul = topsort(listkul)
listkul.printSemester()
