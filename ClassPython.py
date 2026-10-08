class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
            return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)


    def __str__(self):
        return f"Persegi Panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

input_panjang = int(input("Masukkan panjang (cm): "))
while input_panjang == 0:
    print("Panjang tidak boleh 0!")
    input_panjang = int(input("Masukkan panjang lagi (cm): "))

input_lebar = int(input("Masukkan lebar (cm): "))
while input_lebar == 0:
    print("Lebar tidak boleh 0!")
    input_lebar = int(input("Masukkan lebar lagi (cm): "))

pp = PersegiPanjang(input_panjang, input_lebar)

print(pp)
print("keliling:", pp.hitung_keliling())
print("Luas:", pp.hitung_luas())