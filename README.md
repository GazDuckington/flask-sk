# flask-sk
Pengaplikasian analisis sentimen menggunakan algoritma naive-bayes, dari [proyek ini](https://github.com/RegalOctopus/analisis-sentimen-naive-bayes).

Dibuat untuk memenuhi tugas praktek.
## *backend*

```bash
git clone https://github.com/RegalOctopus/flask-sk.git
cd flask-sk/
cd backend/
# masuk ke lingkungan virtual, dalam kasus ini menggunakan pipenv
pipenv shell
pip install -r requirements.txt
export FLASK_ENV=development
flask run
```
karena nltk dianggap sebagai risiko keamanan dalam github, modul tersebut harus dihapus dari daftar *requirements.txt*. Instalasai nltk dapat dilakukan dengan:
```bash
pip install nltk
```
 <br>

setelah instalasi, buka halaman ```http://127.0.0.1:5000/docs``` untuk daftar API endpoints.

## *frontend*

```bash
cd flask-sk/
cd frontend/
npm i
npm run --dev
# atau
npm run --dev -- --open
```
# Peringatan
Jika menggunakan Visual Studio Code, hapus/edit folder ```.vscode```
