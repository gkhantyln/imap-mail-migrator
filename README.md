# IMAP Mail Migrator

Python ile geliştirilen basit bir araç sayesinde, IMAP tabanlı e-posta sunucuları arasında e-posta kutularınızı kolayca taşıyabilirsiniz.

## Özellikler

- IMAP protokolünü kullanır
- SSL üzerinden güvenli bağlantı
- INBOX içeriğini birebir taşır
- Taşıma işlemi birkaç dakikada tamamlanır

## Kullanım

1. `imaplib` ve `email` kütüphaneleri Python'un içinde gömülüdür, ek kurulum gerekmez.
2. `main.py` dosyasında kaynak ve hedef hesap bilgilerini doldurun.
3. Terminal üzerinden çalıştırın:

```bash
python main.py
