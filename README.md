
# 📊 Relatório Diário de Consumo de Combustível

Este repositório contém:

- `relatorio_kml_validado_ultimo_dia.py`: Script validado que gera relatórios diários de consumo por veículo e tipo de combustível.
- `app.py`: Interface visual com Streamlit para explorar os relatórios gerados.
- `planilhas/`: Pasta onde você deve colocar os arquivos `.xlsx` dos abastecimentos e o modelo de colunas.

## ✅ Como usar localmente

1. Instale as dependências:
```bash
pip install pandas openpyxl streamlit
```

2. Coloque suas planilhas na pasta `planilhas/`.

3. Execute o script para gerar o relatório do último dia com dados:
```bash
python relatorio_kml_validado_ultimo_dia.py
```

4. Para visualizar com interface web:
```bash
streamlit run app.py
```

## 🌐 Como usar online (Streamlit Cloud)

1. Faça o upload deste repositório para o GitHub.
2. Vá até [streamlit.io/cloud](https://streamlit.io/cloud) e conecte ao seu GitHub.
3. Selecione o repositório e defina `app.py` como ponto de entrada.
4. Pronto! Você poderá visualizar os relatórios diretamente no navegador.

## 📁 Estrutura esperada

```
.
├── app.py
├── relatorio_kml_validado_ultimo_dia.py
├── planilhas/
│   ├── modelo a ser seguido.xlsx
│   ├── 01-04 - 04-05.xlsx
│   ├── 06.xlsx
│   └── ...
└── README.md
```

---

Feito por: [Seu Nome ou Equipe]
