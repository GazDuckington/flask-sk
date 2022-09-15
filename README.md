# flask-sk
Pengaplikasian analisis sentimen menggunakan algoritma naive-bayes, dari [proyek ini](https://github.com/RegalOctopus/analisis-sentimen-naive-bayes).
Dibuat untuk memenuhi tugas praktik.

- _Repository_ ini: https://github.com/RegalOctopus/flask-sk

- _Frontend_ yang masih aktif, dapat diakses [disini](https://gzfront.herokuapp.com/)

- [buka situs](https://ghazy-kp.herokuapp.com) (no longer maintained)

## *backend*
Ada dua cara untuk meluncurkan backend:

### *Terminal*
Pastikan sudah didalam lingkungan _virtual_

```bash
git clone https://github.com/RegalOctopus/flask-sk.git
cd flask-sk/
cd backend/
pipenv shell
pip install -r requirements.txt
export FLASK_ENV=development
flask run
```
### *Docker*

```bash
docker build -t flask-sk:latest .
docker run flask-sk
```

setelah instalasi, buka halaman ```http://127.0.0.1:5000/docs``` untuk melihat daftar API endpoints.

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
