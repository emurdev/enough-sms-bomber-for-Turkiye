def show_disclaimer():
    with open("OKU.txt", "r", encoding="utf-8") as f:
        disclaimer = f.read()
    print(disclaimer)

    while True:
        answer = input(
            """
=== SORUMLULUK REDDİ ===

Bu yazılım yalnızca eğitimsel ve etik test amaçlıdır.
İzinsiz kullanım, rahatsız etme veya zarar verme amacıyla
kullanılması yasaktır. Tüm sorumluluk kullanıcıya aittir.

Devam ederek bu şartları kabul etmiş olursunuz.
Yukarıdaki şartları okudunuz ve kabul ediyor musunuz? (E/H): """
        ).strip().upper()

        if answer == "E":
            return True
        elif answer == "H":
            print("Kabul etmediğiniz için program kapanıyor.")
            return False
        else:
            print("Lütfen sadece 'E' (Evet) veya 'H' (Hayır) giriniz.")

if __name__ == "__main__":
    if show_disclaimer():
        import enough
        # enough.py içindeki main fonksiyonunu çalıştırmak için:
        # enough.main()
    else:
        exit()
