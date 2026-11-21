import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil_model.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

years = st.number_input('Tahun Mobil', min_value=1990, max_value=2024, value=2015)
mileage = st.number_input('Input Jarak Tempuh Km (Mileage)')
tax = st.number_input('Input Pajak Mobil (Tax)')
mpg = st.number_input('Input Konsumsi Bahan Bakar (MPG)')
engine_size = st.number_input('Input Ukuran Mesin (Engine Size)')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[years, mileage, tax, mpg, engine_size]]
        )
    
    harga_ponds = float(predict[0])
    harga_rupiah = harga_ponds * 18000
    
    format_pounds = f"£ {harga_ponds:,.2f}"
    format_rupiah = f"Rp {harga_rupiah:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
    st.write('Estimasi Harga Mobil Bekas dalam ponds: ', format_pounds)
    st.write('Estimasi Harga Mobil Bekas dalam rupiah: ', format_rupiah)
