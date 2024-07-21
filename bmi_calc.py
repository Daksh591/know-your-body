import streamlit as st
st.set_page_config(page_title="BMI_CALC",page_icon="Capture.jpg")
st.subheader("This is a BMI (Body Mass Index) Calculator")

# Weight selection and input
weight_unit = st.selectbox("Weight", ("Kilograms (KG)", "Pounds (lbs)", "Grams (g)"))
if weight_unit == "Kilograms (KG)":
    weight = st.text_input("Weight in Kilograms", "0")
    bmi_w = float(weight)
elif weight_unit == "Pounds (lbs)":
    weight = st.text_input("Weight in Pounds", "0")
    bmi_w = float(weight) / 2.205
elif weight_unit == "Grams (g)":
    weight = st.text_input("Weight in Grams", "0")
    bmi_w = float(weight) / 1000

# Height selection and input
height_unit = st.selectbox("Height", ("Feet (ft)", "Metres (m)", "Centimetres (cm)"))
if height_unit == "Feet (ft)":
    height = st.text_input("Height in Feet", "0")
    bmi_h = float(height) / 3.281
elif height_unit == "Metres (m)":
    height = st.text_input("Height in Metres", "0")
    bmi_h = float(height)
elif height_unit == "Centimetres (cm)":
    height = st.text_input("Height in Centimetres", "0")
    bmi_h = float(height) / 100

# Calculate BMI on button click
button = st.button("Calculate BMI")
if button:
    try:
        bmi_h_square = bmi_h ** 2
        bmi = bmi_w / bmi_h_square
        st.text(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            rating = "Underweight"
        elif 18.5 <= bmi < 24.9:
            rating = "Normal weight"
        elif 25 <= bmi < 29.9:
            rating = "Overweight"
        else:
            rating = "Obese"
        st.text(f"Your body is {rating}")

    except Exception as e:
        st.text(f"An error occurred: {e}")
