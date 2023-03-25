import streamlit as st
import pytube

url = st.text_input("Lütfen indirmek istediğiniz video adresini yazın...")

if len(url)>0:
    sonuc = pytube.YouTube(url)#.streams.first().download()
    yr= sonuc.streams.get_highest_resolution().download()
   
    


    with open(yr, "rb") as file:
        btn = st.download_button(
                label="Video İndir",
                data=file,
                file_name="video.mp4",
                mime="video/mp4"
            )