# AssetExpl - ETF Explorer 📊

**Web App educativa per l'esplorazione di indici ETF globali**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

## 🎯 Caratteristiche Principali

- **📱 Interfaccia Multilingua**: Supporto completo per Italiano e Inglese con cambio lingua dinamico
- **📊 Visualizzazioni Interattive**: Grafici professionali con Plotly per analisi geografiche e settoriali
- **🎨 Design Modulare**: Architettura scalabile pronta per l'aggiunta di nuovi indici
- **📈 3 Indici ETF**: MSCI World, S&P 500, MSCI Emerging Markets con dati completi
- **🎯 Strategie d'Investimento**: Guide dettagliate su come utilizzare ciascun indice

## 🚀 Quick Start

### Installazione Locale

```bash
# Clona il repository
git clone https://github.com/your-username/AssetExpl.git
cd AssetExpl

# Installa le dipendenze
pip install -r requirements.txt

# Avvia l'app
streamlit run app.py
```

L'app sarà disponibile su `http://localhost:8501`

### Deploy su Streamlit Community Cloud

1. Fai il fork di questo repository
2. Vai su [share.streamlit.io](https://share.streamlit.io)
3. Collega il tuo repository GitHub
4. Deploy automatico! 🎉

## 📁 Struttura del Progetto

```
AssetExpl/
│
├── app.py                 # File principale dell'applicazione
├── requirements.txt       # Dipendenze Python
└── README.md             # Documentazione
```

## 🛠️ Tecnologie Utilizzate

- **Streamlit**: Framework per web app Python
- **Pandas**: Manipolazione e analisi dati
- **Plotly**: Grafici interattivi professionali

## 📊 Indici Disponibili

### 1. MSCI World
- 23 mercati sviluppati
- ~1,500 titoli
- Esposizione globale bilanciata

### 2. S&P 500
- 500 aziende USA
- Large-cap americane
- Benchmark mercato USA

### 3. MSCI Emerging Markets
- 24 mercati emergenti
- ~1,400 titoli
- Alto potenziale di crescita

## 🔧 Personalizzazione

### Aggiungere un Nuovo Indice

Il design modulare permette di aggiungere facilmente nuovi indici. Esempio:

```python
"nasdaq100": {
    "name": "Nasdaq 100",
    "description": "...",
    "risk_profile": {
        "risk_level": "Alto",
        "volatility": "20-25% annua",
        "time_horizon": "7-10+ anni",
        "return_potential": "10-13% annuo storico"
    },
    "composition": {
        "geographic": {...},
        "sectors": {...}
    },
    "strategy": "..."
}
```

### Aggiungere Nuove Lingue

Estendi semplicemente il dizionario `CONTENT`:

```python
CONTENT = {
    "it": {...},
    "en": {...},
    "es": {...}  # Spagnolo
}
```

## 📈 Prossimi Sviluppi

- [ ] Integrazione dati real-time con yfinance
- [ ] Grafici storici performance
- [ ] Comparatore multi-indice
- [ ] Calcolatore allocazione portfolio
- [ ] Export PDF report
- [ ] Dashboard personalizzabile
- [ ] 50+ indici ETF aggiuntivi

## 🤝 Contribuire

I contributi sono benvenuti! Per favore:

1. Fai il fork del progetto
2. Crea un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. Commit delle modifiche (`git commit -m 'Add some AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## 📝 Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi `LICENSE` per maggiori informazioni.

## ⚠️ Disclaimer

Questa applicazione è stata creata esclusivamente a scopo educativo e informativo. I dati presentati sono semplificati e non devono essere utilizzati come unica base per decisioni di investimento reali. Si consiglia sempre di consultare un consulente finanziario professionista prima di prendere decisioni di investimento.

## 👨‍💻 Autore

Creato con ❤️ usando Streamlit e Python

---

**Note**: I dati mostrati sono simulati a scopo didattico. Per analisi di mercato professionali, utilizzare fonti ufficiali come MSCI, S&P Dow Jones Indices, Bloomberg, ecc.
