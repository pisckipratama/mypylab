# di python list sama seperti di bahasa pemrograman lain yang berupa array

books_list = ["atomic habits", "deep work", "the power of habit"]

for book in books_list:
    print(book)

for i in range(0, len(books_list)):
    print(books_list[i])

books_list2 = [1, True, 'Oke', [1, 'A']]

# menambahkan nilai
books_list2.append("okee")
print(books_list2)

# menghapus nilai dengan pop
books_list2.pop(-2)  # dimulai dari belakang dimulai dengan -1
books_list2.pop(0)  # dimulai dari depan dimulai dengan 0
print(books_list2)

# menghapus elemen dengan del
del books_list2[1]
print(books_list2)

# comprehension list
books_list3 = ["Learn Python", "Learn Kubernetes", "Learn Docker", "Learn AWS"]
del books_list3[0:2]  # menghapus semua, [start:end]
print(books_list3)

books_list4 = ["Learn Python", "Learn Kubernetes", "Learn Docker", "Learn AWS", "Learn Terraform"]
del books_list4[0::2]  # dengan step [start:end:step]
print(books_list4)
