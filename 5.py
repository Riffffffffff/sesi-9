arr = [105, 20, 8, 150, 30, 5, 200]
hasil = []
for n in arr:
    if 10 <= n <= 100:
        hasil.append(n)
    hasil.sort()
    print ("outpur : ", hasil)