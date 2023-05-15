"""**kwargs"""

# def fungsi(nama, tinggi, berat):
#     print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
# fungsi("ucup", 183, 79)

# def fungsi(**kwargs):
#     print(kwargs)
# fungsi("ucup", 183, 79)
# fungsi(nama="ucup", tinggi=183, berat=79)


# def fungsi(**kwargs):
#     nama = kwargs["nama"]
#     tinggi = kwargs["tinggi"]
#     berat = kwargs["berat"]
#     print(f"{nama} punya tinggi {tinggi} berat {berat}")
# fungsi(nama="ucup", tinggi=183, berat=79)


# Studi Kasus
def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        # print("operasi penjumlahan")
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        # print("operasi perkalian")
        output = 1
        for angka in args:
            output *= angka
        output += angka
    else:
        print("tidak ada operasi")

    # return 0
    return output


hasil = math(1, 2, 3, 4, 5, 6, option="tambah")
print(f"hasil jumlah {hasil}")
hasil = math(1, 2, 3, 4, 5, 6, option="kali")
print(f"hasil kali {hasil}")
