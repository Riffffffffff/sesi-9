list1 = ["apel", "jeruk", "mangga"]
list2 = ["apel", "anggur", "nanas"]

buah = list1.copy()
buah.extend(list2)
saring = set(buah)
buahDewi = sorted(saring)
print("Buah Dewi Sekarang = ", buahDewi)
