# Lambda Function
def f_kuadrat(angka):
    return angka**2


# print(f"hasil fungsi kuadrat 3 = {f_kuadrat(3)}")

# Dengan Lambda
kuadrat = lambda angka: angka**2
# print(f"hasil lambda kuadrat 4 = {kuadrat(4)}")

pangkat = lambda num, pow: num**pow
# print(f"hasil lambda 2 pangkat 5 = {pangkat(2,5)}")


# Kegunaan
# Sorting untuk list biasa
data_list = ['Otong', "Ucup", "Z", "Dudung", 'Abu']
data_list.sort()
print(f"sorted list = {data_list}")

# Sorting dia pakai panjang
data_list.sort(key=len)
print(f"sorted list by panjang = {data_list}")