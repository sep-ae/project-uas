# 📈 Project UAS Data Science — Dow Jones Index (UCI)

**Judul:** *Analisis dan Klasifikasi Pergerakan Harga Saham Minggu Berikutnya Menggunakan Machine Learning dan Deep Learning pada Dataset Dow Jones Index (UCI)*

Proyek ini membangun dan membandingkan **3 model** untuk klasifikasi arah pergerakan harga saham **minggu berikutnya** (label **naik/turun**):
1) **Baseline:** Logistic Regression  
2) **Advanced ML:** Random Forest Classifier  
3) **Deep Learning:** Multilayer Perceptron (MLP)

---

## 👨‍🎓 Informasi Mahasiswa
- **Nama:** Septito Aldo Elvianto  
- **NIM:** 233307026  
- **Prodi:** Teknologi Informasi  
- **Mata Kuliah:** TI22406 – Data Science  
- **Dosen Pengampu:** Gus Nanang Syaifuddiin  
- **Tahun Akademik:** 2025/2026  

---

## 🗂️ Struktur Folder
```
PROJECT-UAS/
├── .venv/                        # Virtual environment (tidak di-commit)
├── data/
│   └── .gitkeep                  # Placeholder (dataset bisa diambil via UCI)
├── images/                       # Output visualisasi (EDA, CM, grafik training)
│   ├── Confusion_Matrix_LogisticRegression.png
│   ├── Confusion_Matrix_MLP.png
│   ├── Confusion_Matrix_RandomForest.png
│   ├── mlp_accuracy.png
│   ├── mlp_loss.png
│   └── Perbandingan_Metrik_Model.png
├── models/                       # Model tersimpan (hasil training)
│   ├── model_logistic_regression.pkl
│   ├── model_random_forest.pkl
│   └── model_mlp.h5
├── notebooks/
│   ├── .gitkeep
│   └── DowJones.ipynb            # Notebook utama eksperimen
├── reports/                      # Laporan/hasil (opsional)
├── src/
│   └── load_data.py              # Helper load & preprocessing data
├── .gitignore
└── requirements.txt
```

---

## 📌 Dataset
- **Sumber:** UCI Machine Learning Repository (Dow Jones Index)  
- **Akses dataset:** via `ucimlrepo` (tidak perlu download manual jika memakai notebook/script)  
- **Target/Label:** dibuat dari `percent_change_next_weeks_price`  
  - `label_updown = 1` jika `percent_change_next_weeks_price > 0` (naik)  
  - `label_updown = 0` jika `<= 0` (turun)

---

## ⚙️ Cara Menjalankan (Windows / VS Code)

### 1) Buat & aktifkan virtual environment
Buka terminal di folder project:

```bat
python -m venv .venv
.venv\Scripts\activate
```

### 2) Install dependency
```bat
pip install -r requirements.txt
```

### 3) Jalankan Notebook (disarankan)
```bat
jupyter notebook
```
Lalu buka:
- `notebooks/DowJones.ipynb`

Notebook ini berisi:
- Load dataset dari UCI (`ucimlrepo`)
- Data cleaning (imputasi missing pada kolom tertentu)
- Feature engineering (label naik/turun)
- Train-test split (stratified)
- Training 3 model + evaluasi (accuracy, precision, recall, f1)
- Confusion matrix + plot training loss/accuracy (MLP)
- Perbandingan metrik antar model

---

## ▶️ (Opsional) Menjalankan via Script
Jika kamu menaruh pipeline di `src/load_data.py`, jalankan:

```bat
python src\load_data.py
```

> Catatan: jika `load_data.py` hanya helper, tetap jalankan eksperimen utama melalui notebook.

---

## 💾 Menyimpan & Load Model
Model yang sudah ditraining disimpan di folder `models/`:
- `model_logistic_regression.pkl` (Logistic Regression)
- `model_random_forest.pkl` (Random Forest)
- `model_mlp.h5` (MLP)

Contoh load ulang:
```python
import joblib
from tensorflow.keras.models import load_model

logreg = joblib.load("models/model_logistic_regression.pkl")
rf     = joblib.load("models/model_random_forest.pkl")
mlp    = load_model("models/model_mlp.h5")
```

---

## 🧪 Evaluasi
Metrik yang digunakan untuk klasifikasi:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**
- **Confusion Matrix**

Visualisasi hasil ada di folder `images/`.

---

## ✅ Reproducibility
- Tidak ada hardcoded path (menggunakan path relatif)
- Dependency terdokumentasi di `requirements.txt`
- Struktur folder rapi & siap dinilai dosen

---

## 🔗 Link
- **GitHub Repo:** *(isi link repo kamu di sini)*  
- **Video Pembahasan:** *(isi link video kamu di sini)*  

