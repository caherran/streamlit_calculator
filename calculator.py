import streamlit as st
from time import sleep

st.title("Mi Calculadora")

first_number = st.text_input("Ingrese primer numero", "0")
second_number = st.text_input("Ingrese segundo numero", "5")

operation = st.selectbox("Selecciona Operacion:", ["Suma", "Resta", "Multiplicacion", "Division"])

if(st.button("Realizar Calculo")):
    with(st.spinner("Calculando resultados...")):
        sleep(2)
        if(operation == "Suma"):
            result = int(first_number) + int(second_number)
            st.success(f"El resultado de la {operation} es: {result}")
        elif(operation == "Resta"):
            result = int(first_number) - int(second_number)
            st.success(f"El resultado de la {operation} es: {result}")
        elif(operation == "Multiplicacion"):
            result = int(first_number) * int(second_number)
            st.success(f"El resultado de la {operation} es: {result}")
        elif(operation == "Division"):
            if(int(second_number) == 0):
                e = RuntimeError("Denominador en cero (0), resultado indeterminado")
                st.exception(e)
            else:
                result = int(first_number) / int(second_number)
                st.success(f"El resultado de la {operation} es: {result}")
