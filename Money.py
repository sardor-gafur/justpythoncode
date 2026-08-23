class BankHisobi:
    """Mijozning bank hisob raqamini boshqarish uchun klass."""
    
    def __init__(self, egasi, boshlangich_balans=0):
        self.egasi = egasi
        self.balans = boshlangich_balans

    def balansni_tekshirish(self):
        print(f"\nHozirgi balans: {self.balans} so'm")

    def pul_kiritish(self, miqdor):
        if miqdor > 0:
            self.balans += miqdor
            print(f"Muvaffaqiyatli! {miqdor} so'm qo'shildi.")
            self.balansni_tekshirish()
        else:
            print("Xatolik: Miqdor 0 dan katta bo'lishi kerak!")

    def pul_yechish(self, miqdor):
        if miqdor > self.balans:
            print(f"Xatolik: Mablag' yetarli emas! Balansda: {self.balans} so'm bor.")
        elif miqdor <= 0:
            print("Xatolik: Noto'g'ri miqdor kiritildi!")
        else:
            self.balans -= miqdor
            print(f"Muvaffaqiyatli! {miqdor} so'm yechildi.")
            self.balansni_tekshirish()

# --- Dasturni ishga tushirish va sinab ko'rish ---

# 1. Yangi mijoz ochamiz (Ismi: Anvar, Balansi: 50,000 so'm)
mijoz = BankHisobi("Anvar", 50000)

print(f"Hisob egasi: {mijoz.egasi}")

# 2. Pul kiritamiz
mijoz.pul_kiritish(20000)

# 3. Ko'proq pul yechishga urinib ko'ramiz (Xatolik berishi kerak)
mijoz.pul_yechish(100000)

# 4. To'g'ri miqdorda pul yechamiz
mijoz.pul_yechish(30000)
