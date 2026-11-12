import streamlit as st
import pandas as pd

# Lire le fichier taxis.csv directement depuis l'URL et le convertir en un DataFrame
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv")

# Titre de la page
st.title("Dashboard Analyse Taxis - Luisa")

# Liste des quartiers pour le menu.
quartiers = sorted(df["pickup_borough"].dropna().unique())
# Menu déroulant avec ces quartiers
quartier_choisi = st.selectbox("Choisissez un quartier de prise en charge :", quartiers)

# Nouvelle table avec les lignes du quartier choisi
df_choisi = df[df["pickup_borough"] == quartier_choisi]

# Les 5 premières lignes du tableau
st.dataframe(df_choisi.head(5))
# Nombre de déplacements depuis ce quartier
st.metric("Nombre total de courses", len(df_choisi))