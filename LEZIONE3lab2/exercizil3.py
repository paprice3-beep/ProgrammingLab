#exo1
import pandas as pd
import matplotlib.pyplot as plt

# Caricamento del dataset
url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv"
df = pd.read_csv(url)

# 1. Visualizza i primi 10 paesi ordinati per total_litres_of_pure_alcohol (dal più alto)
top_10_pure_alcohol = df.sort_values(by='total_litres_of_pure_alcohol', ascending=False).head(10)
print("Primi 10 paesi per litri totali di alcol puro:")
print(top_10_pure_alcohol[['country', 'total_litres_of_pure_alcohol']])

# 2. Calcola la media del consumo di birra, vino, e distillati
medie_consumi = df[['beer_servings', 'wine_servings', 'spirit_servings']].mean()
print("\nMedia dei consumi mondiali (porzioni):")
print(medie_consumi)

# 3. Crea una nuova colonna alcohol_index
df['alcohol_index'] = (df['beer_servings'] + df['wine_servings'] + df['spirit_servings']) / 3

# 4. Trova il paese con il valore massimo di alcohol_index
paese_max_index = df.loc[df['alcohol_index'].idxmax(), 'country']
print(f"\nIl paese con l'indice di consumo (alcohol_index) più alto è: {paese_max_index}")

# 5. Filtra solo i paesi che consumano più di 100 birre all’anno
paesi_birra_100 = df[df['beer_servings'] > 100]
print(f"\nNumero di paesi che consumano più di 100 birre all'anno: {len(paesi_birra_100)}")

# --- VISUALIZZAZIONI ---

# 6. Bar chart dei 10 paesi con più consumo totale (total_litres_of_pure_alcohol)
plt.figure(figsize=(12, 6))
plt.bar(top_10_pure_alcohol['country'], top_10_pure_alcohol['total_litres_of_pure_alcohol'], color='orange')
plt.title('Top 10 Paesi per Consumo di Alcol Puro')
plt.xlabel('Paese')
plt.ylabel('Litri di alcol puro')
plt.xticks(rotation=45)
plt.show()

# 7. Line plot con wine_servings ordinato per paese
df_sorted_country = df.sort_values(by='country')
plt.figure(figsize=(15, 6))
plt.plot(df_sorted_country['country'], df_sorted_country['wine_servings'], marker='o', color='purple', markersize=3)
plt.title('Consumo di Vino per Paese (Ordine Alfabetico)')
plt.xlabel('Paese')
plt.ylabel('Porzioni di vino')
plt.xticks([]) # Nascondiamo le etichette X perché sono troppe per essere leggibili
plt.grid(True, alpha=0.3)
plt.show()

#exo2

import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt
import seaborn as sns

# Caricamento del dataset
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Conversione date e pulizia minima (rimozione righe senza stipendio per l'analisi specifica)
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df_salary = df.dropna(subset=['salary_year_avg'])

# --- 1. Analisi Esplorativa per Paese ---

# Raggruppiamo per paese e calcoliamo media, conteggio, minimo e massimo
country_analysis = df_salary.groupby('job_country')['salary_year_avg'].agg([
    'mean', 
    'count', 
    'min', 
    'max'
]).sort_values(by='mean', ascending=False)

# Rinominiamo le colonne per chiarezza
country_analysis.columns = ['Stipendio Medio', 'Offerte (Count)', 'Minimo', 'Massimo']

print("Analisi per Paese (Top 10 per stipendio medio):")
print(country_analysis.head(10))

# --- 2. Grafico a barre orizzontali: Stipendio Medio per Ruolo ---

# Calcoliamo la media per ogni ruolo e ordiniamo
job_salary_avg = df_salary.groupby('job_title_short')['salary_year_avg'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
# Creazione del grafico
job_salary_avg.plot(kind='barh', color='skyblue', edgecolor='navy')

# Personalizzazione
plt.title('Stipendio Medio Annuale per Ruolo (Data Jobs)', fontsize=14)
plt.xlabel('Stipendio Medio (USD)', fontsize=12)
plt.ylabel('Titolo del Lavoro', fontsize=12)
plt.gca().invert_yaxis()  # Inverte l'asse per avere lo stipendio più alto in alto
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

#exo3

import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

daily_stats = df.groupby('day')['total_bill'].agg(['mean', 'count', 'min', 'max'])
daily_stats.columns = ['mean', 'count', 'min', 'max']

df['conto_per_persona'] = df['total_bill'] / df['size']

giorno_max = daily_stats['mean'].idxmax()

plot_data = daily_stats['mean'].sort_values(ascending=False)

plt.figure(figsize=(8, 6))
plot_data.plot(kind='bar', color='teal')
plt.title('Conto medio per giorno')
plt.xlabel('Giorno')
plt.ylabel('Total Bill medio')
plt.show()

print(daily_stats)
print(f"\nGiorno con media più alta: {giorno_max}")