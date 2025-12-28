"""
AssetExpl - ETF Explorer Web App
Educational app for exploring ETF indices with multilingual support
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
            "msci_em": content["indices"]["msci_em"]["name"]
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
            **AssetExpl v1.0**
            
            Educational ETF Explorer
            
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
