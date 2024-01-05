
import streamlit as st
import matplotlib.pyplot as plt
import string

with st.form("input"):
    name = st.text_input("What is your alter ego?")
    st.form_submit_button("Submit")

name = name or "world"
st.title(f"Hello {name}!")

y = [
    string.ascii_lowercase.index(letter) if letter.isalpha() else 0
    for letter in name.lower()
]
x = range(len(name))

plt.plot(x, y)
plt.title(f"Hello {name}!", {'fontname':'Helvetica'})
plt.ylim([0,26])
plt.savefig('plot.png')

st.image('plot.png')
