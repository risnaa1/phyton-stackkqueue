#Latihan 1

class BookStack :
    def __init__(self) :
        self.stack = []
    
    def add_book (self, book_name, author_name) :
        self.stack.append((book_name, author_name))

    def remove_book(self) :
        if not self.is_empty() :
            self.stack.pop()
    
    def top_book(self) :
        if not self.is_empty() :
            return self.stack[-1]
        else :
            return None
    
    def is_empty(self) :
        return len (self.stack) == 0
    
#Membuat Tumpukan Buku
stack = BookStack()

while True :
    print("\nMenu")
    print("1. Tambah Buku")
    print("2. Hapus Buku Terakhir")
    print("3. Tampilkan Buku Terakhir")
    print("4. Keluar")

    choice = input ("Pilih Menu (1/2/3/4/) : ")

    if choice == '1' :
        book_name = input ("Masukkan nama buku : ")
        author_name = input ("masukkan nama pengarang : ")
        stack.add_book(book_name, author_name)
        print ("Buku berhasil ditambahkan kedalam tumpukan")
    elif choice == '2' :
        if stack.is_empty() :
            print("Tumpukan buku kosong.")
        else :
            stack.remove_book()
            print ("Buku terakhir dihapus dari tumpukan.")
    elif choice == '3' :
        top_book = stack.top_book()
        if top_book is None :
            print ("Tumpukan buku kosong.")
        else :
            book_name, author_name = top_book
            print ("Buku teratas")
            print ("Nama buku : ", book_name)
            print ("Pengarang : ", author_name)
    elif choice == '4' :
        print ("Program selesai.")
        break
    else :
        print ("Pilihan tidak valid. Silahkan pilih menu yang tersedia.")