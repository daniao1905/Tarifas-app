import streamlit as st
from load_data import get_vehicle_tariffs

st.set_page_config(page_title="Tarifas MK Osaka", layout="centered")
st.title("Tarifas - Vehículos Privados Osaka")

vehicles_data = get_vehicle_tariffs()
vehicle_type = st.selectbox("Selecciona el tipo de vehículo", list(vehicles_data.keys()))

available_hours = sorted(
    int(k) for k in vehicles_data[vehicle_type].keys() if k.isdigit()
)
selected_hours = st.selectbox("Horas de reserva", available_hours)

add_extra = st.checkbox("¿Incluir 30 minutos adicionales? (+¥3,500)")

if st.button("Calcular tarifa"):
    base_price = vehicles_data[vehicle_type][str(selected_hours)]
    extra_fee = vehicles_data[vehicle_type].get("ext_30min", 0) if add_extra else 0
    total = base_price + extra_fee

    st.markdown(f"""
    ### Resumen de tarifa
    - **Vehículo:** {vehicle_type}  
    - **Duración:** {selected_hours} hora(s){' + 30 min' if add_extra else ''}  
    - **Tarifa Base:** ¥{base_price:,}  
    {f"- **Extra 30 min:** ¥{extra_fee:,}" if add_extra else ""}
    - **Total:** ¥{total:,}
    """)
