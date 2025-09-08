# diabetes-predict

### Deskripsi Proyek

Proyek ini adalah API prediksi yang dibangun dengan **FastAPI**. API ini menggunakan model _machine learning_ untuk memprediksi kemungkinan seseorang menderita diabetes berdasarkan data kesehatan yang diberikan.

API ini memiliki satu _endpoint_ utama:

- **POST `/predict/diabetes/`**: Menerima data kesehatan pasien dan mengembalikan hasil prediksi (diabetes atau tidak) serta tingkat probabilitasnya.

---

### Persyaratan

Pastikan Anda memiliki **Python 3.8** atau versi yang lebih baru terinstal di sistem Anda.

### Instalasi dan Penggunaan

#### 1. Klon Repositori

```bash
git clone [https://github.com/IrvanYusuf/fast-api-diabetes.git])
cd nama-repo-anda
```

#### 2. Buat dan Aktifkan Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux / bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Instal Dependensi

Setelah virtual environment aktif, instal semua pustaka yang diperlukan.

```bash
pip install -r requirements.txt
```

#### 4. Jalankan Server API

Anda dapat menjalankan server menggunakan uvicorn.

```bash
uvicorn main:app --reload
```

Setelah server berjalan, API akan tersedia di http://127.0.0.1:8000 🐱‍🏍.
