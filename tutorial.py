import streamlit as st
from matplotlib import pyplot as plt

st.title("Khalid Kheiri")

st.write("My name is Khalid Kheiri")

fig = plt.figure()
plt.plot([1,2,3,4,5], [5,2,4,7,5])
st.write(fig)
