def user_info():
    name = input("Adınızı girin: ")
    age = int(input("Yaşınızı girin: "))
    birth_year = int(input("Doğum yılınızı girin: "))

    print(f"Merhaba {name}! {age} yaşındasın ve {birth_year} yılında doğmuşsun.")


user_info()

def calculate_numbers():
    num1 = float(input("Birinci sayıyı girin: "))
    num2 = float(input("İkinci sayıyı girin: "))

    print(f"Toplam: {num1 + num2}")
    print(f"Fark: {num1 - num2}")
    print(f"Çarpım: {num1 * num2}")
    if num2 != 0:
        print(f"Bölüm: {num1 / num2}")
    else:
        print("Bölme işlemi yapılamaz! (Sıfıra bölme hatası)")


calculate_numbers()
