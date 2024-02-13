import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

data = pd.read_csv("all_data.csv")

x_season = data.groupby('season')['cnt'].sum()
data_kerja = data[data['workingday'] == 1]
data_libur = data[data['workingday'] == 0]

'''''
def plot_season_data(x_season):
    plt.figure(figsize=(8, 6))
    x_season.plot(kind='bar', color='skyblue')
    plt.title('Total Pembelian per Musim')
    plt.xlabel('Musim')
    plt.ylabel('Total Pembelian')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot()
    '''''
    
    #grafik pertama
fig, ax = plt.subplots(figsize=(8, 6))
x_season.plot(kind='bar', color='skyblue', ax=ax)
plt.title('Total Pembelian per Musim')
plt.xlabel('Musim')
plt.ylabel('Total Pembelian')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig)

# fig, ax = plt.subplots(figsize=(5, 3))
# ax.bar(['Kerja', 'Libur'], [data_kerja['cnt'][0], data_libur['cnt'].sum[0]], color='skyblue')
# ax.set_title('Total Penyewaan Sepeda di Hari Kerja & Libur'.upper())
# ax.set_xlabel(' ')
# ax.set_ylabel('Total Penyewaan')
# plt.tight_layout()

# # Menampilkan plot di Streamlit
# st.pyplot(fig)

#grafik ke 2
st.header('Total Penyewaan Sepedah di hari libur & Kerja')
fig, ax = plt.subplots(figsize=(5, 3))
ax.bar(['Kerja', 'Libur'], [data_kerja['cnt'].sum(), data_libur['cnt'].sum()], color='skyblue')
plt.title('Total Penyewaan Sepeda di Hari Libur & Kerja'.upper())
plt.xlabel(' ')
plt.ylabel('Total Penyewaan')
plt.tight_layout()
st.pyplot(fig)