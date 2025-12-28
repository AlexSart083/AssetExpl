"""
AssetExpl - ETF Explorer Web App
Educational app for exploring ETF indices with multilingual support
Version 2.0 - Extended with 8 major indices
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ============================================================================
# CONFIGURAZIONE PAGINA
# ============================================================================

st.set_page_config(
    page_title="AssetExpl - ETF Explorer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CONTENUTI MULTILINGUA
# ============================================================================

CONTENT = {
    "it": {
        "app_title": "📊 AssetExpl - Esploratore ETF",
        "app_subtitle": "Esplora i principali indici ETF globali con dati interattivi",
        "sidebar_title": "⚙️ Impostazioni",
        "language_label": "Lingua",
        "select_index": "Seleziona Indice",
        "tabs": {
            "description": "📄 Descrizione",
            "statistics": "📈 Statistiche",
            "strategy": "🎯 Strategia d'Uso"
        },
        "indices": {
            "msci_world": {
                "name": "MSCI World",
                "description": """
                ### MSCI World Index
                
                L'**MSCI World Index** è un indice azionario globale che rappresenta le large e mid-cap 
                di 23 paesi sviluppati. Copre circa l'85% del mercato azionario capitalizzato in ciascun paese.
                
                #### Caratteristiche Principali:
                - **Copertura**: 23 mercati sviluppati
                - **Numero titoli**: ~1,500 azioni
                - **Capitalizzazione**: Large e Mid-cap
                - **Benchmark**: Standard per portafogli globali diversificati
                
                #### Perché sceglierlo:
                L'MSCI World è ideale per investitori che cercano un'esposizione diversificata ai mercati 
                sviluppati globali, con una forte presenza del mercato statunitense (~70%) ma anche 
                significativa esposizione a Europa e Asia-Pacifico.
                """,
                "risk_profile": {
                    "risk_level": "Medio-Alto",
                    "volatility": "15-20% annua",
                    "time_horizon": "7-10+ anni",
                    "return_potential": "7-9% annuo storico"
                },
                "composition": {
                    "geographic": {
                        "USA": 70.5,
                        "Giappone": 6.2,
                        "Regno Unito": 4.1,
                        "Francia": 3.4,
                        "Canada": 3.2,
                        "Svizzera": 2.8,
                        "Germania": 2.5,
                        "Australia": 2.1,
                        "Altri": 5.2
                    },
                    "sectors": {
                        "Tecnologia": 23.5,
                        "Finanza": 14.8,
                        "Salute": 12.3,
                        "Beni Ciclici": 11.2,
                        "Industria": 10.5,
                        "Beni di Consumo": 7.8,
                        "Energia": 4.9,
                        "Utilities": 3.2,
                        "Materiali": 4.1,
                        "Altri": 7.7
                    }
                },
                "strategy": """
                ### Come Utilizzare MSCI World nel tuo Portfolio
                
                #### 🎯 Strategia Core
                - **Portafoglio Base**: Usa MSCI World come asset principale (50-70% del portfolio)
                - **Ribilanciamento**: Annuale o semestrale
                - **Accumulo**: Piano di accumulo mensile (PAC) per ridurre il rischio timing
                
                #### ⚖️ Combinazioni Efficaci
                - **MSCI World (70%) + Obbligazioni (30%)**: Portfolio bilanciato moderato
                - **MSCI World (60%) + Emerging Markets (20%) + Obbligazioni (20%)**: Crescita con diversificazione
                - **MSCI World (80%) + Small Cap (20%)**: Aggressivo orientato all'equity
                
                #### ⚠️ Considerazioni
                - Alta esposizione USA (~70%) - considera diversificazione geografica aggiuntiva
                - Non include mercati emergenti - valuta integrazione con MSCI EM
                - Esclude small-cap - opportunità di rendimenti superiori escluse
                """
            },
            "sp500": {
                "name": "S&P 500",
                "description": """
                ### S&P 500 Index
                
                Lo **S&P 500** è l'indice più seguito al mondo, rappresentando le 500 maggiori aziende 
                quotate negli Stati Uniti. È considerato il miglior indicatore della performance 
                del mercato azionario americano.
                
                #### Caratteristiche Principali:
                - **Copertura**: Mercato USA
                - **Numero titoli**: 500 azioni
                - **Capitalizzazione**: Large-cap
                - **Benchmark**: Standard per il mercato azionario USA
                
                #### Perché sceglierlo:
                L'S&P 500 offre esposizione alle più grandi e consolidate aziende americane, 
                inclusi giganti tecnologici come Apple, Microsoft, Amazon. Storicamente ha 
                fornito rendimenti medi del 10% annuo nel lungo periodo.
                """,
                "risk_profile": {
                    "risk_level": "Medio-Alto",
                    "volatility": "15-18% annua",
                    "time_horizon": "5-10+ anni",
                    "return_potential": "9-11% annuo storico"
                },
                "composition": {
                    "geographic": {
                        "USA": 100.0
                    },
                    "sectors": {
                        "Tecnologia": 29.3,
                        "Salute": 13.2,
                        "Finanza": 12.8,
                        "Beni Ciclici": 10.9,
                        "Servizi Comunicazione": 8.7,
                        "Industria": 8.4,
                        "Beni di Consumo": 6.1,
                        "Energia": 3.8,
                        "Utilities": 2.5,
                        "Materiali": 2.4,
                        "Immobiliare": 2.0
                    }
                },
                "strategy": """
                ### Come Utilizzare S&P 500 nel tuo Portfolio
                
                #### 🎯 Strategia Core USA
                - **Esposizione USA**: Ideale per chi crede nel mercato americano
                - **Investimento Long-Term**: Buy and hold per 10+ anni
                - **Dollar Cost Averaging**: Investimenti mensili per mediare i prezzi
                
                #### ⚖️ Combinazioni Efficaci
                - **S&P 500 (60%) + International (30%) + Bonds (10%)**: Globale con focus USA
                - **S&P 500 (50%) + Nasdaq 100 (20%) + Bonds (30%)**: Tech-heavy moderato
                - **S&P 500 (70%) + REIT (15%) + Gold (15%)**: Diversificazione asset class
                
                #### ⚠️ Considerazioni
                - Concentrazione geografica al 100% USA - rischio paese
                - Alta esposizione tech (~30%) - volatile ma ad alto potenziale
                - Dominanza di mega-cap - poche opportunità small/mid cap
                - Sensibile a tassi Fed e politiche USA
                """
            },
            "msci_em": {
                "name": "MSCI Emerging Markets",
                "description": """
                ### MSCI Emerging Markets Index
                
                L'**MSCI Emerging Markets Index** cattura le large e mid-cap di 24 paesi emergenti, 
                rappresentando circa l'85% della capitalizzazione di mercato in ciascun paese.
                
                #### Caratteristiche Principali:
                - **Copertura**: 24 mercati emergenti
                - **Numero titoli**: ~1,400 azioni
                - **Capitalizzazione**: Large e Mid-cap
                - **Benchmark**: Standard per mercati emergenti
                
                #### Perché sceglierlo:
                Offre esposizione a economie in rapida crescita come Cina, India, Taiwan, Brasile. 
                Maggiore potenziale di crescita rispetto ai mercati sviluppati ma con volatilità 
                più elevata. Essenziale per diversificazione geografica.
                """,
                "risk_profile": {
                    "risk_level": "Alto",
                    "volatility": "20-25% annua",
                    "time_horizon": "10+ anni",
                    "return_potential": "8-12% annuo storico (alta variabilità)"
                },
                "composition": {
                    "geographic": {
                        "Cina": 28.5,
                        "Taiwan": 16.8,
                        "India": 18.2,
                        "Corea del Sud": 11.4,
                        "Brasile": 5.1,
                        "Arabia Saudita": 3.8,
                        "Sud Africa": 3.2,
                        "Messico": 2.4,
                        "Tailandia": 2.1,
                        "Altri": 8.5
                    },
                    "sectors": {
                        "Tecnologia": 21.4,
                        "Finanza": 20.3,
                        "Beni Ciclici": 13.8,
                        "Servizi Comunicazione": 9.7,
                        "Materiali": 8.2,
                        "Energia": 6.8,
                        "Industria": 6.1,
                        "Beni di Consumo": 5.9,
                        "Salute": 4.2,
                        "Utilities": 2.4,
                        "Altri": 1.2
                    }
                },
                "strategy": """
                ### Come Utilizzare MSCI EM nel tuo Portfolio
                
                #### 🎯 Strategia Satellite
                - **Allocazione**: 10-30% del portfolio equity
                - **Complemento**: Affianca MSCI World o S&P 500
                - **Pazienza**: Richiede orizzonte temporale lungo (10+ anni)
                
                #### ⚖️ Combinazioni Efficaci
                - **MSCI World (70%) + MSCI EM (20%) + Bonds (10%)**: Globale completo
                - **S&P 500 (60%) + MSCI EM (30%) + REIT (10%)**: Crescita aggressiva
                - **MSCI World (50%) + MSCI EM (25%) + Bonds (25%)**: Bilanciato globale
                
                #### ⚠️ Considerazioni
                - **Alta volatilità**: Oscillazioni anche >30% annue
                - **Rischio politico**: Instabilità in alcuni paesi emergenti
                - **Rischio valutario**: Esposizione a monete volatili
                - **Concentrazione Asia**: ~75% in mercati asiatici
                - **Opportunità**: Crescita demografica e espansione classe media
                """
            },
            "msci_acwi": {
                "name": "MSCI ACWI",
                "description": """
                ### MSCI All Country World Index (ACWI)
                
                L'**MSCI ACWI** è l'indice più completo per l'equity globale, combinando mercati 
                sviluppati ed emergenti. Rappresenta il 99% dell'opportunità di investimento 
                azionario globale.
                
                #### Caratteristiche Principali:
                - **Copertura**: 23 mercati sviluppati + 24 mercati emergenti
                - **Numero titoli**: ~3,000 azioni
                - **Capitalizzazione**: Large e Mid-cap
                - **Benchmark**: Il più completo indice azionario globale
                
                #### Perché sceglierlo:
                L'MSCI ACWI è la soluzione "one-stop-shop" per l'equity globale. Con una singola 
                posizione ottieni esposizione bilanciata a mercati sviluppati (~85%) ed emergenti 
                (~15%), eliminando la necessità di combinare più indici.
                """,
                "risk_profile": {
                    "risk_level": "Medio-Alto",
                    "volatility": "16-21% annua",
                    "time_horizon": "7-10+ anni",
                    "return_potential": "7-10% annuo storico"
                },
                "composition": {
                    "geographic": {
                        "USA": 62.3,
                        "Giappone": 5.4,
                        "Regno Unito": 3.6,
                        "Cina": 3.2,
                        "Francia": 3.0,
                        "Canada": 2.8,
                        "India": 2.1,
                        "Taiwan": 1.9,
                        "Svizzera": 2.4,
                        "Altri": 13.3
                    },
                    "sectors": {
                        "Tecnologia": 23.8,
                        "Finanza": 15.6,
                        "Salute": 11.9,
                        "Beni Ciclici": 11.5,
                        "Industria": 10.2,
                        "Beni di Consumo": 7.4,
                        "Servizi Comunicazione": 7.1,
                        "Energia": 4.7,
                        "Materiali": 4.3,
                        "Altri": 3.5
                    }
                },
                "strategy": """
                ### Come Utilizzare MSCI ACWI nel tuo Portfolio
                
                #### 🎯 Strategia "All-in-One"
                - **Portafoglio Semplificato**: MSCI ACWI come unico ETF equity (60-100%)
                - **Gestione Passiva**: Perfetto per approccio "set and forget"
                - **Ribilanciamento Automatico**: L'indice si aggiusta automaticamente tra DM e EM
                
                #### ⚖️ Combinazioni Efficaci
                - **MSCI ACWI (80%) + Obbligazioni (20%)**: Portfolio globale semplice
                - **MSCI ACWI (70%) + Obbligazioni (25%) + Oro (5%)**: Protezione inflazione
                - **MSCI ACWI (90%) + Small Cap (10%)**: Massima equity exposure
                
                #### ⚠️ Considerazioni
                - **Vantaggio principale**: Massima diversificazione in un solo ETF
                - **Esposizione USA**: Ancora dominante (~62%)
                - **EM inclusi**: Non serve combinare con MSCI EM
                - **TER leggermente superiore**: Rispetto a MSCI World per via degli EM
                - **Ideale per principianti**: Semplicità gestionale massima
                """
            },
            "ftse_all_world": {
                "name": "FTSE All-World",
                "description": """
                ### FTSE All-World Index
                
                Il **FTSE All-World Index** è l'alternativa di FTSE all'MSCI ACWI, offrendo 
                esposizione completa a mercati sviluppati ed emergenti con una copertura ancora 
                più ampia.
                
                #### Caratteristiche Principali:
                - **Copertura**: 49 paesi (25 sviluppati + 24 emergenti)
                - **Numero titoli**: ~4,000 azioni
                - **Capitalizzazione**: Large, Mid e Small-cap
                - **Benchmark**: Alternativa completa all'MSCI ACWI
                
                #### Perché sceglierlo:
                FTSE All-World include anche le small-cap, offrendo una copertura del 98% del 
                mercato azionario globale investibile. È la scelta preferita per chi cerca la 
                massima diversificazione possibile in un singolo strumento.
                """,
                "risk_profile": {
                    "risk_level": "Medio-Alto",
                    "volatility": "16-22% annua",
                    "time_horizon": "7-10+ anni",
                    "return_potential": "7-10% annuo storico"
                },
                "composition": {
                    "geographic": {
                        "USA": 61.8,
                        "Giappone": 5.6,
                        "Regno Unito": 3.8,
                        "Cina": 3.4,
                        "Canada": 3.1,
                        "Francia": 2.9,
                        "Svizzera": 2.5,
                        "Germania": 2.3,
                        "India": 2.2,
                        "Taiwan": 1.9,
                        "Altri": 10.5
                    },
                    "sectors": {
                        "Tecnologia": 24.1,
                        "Finanza": 15.3,
                        "Beni Ciclici": 11.8,
                        "Salute": 11.6,
                        "Industria": 10.4,
                        "Beni di Consumo": 7.2,
                        "Servizi Comunicazione": 6.9,
                        "Energia": 4.6,
                        "Materiali": 4.2,
                        "Altri": 3.9
                    }
                },
                "strategy": """
                ### Come Utilizzare FTSE All-World nel tuo Portfolio
                
                #### 🎯 Strategia Massima Diversificazione
                - **Portfolio Completo**: FTSE All-World come unico ETF equity necessario
                - **Inclusione Small-Cap**: Cattura opportunità anche in aziende più piccole
                - **Buy & Hold**: Ideale per investitori passivi a lungo termine
                
                #### ⚖️ Combinazioni Efficaci
                - **FTSE All-World (80%) + Obbligazioni Globali (20%)**: Semplicità massima
                - **FTSE All-World (70%) + Bonds (20%) + Oro (10%)**: Portfolio resiliente
                - **FTSE All-World (100%)**: Opzione 100% equity per profili aggressivi
                
                #### ⚠️ Considerazioni
                - **Copertura superiore**: Include small-cap (vs MSCI ACWI)
                - **4,000+ titoli**: Massima diversificazione disponibile
                - **Alternativa MSCI**: Metodologia leggermente diversa ma risultati simili
                - **Liquidità ETF**: Verificare gli spread bid-ask
                - **Perfetto per "Lazy Portfolio"**: Soluzione completa in un solo ETF
                """
            },
            "solactive_str": {
                "name": "Solactive €STR +8.5% Daily",
                "description": """
                ### Solactive €STR +8.5% Daily Index
                
                Il **Solactive €STR +8.5% Daily** è un indice sintetico che mira a fornire un 
                rendimento del tasso €STR (Euro Short-Term Rate) più 8.5% annualizzato. 
                Utilizzato principalmente in prodotti assicurativi italiani (polizze Unit-Linked).
                
                #### Caratteristiche Principali:
                - **Target**: €STR + 8.5% annuo
                - **Tipologia**: Indice sintetico a rendimento target
                - **Sottostante**: Portafoglio dinamico multi-asset
                - **Uso**: Prodotti assicurativi e risparmio gestito
                
                #### Perché sceglierlo:
                Questo indice non è direttamente investibile via ETF tradizionali, ma è incorporato 
                in polizze vita e fondi assicurativi. Il rendimento target dell'8.5% sopra il tasso 
                risk-free lo rende attraente, ma comporta rischi significativi e costi elevati.
                """,
                "risk_profile": {
                    "risk_level": "Variabile (Medio-Alto)",
                    "volatility": "Dipende dal sottostante (10-25%)",
                    "time_horizon": "5-10+ anni",
                    "return_potential": "€STR + 8.5% (target, non garantito)"
                },
                "composition": {
                    "geographic": {
                        "Esposizione Globale": 60.0,
                        "Europa": 25.0,
                        "USA": 10.0,
                        "Altri": 5.0
                    },
                    "sectors": {
                        "Azionario": 40.0,
                        "Obbligazionario": 35.0,
                        "Alternative": 15.0,
                        "Liquidità": 10.0
                    }
                },
                "strategy": """
                ### Come Valutare Prodotti legati a €STR +8.5%
                
                #### 🎯 Attenzione ai Prodotti Assicurativi
                - **Non è un ETF**: Disponibile solo tramite polizze unit-linked
                - **Costi elevati**: Commissioni di gestione e caricamenti significativi
                - **Rendimento non garantito**: Il target può non essere raggiunto
                
                #### ⚖️ Alternative più Trasparenti
                - **ETF Multi-Asset**: Maggiore trasparenza e costi inferiori
                - **Portfolio 60/40**: Azionario globale + obbligazioni
                - **Robo-Advisor**: Gestione automatica a costi contenuti
                
                #### ⚠️ CONSIDERAZIONI CRITICHE
                - **⚠️ COSTI NASCOSTI**: Verifica sempre il TER totale e i caricamenti
                - **⚠️ LIQUIDITÀ**: Vincoli temporali e penali di uscita anticipata
                - **⚠️ RENDIMENTO TARGET**: Non è garantito, solo un obiettivo
                - **⚠️ COMPLESSITÀ**: Struttura difficile da comprendere per investitori retail
                - **✅ ALTERNATIVA**: Considera ETF bilanciati con costi <0.30% annui
                - **✅ TRASPARENZA**: Preferisci strumenti quotati con prezzi real-time
                """
            },
            "msci_europe": {
                "name": "MSCI Europe",
                "description": """
                ### MSCI Europe Index
                
                L'**MSCI Europe Index** rappresenta le large e mid-cap di 15 paesi europei 
                sviluppati, offrendo esposizione concentrata al mercato azionario europeo.
                
                #### Caratteristiche Principali:
                - **Copertura**: 15 paesi europei sviluppati
                - **Numero titoli**: ~430 azioni
                - **Capitalizzazione**: Large e Mid-cap
                - **Benchmark**: Standard per equity europea
                
                #### Perché sceglierlo:
                MSCI Europe è ideale per chi vuole esposizione all'Europa sviluppata, includendo 
                sia paesi dell'Eurozona che UK, Svizzera, e paesi nordici. Offre accesso a 
                leader globali in settori come lusso, farmaceutico, automotive e finanziario.
                """,
                "risk_profile": {
                    "risk_level": "Medio",
                    "volatility": "14-19% annua",
                    "time_horizon": "7-10+ anni",
                    "return_potential": "6-8% annuo storico"
                },
                "composition": {
                    "geographic": {
                        "Regno Unito": 23.5,
                        "Francia": 19.2,
                        "Svizzera": 16.8,
                        "Germania": 14.3,
                        "Paesi Bassi": 7.2,
                        "Svezia": 5.8,
                        "Danimarca": 4.1,
                        "Spagna": 3.9,
                        "Italia": 3.2,
                        "Altri": 2.0
                    },
                    "sectors": {
                        "Finanza": 18.4,
                        "Salute": 16.2,
                        "Industria": 14.8,
                        "Beni Ciclici": 12.1,
                        "Beni di Consumo": 10.9,
                        "Tecnologia": 8.3,
                        "Energia": 6.7,
                        "Materiali": 5.9,
                        "Utilities": 4.2,
                        "Altri": 2.5
                    }
                },
                "strategy": """
                ### Come Utilizzare MSCI Europe nel tuo Portfolio
                
                #### 🎯 Strategia Regional Focus
                - **Esposizione Europa**: Ideale per ridurre dipendenza USA
                - **Diversificazione Geografica**: Complementa S&P 500 o Nasdaq
                - **Valutazioni Attraenti**: Storicamente più economico rispetto a USA
                
                #### ⚖️ Combinazioni Efficaci
                - **S&P 500 (50%) + MSCI Europe (30%) + MSCI EM (20%)**: Globale bilanciato
                - **MSCI Europe (60%) + MSCI USA (30%) + Bonds (10%)**: Riduzione home bias USA
                - **MSCI Europe (40%) + MSCI World (40%) + Bonds (20%)**: Tilt europeo
                
                #### ⚠️ Considerazioni
                - **Crescita inferiore a USA**: Storicamente rendimenti più bassi
                - **Include UK**: Circa 24% in aziende britanniche
                - **Focus Value**: Meno tech, più finanza e industria
                - **Diversificazione valutaria**: Esposizione GBP, CHF, EUR
                - **Opportunità**: Valutazioni più basse possono offrire potenziale upside
                """
            },
            "msci_emu": {
                "name": "MSCI EMU",
                "description": """
                ### MSCI EMU Index (European Monetary Union)
                
                L'**MSCI EMU Index** rappresenta le large e mid-cap dei paesi dell'Eurozona, 
                offrendo esposizione pura ai mercati che utilizzano l'Euro come valuta.
                
                #### Caratteristiche Principali:
                - **Copertura**: 10 paesi dell'Eurozona
                - **Numero titoli**: ~240 azioni
                - **Capitalizzazione**: Large e Mid-cap
                - **Benchmark**: Standard per equity Eurozona
                
                #### Perché sceglierlo:
                MSCI EMU elimina il rischio valutario per investitori europei, concentrandosi 
                esclusivamente su paesi che usano l'Euro. Ideale per chi vuole esposizione 
                all'Eurozona senza l'influenza di UK e Svizzera.
                """,
                "risk_profile": {
                    "risk_level": "Medio",
                    "volatility": "15-20% annua",
                    "time_horizon": "7-10+ anni",
                    "return_potential": "5-8% annuo storico"
                },
                "composition": {
                    "geographic": {
                        "Francia": 35.8,
                        "Germania": 27.2,
                        "Paesi Bassi": 13.4,
                        "Spagna": 8.9,
                        "Italia": 7.6,
                        "Irlanda": 3.2,
                        "Belgio": 2.1,
                        "Finlandia": 1.2,
                        "Altri": 0.6
                    },
                    "sectors": {
                        "Finanza": 17.8,
                        "Industria": 16.4,
                        "Salute": 14.2,
                        "Beni Ciclici": 13.6,
                        "Beni di Consumo": 11.8,
                        "Tecnologia": 9.3,
                        "Energia": 5.9,
                        "Materiali": 5.7,
                        "Utilities": 3.8,
                        "Altri": 1.5
                    }
                },
                "strategy": """
                ### Come Utilizzare MSCI EMU nel tuo Portfolio
                
                #### 🎯 Strategia Eurozona
                - **No Rischio Cambio**: Ideale per investitori italiani/europei
                - **Home Region Bias**: Investire nella propria area geografica
                - **Accumulo EUR**: Esposizione 100% in Euro
                
                #### ⚖️ Combinazioni Efficaci
                - **MSCI EMU (40%) + S&P 500 (40%) + Bonds EUR (20%)**: Bilanciato EUR-USA
                - **MSCI EMU (60%) + MSCI World ex-EMU (30%) + Bonds (10%)**: Tilt Eurozona
                - **MSCI EMU (50%) + MSCI EM (20%) + Bonds (30%)**: Diversificazione completa
                
                #### ⚠️ Considerazioni
                - **Esclude UK e Svizzera**: Elimina 2 dei maggiori mercati europei
                - **Concentrazione Francia-Germania**: ~63% del peso totale
                - **Meno tech**: Sottopesato in tecnologia rispetto a indici globali
                - **Rischio politico UE**: Esposto a dinamiche politiche dell'Eurozona
                - **Per investitori EUR**: Elimina rischio cambio ma riduce diversificazione
                - **Valutazioni**: Generalmente più convenienti rispetto a mercati USA
                """
            }
        },
        "metrics_labels": {
            "risk": "Livello di Rischio",
            "volatility": "Volatilità",
            "horizon": "Orizzonte Temporale",
            "returns": "Rendimento Atteso"
        },
        "chart_titles": {
            "geographic": "Composizione Geografica",
            "sectors": "Composizione Settoriale"
        }
    },
    "en": {
        "app_title": "📊 AssetExpl - ETF Explorer",
        "app_subtitle": "Explore major global ETF indices with interactive data",
        "sidebar_title": "⚙️ Settings",
        "language_label": "Language",
        "select_index": "Select Index",
        "tabs": {
            "description": "📄 Description",
            "statistics": "📈 Statistics",
            "strategy": "🎯 Usage Strategy"
        },
        "indices": {
            "msci_world": {
                "name": "MSCI World",
                "description": """
                ### MSCI World Index
                
                The **MSCI World Index** is a global equity index representing large and mid-cap 
                stocks from 23 developed countries. It covers approximately 85% of the free 
                float-adjusted market capitalization in each country.
                
                #### Key Features:
                - **Coverage**: 23 developed markets
                - **Number of stocks**: ~1,500 companies
                - **Capitalization**: Large and Mid-cap
                - **Benchmark**: Standard for global diversified portfolios
                
                #### Why choose it:
                MSCI World is ideal for investors seeking diversified exposure to global developed 
                markets, with strong US market presence (~70%) but also significant exposure to 
                Europe and Asia-Pacific.
                """,
                "risk_profile": {
                    "risk_level": "Medium-High",
                    "volatility": "15-20% annual",
                    "time_horizon": "7-10+ years",
                    "return_potential": "7-9% historical annual"
                },
                "composition": {
                    "geographic": {
                        "USA": 70.5,
                        "Japan": 6.2,
                        "United Kingdom": 4.1,
                        "France": 3.4,
                        "Canada": 3.2,
                        "Switzerland": 2.8,
                        "Germany": 2.5,
                        "Australia": 2.1,
                        "Others": 5.2
                    },
                    "sectors": {
                        "Technology": 23.5,
                        "Finance": 14.8,
                        "Healthcare": 12.3,
                        "Consumer Cyclical": 11.2,
                        "Industrials": 10.5,
                        "Consumer Staples": 7.8,
                        "Energy": 4.9,
                        "Utilities": 3.2,
                        "Materials": 4.1,
                        "Others": 7.7
                    }
                },
                "strategy": """
                ### How to Use MSCI World in Your Portfolio
                
                #### 🎯 Core Strategy
                - **Base Portfolio**: Use MSCI World as main asset (50-70% of portfolio)
                - **Rebalancing**: Annual or semi-annual
                - **Accumulation**: Monthly investment plan (DCA) to reduce timing risk
                
                #### ⚖️ Effective Combinations
                - **MSCI World (70%) + Bonds (30%)**: Moderate balanced portfolio
                - **MSCI World (60%) + Emerging Markets (20%) + Bonds (20%)**: Growth with diversification
                - **MSCI World (80%) + Small Cap (20%)**: Aggressive equity-oriented
                
                #### ⚠️ Considerations
                - High US exposure (~70%) - consider additional geographic diversification
                - Excludes emerging markets - evaluate integration with MSCI EM
                - Excludes small-cap - superior return opportunities excluded
                """
            },
            "sp500": {
                "name": "S&P 500",
                "description": """
                ### S&P 500 Index
                
                The **S&P 500** is the world's most followed index, representing the 500 largest 
                publicly traded companies in the United States. It's considered the best indicator 
                of US stock market performance.
                
                #### Key Features:
                - **Coverage**: US Market
                - **Number of stocks**: 500 companies
                - **Capitalization**: Large-cap
                - **Benchmark**: Standard for US equity market
                
                #### Why choose it:
                The S&P 500 offers exposure to the largest and most established American companies, 
                including tech giants like Apple, Microsoft, Amazon. Historically has provided 
                average returns of 10% annually over the long term.
                """,
                "risk_profile": {
                    "risk_level": "Medium-High",
                    "volatility": "15-18% annual",
                    "time_horizon": "5-10+ years",
                    "return_potential": "9-11% historical annual"
                },
                "composition": {
                    "geographic": {
                        "USA": 100.0
                    },
                    "sectors": {
                        "Technology": 29.3,
                        "Healthcare": 13.2,
                        "Finance": 12.8,
                        "Consumer Cyclical": 10.9,
                        "Communication Services": 8.7,
                        "Industrials": 8.4,
                        "Consumer Staples": 6.1,
                        "Energy": 3.8,
                        "Utilities": 2.5,
                        "Materials": 2.4,
                        "Real Estate": 2.0
                    }
                },
                "strategy": """
                ### How to Use S&P 500 in Your Portfolio
                
                #### 🎯 Core USA Strategy
                - **US Exposure**: Ideal for those bullish on American market
                - **Long-Term Investment**: Buy and hold for 10+ years
                - **Dollar Cost Averaging**: Monthly investments to average prices
                
                #### ⚖️ Effective Combinations
                - **S&P 500 (60%) + International (30%) + Bonds (10%)**: Global with US focus
                - **S&P 500 (50%) + Nasdaq 100 (20%) + Bonds (30%)**: Moderate tech-heavy
                - **S&P 500 (70%) + REIT (15%) + Gold (15%)**: Asset class diversification
                
                #### ⚠️ Considerations
                - 100% US geographic concentration - country risk
                - High tech exposure (~30%) - volatile but high potential
                - Mega-cap dominance - few small/mid cap opportunities
                - Sensitive to Fed rates and US policies
                """
            },
            "msci_em": {
                "name": "MSCI Emerging Markets",
                "description": """
                ### MSCI Emerging Markets Index
                
                The **MSCI Emerging Markets Index** captures large and mid-cap representation 
                across 24 emerging market countries, representing approximately 85% of the 
                free float-adjusted market capitalization in each country.
                
                #### Key Features:
                - **Coverage**: 24 emerging markets
                - **Number of stocks**: ~1,400 companies
                - **Capitalization**: Large and Mid-cap
                - **Benchmark**: Standard for emerging markets
                
                #### Why choose it:
                Offers exposure to rapidly growing economies like China, India, Taiwan, Brazil. 
                Higher growth potential than developed markets but with higher volatility. 
                Essential for geographic diversification.
                """,
                "risk_profile": {
                    "risk_level": "High",
                    "volatility": "20-25% annual",
                    "time_horizon": "10+ years",
                    "return_potential": "8-12% historical annual (high variability)"
                },
                "composition": {
                    "geographic": {
                        "China": 28.5,
                        "Taiwan": 16.8,
                        "India": 18.2,
                        "South Korea": 11.4,
                        "Brazil": 5.1,
                        "Saudi Arabia": 3.8,
                        "South Africa": 3.2,
                        "Mexico": 2.4,
                        "Thailand": 2.1,
                        "Others": 8.5
                    },
                    "sectors": {
                        "Technology": 21.4,
                        "Finance": 20.3,
                        "Consumer Cyclical": 13.8,
                        "Communication Services": 9.7,
                        "Materials": 8.2,
                        "Energy": 6.8,
                        "Industrials": 6.1,
                        "Consumer Staples": 5.9,
                        "Healthcare": 4.2,
                        "Utilities": 2.4,
                        "Others": 1.2
                    }
                },
                "strategy": """
                ### How to Use MSCI EM in Your Portfolio
                
                #### 🎯 Satellite Strategy
                - **Allocation**: 10-30% of equity portfolio
                - **Complement**: Pair with MSCI World or S&P 500
                - **Patience**: Requires long time horizon (10+ years)
                
                #### ⚖️ Effective Combinations
                - **MSCI World (70%) + MSCI EM (20%) + Bonds (10%)**: Complete global
                - **S&P 500 (60%) + MSCI EM (30%) + REIT (10%)**: Aggressive growth
                - **MSCI World (50%) + MSCI EM (25%) + Bonds (25%)**: Balanced global
                
                #### ⚠️ Considerations
                - **High volatility**: Swings can exceed 30% annually
                - **Political risk**: Instability in some emerging countries
                - **Currency risk**: Exposure to volatile currencies
                - **Asia concentration**: ~75% in Asian markets
                - **Opportunities**: Demographic growth and middle class expansion
                """
            },
            "msci_acwi": {
                "name": "MSCI ACWI",
                "description": """
                ### MSCI All Country World Index (ACWI)
                
                The **MSCI ACWI** is the most comprehensive global equity index, combining developed 
                and emerging markets. It represents 99% of the global investable equity opportunity.
                
                #### Key Features:
                - **Coverage**: 23 developed + 24 emerging markets
                - **Number of stocks**: ~3,000 companies
                - **Capitalization**: Large and Mid-cap
                - **Benchmark**: Most complete global equity index
                
                #### Why choose it:
                MSCI ACWI is the "one-stop-shop" solution for global equity. With a single position 
                you get balanced exposure to developed (~85%) and emerging (~15%) markets, 
                eliminating the need to combine multiple indices.
                """,
                "risk_profile": {
                    "risk_level": "Medium-High",
                    "volatility": "16-21% annual",
                    "time_horizon": "7-10+ years",
                    "return_potential": "7-10% historical annual"
                },
                "composition": {
                    "geographic": {
                        "USA": 62.3,
                        "Japan": 5.4,
                        "United Kingdom": 3.6,
                        "China": 3.2,
                        "France": 3.0,
                        "Canada": 2.8,
                        "India": 2.1,
                        "Taiwan": 1.9,
                        "Switzerland": 2.4,
                        "Others": 13.3
                    },
                    "sectors": {
                        "Technology": 23.8,
                        "Finance": 15.6,
                        "Healthcare": 11.9,
                        "Consumer Cyclical": 11.5,
                        "Industrials": 10.2,
                        "Consumer Staples": 7.4,
                        "Communication Services": 7.1,
                        "Energy": 4.7,
                        "Materials": 4.3,
                        "Others": 3.5
                    }
                },
                "strategy": """
                ### How to Use MSCI ACWI in Your Portfolio
                
                #### 🎯 "All-in-One" Strategy
                - **Simplified Portfolio**: MSCI ACWI as single equity ETF (60-100%)
                - **Passive Management**: Perfect for "set and forget" approach
                - **Automatic Rebalancing**: Index auto-adjusts between DM and EM
                
                #### ⚖️ Effective Combinations
                - **MSCI ACWI (80%) + Bonds (20%)**: Simple global portfolio
                - **MSCI ACWI (70%) + Bonds (25%) + Gold (5%)**: Inflation protection
                - **MSCI ACWI (90%) + Small Cap (10%)**: Maximum equity exposure
                
                #### ⚠️ Considerations
                - **Main advantage**: Maximum diversification in one ETF
                - **US exposure**: Still dominant (~62%)
                - **EM included**: No need to combine with MSCI EM
                - **Slightly higher TER**: Compared to MSCI World due to EM inclusion
                - **Ideal for beginners**: Maximum management simplicity
                """
            },
            "ftse_all_world": {
                "name": "FTSE All-World",
                "description": """
                ### FTSE All-World Index
                
                The **FTSE All-World Index** is FTSE's alternative to MSCI ACWI, offering 
                comprehensive exposure to developed and emerging markets with even broader coverage.
                
                #### Key Features:
                - **Coverage**: 49 countries (25 developed + 24 emerging)
                - **Number of stocks**: ~4,000 companies
                - **Capitalization**: Large, Mid and Small-cap
                - **Benchmark**: Comprehensive alternative to MSCI ACWI
                
                #### Why choose it:
                FTSE All-World also includes small-caps, providing coverage of 98% of the global 
                investable equity market. The preferred choice for those seeking maximum 
                diversification in a single instrument.
                """,
                "risk_profile": {
                    "risk_level": "Medium-High",
                    "volatility": "16-22% annual",
                    "time_horizon": "7-10+ years",
                    "return_potential": "7-10% historical annual"
                },
                "composition": {
                    "geographic": {
                        "USA": 61.8,
                        "Japan": 5.6,
                        "United Kingdom": 3.8,
                        "China": 3.4,
                        "Canada": 3.1,
                        "France": 2.9,
                        "Switzerland": 2.5,
                        "Germany": 2.3,
                        "India": 2.2,
                        "Taiwan": 1.9,
                        "Others": 10.5
                    },
                    "sectors": {
                        "Technology": 24.1,
                        "Finance": 15.3,
                        "Consumer Cyclical": 11.8,
                        "Healthcare": 11.6,
                        "Industrials": 10.4,
                        "Consumer Staples": 7.2,
                        "Communication Services": 6.9,
                        "Energy": 4.6,
                        "Materials": 4.2,
                        "Others": 3.9
                    }
                },
                "strategy": """
                ### How to Use FTSE All-World in Your Portfolio
                
                #### 🎯 Maximum Diversification Strategy
                - **Complete Portfolio**: FTSE All-World as only equity ETF needed
                - **Small-Cap Inclusion**: Captures opportunities in smaller companies too
                - **Buy & Hold**: Ideal for long-term passive investors
                
                #### ⚖️ Effective Combinations
                - **FTSE All-World (80%) + Global Bonds (20%)**: Maximum simplicity
                - **FTSE All-World (70%) + Bonds (20%) + Gold (10%)**: Resilient portfolio
                - **FTSE All-World (100%)**: 100% equity option for aggressive profiles
                
                #### ⚠️ Considerations
                - **Superior coverage**: Includes small-cap (vs MSCI ACWI)
                - **4,000+ holdings**: Maximum available diversification
                - **MSCI alternative**: Slightly different methodology but similar results
                - **ETF liquidity**: Check bid-ask spreads
                - **Perfect for "Lazy Portfolio"**: Complete solution in one ETF
                """
            },
            "solactive_str": {
                "name": "Solactive €STR +8.5% Daily",
                "description": """
                ### Solactive €STR +8.5% Daily Index
                
                The **Solactive €STR +8.5% Daily** is a synthetic index aiming to provide a return 
                of the €STR (Euro Short-Term Rate) plus 8.5% annualized. Primarily used in Italian 
                insurance products (Unit-Linked policies).
                
                #### Key Features:
                - **Target**: €STR + 8.5% annual
                - **Type**: Synthetic target return index
                - **Underlying**: Dynamic multi-asset portfolio
                - **Use**: Insurance products and managed savings
                
                #### Why consider it:
                This index is not directly investable via traditional ETFs but is embedded in life 
                insurance policies and insurance funds. The 8.5% target return above the risk-free 
                rate makes it attractive, but carries significant risks and high costs.
                """,
                "risk_profile": {
                    "risk_level": "Variable (Medium-High)",
                    "volatility": "Depends on underlying (10-25%)",
                    "time_horizon": "5-10+ years",
                    "return_potential": "€STR + 8.5% (target, not guaranteed)"
                },
                "composition": {
                    "geographic": {
                        "Global Exposure": 60.0,
                        "Europe": 25.0,
                        "USA": 10.0,
                        "Others": 5.0
                    },
                    "sectors": {
                        "Equity": 40.0,
                        "Fixed Income": 35.0,
                        "Alternatives": 15.0,
                        "Cash": 10.0
                    }
                },
                "strategy": """
                ### How to Evaluate €STR +8.5% Products
                
                #### 🎯 Beware of Insurance Products
                - **Not an ETF**: Only available through unit-linked policies
                - **High costs**: Significant management fees and loadings
                - **Return not guaranteed**: Target may not be achieved
                
                #### ⚖️ More Transparent Alternatives
                - **Multi-Asset ETFs**: Greater transparency and lower costs
                - **60/40 Portfolio**: Global equity + bonds
                - **Robo-Advisors**: Automatic management at contained costs
                
                #### ⚠️ CRITICAL CONSIDERATIONS
                - **⚠️ HIDDEN COSTS**: Always verify total TER and loadings
                - **⚠️ LIQUIDITY**: Time constraints and early exit penalties
                - **⚠️ TARGET RETURN**: Not guaranteed, only an objective
                - **⚠️ COMPLEXITY**: Difficult structure for retail investors to understand
                - **✅ ALTERNATIVE**: Consider balanced ETFs with costs <0.30% annual
                - **✅ TRANSPARENCY**: Prefer listed instruments with real-time pricing
                """
            },
            "msci_europe": {
                "name": "MSCI Europe",
                "description": """
                ### MSCI Europe Index
                
                The **MSCI Europe Index** represents large and mid-cap stocks from 15 developed 
                European countries, offering concentrated exposure to the European equity market.
                
                #### Key Features:
                - **Coverage**: 15 developed European countries
                - **Number of stocks**: ~430 companies
                - **Capitalization**: Large and Mid-cap
                - **Benchmark**: Standard for European equity
                
                #### Why choose it:
                MSCI Europe is ideal for those seeking exposure to developed Europe, including both 
                Eurozone countries and UK, Switzerland, and Nordic countries. Provides access to 
                global leaders in sectors like luxury, pharmaceuticals, automotive, and finance.
                """,
                "risk_profile": {
                    "risk_level": "Medium",
                    "volatility": "14-19% annual",
                    "time_horizon": "7-10+ years",
                    "return_potential": "6-8% historical annual"
                },
                "composition": {
                    "geographic": {
                        "United Kingdom": 23.5,
                        "France": 19.2,
                        "Switzerland": 16.8,
                        "Germany": 14.3,
                        "Netherlands": 7.2,
                        "Sweden": 5.8,
                        "Denmark": 4.1,
                        "Spain": 3.9,
                        "Italy": 3.2,
                        "Others": 2.0
                    },
                    "sectors": {
                        "Finance": 18.4,
                        "Healthcare": 16.2,
                        "Industrials": 14.8,
                        "Consumer Cyclical": 12.1,
                        "Consumer Staples": 10.9,
                        "Technology": 8.3,
                        "Energy": 6.7,
                        "Materials": 5.9,
                        "Utilities": 4.2,
                        "Others": 2.5
                    }
                },
                "strategy": """
                ### How to Use MSCI Europe in Your Portfolio
                
                #### 🎯 Regional Focus Strategy
                - **Europe Exposure**: Ideal for reducing US dependency
                - **Geographic Diversification**: Complements S&P 500 or Nasdaq
                - **Attractive Valuations**: Historically cheaper than US
                
                #### ⚖️ Effective Combinations
                - **S&P 500 (50%) + MSCI Europe (30%) + MSCI EM (20%)**: Balanced global
                - **MSCI Europe (60%) + MSCI USA (30%) + Bonds (10%)**: Reduce US home bias
                - **MSCI Europe (40%) + MSCI World (40%) + Bonds (20%)**: European tilt
                
                #### ⚠️ Considerations
                - **Lower growth than US**: Historically lower returns
                - **Includes UK**: About 24% in British companies
                - **Value focus**: Less tech, more finance and industrials
                - **Currency diversification**: Exposure to GBP, CHF, EUR
                - **Opportunity**: Lower valuations may offer upside potential
                """
            },
            "msci_emu": {
                "name": "MSCI EMU",
                "description": """
                ### MSCI EMU Index (European Monetary Union)
                
                The **MSCI EMU Index** represents large and mid-cap stocks from Eurozone countries, 
                offering pure exposure to markets using the Euro as currency.
                
                #### Key Features:
                - **Coverage**: 10 Eurozone countries
                - **Number of stocks**: ~240 companies
                - **Capitalization**: Large and Mid-cap
                - **Benchmark**: Standard for Eurozone equity
                
                #### Why choose it:
                MSCI EMU eliminates currency risk for European investors, focusing exclusively on 
                countries using the Euro. Ideal for those wanting Eurozone exposure without the 
                influence of UK and Switzerland.
                """,
                "risk_profile": {
                    "risk_level": "Medium",
                    "volatility": "15-20% annual",
                    "time_horizon": "7-10+ years",
                    "return_potential": "5-8% historical annual"
                },
                "composition": {
                    "geographic": {
                        "France": 35.8,
                        "Germany": 27.2,
                        "Netherlands": 13.4,
                        "Spain": 8.9,
                        "Italy": 7.6,
                        "Ireland": 3.2,
                        "Belgium": 2.1,
                        "Finland": 1.2,
                        "Others": 0.6
                    },
                    "sectors": {
                        "Finance": 17.8,
                        "Industrials": 16.4,
                        "Healthcare": 14.2,
                        "Consumer Cyclical": 13.6,
                        "Consumer Staples": 11.8,
                        "Technology": 9.3,
                        "Energy": 5.9,
                        "Materials": 5.7,
                        "Utilities": 3.8,
                        "Others": 1.5
                    }
                },
                "strategy": """
                ### How to Use MSCI EMU in Your Portfolio
                
                #### 🎯 Eurozone Strategy
                - **No Currency Risk**: Ideal for Italian/European investors
                - **Home Region Bias**: Invest in your own geographic area
                - **EUR Accumulation**: 100% Euro exposure
                
                #### ⚖️ Effective Combinations
                - **MSCI EMU (40%) + S&P 500 (40%) + EUR Bonds (20%)**: Balanced EUR-USA
                - **MSCI EMU (60%) + MSCI World ex-EMU (30%) + Bonds (10%)**: Eurozone tilt
                - **MSCI EMU (50%) + MSCI EM (20%) + Bonds (30%)**: Complete diversification
                
                #### ⚠️ Considerations
                - **Excludes UK and Switzerland**: Removes 2 of Europe's largest markets
                - **France-Germany concentration**: ~63% of total weight
                - **Less tech**: Underweight in technology vs global indices
                - **EU political risk**: Exposed to Eurozone political dynamics
                - **For EUR investors**: Eliminates currency risk but reduces diversification
                - **Valuations**: Generally more attractive than US markets
                """
            }
        },
        "metrics_labels": {
            "risk": "Risk Level",
            "volatility": "Volatility",
            "horizon": "Time Horizon",
            "returns": "Expected Returns"
        },
        "chart_titles": {
            "geographic": "Geographic Composition",
            "sectors": "Sector Composition"
        }
    }
}

# ============================================================================
# FUNZIONI HELPER
# ============================================================================

def create_pie_chart(data, title, lang):
    """Crea un grafico a torta professionale con Plotly"""
    df = pd.DataFrame(list(data.items()), columns=['Category', 'Percentage'])
    
    fig = go.Figure(data=[go.Pie(
        labels=df['Category'],
        values=df['Percentage'],
        hole=0.4,
        marker=dict(
            colors=px.colors.qualitative.Set3,
            line=dict(color='white', width=2)
        ),
        textposition='auto',
        textinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>%{percent}<br><extra></extra>'
    )])
    
    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor='center', font=dict(size=18)),
        showlegend=True,
        height=450,
        margin=dict(t=80, b=40, l=40, r=40),
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.05
        )
    )
    
    return fig

def create_bar_chart(data, title, lang):
    """Crea un grafico a barre orizzontale con Plotly"""
    df = pd.DataFrame(list(data.items()), columns=['Category', 'Percentage'])
    df = df.sort_values('Percentage', ascending=True)
    
    fig = go.Figure(data=[go.Bar(
        x=df['Percentage'],
        y=df['Category'],
        orientation='h',
        marker=dict(
            color=df['Percentage'],
            colorscale='Viridis',
            line=dict(color='white', width=1)
        ),
        text=df['Percentage'].apply(lambda x: f'{x:.1f}%'),
        textposition='auto',
        hovertemplate='<b>%{y}</b><br>%{x:.1f}%<extra></extra>'
    )])
    
    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor='center', font=dict(size=18)),
        xaxis=dict(title='Percentage (%)', showgrid=True, gridcolor='lightgray'),
        yaxis=dict(title=''),
        height=450,
        margin=dict(t=80, b=60, l=150, r=40),
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

def display_risk_metrics(risk_data, labels, lang):
    """Visualizza le metriche di rischio in colonne"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label=labels['risk'],
            value=risk_data['risk_level'],
            delta=None
        )
    
    with col2:
        st.metric(
            label=labels['volatility'],
            value=risk_data['volatility'],
            delta=None
        )
    
    with col3:
        st.metric(
            label=labels['horizon'],
            value=risk_data['time_horizon'],
            delta=None
        )
    
    with col4:
        st.metric(
            label=labels['returns'],
            value=risk_data['return_potential'],
            delta=None
        )

# ============================================================================
# INTERFACCIA PRINCIPALE
# ============================================================================

def main():
    # Sidebar - Impostazioni
    with st.sidebar:
        st.title(CONTENT["it"]["sidebar_title"])
        
        # Selezione Lingua
        language = st.selectbox(
            "🌐 " + CONTENT["it"]["language_label"],
            options=["it", "en"],
            format_func=lambda x: "🇮🇹 Italiano" if x == "it" else "🇬🇧 English",
            index=0
        )
        
        st.divider()
        
        # Selezione Indice
        content = CONTENT[language]
        index_options = {
            "msci_world": content["indices"]["msci_world"]["name"],
            "sp500": content["indices"]["sp500"]["name"],
            "msci_em": content["indices"]["msci_em"]["name"],
            "msci_acwi": content["indices"]["msci_acwi"]["name"],
            "ftse_all_world": content["indices"]["ftse_all_world"]["name"],
            "solactive_str": content["indices"]["solactive_str"]["name"],
            "msci_europe": content["indices"]["msci_europe"]["name"],
            "msci_emu": content["indices"]["msci_emu"]["name"]
        }
        
        selected_index = st.selectbox(
            "📊 " + content["select_index"],
            options=list(index_options.keys()),
            format_func=lambda x: index_options[x]
        )
        
        st.divider()
        
        # Info app
        st.info(
            """
            **AssetExpl v2.0**
            
            Educational ETF Explorer
            
            8 Major Global Indices
            
            Developed with Streamlit
            """
        )
    
    # Header
    st.title(content["app_title"])
    st.markdown(f"*{content['app_subtitle']}*")
    st.divider()
    
    # Dati indice selezionato
    index_data = content["indices"][selected_index]
    
    # Tabs
    tab1, tab2, tab3 = st.tabs([
        content["tabs"]["description"],
        content["tabs"]["statistics"],
        content["tabs"]["strategy"]
    ])
    
    # TAB 1: Descrizione
    with tab1:
        st.markdown(index_data["description"])
    
    # TAB 2: Statistiche
    with tab2:
        st.subheader("📊 " + (
            "Profilo Rischio/Rendimento" if language == "it" else "Risk/Return Profile"
        ))
        
        # Metriche di rischio
        display_risk_metrics(
            index_data["risk_profile"],
            content["metrics_labels"],
            language
        )
        
        st.divider()
        
        # Grafici di composizione
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(content["chart_titles"]["geographic"])
            fig_geo = create_pie_chart(
                index_data["composition"]["geographic"],
                content["chart_titles"]["geographic"],
                language
            )
            st.plotly_chart(fig_geo, use_container_width=True)
        
        with col2:
            st.subheader(content["chart_titles"]["sectors"])
            fig_sectors = create_bar_chart(
                index_data["composition"]["sectors"],
                content["chart_titles"]["sectors"],
                language
            )
            st.plotly_chart(fig_sectors, use_container_width=True)
    
    # TAB 3: Strategia
    with tab3:
        st.markdown(index_data["strategy"])
    
    # Footer
    st.divider()
    st.caption(
        "💡 " + (
            "I dati mostrati sono a scopo puramente didattico. Per investimenti reali, consulta un consulente finanziario."
            if language == "it"
            else "The data shown is for educational purposes only. For real investments, consult a financial advisor."
        )
    )

if __name__ == "__main__":
    main()
