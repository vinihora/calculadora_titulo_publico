import streamlit as st
from supabase import create_client, Client
import datetime
from functions import get_vna, get_pu, get_pu_ltn, get_tax_ltn, get_pu_ntnf, get_vna_lft, get_pu_lft, get_vna_igpm, get_pu_ntn_c, verify_busday

# Conectando com o database
url: str = "https://geghwzramcdyqmnziwwf.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdlZ2h3enJhbWNkeXFtbnppd3dmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDA4NDg1NDksImV4cCI6MjAxNjQyNDU0OX0.S_SmrTeOIEJgkdGVpNVcQpF6O9hZ61pdaDXiTk_x-wo"
supabase: Client = create_client(url, key)
user = supabase.auth.sign_in_with_password({ "email": "vinidahora08@gmail.com", "password": "tera@capital" })

# Setting streamlit
st.set_page_config(page_title = "Calculadora Títulos Públicos", page_icon="📈",)

st.image("https://media.licdn.com/dms/image/D4D0BAQFO1E7hnBQfYg/company-logo_200_200/0/1692212616600/teracapital_logo?e=1709769600&v=beta&t=1nJA4xfbonGF84YqcjLNJrpA6F7FoWExFkrT3D66qyA", width=100)
st.title("TERA CAPITAL")
st.subheader("Calculadora de títulos públicos")

# Busca informações
def get_titulos():
    data_base = supabase.table("titulos_data").select("*").execute()
    return data_base.data

titulos = get_titulos()

titles = [x['name'] for x in titulos]

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        option = st.selectbox(
        'Selecione um ativo',
        titles, index=None, placeholder="Escolha um ativo")

    index_title = 0
    index_type = ""
    for i,t in enumerate(titulos):
        if t['name'] == option:
            index_title = i
            index_type = t['type']
            break

    if index_type == "LFT":
        now = datetime.datetime.now()
        min_date = now - datetime.timedelta(days=5)
        max_date = now
    else:
        now = datetime.datetime.now()
        min_date = now - datetime.timedelta(days=5)
        max_date = now + datetime.timedelta(days=5)

    with col2:
        selected_date = st.date_input("Selecione a data: ", None, min_date, max_date, format="DD/MM/YYYY", disabled=True if option == None else False)

    options_tax = ['TAXA', 'PU'] if index_type in ['LTN'] else ['TAXA']

    select_tax = st.selectbox(
        'TAXA OU PU',
        (options_tax), placeholder="Escolha uma opção", disabled=True if option == None else False)

    if select_tax == "PU":
        input_calc = st.number_input('Digite o PU desejado')
    elif select_tax == "TAXA":
        input_calc = st.number_input('Digite a TAXA desejada (%)')

    press_button = st.button("Calcular", type="primary")

with st.container():
        
        index_title = 0
        index_type = ""
        for i,t in enumerate(titulos):
            if t['name'] == option:
                index_title = i
                index_type = t['type']
                break

        if index_type == "NTN-B" and selected_date:
            due_date_string = titulos[index_title]['due_date']
            due_date = datetime.datetime.strptime(due_date_string, "%Y-%m-%d")

            print(due_date)

            selected_date = datetime.datetime.strptime(selected_date.strftime("%d/%m/%Y"), "%d/%m/%Y")
            selected_date_string = selected_date.strftime("%d/%m/%Y")
            selected_date = verify_busday(selected_date)

            if press_button:
                if select_tax == "TAXA":
                    vna = get_vna(selected_date)
                    pu = get_pu(vna, selected_date, due_date, float(input_calc) * 0.01)

                    st.markdown("""
                    <style>
                    .big-font {
                        font-size:25px !important;
                    }
                    }
                    </style>
                    """, unsafe_allow_html=True)

                    st.markdown(f'<div class="big-font">TAXA</div>', unsafe_allow_html=True)
                    st.write(f'{input_calc}%')

                    st.markdown(f'<div class="big-font">VNA</div>', unsafe_allow_html=True)
                    st.write(f'{vna}')

                    st.markdown(f'<div class="big-font">PU</div>', unsafe_allow_html=True)
                    st.write(f'{pu}')

                    
        
        if index_type == "NTN-F" and selected_date:
            due_date_string = titulos[index_title]['due_date']
            due_date = datetime.datetime.strptime(due_date_string, "%Y-%m-%d")

            selected_date = datetime.datetime.strptime(selected_date.strftime("%d/%m/%Y"), "%d/%m/%Y")
            selected_date_string = selected_date.strftime("%d/%m/%Y")
            selected_date = verify_busday(selected_date)

            if press_button:
                if select_tax == "TAXA":
                    pu = get_pu_ntnf(selected_date, due_date, float(input_calc) * 0.01)

                    st.markdown("""
                    <style>
                    .big-font {
                        font-size:25px !important;
                    }
                    }
                    </style>
                    """, unsafe_allow_html=True)

                    st.markdown(f'<div class="big-font">TAXA</div>', unsafe_allow_html=True)
                    st.write(f'{input_calc}%')

                    st.markdown(f'<div class="big-font">VNA</div>', unsafe_allow_html=True)
                    st.write(f'1000.000000')

                    st.markdown(f'<div class="big-font">PU</div>', unsafe_allow_html=True)
                    st.write(f'{pu}')

        if index_type == "LFT" and selected_date:
            due_date_string = titulos[index_title]['due_date']
            due_date = datetime.datetime.strptime(due_date_string, "%Y-%m-%d")

            selected_date = datetime.datetime.strptime(selected_date.strftime("%d/%m/%Y"), "%d/%m/%Y")
            selected_date_string = selected_date.strftime("%d/%m/%Y")
            selected_date = verify_busday(selected_date)

            if press_button:
                if select_tax == "TAXA":
                    vna = get_vna_lft(selected_date)
                    pu = get_pu_lft(vna, selected_date, due_date, float(input_calc) * 0.01)

                    st.markdown("""
                    <style>
                    .big-font {
                        font-size:25px !important;
                    }
                    }
                    </style>
                    """, unsafe_allow_html=True)

                    st.markdown(f'<div class="big-font">TAXA</div>', unsafe_allow_html=True)
                    st.write(f'{input_calc}%')

                    st.markdown(f'<div class="big-font">VNA</div>', unsafe_allow_html=True)
                    st.write(f'{vna}')

                    st.markdown(f'<div class="big-font">PU</div>', unsafe_allow_html=True)
                    st.write(f'{pu}')

        if index_type == "LTN" and selected_date:
            due_date_string = titulos[index_title]['due_date']
            due_date = datetime.datetime.strptime(due_date_string, "%Y-%m-%d")
            
            selected_date = datetime.datetime.strptime(selected_date.strftime("%d/%m/%Y"), "%d/%m/%Y")
            selected_date_string = selected_date.strftime("%d/%m/%Y")
            selected_date = verify_busday(selected_date)

            if press_button:
                if select_tax == "TAXA":
                    pu = get_pu_ltn(float(input_calc) * 0.01, selected_date, due_date)

                    st.markdown("""
                    <style>
                    .big-font {
                        font-size:25px !important;
                    }
                    }
                    </style>
                    """, unsafe_allow_html=True)

                    st.markdown(f'<div class="big-font">TAXA</div>', unsafe_allow_html=True)
                    st.write(f'{input_calc}%')

                    st.markdown(f'<div class="big-font">VNA</div>', unsafe_allow_html=True)
                    st.write(f'1000.000000')

                    st.markdown(f'<div class="big-font">PU</div>', unsafe_allow_html=True)
                    st.write(f'{pu}')

                elif select_tax == "PU":
                    taxa = get_tax_ltn(float(input_calc), selected_date, due_date)

                    st.markdown("""
                    <style>
                    .big-font {
                        font-size:25px !important;
                    }
                    }
                    </style>
                    """, unsafe_allow_html=True)

                    st.markdown(f'<div class="big-font">TAXA</div>', unsafe_allow_html=True)
                    st.write(f'{taxa}%')

                    st.markdown(f'<div class="big-font">VNA</div>', unsafe_allow_html=True)
                    st.write(f'1000.000000')

                    st.markdown(f'<div class="big-font">PU</div>', unsafe_allow_html=True)
                    st.write(f'{input_calc}')

        if index_type == "NTN-C" and selected_date:
            due_date_string = titulos[index_title]['due_date']
            due_date = datetime.datetime.strptime(due_date_string, "%Y-%m-%d")

            selected_date = datetime.datetime.strptime(selected_date.strftime("%d/%m/%Y"), "%d/%m/%Y")
            selected_date_string = selected_date.strftime("%d/%m/%Y")
            selected_date = verify_busday(selected_date)

            if press_button:
                if select_tax == "TAXA":
                    vna = get_vna_igpm(selected_date)
                    pu = get_pu_ntn_c(vna, selected_date, due_date, float(input_calc) * 0.01)

                    st.markdown("""
                    <style>
                    .big-font {
                        font-size:25px !important;
                    }
                    }
                    </style>
                    """, unsafe_allow_html=True)

                    st.markdown(f'<div class="big-font">TAXA</div>', unsafe_allow_html=True)
                    st.write(f'{input_calc}%')

                    st.markdown(f'<div class="big-font">VNA</div>', unsafe_allow_html=True)
                    st.write(f'{vna}')

                    st.markdown(f'<div class="big-font">PU</div>', unsafe_allow_html=True)
                    st.write(f'{pu}')