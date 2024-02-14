import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

data = pd.read_csv("data.csv")


x_season = data.groupby('season')['cnt'].sum()
data_kerja = data[data['workingday'] == 1]
data_libur = data[data['workingday'] == 0]

st.title('Analisis Penyewaan Sepedah Setiap Musimnya')
st.write(" ", data)

st.header('Penyewaan Sepedah di setiap Musim')
# grafik pertama
fig, ax = plt.subplots(figsize=(8, 6))
x_season.plot(kind='bar', color='skyblue', ax=ax)

plt.title('Total Penyewaan per Musim')
plt.xlabel('Musim')
plt.ylabel('Total Pembelian')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig)


#grafik ke 2
st.header('Total Penyewaan Sepedah di hari libur & Kerja')
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(['Kerja', 'Libur'], [data_kerja['cnt'].sum(), data_libur['cnt'].sum()], color='skyblue')
plt.title('Total Penyewaan Sepeda di Hari Libur & Kerja'.upper())
plt.xlabel(' ')
plt.ylabel('Total Penyewaan')
plt.tight_layout()
st.pyplot(fig)
