import pandas as pd
from fpdf import FPDF
import os
import math

# Cargar el archivo Excel, se debe cambiar "ARCHIVO-BD", según el archivo generado en la base de datos
df = pd.read_excel('ARCHIVO-BD.xls')

# Filtrar solo las filas que contienen "ENVIADO" en la columna "I_ESTADO", solo se sacaran los textos que estén en estado "ENVIADO"
df_filtrado = df[df['I_ESTADO'] == 'ENVIADO']

# Crear las carpetas necesarias
def crear_carpetas(base, cantidad, tipo):
    for i in range(1, cantidad + 1):
        carpeta = os.path.join(base, f"{tipo} - Evaluador {i}")
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

# Crear las 40 carpetas, los números representan la cantidad de evaluadores por cada uno de las modalidades.
base_carpetas = "PDFs_Generados"
crear_carpetas(base_carpetas, 33, "Cuento")
crear_carpetas(base_carpetas, 3, "Ensayo")
crear_carpetas(base_carpetas, 4, "Crónica")

# Función para obtener la carpeta correspondiente
def obtener_carpeta(modalidad, index, total, tipo, cantidad_evaluadores):
    evaluador = (index % cantidad_evaluadores) + 1
    return os.path.join(base_carpetas, f"{tipo} - Evaluador {evaluador}")

# Función para traducir la modalidad, se deben colocar las categorias exactamente como estan escritas en la celda.
def traducir_modalidad(modalidad):
    if modalidad == "Cuento":
        return "Cuento"
    elif modalidad == "Ensayo":
        return "Ensayo"
    elif modalidad == "Crónica":
        return "Crónica"
    else:
        return modalidad  # Si no coincide, se deja el valor original

# Función para traducir la categoría, se deben colocar las categorias exactamente como estan escritas en la celda.
def traducir_categoria(categoria):
    if categoria == "Adulto":
        return "Adulto"
    elif categoria == "Juvenil":
        return "Juvenil"
    elif categoria == "Infantil":
        return "Infantil"
    else:
        return categoria  # Si no coincide, se deja el valor original

# Iterar sobre las filas filtradas
for index, row in df_filtrado.iterrows():
    # Obtener el valor de la columna "K_PARTICIPACION" para el nombre del archivo PDF
    nombre_archivo = row['K_PARTICIPACION']
    
    # Obtener el texto de la columna específica "D_TEXTO"
    texto = str(row['D_TEXTO'])  # Solo toma el valor de la columna "D_TEXTO"
    
    # Validar si el texto está vacío o es NaN (hojas en blanco)
    if pd.isna(texto) or texto.strip() == "":
        print(f"Advertencia: La fila {index} tiene un texto vacío en 'D_TEXTO'. No se generará PDF.")
        continue  # Saltar esta fila y continuar con la siguiente
    
    # Obtener la modalidad y categoría traducidas
    modalidad = traducir_modalidad(row['R_CONCURSO_MODALIDAD'])
    categoria = traducir_categoria(row['R_CONCURSO_CATEGORIA'])
    
    # Determinar la carpeta de destino según la modalidad
    if row['R_CONCURSO_MODALIDAD'] == "Cuento":
        carpeta_destino = obtener_carpeta(modalidad, index, len(df_filtrado), "Cuento", 33)
    elif row['R_CONCURSO_MODALIDAD'] == "Ensayo":
        carpeta_destino = obtener_carpeta(modalidad, index, len(df_filtrado), "Ensayo", 3)
    elif row['R_CONCURSO_MODALIDAD'] == "Crónica":
        carpeta_destino = obtener_carpeta(modalidad, index, len(df_filtrado), "Crónica", 4)
    else:
        print(f"Advertencia: Modalidad desconocida '{row['R_CONCURSO_MODALIDAD']}' en la fila {index}. No se generará PDF.")
        continue  # Saltar esta fila y continuar con la siguiente
    
    # Crear una nueva instancia de FPDF para cada fila
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Se agrega un encabezado con distintas celdas que ayudan al evaluador.
    pdf.cell(0, 10, txt=f"Código del escrito: {row['K_PARTICIPACION']}", ln=True)
    pdf.cell(0, 10, txt=f"Modalidad: {modalidad}", ln=True)
    pdf.cell(0, 10, txt=f"Categoría: {categoria}", ln=True)
    pdf.cell(0, 10, txt=f"Título: {row['D_TITULO']}", ln=True)
    
    # Dos saltos de línea
    pdf.ln(10)
    pdf.ln(10)
    
    # Usar multi_cell para manejar texto largo (D_TEXTO)
    pdf.multi_cell(0, 10, txt=texto)
    
    # Guardar el PDF en la carpeta correspondiente
    pdf.output(os.path.join(carpeta_destino, f"{nombre_archivo}.pdf"))

# Print Final de ejecución
print(f"PDFs generados exitosamente en las carpetas dentro de: {os.path.abspath(base_carpetas)}")