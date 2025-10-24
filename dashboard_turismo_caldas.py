import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# DATOS
# -----------------------------
data = {
    "Año": [2019, 2020, 2021, 2022, 2023, 2024],
    "Visitantes": [736037, 128443, 245687, 225874, 358742, 412350]
}
df = pd.DataFrame(data)

# -----------------------------
# TÍTULOS
# -----------------------------
st.title("📊 Dashboard Turístico - Departamento de Caldas")
st.caption("Fuente: Boletín Sector Turismo Caldas – Marzo 2023")

# -----------------------------
# TABLA
# -----------------------------
st.subheader("Datos históricos")
st.dataframe(df)

# -----------------------------
# GRÁFICO
# -----------------------------
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(df["Año"], df["Visitantes"], color="#2E86C1")

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 5000, f"{int(yval):,}",
            ha="center", va="bottom", fontsize=10, fontweight="bold")

ax.set_title("Número de Visitantes por Año")
ax.set_xlabel("Año")
ax.set_ylabel("Visitantes")
ax.grid(axis="y", linestyle="--", alpha=0.6)

st.pyplot(fig)