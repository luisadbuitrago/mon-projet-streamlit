import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement direct du dataset "flights" depuis GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"
    return pd.read_csv(url)
df_flights = load_data()

# Titre de la page
st.title("Dashboard Analyse Vols - Luisa")

# Filtrer les données sur une plage d'années à l'aide d'un st.slider
annee_min = int(df_flights["year"].min())
annee_max = int(df_flights["year"].max())
plage_annee = st.slider("Sélectionnez la plage d'années :", min_value=annee_min, max_value=annee_max, value=(1949, 1960))

# Liste des mois ordonée - Traduction des mois en français.
mois = {"January": "Janvier", "February": "Février", "March": "Mars", "April": "Avril",
    "May": "Mai", "June": "Juin", "July": "Juillet", "August": "Août",
    "September": "Septembre", "October": "Octobre", "November": "Novembre", "December": "Décembre"}
df_flights["month"] = df_flights["month"].replace(mois)

# Données filtrées par plage d'années
df_plage_annee = df_flights[(df_flights["year"] >= plage_annee[0]) & (df_flights["year"] <= plage_annee[1])]

# Choisir un mois spécifique via un st.selectbox ou sélectionner tous les mois.
mois_choisi = st.selectbox("Choisissez un mois spécifique :", ["Tous les mois"] + list(mois.values()))

df_filtre = df_plage_annee
if mois_choisi != "Tous les mois":
    df_filtre = df_plage_annee[df_plage_annee["month"] == mois_choisi]


# Nombre total de passagers sur la période sélectionnée.
st.metric("Nombre total de passagers", df_filtre["passengers"].sum())



# Préparation des données : évolution annuelle du total des passagers
annual_passengers = df_filtre.groupby("year")["passengers"].sum()
st.subheader("Évolution nombre de passagers par année")
st.line_chart(annual_passengers)


# Une case à cocher (st.checkbox) qui, lorsqu'elle est activée, affiche la Heatmap
st.divider()
if st.checkbox("Afficher la Heatmap des passagers par année et par mois"):
    st.subheader("Heatmap")
    corr = df_plage_annee.pivot(index='month', columns='year', values='passengers')
    fig_corr, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".0f", ax=ax)
    st.pyplot(fig_corr)