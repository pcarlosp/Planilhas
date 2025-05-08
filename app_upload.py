
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title='Relatório de Consumo Diário', layout='wide')
st.title('📊 Painel Diário de Consumo de Combustível')

st.markdown("Faça upload de um ou mais arquivos de relatório (`Relatorio_KML_YYYYMMDD.xlsx`) gerados pelo script.")

# Upload múltiplo
arquivos = st.file_uploader("Selecionar relatórios (.xlsx)", type="xlsx", accept_multiple_files=True)

if arquivos:
    nomes_validos = [f.name for f in arquivos if "Relatorio_KML_" in f.name]
    datas_disponiveis = sorted([
        nome.replace("Relatorio_KML_", "").replace(".xlsx", "") for nome in nomes_validos
    ])

    if not datas_disponiveis:
        st.warning("Nenhum arquivo válido (com prefixo Relatorio_KML_) foi detectado.")
    else:
        data_escolhida = st.selectbox("Selecione a data:", datas_disponiveis[::-1])
        nome_arquivo = f"Relatorio_KML_{data_escolhida}.xlsx"

        arquivo_alvo = next((f for f in arquivos if f.name == nome_arquivo), None)

        if arquivo_alvo:
            try:
                df = pd.read_excel(arquivo_alvo)
                st.success(f"Relatório carregado: {nome_arquivo}")
                st.dataframe(df)

                if "KM/L" in df.columns:
                    st.markdown("### 🔍 Médias de Consumo (KM/L)")
                    st.bar_chart(df.set_index("PLACA")["KM/L"])

            except Exception as e:
                st.error(f"Erro ao ler o arquivo: {e}")
        else:
            st.error("Arquivo correspondente à data selecionada não encontrado entre os enviados.")
else:
    st.info("Aguardando upload de arquivos...")
