kata_int = ["apel"], "jeruk", "mangga", "pisang", "anggur", "durian"
output = []
for kata in kata_int:
    if len(kata) >= 5:
        output.append(kata)
output.sort()
print("output : ", output)
