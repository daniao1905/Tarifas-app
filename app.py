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

extra_hours = 0
if selected_hours == max(available_hours):
    extra_hours = st.number_input("¿Cuántas horas adicionales necesitas?", min_value=0, max_value=10, step=1)

if st.button("Calcular tarifa"):
    base_price = vehicles_data[vehicle_type][str(selected_hours)]
    extra_price_per_hour = vehicles_data[vehicle_type].get("extra_hour_price", 0)
    extra_fee = extra_hours * extra_price_per_hour
    subtotal = base_price + extra_fee
    tax = int(subtotal * 0.10)
    total = subtotal + tax

    st.markdown(f"""
    ### Resumen de tarifa
    - **Vehículo:** {vehicle_type}  
    - **Duración:** {selected_hours} horas{f" + {extra_hours} hora(s) extra" if extra_hours else ""}  
    - **Tarifa base:** ¥{base_price:,}  
    {f"- **Horas extra:** {extra_hours} × ¥{extra_price_per_hour:,} = ¥{extra_fee:,}" if extra_hours else ""}
    - **Subtotal:** ¥{subtotal:,}  
    - **Impuestos (10%):** ¥{tax:,}  
    - **Total con impuestos:** ¥{total:,}
    """)

st.markdown("""
---

### Avisos importantes

- Las tarifas **no incluyen** estacionamiento, peajes, entradas a instalaciones ni costos de alimentos.
- Si se realizan paradas intermedias o el lugar de recogida/llegada está fuera de Osaka, puede haber **variaciones en el precio**. Consulta con anticipación.
- Si la distancia total del viaje **supera los 100 km**, se aplicará una tarifa adicional.
- **No se puede garantizar un modelo exacto** al reservar vehículos como Alphard HV / GranAce / Vellfire HV. Uno de estos será asignado según disponibilidad.
- Si necesitas un vehículo para instalaciones específicas (restaurantes, ferris, etc.), por favor **haz la reserva con anticipación**.
- Métodos de pago: se informarán al momento de confirmar la reserva.
- **Política de cancelación:**
  - Cancelación el día anterior: 50%
  - Cancelación o cambio el mismo día: 100%
""")
