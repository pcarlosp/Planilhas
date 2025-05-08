
import streamlit as st
import pandas as pd
import os
from datetime import datetime

# CONFIGURAÇÃO DO CAMINHO PADRÃO
CAMINHO_PLANILHAS = 'planilhas'
ARQUIVO_MODELO = 'modelo a ser seguido.xlsx'

st.set_page_config(page_title='Relatório de Consumo Diário', layout='wide')
st.title('📊 Painel Diário de Consumo de Combustível')

# Selecionar data
arquivos = [f for f in os.listdir(CAMINHO_PLANILHAS) if f.endswith('.xlsx') and not f.startswith('modelo')]
datas_disponiveis = sorted([
    f.replace("Relatorio_KML_", "").replace(".xlsx", "") for f in arquivos if "Relatorio_KML_" in f
])

if not datas_disponiveis:
    st.warning("Nenhum relatório encontrado na pasta.")
else:
    data_escolhida = st.selectbox("Selecione a data do relatório:", datas_disponiveis[::-1])
    arquivo_escolhido = f"Relatorio_KML_{data_escolhida}.xlsx"
    caminho_completo = os.path.join(CAMINHO_PLANILHAS, arquivo_escolhido)

    try:
        df = pd.read_excel(caminho_completo)
        st.success(f"Relatório carregado: {arquivo_escolhido}")
        st.dataframe(df)

        if "KM/L" in df.columns:
            st.markdown("### 🔍 Médias de Consumo (KM/L)")
            st.bar_chart(df.set_index("PLACA")["KM/L"])

    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
