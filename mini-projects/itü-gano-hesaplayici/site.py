#ORTALAMA HESAPLAMA SİTESİ
import streamlit as st

st.title("İTÜ GANO Hesaplayıcı 🚀")
isim = st.text_input("Adın:")
soyisim = st.text_input("Soyadın:")

not_tablosu = {
    "AA": 4.00, "BA+": 3.75, "BA": 3.50, "BB+": 3.25, 
    "BB": 3.00, "CB+": 2.75, "CB": 2.50, "CC+": 2.25, 
    "CC": 2.00, "DC+": 1.75, "DC": 1.50, "DD+": 1.25, 
    "DD": 1.00, "FF": 0.00
}

ders_sayisi = st.slider("Kaç dersin var?", 1, 10, 5)

tum_veriler = []

for i in range(ders_sayisi):
    col1, col2, col3 = st.columns(3) 
    with col1:
        d_ad = st.text_input(f"{i+1}. Ders", key=f"ad_{i}")
    with col2:
        d_kredi = st.number_input("Kredi", min_value=0.5, max_value=10.0, value=3.0, step=0.5, key=f"kr_{i}")
    with col3:
        d_harf = st.selectbox("Not", list(not_tablosu.keys()), key=f"hf_{i}")
    
    tum_veriler.append([d_ad, d_kredi, d_harf])

if st.button("GANO Hesapla"):
    toplam_puan = 0.0
    toplam_kredi = 0.0
    
    for d in tum_veriler:
        katsayi = not_tablosu.get(d[2], 0.0)
        toplam_puan += katsayi * d[1]
        toplam_kredi += d[1]
    
    if toplam_kredi > 0:
        gano = toplam_puan / toplam_kredi
        st.success(f"Tebrikler {isim} {soyisim}! Ortalaman: {round(gano, 2)}")
    else:
        st.warning("Lütfen kredi bilgilerini kontrol et!")