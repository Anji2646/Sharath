import streamlit as st

def calculate_norton(current_sources, resistances):
    # Assuming a simple parallel circuit for demonstration
    I_n = sum(current_sources)
    R_n = 1 / sum(1 / r for r in resistances)
    return I_n, R_n

st.title("Norton's Theorem Calculator")

st.write("Enter the values of current sources (in amperes) and resistances (in ohms):")

num_sources = st.number_input("Number of current sources", min_value=1, step=1)
num_resistances = st.number_input("Number of resistances", min_value=1, step=1)

current_sources = []
resistances = []

for i in range(num_sources):
    current_sources.append(st.number_input(f"Current source {i+1} (A)", step=0.1))

for i in range(num_resistances):
    resistances.append(st.number_input(f"Resistance {i+1} (Ω)", step=0.1))

if st.button("Calculate Norton Equivalent"):
    I_n, R_n = calculate_norton(current_sources, resistances)
    st.write(f"Norton Equivalent Current (I_n): {I_n} A")
    st.write(f"Norton Equivalent Resistance (R_n): {R_n} Ω")
