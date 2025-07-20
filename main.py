import imaplib
import email
import time
import sys

# -------------------- KULLANICI AYARLARI --------------------
SOURCE_IMAP = "imap.godaddy.com"
SOURCE_EMAIL = "kaynak@example.com"
SOURCE_PASSWORD = "kaynak_sifre"

TARGET_IMAP = "imap.destinationhost.com"
TARGET_EMAIL = "hedef@example.com"
TARGET_PASSWORD = "hedef_sifre"
# -----------------------------------------------------------

def connect_to_imap(host, email_addr, password):
    try:
        conn = imaplib.IMAP4_SSL(host)
        conn.login(email_addr, password)
        return conn
    except Exception as e:
        print(f"[!] IMAP bağlantı hatası: {e}")
        sys.exit(1)

def migrate_emails(src_conn, tgt_conn):
    src_conn.select("INBOX")
    typ, data = src_conn.search(None, "ALL")

    if typ != 'OK':
        print("[!] Mail arama başarısız.")
        return

    msg_ids = data[0].split()
    print(f"[+] Toplam {len(msg_ids)} mail bulundu. Aktarılıyor...")

    for i, msg_id in enumerate(msg_ids, 1):
        typ, msg_data = src_conn.fetch(msg_id, '(RFC822)')
        if typ != 'OK':
            print(f"[!] Mail {msg_id} alınamadı.")
            continue

        raw_email = msg_data[0][1]

        # İsteğe bağlı: maili decode etmeden direk hedefe aktar
        try:
            tgt_conn.append("INBOX", '', imaplib.Time2Internaldate(time.time()), raw_email)
            print(f"[{i}/{len(msg_ids)}] Mail başarıyla taşındı.")
        except Exception as e:
            print(f"[!] Mail {msg_id} aktarım hatası: {e}")

def main():
    print("[*] Kaynak sunucuya bağlanılıyor...")
    src = connect_to_imap(SOURCE_IMAP, SOURCE_EMAIL, SOURCE_PASSWORD)

    print("[*] Hedef sunucuya bağlanılıyor...")
    tgt = connect_to_imap(TARGET_IMAP, TARGET_EMAIL, TARGET_PASSWORD)

    print("[*] Mailler taşınıyor...")
    migrate_emails(src, tgt)

    print("[✓] Tüm mailler başarıyla aktarıldı.")
    src.logout()
    tgt.logout()

if __name__ == "__main__":
    main()
