from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

def turbo_20x(send_sms):
    threads = []
    for _ in range(20):
        for fonk in servisler_sms:
            t = threading.Thread(target=getattr(send_sms, fonk))
            threads.append(t)
            t.start()
    for t in threads:
        t.join()

while 1:
    system("cls||clear")
    print("""{}

                         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                         ░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░
                         ░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░
                         ░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░
                         ░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░
                         ░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░
                         ░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░
                         ░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░
                         ░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░
                         ░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░
                         ░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░
                         ░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░
                         ░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░
                         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                         

░█▀▀▀ ░█▀▄▀█ ░█─░█ ░█▀▀█ 　 ░█▀▀▀█ ░█▀▄▀█ ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀▀█ ░█▀▄▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀█ 
░█▀▀▀ ░█░█░█ ░█─░█ ░█▄▄▀ 　 ─▀▀▀▄▄ ░█░█░█ ─▀▀▀▄▄ 　 ░█▀▀▄ ░█──░█ ░█░█░█ ░█▀▀▄ ░█▀▀▀ ░█▄▄▀ 
░█▄▄▄ ░█──░█ ─▀▄▄▀ ░█─░█ 　 ░█▄▄▄█ ░█──░█ ░█▄▄▄█ 　 ░█▄▄█ ░█▄▄▄█ ░█──░█ ░█▄▄█ ░█▄▄▄ ░█─░█


    Sms: {}           {}by {}@emirhan_dq\n  

    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = (input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder (Normal)\n\n 2- SMS Gönder (Turbo)\n\n 3- Çıkış\n\n 4- Turbo 20x (Çok hızlı/20x)\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue
    if menu == 1:
        # ... (eski normal mod kodu buraya)
        pass
    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
    elif menu == 2:
        # ... (eski turbo kodu buraya)
        pass
    elif menu == 4:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue
        print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
        mail = input()
        if ("@" not in mail or ".com" not in mail) and mail != "":
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        send_sms = SendSms(tel_no, mail)
        print(Fore.LIGHTCYAN_EX + "20x Turbo başlatılıyor...")
        turbo_20x(send_sms)
        print(Fore.LIGHTGREEN_EX + "Tüm işlemler tamamlandı. Menüye dönmek için 'enter' tuşuna basınız..")
        from colorama import Fore, Style
        from time import sleep
        from os import system
        from sms import SendSms
        import threading

        # Servisleri dinamik olarak listeleme
        servisler_sms = [attr for attr in dir(SendSms) if callable(getattr(SendSms, attr)) and not attr.startswith("__")]

        def turbo_20x(send_sms):
            threads = []
            import tkinter as tk
            from tkinter import messagebox

            def turbo_20x_window():
                """
                Turbo 20x işlemini başlatan pencere.
                """
                messagebox.showinfo("Bilgi", "20x Turbo işlemi başlatılıyor...")

            # Ana pencere oluşturma
            root = tk.Tk()
            root.title("SMS Gönderim Aracı")
            root.geometry("600x400")  # Pencere boyutu
            root.configure(bg="#f5f5dc")  # Açık kahverengi (beyaza yakın)

            # Şeffaflık ayarı
            root.attributes("-alpha", 0.95)  # %95 şeffaflık

            # Pencere kenarlıklarını kaldırma (isteğe bağlı)
            root.overrideredirect(False)

            # Başlık etiketi
            title_label = tk.Label(
                root,
                text="SMS Gönderim Aracı",
                font=("Arial", 18, "bold"),
                bg="#f5f5dc",
                fg="black"
            )
            title_label.pack(pady=20)

            # Menü seçenekleri
            def normal_sms():
                messagebox.showinfo("Bilgi", "Normal SMS Gönderme seçildi.")

            def turbo_sms():
                messagebox.showinfo("Bilgi", "Turbo SMS Gönderme seçildi.")

            def exit_app():
                root.destroy()

            # Butonlar
            btn_normal = tk.Button(
                root,
                text="Normal SMS Gönder",
                font=("Arial", 12),
                bg="#dcdcdc",
                fg="black",
                command=normal_sms
            )
            btn_normal.pack(pady=10)

            btn_turbo = tk.Button(
                root,
                text="Turbo SMS Gönder",
                font=("Arial", 12),
                bg="#dcdcdc",
                fg="black",
                command=turbo_sms
            )
            btn_turbo.pack(pady=10)

            btn_turbo_20x = tk.Button(
                root,
                text="Turbo 20x Gönder",
                font=("Arial", 12),
                bg="#dcdcdc",
                fg="black",
                command=turbo_20x_window
            )
            btn_turbo_20x.pack(pady=10)

            btn_exit = tk.Button(
                root,
                text="Çıkış",
                font=("Arial", 12),
                bg="#dcdcdc",
                fg="black",
                command=exit_app
            )
            btn_exit.pack(pady=10)

            # Ana döngü
            root.mainloop()
            for _ in range(20):
                for fonk in servisler_sms:
                    t = threading.Thread(target=getattr(send_sms, fonk))
                    threads.append(t)
                    t.start()
            for t in threads:
                t.join()

        def clear_screen():
            system("cls||clear")

        def main_menu():
            clear_screen()
            print(f"""{Fore.LIGHTCYAN_EX}

                         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                         ░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░
                         ░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░
                         ░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░
                         ░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░
                         ░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░
                         ░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░
                         ░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░
                         ░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░
                         ░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░
                         ░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░
                         ░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░
                         ░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░
                         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                         

░█▀▀▀ ░█▀▄▀█ ░█─░█ ░█▀▀█ 　 ░█▀▀▀█ ░█▀▄▀█ ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀▀█ ░█▀▄▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀█ 
░█▀▀▀ ░█░█░█ ░█─░█ ░█▄▄▀ 　 ─▀▀▀▄▄ ░█░█░█ ─▀▀▀▄▄ 　 ░█▀▀▄ ░█──░█ ░█░█░█ ░█▀▀▄ ░█▀▀▀ ░█▄▄▀ 
░█▄▄▄ ░█──░█ ─▀▄▄▀ ░█─░█ 　 ░█▄▄▄█ ░█──░█ ░█▄▄▄█ 　 ░█▄▄█ ░█▄▄▄█ ░█──░█ ░█▄▄█ ░█▄▄▄ ░█─░█


            Sms: {len(servisler_sms)}           {Style.RESET_ALL}by {Fore.LIGHTRED_EX}@emirhan_dq\n  
            """)

        def get_user_input(prompt, validation_func=None):
            while True:
                user_input = input(prompt)
                if validation_func and not validation_func(user_input):
                    print(Fore.LIGHTRED_EX + "Hatalı giriş. Tekrar deneyiniz.")
                    continue
                return user_input

        def validate_phone(phone):
            return phone.isdigit() and len(phone) == 10

        def validate_email(email):
            return "@" in email and ".com" in email or email == ""

        while True:
            main_menu()
            menu = get_user_input(
                Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder (Normal)\n\n 2- SMS Gönder (Turbo)\n\n 3- Çıkış\n\n 4- Turbo 20x (Çok hızlı/20 tekrar)\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: ",
                lambda x: x.isdigit() and 1 <= int(x) <= 4
            )
            menu = int(menu)

            if menu == 1:
                # Normal SMS Gönderme
                pass
            elif menu == 2:
                # Turbo SMS Gönderme
                pass
            elif menu == 3:
                clear_screen()
                print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
                break
            elif menu == 4:
                clear_screen()
                tel_no = get_user_input(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: " + Fore.LIGHTGREEN_EX, validate_phone)
                mail = get_user_input(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): " + Fore.LIGHTGREEN_EX, validate_email)
                send_sms = SendSms(tel_no, mail)
                print(Fore.LIGHTCYAN_EX + "20x Turbo başlatılıyor...")
                turbo_20x(send_sms)
                input(Fore.LIGHTGREEN_EX + "Tüm işlemler tamamlandı. Menüye dönmek için 'enter' tuşuna basınız..")
        import tkinter as tk
        from tkinter import messagebox

        def turbo_20x_window():
            """
            Turbo 20x işlemini başlatan pencere.
            """
            messagebox.showinfo("Bilgi", "20x Turbo işlemi başlatılıyor...")

        # Ana pencere oluşturma
        root = tk.Tk()
        root.title("SMS Gönderim Aracı")
        root.geometry("600x400")  # Pencere boyutu
        root.configure(bg="#f5f5dc")  # Açık kahverengi (beyaza yakın)

        # Şeffaflık ayarı
        root.attributes("-alpha", 0.95)  # %95 şeffaflık

        # Pencere kenarlıklarını kaldırma (isteğe bağlı)
        root.overrideredirect(False)

        # Başlık etiketi
        title_label = tk.Label(
            root,
            text="SMS Gönderim Aracı",
            font=("Arial", 18, "bold"),
            bg="#f5f5dc",
            fg="black"
        )
        title_label.pack(pady=20)

        # Menü seçenekleri
        def normal_sms():
            messagebox.showinfo("Bilgi", "Normal SMS Gönderme seçildi.")

        def turbo_sms():
            messagebox.showinfo("Bilgi", "Turbo SMS Gönderme seçildi.")

        def exit_app():
            root.destroy()

        # Butonlar
        btn_normal = tk.Button(
            root,
            text="Normal SMS Gönder",
            font=("Arial", 12),
            bg="#dcdcdc",
            fg="black",
            command=normal_sms
        )
        btn_normal.pack(pady=10)

        btn_turbo = tk.Button(
            root,
            text="Turbo SMS Gönder",
            font=("Arial", 12),
            bg="#dcdcdc",
            fg="black",
            command=turbo_sms
        )
        btn_turbo.pack(pady=10)

        btn_turbo_20x = tk.Button(
            root,
            text="Turbo 20x Gönder",
            font=("Arial", 12),
            bg="#dcdcdc",
            fg="black",
            command=turbo_20x_window
        )
        btn_turbo_20x.pack(pady=10)

        btn_exit = tk.Button(
            root,
            text="Çıkış",
            font=("Arial", 12),
            bg="#dcdcdc",
            fg="black",
            command=exit_app
        )
        btn_exit.pack(pady=10)

        # Ana döngü
        root.mainloop()
        input()