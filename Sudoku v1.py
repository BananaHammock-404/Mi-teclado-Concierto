# Menggunakan Backtracking sbg ganti dari Naive karena lebih cepat dan lebih sedikit workloadnya.
# Cara Code ini bekerja:
    # 1.  Pilih kotak yang kosong ( dari atas kiri ke kanan).
    # 2.  Coba semua angka 1 - 9 .
    # 3.  Pilih angka yang sesuai dgn aturan Sudoku(Hanya satu di kolomom, baris, dan kotaknya)
    # 4.  Ulangi/ Repeat.
    # ^^^^^Naive^^^^^^^
    # 5.  Backtracking: Jika tidak ada solusi ketika memasukan angka pada kotak lainnya, maka 
    #     program akan Backtack ke kotak yang di isi sebelum itu dan ubah angka tersebut.


papan = [                       # papan sudoku yang akan kita gunakan sbg contoh. Program ini tidak bisa Generate random Sudoku boxes
    [0,2,0,0,7,5,6,9,3],
    [0,0,1,4,0,9,0,0,0],
    [0,9,7,0,0,0,0,0,0],
    [1,0,0,6,3,0,0,0,2],
    [0,0,6,9,0,2,8,0,0],
    [2,0,0,0,5,8,0,0,6],
    [9,0,0,0,0,0,3,6,0],
    [0,0,0,8,0,3,1,0,0],
    [8,3,2,5,6,0,0,4,0]
]


def print_papan(ppn):
    # x Adalah barisnya. Setiap 3 baris kita ingin membuat pembagi untuk bagian bawah dan atas dari 9 kotak sudoku
    for x in range(len(ppn)):               
        if x % 3 == 0 and x != 0:                   
            print("- - - - - - - - - - - - ")
            #print("________________________") 

        # y Adalah kolomnya. Setiap 3 kolom kita ingin membuat pembagi untuk bagian kanan dan kiri dari 9 kotak sudoku
        for y in range(len(ppn[0])):         
            if y % 3 == 0 and y != 0:
                print(" | ", end="")

            # Print angka-angka Sudokunya. 
            if y == 8:                       
                print(ppn[x][y])
            else:
                print(str(ppn[x][y]) + " ", end="")



def find_zero(ppn):                          # Mencari kotak yang kosong (atau di kasus ini '0')
    for x in range(len(ppn)):
        for y in range(len(ppn[0])):
            if ppn[x][y] == 0:
                return (x, y)  # baris, kolom

    return None



def valid_num(ppn, num, pos):               # Cek apakah angka yang akan di input valid apa tidak.
    # Check Baris
    for x in range(9):  # Loop hanya utk 9*9. Jika ingin lebih flexible ganti menjadi "for i in range(len(bo[0])):"   
        if ppn[pos[0]][x] == num and pos[1] != x:   # Guna dari "pos[1] != x" agar pd saat Backtracking kita ignore angkanya.
            return False

    # Check kolom
    for x in range(len(ppn)):
        if ppn[x][pos[1]] == num and pos[0] != x:
            return False

    # Check kotak           
    coor_x = pos[1] // 3        # Memakai 'Integer Division' utk menentukan function saat ini berada di kotak yang mana.
    coor_y = pos[0] // 3

    for x in range(coor_y*3, coor_y*3 + 3):
        for y in range(coor_x * 3, coor_x*3 + 3):
            if ppn[x][y] == num and (x, y) != pos:
                return False

    return True



def solve(ppn):

    # print(ppn)        # <<< UNCOMMENT THIS! jika ingin melihat step by step bagaimana kerja algoritma Bactracking.

    find = find_zero(ppn)           # Function yang mengindikasikan apakah kita sudah menyelesaikan seluruh papan sudoku atau belum (boolean).
    if not find:
        return True
    else:
        baris, kolom = find

    for x in range(1,10):       # '1-10' karena 10 disini tidak akan di proses
        if valid_num(ppn, x, (baris, kolom)):
            ppn[baris][kolom] = x   # Jika angka yang kita dapat dari function 'valid_num' valid, maka angka itu akan di input ke papan sudoku.

            if solve(ppn):      # Memanggil function ini jika tidak ada angka yang valid, maka program akan melakukan Backtracking
                return True

            ppn[baris][kolom] = 0  # Reset value sebelumnya dengan yang berbeda atau lebih tinggi.

    return False


print_papan(papan)
solve(papan)
print('_______________________')
print('_______________________')
print('')
print_papan(papan)