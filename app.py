import streamlit as st
from load_data import get_vehicle_tariffs

st.set_page_config(page_title="Tarifas MK Osaka", layout="centered")
st.title("Calculadora de Tarifas - MK Group Osaka")

vehicles_data = get_vehicle_tariffs()

if not vehicles_data:
    st.error("No se pudo cargar la información desde el archivo.")
    st.stop()

vehicle_type = st.selectbox("Selecciona el tipo de vehículo", list(vehicles_data.keys()))
available_hours = sorted(
    int(k) for k in vehicles_data[vehicle_type].keys() if k.isdigit()
)
selected_hours = st.selectbox("Horas de reserva", available_hours)

if st.button("Calcular tarifa"):
    price = vehicles_data[vehicle_type][str(selected_hours)]
    st.success(f"Tarifa total por {selected_hours} hora(s): ¥{price:,} yenes")
