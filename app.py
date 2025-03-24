import streamlit as st
from scraper import get_vehicle_tariffs

st.set_page_config(page_title="Tarifas MK Osaka", layout="centered")
st.title("Calculadora de Tarifas - MK Group Osaka")

with st.spinner("Cargando tarifas en tiempo real..."):
    vehicles_data = get_vehicle_tariffs()

if not vehicles_data:
    st.error("No se pudo cargar la información desde la web.")
    st.stop()

vehicle_type = st.selectbox("Selecciona el tipo de vehículo", list(vehicles_data.keys()))
available_hours = sorted(vehicles_data[vehicle_type].keys())
selected_hours = st.selectbox("Horas de reserva", available_hours)

if st.button("Calcular tarifa"):
    price = vehicles_data[vehicle_type][selected_hours]
    st.success(f"Tarifa total por {selected_hours} hora(s): ¥{price:,} yenes")
