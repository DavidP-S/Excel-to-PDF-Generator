# Excel-to-PDF Bulk Generator 🚀

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Herramienta profesional para convertir bases de datos de Excel a PDFs organizados con metadatos.

## 📝 Descripción
Solución automatizada que transforma grandes volúmenes de datos desde Excel a archivos PDF organizados, ideal para:

- Concursos literarios
- Procesos de evaluación académica
- Organización de documentos empresariales
- Cualquier flujo de trabajo que requiera distribución masiva de documentos

## 🛠 Requisitos técnicos
```bash
Python >= 3.8
Bibliotecas:
- pandas >= 1.3.0
- fpdf2 >= 2.5.5
- openpyxl >= 3.0.0
```

## 📦 Instalación
```bash
pip install pandas fpdf2 openpyxl
```
## 🛠 Configuración
Prepara tu archivo Excel (ARCHIVO-BD.xls) con estas columnas mínimas:

- K_PARTICIPACION (ID único)
- I_ESTADO (debe contener "ENVIADO")
- D_TEXTO (contenido principal)
- R_CONCURSO_MODALIDAD (Cuento/Ensayo/Crónica)
- R_CONCURSO_CATEGORIA (Adulto/Juvenil/Infantil)
- D_TITULO (título del trabajo)

Descarga el script generador_pdfs.py

##  🚀 Uso
```bash
python generador_pdfs.py
```

El sistema generará:

- 33 carpetas para "Cuento - Evaluador X"
- 3 carpetas para "Ensayo - Evaluador X"
- 4 carpetas para "Crónica - Evaluador X"

##  📂 Estructura de salida
```bash
PDFs_Generados/
├── Cuento - Evaluador 1/
│   ├── 001.pdf
│   └── 034.pdf
├── Ensayo - Evaluador 1/
│   └── 005.pdf
└── Crónica - Evaluador 1/
    └── 012.pdf
```

##  📜 Licencia
MIT License. Ver archivo [texto](LICENSE) para detalles.
