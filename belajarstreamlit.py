# library
import streamlit as st

#writer
st.title ('kalkulator ajaib')
st.subheader('kalkulator kimia')

#input angka pertama
number1 = st.number_input('MASUKKAN ANGKA v1')
st.write('angka asli adalah:' , number1)

#input angka ke 2
number2 = st.number_input('masukkan angka n1')
st.write('angka asli adalah ' , number2)

#input angka ke 3
number3 = st.number_input('masukkan angka v2')
st.write('angka asli adalah ' , number3)

#input angka ke 4
number4 = st.number_input('masukkan angka n2')
st.write('angka asli adalah' , number4)


#hasil pengurangan
hasil = number1*number2/number2
if st.button('hitung'):
    st.write(f'hasil kali antara {number1} dan {number2} dibagi {number3} dan {number4} adalah {hasil}')
    
else:
    st.writer ('silahkan pencet tombol hitung')