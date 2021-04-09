n = int(input("Masukkan jumlah data: "))
print("Jumlah data: ", n)

data = []
jumlah = 0
for i in range(0,n):
    nilai = int(input("Masukkan nilai ke-%d: " % (i+1)))
    data.append(nilai)
    jumlah += data[i]

    rata_rata = jumlah/n
print(float(rata_rata))
