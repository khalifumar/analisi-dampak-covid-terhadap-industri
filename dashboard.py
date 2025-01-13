import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Kumpulan Data
# Jenis Kelamin Tiap Tahum di Perkotaan pada 34 Provinsi 
data_gender_pertahun_perkotaan = pd.read_csv('data/penduduk/data_rumah_tangga_perkotaan_kelamin.csv')

# Jenis Kelamin Tiap Tahum di Perdesaan pada 34 Provinsi
data_gender_pertahun_pedesaan = pd.read_csv('data/penduduk/data_rumah_tangga_pedesaan_kelamin.csv')

# Data Lowongan Pekerjaan
data_lowongan_2021 = pd.read_csv('data/lowongan/data_pencari_lowongan_pemenuhan_tenaga_kerja_terdaftar_2021.csv')
data_lowongan_2020 = pd.read_csv('data/lowongan/data_pencari_lowongan_pemenuhan_tenaga_kerja_terdaftar_2020.csv')
data_lowongan_2019 = pd.read_csv('data/lowongan/data_pencari_lowongan_pemenuhan_tenaga_kerja_terdaftar_2019.csv')
data_lowongan_2018 = pd.read_csv('data/lowongan/data_pencari_lowongan_pemenuhan_tenaga_kerja_terdaftar_2018.csv')

# Data Jumlah Penduduk berdasarkan Status Pekerjaannya
data_status_pekerjaan_2021 = pd.read_csv('data/penduduk/data_jumlah_penduduk_provinsi_dan_jenis_kegiatan_2021.csv')
data_status_pekerjaan_2020 = pd.read_csv('data/penduduk/data_jumlah_penduduk_provinsi_dan_jenis_kegiatan_2020.csv')
data_status_pekerjaan_2019 = pd.read_csv('data/penduduk/data_jumlah_penduduk_provinsi_dan_jenis_kegiatan_2019.csv')
data_status_pekerjaan_2018 = pd.read_csv('data/penduduk/data_jumlah_penduduk_provinsi_dan_jenis_kegiatan_2018.csv')



st.set_page_config(layout='wide')


with open('style.css') as f:
    css = f.read()




st.sidebar.title("Pilih Halaman:")
option_menu = st.sidebar.selectbox('', ['Home', 'Analisis Data', 'Kumpulan Data'])

with st.sidebar:
    with st.container(border=True):
        st.subheader('Noted:')
        st.write('Data yang digunakan berdasarkan data BPS (Badan Pusat Statistik) Republik Indonesia.\n Data yang digunakan sebagai berikut:')
        
        selectbox_data = st.selectbox('Data yang digunakan :',("Pilih Data...", "Data Penduduk Berdasarkan Jenis Kelamin", "Data Industri Berdasarkan Pencari, Lowongan, dan Penerimaan Tenaga Kerja", "Data Penduduk Berdasarkan Status Pekerjaannya"))
        if selectbox_data == "Data Penduduk Berdasarkan Jenis Kelamin":
            st.write("1. Data Penduduk Berdasarkan Jenis Kelamin")
            st.markdown("[Data Jumlah Penduduk](https://www.bps.go.id/id/statistics-table/1/MTYwNCMx/persentase-rumah-tangga-menurut-provinsi--daerah-tempat-tinggal--dan-jenis-kelamin-kepala-rumah-tangga--2009-2024.html)")

        elif selectbox_data == "Data Industri Berdasarkan Pencari, Lowongan, dan Penerimaan Tenaga Kerja":  
            st.write("2. Data Industri Berdasarkan Pencari, Lowongan, dan Penerimaan Tenaga Kerja")
            st.markdown("[2018](https://www.bps.go.id/id/statistics-table/3/VEU5VVVERlVWM0JwYTNvdk1ISkpWR3R1VUhaVmR6MDkjMw==/pencari-kerja-terdaftar--lowongan-kerja-terdaftar--dan-penempatan-pemenuhan-tenaga-kerja-menurut-provinsi-dan-jenis-kelamin--2018.html?year=2018)")
            st.markdown("[2019](https://www.bps.go.id/id/statistics-table/3/VEU5VVVERlVWM0JwYTNvdk1ISkpWR3R1VUhaVmR6MDkjMw==/pencari-kerja-terdaftar--lowongan-kerja-terdaftar--dan-penempatan-pemenuhan-tenaga-kerja-menurut-provinsi-dan-jenis-kelamin--2019.html?year=2019)")
            st.markdown("[2020](https://www.bps.go.id/id/statistics-table/3/VEU5VVVERlVWM0JwYTNvdk1ISkpWR3R1VUhaVmR6MDkjMw==/pencari-kerja-terdaftar--lowongan-kerja-terdaftar--dan-penempatan-pemenuhan-tenaga-kerja-menurut-provinsi-dan-jenis-kelamin--2018.html?year=2020)")
            st.markdown("[2021](https://www.bps.go.id/id/statistics-table/3/VEU5VVVERlVWM0JwYTNvdk1ISkpWR3R1VUhaVmR6MDkjMw==/pencari-kerja-terdaftar--lowongan-kerja-terdaftar--dan-penempatan-pemenuhan-tenaga-kerja-menurut-provinsi-dan-jenis-kelamin--2018.html?year=2021)")

        elif selectbox_data == "Data Penduduk Berdasarkan Status Pekerjaannya":
            st.write("3. Data Penduduk Berdasarkan Status Pekerjaannya")
            st.markdown("[Data Jumlah Penduduk](https://www.bps.go.id/id/statistics-table/1/MTYwNCMx/persentase-rumah-tangga-menurut-provinsi--daerah-tempat-tinggal--dan-jenis-kelamin-kepala-rumah-tangga--2009-2024.html)")
    

if option_menu == 'Analisis Data':
    st.title('Analisis Data')
    st.subheader("Pilih Data yang Ingin Dianalisis:")

    options_analisis = st.multiselect("", [
            "Dampak Covid-19 Terhadap Jumlah Pertumbuhan Penduduk", 
            "Jumlah Pertumbuhan Pencari Kerja", 
            "Pertumbuhan Lowongan Pekerjaan", 
            "Pertumbuhan Penempatan / Penerimaan Tenaga Kerja",
            "Pertumbuhan Penduduk Pernah Bekerja"
        ]
    )

    if "Dampak Covid-19 Terhadap Jumlah Pertumbuhan Penduduk" in options_analisis:
        with st.container(border=True):
            st.header('Analisis Dampak Covid-19 Terhadap Jumlah Pertumbuhan Penduduk Tiap Tahun')

            tab_a1, tab_a2 = st.tabs(['Perkotaan', 'Pedesaan'])
            with tab_a1:
                st.subheader("Data Laki-Laki Perkotaan")
                st.write("")
                col_a1, col_a2 = st.columns(2)
                with col_a1:
                    tahun = ['2018', '2019', '2020', '2021']
                    perkotaan_average = {
                        "Rata-rata_2018" : data_gender_pertahun_perkotaan["2018_laki-laki"].mean(),
                        "Rata-rata_2019" : data_gender_pertahun_perkotaan["2019_laki-laki"].mean(),
                        "Rata-rata_2020" : data_gender_pertahun_perkotaan["2020_laki-laki"].mean(),
                        "Rata-rata_2021" : data_gender_pertahun_perkotaan["2021_laki-laki"].mean()
                    }
                    rata_rata_Laki_Perkotaan = [
                        perkotaan_average["Rata-rata_2018"],
                        perkotaan_average["Rata-rata_2019"],
                        perkotaan_average["Rata-rata_2020"],
                        perkotaan_average["Rata-rata_2021"]
                    ]
                    
                    fig, ax =plt.subplots()
                    for i, jumlah in enumerate(rata_rata_Laki_Perkotaan):
                        ax.text(tahun[i], jumlah + 0.5, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')

                    sns.barplot(data=perkotaan_average, x=tahun, y=rata_rata_Laki_Perkotaan, ax=ax, color='silver')
                    st.pyplot(fig)



                with col_a2:
                    penjelasan1 = st.container(border=True)
                    penjelasan1.write("""
                                    Penjelasan:\n
                                    Grafik tersebut menjelaskan bahwa sempat terjadi 2 fase dari tahun 2018 sampai dengan 2021.\n
                                    Fase Pertama, terjadi penurunan di tahun 2018 sampai dengan 2019 dengan peprsentase 84,14 ke 83,70.\n
                                    Fase Kedua, terjadi kenaikan yang cukup signigikan di tahun 2019 sampai tahun 2021 dari persentase 83,70 sampai dengan 86,67.\n
                                    """)

                st.subheader("Data Perempuan Perkotaan")
                st.write("")
                col_aa1, col_aa2 = st.columns(2)
                with col_aa1:
                    
                    tahun = ['2018', '2019', '2020', '2021']
                    perempuan_perkotaan_average = {
                        "Rata-rata_2018" : data_gender_pertahun_perkotaan["2018_perempuan"].mean(),
                        "Rata-rata_2019" : data_gender_pertahun_perkotaan["2019_perempuan"].mean(),
                        "Rata-rata_2020" : data_gender_pertahun_perkotaan["2020_perempuan"].mean(),
                        "Rata-rata_2021" : data_gender_pertahun_perkotaan["2021_perempuan"].mean()
                    }

                    rata_rata_perempuan_perkotaan = [
                        perempuan_perkotaan_average["Rata-rata_2018"],
                        perempuan_perkotaan_average["Rata-rata_2019"],
                        perempuan_perkotaan_average["Rata-rata_2020"],
                        perempuan_perkotaan_average["Rata-rata_2021"]
                    ]

                    fig, ax =plt.subplots()
                    for i, jumlah in enumerate(rata_rata_perempuan_perkotaan):
                        ax.text(tahun[i], jumlah + 0.2, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')

                    sns.barplot(data=perempuan_perkotaan_average, x=tahun, y=rata_rata_perempuan_perkotaan, ax=ax, color='yellow')
                    st.pyplot(fig)

                with col_aa2:
                    penjelasan2 = st.container(border=True)
                    penjelasan2.write("""
                                    Penjelasan\n
                                    Grafik tersebut menjelaskan bahwa sempat terjadi 2 fase dari tahun 2018 sampai dengan 2021.\n
                                    Fase Pertama, terjadi kenaikan di tahun 2018 sampai dengan 2019 daro peprsentase 15,86 ke 16,30.\n
                                    Fase Kedua, terjadi penurunan yang cukup signigikan di tahun 2019 sampai tahun 2021 dari persentase 16,30 sampai dengan 13,33.
                                    """)
            
            with tab_a2:
                st.subheader("Data Laki-Laki Pedesaan")
                st.write("")
                col_a3, col_a4 = st.columns(2)
                with col_a3:
                    tahun = ['2018', '2019', '2020', '2021']
                    pedesaan_average = {
                    "Rata-rata_2018" : data_gender_pertahun_pedesaan["2018_laki-laki"].mean(),
                    "Rata-rata_2019" : data_gender_pertahun_pedesaan["2019_laki-laki"].mean(),
                    "Rata-rata_2020" : data_gender_pertahun_pedesaan["2020_laki-laki"].mean(),
                    "Rata-rata_2021" : data_gender_pertahun_pedesaan["2021_laki-laki"].mean()
                    }

                    rata_rata_Laki_Pedesaan = [
                        pedesaan_average["Rata-rata_2018"],
                        pedesaan_average["Rata-rata_2019"],
                        pedesaan_average["Rata-rata_2020"],
                        pedesaan_average["Rata-rata_2021"]
                    ]

                    fig, ax = plt.subplots()

                    for i, jumlah in enumerate(rata_rata_Laki_Pedesaan):
                        ax.text(tahun[i], jumlah + 0.2, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')
            
                    sns.barplot(data=pedesaan_average, x=tahun, y=rata_rata_Laki_Pedesaan, ax=ax, color='silver')
                    st.pyplot(fig)


                with col_a4:
                    penjelasan3 = st.container(border=True)
                    penjelasan3.write("""
                                    Penjelasan\n
                                    Grafik tersebut menjelaskan bahwa sempat terjadi 2 fase dari tahun 2018 sampai dengan 2021.\n
                                    Fase Pertama, terjadi penurunan di tahun 2018 sampai dengan 2019 dengan peprsentase 86,36 ke 84,53.\n
                                    Fase Kedua, terjadi kenaikan yang cukup signigikan di tahun 2019 sampai tahun 2021 dari persentase 84,53 sampai dengan 87,04. 
                                    """)

                st.subheader("Data Perempuan Pedesaan")
                col_aa3, col_aa4 = st.columns(2)
                with col_aa3:
                    tahun = ['2018', '2019', '2020', '2021']
                    perempuan_pedesaan_average = {
                        "Rata-rata_2018" : data_gender_pertahun_pedesaan["2018_perempuan"].mean(),
                        "Rata-rata_2019" : data_gender_pertahun_pedesaan["2019_perempuan"].mean(),
                        "Rata-rata_2020" : data_gender_pertahun_pedesaan["2020_perempuan"].mean(),
                        "Rata-rata_2021" : data_gender_pertahun_pedesaan["2021_perempuan"].mean()
                    }

                    rata_rata_perempuan_pedesaan = [
                        perempuan_pedesaan_average["Rata-rata_2018"],
                        perempuan_pedesaan_average["Rata-rata_2019"],
                        perempuan_pedesaan_average["Rata-rata_2020"],
                        perempuan_pedesaan_average["Rata-rata_2021"]
                    ]

                    fig, ax =plt.subplots()

                    for i, jumlah in enumerate(rata_rata_perempuan_pedesaan):
                        ax.text(tahun[i], jumlah + 0.2, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')

                    sns.barplot(data=perempuan_pedesaan_average, x=tahun, y=rata_rata_perempuan_pedesaan, ax=ax, color='yellow')
                    st.pyplot(fig)

                with col_aa4:
                    penjelasan2 = st.container(border=True)
                    penjelasan2.write("""
                                    Penjelasan\n
                                    Grafik tersebut menjelaskan bahwa sempat terjadi 2 fase dari tahun 2018 sampai dengan 2021.\n
                                    Fase Pertama, terjadi kenaikan di tahun 2018 sampai dengan 2019 daro peprsentase 13,64 ke 15,47.\n
                                    Fase Kedua, terjadi penurunan yang cukup signigikan di tahun 2019 sampai tahun 2021 dari persentase 15,47 sampai dengan 12,96.                             
                                    """)
            
            st.write('')
            st.subheader('Kesimpulan Analisis:')
            st.write("""
                            Diasumsikan awal pandemi Covid-19 berada di antara tahun 2019 dan 2020. Dapat dianalisis bahwa penduduk berjenis kelamin laki-laki cenderung lebih berprogresif naik tiap tahunnya dibanding progres penduduk perempuan. Itu memungkinan kalau penduduk berjenis kelamin laki-laki dapat bertahan dan melawan disaat pandemi Covid-19 sedang merajalela.
                            """)
        
    
    if "Jumlah Pertumbuhan Pencari Kerja" in options_analisis:
        with st.container(border=True):
            st.header("Analisis Jumlah Pertumbuhan Pencari Kerja Tiap Tahun")
            col_a3, col_a4 = st.columns(2)
            with col_a3:
                tahun = ['2018', '2019', '2020', '2021']
                pencari_average_laki = {
                    "Pencari_2018": data_lowongan_2018['Pencari Kerja Terdaftar - Laki-Laki'].mean(),
                    "Pencari_2019": data_lowongan_2019['Pencari Kerja Terdaftar - Laki-Laki'].mean(),
                    "Pencari_2020": data_lowongan_2020['Pencari Kerja Terdaftar - Laki-Laki'].mean(),
                    "Pencari_2021": data_lowongan_2021['Pencari Kerja Terdaftar - Laki-Laki'].mean()
                }

                pencari_laki_perkotaan = [
                    pencari_average_laki["Pencari_2018"],
                    pencari_average_laki["Pencari_2019"],
                    pencari_average_laki["Pencari_2020"],
                    pencari_average_laki["Pencari_2021"]
                ]

                fig, ax = plt.subplots()
                sns.scatterplot(x=tahun, y=pencari_laki_perkotaan, color="green", s=100, marker='d', label='Data')
                plt.plot(tahun, pencari_laki_perkotaan, color="green", linestyle='-', label='Trend Line')

                for i, jumlah in enumerate(pencari_laki_perkotaan):
                    ax.text(tahun[i], jumlah + 0.5, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')

                ax.set_title("Pertumbuhan Pencari Kerja Terdaftar (Laki-Laki)")
                ax.set_xlabel("Tahun")
                ax.set_ylabel("Rata-Rata Pencari Kerja")
                ax.legend()

                st.pyplot(fig)

            with col_a4:
                pencari_average_perempuan = {
                    "Pencari_2018" : data_lowongan_2018['Pencari Kerja Terdaftar - Perempuan'].mean(),
                    "Pencari_2019" : data_lowongan_2019['Pencari Kerja Terdaftar - Perempuan'].mean(),
                    "Pencari_2020" : data_lowongan_2020['Pencari Kerja Terdaftar - Perempuan'].mean(),
                    "Pencari_2021" : data_lowongan_2021['Pencari Kerja Terdaftar - Perempuan'].mean()    
                }

                pencari_perempuan_perkotaan = [
                    pencari_average_perempuan["Pencari_2018"],
                    pencari_average_perempuan["Pencari_2019"],
                    pencari_average_perempuan["Pencari_2020"],
                    pencari_average_perempuan["Pencari_2021"]
                ]

                fig, ax = plt.subplots()
                sns.scatterplot(x=tahun, y=pencari_perempuan_perkotaan, color="green", s=100, marker='d', label='Data')
                plt.plot(tahun, pencari_perempuan_perkotaan, color="green", linestyle='-', label='Trend Line')

                for i, jumlah in enumerate(pencari_perempuan_perkotaan):
                    ax.text(tahun[i], jumlah + 0.5, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')

                ax.set_title("Pertumbuhan Pencari Kerja Terdaftar (Perempuan)")
                ax.set_xlabel("Tahun")
                ax.set_ylabel("Rata-Rata Pencari Kerja")
                ax.legend()

                st.pyplot(fig)

            st.header("Kesimpulan Analisis")
            st.write("""
                Diasumsikan awal pandemi Covid-19 berada diantara tahun 2019 dan 2020. Dari grafik diatas dapat dianalisis bahwa pertumbuhan pencari kerja sebelum terjadinya pandemi menyatakan kenaikan yang signifikan. Namun, pertumbuhan pencari kerja setelah pandemi menurun sangat drastis. Hal tersebut kemungkinan terjadi karena adanya batasan protokol yang dibuat oleh pemerintah sehingga membatasi jumlah para pencari kerjanya. 
            """)

    if "Pertumbuhan Lowongan Pekerjaan" in options_analisis:
        with st.container(border=True):
            st.header("Eksplorasi Pertumbuhan Lowongan Pekerjaan Tiap Tahun")
            col_a5, col_a6 = st.columns(2)
            with col_a5:
                tahun = ['2018', '2019', '2020', '2021']
                lowongan_average_laki = {
                    "Lowongan_2018" : data_lowongan_2018['Lowongan Kerja Terdaftar - Laki-Laki'].mean(),
                    "Lowongan_2019" : data_lowongan_2019['Lowongan Kerja Terdaftar - Laki-Laki'].mean(),
                    "Lowongan_2020" : data_lowongan_2020['Lowongan Kerja Terdaftar - Laki-Laki'].mean(),
                    "Lowongan_2021" : data_lowongan_2021['Lowongan Kerja Terdaftar - Laki-Laki'].mean()    
                }

                lowongan_laki_perkotaan = [
                    lowongan_average_laki["Lowongan_2018"],
                    lowongan_average_laki["Lowongan_2019"],
                    lowongan_average_laki["Lowongan_2020"],
                    lowongan_average_laki["Lowongan_2021"]
                ]

                fig, ax = plt.subplots()
                sns.scatterplot(x=tahun, y=lowongan_laki_perkotaan, color="red", s=100, marker='d', label='Data')
                plt.plot(tahun, lowongan_laki_perkotaan, color="red", linestyle='-', label='Trend Line')

                for i, jumlah in enumerate(lowongan_laki_perkotaan):
                        ax.text(tahun[i], jumlah + 0.5, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')

                ax.set_title("Pertumbuhan Lowongan Kerja Terdaftar (Laki-Laki)")
                ax.set_xlabel("Tahun")
                ax.set_ylabel("Rata-Rata Lowongan Kerja")
                ax.legend()

                st.pyplot(fig)


            with col_a6:
                tahun = ['2018', '2019', '2020', '2021']
                lowongan_average_perempuan = {
                    "Lowongan_2018" : data_lowongan_2018['Lowongan Kerja Terdaftar - Perempuan'].mean(),
                    "Lowongan_2019" : data_lowongan_2019['Lowongan Kerja Terdaftar - Perempuan'].mean(),
                    "Lowongan_2020" : data_lowongan_2020['Lowongan Kerja Terdaftar - Perempuan'].mean(),
                    "Lowongan_2021" : data_lowongan_2021['Lowongan Kerja Terdaftar - Perempuan'].mean()    
                }

                lowongan_perempuan_perkotaan = [
                    lowongan_average_perempuan["Lowongan_2018"],
                    lowongan_average_perempuan["Lowongan_2019"],
                    lowongan_average_perempuan["Lowongan_2020"],
                    lowongan_average_perempuan["Lowongan_2021"]
                ]

                fig, ax = plt.subplots()
                sns.scatterplot(x=tahun, y=lowongan_perempuan_perkotaan, color="red", s=100, marker='d', label='Data')
                plt.plot(tahun, lowongan_perempuan_perkotaan, color="red", linestyle='-', label='Trend Line')

                for i, jumlah in enumerate(lowongan_perempuan_perkotaan):
                        ax.text(tahun[i], jumlah + 0.5, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')

                ax.set_title("Pertumbuhan Lowongan Kerja Terdaftar Perempuan")
                ax.set_xlabel("Tahun")
                ax.set_ylabel("Rata-Rata Lowongan Kerja")
                ax.legend()

                st.pyplot(fig)
            
            st.header("Kesimpulan Analisis")
            st.write("""
                Diasumsikan awal pandemi Covid-19 berada diantara tahun 2019 dan 2020. Dari grafik diatas dapat dianalisis bahwa pertumbuhan jumlah lowongan kerja sebelum terjadinya pandemi menyatakan kenaikan yang signifikan dari tahun 2018 ke 2020. Namun, pertumbuuhan jumlah lowongan kerja setelah pandemi menurun sangat drastis. Hal tersebut kemungkinan terjadi akibat adanya batasan protokol yang dibuat oleh pemerintah pusat ataupun daerah sehingga membatasi jumlah perekrutan pada perusahaan-perusahaan. 
            """)


    if "Pertumbuhan Penempatan / Penerimaan Tenaga Kerja" in options_analisis:
        with st.container(border=True):
            st.header("Eksplorasi Pertumbuhan Penempatan / Penerimaan Tenaga Kerja Tiap Tahun")
            col_a7, col_a8 = st.columns(2)
            with col_a7:
                tahun = ['2018', '2019', '2020', '2021']
                penempatan_average_laki = {
                    "Penempatan_2018" : data_lowongan_2018['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki'].mean(),
                    "Penempatan_2019" : data_lowongan_2019['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki'].mean(),
                    "Penempatan_2020" : data_lowongan_2020['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki'].mean(),
                    "Penempatan_2021" : data_lowongan_2021['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki'].mean()    
                }

                penempatan_laki_perkotaan = [
                    penempatan_average_laki["Penempatan_2018"],
                    penempatan_average_laki["Penempatan_2019"],
                    penempatan_average_laki["Penempatan_2020"],
                    penempatan_average_laki["Penempatan_2021"]
                ]

                fig, ax = plt.subplots()
                sns.scatterplot(x=tahun, y=penempatan_laki_perkotaan, color="blue", s=100, marker='d')
                plt.plot(tahun, penempatan_laki_perkotaan, color="blue", linestyle='-')

                for i, jumlah in enumerate(penempatan_laki_perkotaan):
                        ax.text(tahun[i], jumlah + 0.5, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')

                ax.set_title("Pertumbuhan Penerimaan Tenaga kerja Laki-Laki")
                ax.set_xlabel("Tahun")
                ax.set_ylabel("Rata-Rata Lowongan Kerja")
                ax.legend()

                st.pyplot(fig)

                with col_a8:
                    tahun = ['2018', '2019', '2020', '2021']
                    penempatan_average_perempuan = {
                        "Penempatan_2018" : data_lowongan_2018['Penempatan/Pemenuhan Tenaga Kerja - Perempuan'].mean(),
                        "Penempatan_2019" : data_lowongan_2019['Penempatan/Pemenuhan Tenaga Kerja - Perempuan'].mean(),
                        "Penempatan_2020" : data_lowongan_2020['Penempatan/Pemenuhan Tenaga Kerja - Perempuan'].mean(),
                        "Penempatan_2021" : data_lowongan_2021['Penempatan/Pemenuhan Tenaga Kerja - Perempuan'].mean()    
                    }

                    penempatan_perempuan_perkotaan = [
                        penempatan_average_perempuan["Penempatan_2018"],
                        penempatan_average_perempuan["Penempatan_2019"],
                        penempatan_average_perempuan["Penempatan_2020"],
                        penempatan_average_perempuan["Penempatan_2021"]
                    ]

                    fig, ax = plt.subplots()
                    sns.scatterplot(x=tahun, y=penempatan_perempuan_perkotaan, color="blue", s=100, marker='d')
                    plt.plot(tahun, penempatan_perempuan_perkotaan, color="blue", linestyle='-')

                    for i, jumlah in enumerate(penempatan_perempuan_perkotaan):
                            ax.text(tahun[i], jumlah + 0.5, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')

                    ax.set_title("Pertumbuhan Penerimaan Tenaga kerja Perempuan")
                    ax.set_xlabel("Tahun")
                    ax.set_ylabel("Rata-Rata Lowongan Kerja")
                    ax.legend()

                    st.pyplot(fig)

            st.header("Kesimpulan Analisis")
            st.write("""
                Diasumsikan awal pandemi Covid-19 berada diantara tahun 2019 dan 2020. Dari grafik diatas dapat dianalisis bahwa pertumbuhan jumlah penerimaan tenaga kerja sebelum terjadinya pandemi menyatakan kenaikan yang signifikan dari tahun 2018 ke 2020. Namun, jumlah penerimaan tenaga kerja setelah pandemi menurun sangat drastis. Hal tersebut kemungkinan terjadi akibat adanya batasan protokol ataupun kriteria baru yang dibuat oleh masing-masing perusahaan sehingga membatasi jumlah penerimaan tenaga kerja yang mendaftar. 
            """)
    
    if "Pertumbuhan Penduduk Pernah Bekerja" in options_analisis:
        with st.container(border=True):
            st.subheader("Perbandingan Index Kualitas Industri Tiap Tahun")
            tab_h12, tab_h13, tab_h14, tab_h15 = st.tabs(['2018', '2019', '2020', '2021'])

            with tab_h12:
                
                data_persiapan_2018 = {
                    'Provinsi': data_lowongan_2018['Provinsi'],
                    'Pencari Kerja 2018' : data_lowongan_2018['Pencari Kerja Terdaftar - Laki-Laki'],
                    'Jumlah Lowongan 2018' : data_lowongan_2018['Lowongan Kerja Terdaftar - Laki-Laki'],
                    'Penempatan Tenaga Kerja 2018' : data_lowongan_2018['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki']
                }
                df =  pd.DataFrame(data_persiapan_2018)
                
                df['Rasio Penyerapan'] = df['Penempatan Tenaga Kerja 2018'] / df['Pencari Kerja 2018']
                df['Rasio Ketersediaan Lowongan'] = df['Jumlah Lowongan 2018'] / df['Pencari Kerja 2018']
                df['Efisiensi Penyerapan'] = df['Penempatan Tenaga Kerja 2018'] / df['Jumlah Lowongan 2018']

                # Normalisasi indikator
                df['Rasio Penyerapan (Normalisasi)'] = (df['Rasio Penyerapan'] - df['Rasio Penyerapan'].min()) / (df['Rasio Penyerapan'].max() - df['Rasio Penyerapan'].min())
                df['Rasio Ketersediaan Lowongan (Normalisasi)'] = (df['Rasio Ketersediaan Lowongan'] - df['Rasio Ketersediaan Lowongan'].min()) / (df['Rasio Ketersediaan Lowongan'].max() - df['Rasio Ketersediaan Lowongan'].min())
                df['Efisiensi Penyerapan (Normalisasi)'] = (df['Efisiensi Penyerapan'] - df['Efisiensi Penyerapan'].min()) / (df['Efisiensi Penyerapan'].max() - df['Efisiensi Penyerapan'].min())

                # Kombinasi indikator dengan bobot
                w1, w2, w3 = 0.5, 0.3, 0.2
                df['Indeks Kualitas Industri'] = (w1 * df['Rasio Penyerapan (Normalisasi)'] +
                                                w2 * df['Rasio Ketersediaan Lowongan (Normalisasi)'] +
                                                w3 * df['Efisiensi Penyerapan (Normalisasi)'])

                fig, ax = plt.subplots(figsize=(4,2))
                sns.barplot(x='Provinsi', y=df['Indeks Kualitas Industri'], data=df, color='lightblue')
                for i, jumlah in enumerate(df['Indeks Kualitas Industri']):
                    ax.text(i, jumlah + 0.01, f"{jumlah:.2f}", ha='center', fontsize=3, color='black')  # Posisi teks sedikit di atas bar


                plt.xlabel('Provinsi', fontsize=4)
                plt.xticks(rotation=45, ha='right', fontsize=4)
                plt.ylabel('Indeks Kualitas Industri', fontsize=4)
                plt.yticks(fontsize=4)

                st.pyplot(fig)

            with tab_h13:
                data_persiapan_2019 = {
                    'Provinsi': data_lowongan_2019['Provinsi'],
                    'Pencari Kerja 2019' : data_lowongan_2019['Pencari Kerja Terdaftar - Laki-Laki'],
                    'Jumlah Lowongan 2019' : data_lowongan_2019['Lowongan Kerja Terdaftar - Laki-Laki'],
                    'Penempatan Tenaga Kerja 2019' : data_lowongan_2019['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki']
                }
                df_2019 =  pd.DataFrame(data_persiapan_2019)
                
                df_2019['Rasio Penyerapan'] = df_2019['Penempatan Tenaga Kerja 2019'] / df_2019['Pencari Kerja 2019']
                df_2019['Rasio Ketersediaan Lowongan'] = df_2019['Jumlah Lowongan 2019'] / df_2019['Pencari Kerja 2019']
                df_2019['Efisiensi Penyerapan'] = df_2019['Penempatan Tenaga Kerja 2019'] / df_2019['Jumlah Lowongan 2019']

                df_2019['Rasio Penyerapan (Normalisasi)'] = (df_2019['Rasio Penyerapan'] - df_2019['Rasio Penyerapan'].min()) / (df_2019['Rasio Penyerapan'].max() - df_2019['Rasio Penyerapan'].min())
                df_2019['Rasio Ketersediaan Lowongan (Normalisasi)'] = (df_2019['Rasio Ketersediaan Lowongan'] - df_2019['Rasio Ketersediaan Lowongan'].min()) / (df_2019['Rasio Ketersediaan Lowongan'].max() - df_2019['Rasio Ketersediaan Lowongan'].min())
                df_2019['Efisiensi Penyerapan (Normalisasi)'] = (df_2019['Efisiensi Penyerapan'] - df_2019['Efisiensi Penyerapan'].min()) / (df_2019['Efisiensi Penyerapan'].max() - df_2019['Efisiensi Penyerapan'].min())

                w1, w2, w3 = 0.5, 0.3, 0.2
                df_2019['Indeks Kualitas Industri 2019'] = (w1 * df_2019['Rasio Penyerapan (Normalisasi)'] +
                                                w2 * df_2019['Rasio Ketersediaan Lowongan (Normalisasi)'] +
                                                w3 * df_2019['Efisiensi Penyerapan (Normalisasi)'])

                fig, ax = plt.subplots(figsize=(4,2))
                sns.barplot(x='Provinsi', y=df_2019['Indeks Kualitas Industri 2019'], data=df_2019, color='lightblue')
                for i, jumlah in enumerate(df_2019['Indeks Kualitas Industri 2019']):
                    ax.text(i, jumlah + 0.01, f"{jumlah:.2f}", ha='center', fontsize=3, color='black')


                plt.xlabel('Provinsi', fontsize=4)
                plt.xticks(rotation=45, ha='right', fontsize=4)
                plt.ylabel('Indeks Kualitas Industri', fontsize=4)
                plt.yticks(fontsize=4)

                st.pyplot(fig)

            with tab_h14:
                data_persiapan_2020 = {
                    'Provinsi': data_lowongan_2020['Provinsi'],
                    'Pencari Kerja 2020' : data_lowongan_2020['Pencari Kerja Terdaftar - Laki-Laki'],
                    'Jumlah Lowongan 2020' : data_lowongan_2020['Lowongan Kerja Terdaftar - Laki-Laki'],
                    'Penempatan Tenaga Kerja 2020' : data_lowongan_2020['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki']
                }
                df_2020 =  pd.DataFrame(data_persiapan_2020)
                
                df_2020['Rasio Penyerapan'] = np.where(df_2020['Pencari Kerja 2020'] > 0,  df_2020['Penempatan Tenaga Kerja 2020'] / df_2020['Pencari Kerja 2020'], 0)
                df_2020['Rasio Ketersediaan Lowongan'] = df_2020['Jumlah Lowongan 2020'] / df_2020['Pencari Kerja 2020']
                df_2020['Efisiensi Penyerapan'] = df_2020['Penempatan Tenaga Kerja 2020'] / df_2020['Jumlah Lowongan 2020']

                df_2020['Rasio Penyerapan (Normalisasi)'] = (df_2020['Rasio Penyerapan'] - df_2020['Rasio Penyerapan'].min()) / (df_2020['Rasio Penyerapan'].max() - df_2020['Rasio Penyerapan'].min())
                df_2020['Rasio Ketersediaan Lowongan (Normalisasi)'] = (df_2020['Rasio Ketersediaan Lowongan'] - df_2020['Rasio Ketersediaan Lowongan'].min()) / (df_2020['Rasio Ketersediaan Lowongan'].max() - df_2020['Rasio Ketersediaan Lowongan'].min())
                df_2020['Efisiensi Penyerapan (Normalisasi)'] = (df_2020['Efisiensi Penyerapan'] - df_2020['Efisiensi Penyerapan'].min()) / (df_2020['Efisiensi Penyerapan'].max() - df_2020['Efisiensi Penyerapan'].min())

                w1, w2, w3 = 0.5, 0.3, 0.2
                df_2020['Indeks Kualitas Industri 2020'] = (w1 * df_2020['Rasio Penyerapan (Normalisasi)'] +
                                                w2 * df_2020['Rasio Ketersediaan Lowongan (Normalisasi)'] +
                                                w3 * df_2020['Efisiensi Penyerapan (Normalisasi)'])

                fig, ax = plt.subplots(figsize=(4,2))
                sns.barplot(x='Provinsi', y=df_2020['Indeks Kualitas Industri 2020'], data=df_2020, color='lightblue')
                for i, jumlah in enumerate(df_2020['Indeks Kualitas Industri 2020']):
                    ax.text(i, jumlah + 0.01, f"{jumlah:.2f}", ha='center', fontsize=3, color='black')


                plt.xlabel('Provinsi', fontsize=4)
                plt.xticks(rotation=45, ha='right', fontsize=4)
                plt.ylabel('Indeks Kualitas Industri', fontsize=4)
                plt.yticks(fontsize=4)

                st.pyplot(fig)

            with tab_h15:
                data_persiapan_2021 = {
                    'Provinsi': data_lowongan_2021['Provinsi'],
                    'Pencari Kerja 2021' : data_lowongan_2021['Pencari Kerja Terdaftar - Laki-Laki'],
                    'Jumlah Lowongan 2021' : data_lowongan_2021['Lowongan Kerja Terdaftar - Laki-Laki'],
                    'Penempatan Tenaga Kerja 2021' : data_lowongan_2021['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki']
                }
                df_2021 =  pd.DataFrame(data_persiapan_2021)
                
                df_2021['Rasio Penyerapan'] = df_2021['Penempatan Tenaga Kerja 2021'] / df_2021['Pencari Kerja 2021']
                df_2021['Rasio Ketersediaan Lowongan'] = df_2021['Jumlah Lowongan 2021'] / df_2021['Pencari Kerja 2021']
                df_2021['Efisiensi Penyerapan'] = df_2021['Penempatan Tenaga Kerja 2021'] / df_2021['Jumlah Lowongan 2021']
                
                df_2021['Rasio Penyerapan (Normalisasi)'] = (df_2021['Rasio Penyerapan'] - df_2021['Rasio Penyerapan'].min()) / (df_2021['Rasio Penyerapan'].max() - df_2021['Rasio Penyerapan'].min())
                df_2021['Rasio Ketersediaan Lowongan (Normalisasi)'] = (df_2021['Rasio Ketersediaan Lowongan'] - df_2021['Rasio Ketersediaan Lowongan'].min()) / (df_2021['Rasio Ketersediaan Lowongan'].max() - df_2021['Rasio Ketersediaan Lowongan'].min())
                df_2021['Efisiensi Penyerapan (Normalisasi)'] = (df_2021['Efisiensi Penyerapan'] - df_2021['Efisiensi Penyerapan'].min()) / (df_2021['Efisiensi Penyerapan'].max() - df_2021['Efisiensi Penyerapan'].min())
                
                w1, w2, w3 = 0.5, 0.3, 0.2
                df_2021['Indeks Kualitas Industri 2021'] = (w1 * df_2021['Rasio Penyerapan (Normalisasi)'] +
                                                w2 * df_2021['Rasio Ketersediaan Lowongan (Normalisasi)'] +
                                                w3 * df_2021['Efisiensi Penyerapan (Normalisasi)'])
                
                fig, ax = plt.subplots(figsize=(4,2))
                sns.barplot(x='Provinsi', y=df_2021['Indeks Kualitas Industri 2021'], data=df_2021, color='lightblue')
                for i, jumlah in enumerate(df_2021['Indeks Kualitas Industri 2021']):
                    ax.text(i, jumlah + 0.01, f"{jumlah:.2f}", ha='center', fontsize=3, color='black')
                
                plt.xlabel('Provinsi', fontsize=4)
                plt.xticks(rotation=45, ha='right', fontsize=4)
                plt.ylabel('Indeks Kualitas Industri', fontsize=4)
                plt.yticks(fontsize=4)

                st.pyplot(fig)
        

            st.header("Kesimpulan Analisis")
            st.write("""
                Diasumsikan awal pandemi Covid-19 berada diantara tahun 2019 dan 2020. Dari grafik diatas dapat dianalisis bahwa index kualitas industri sebelum terjadinya pandemi menyatakan penerunan yang cukup drastis terutama di tahun 2019. Namun, pertumbuhan index kualitas industri setelah terjadinya pandemi justru menyatakan peningkatan yang cukup signifikan. Hal tersebut kemungkinan terjadi akibat angka penerimaan tenaga kerja di awal pandemi cukup membludak. Disisi lain, mungkin banyak juga karyawan-karyawan yang terkena PHK dari perusahaannya. 
            """)







# COBA GUNAIN TAG (st.pills)
elif option_menu == 'Kumpulan Data':
    st.title('Data Collecting')

    with st.container(border=True):
        st.subheader('Tabel Jumlah Penduduk Tiap Provinsi Bedasarkan :')
        tab_t1, tab_t2 = st.tabs(['Perkotaan', 'Pedesaan'])
        with tab_t1:
            col_t1, col_t2 = st.columns(2)
            with col_t1:
                st.write("Data Laki-Laki")
                data_penduduk_perkotaan = data_gender_pertahun_perkotaan[['Provinsi', '2018_laki-laki', '2019_laki-laki', '2020_laki-laki', '2021_laki-laki']]
                st.write(data_penduduk_perkotaan)
            
            with col_t2:
                st.write("Data Perempuan")
                data_penduduk_perkotaan = data_gender_pertahun_perkotaan[['Provinsi', '2018_perempuan', '2019_perempuan', '2020_perempuan', '2021_perempuan']]
                st.write(data_penduduk_perkotaan)

        with tab_t2:
            col_t3, col_t4 = st.columns(2)
            with col_t3:
                st.write("Data Laki-Laki")
                data_penduduk_pedesaan = data_gender_pertahun_pedesaan[['Provinsi', '2018_laki-laki', '2019_laki-laki', '2020_laki-laki', '2021_laki-laki']]
                st.write(data_penduduk_pedesaan)
            with col_t4:
                st.write("Data Perempuan")
                data_penduduk_pedesaan = data_gender_pertahun_pedesaan[['Provinsi', '2018_perempuan', '2019_perempuan', '2020_perempuan', '2021_perempuan']]
                st.write(data_penduduk_pedesaan)

    with st.container(border=True):
        st.subheader("Tabel Keterangan Industri")
        option_keterangan = st.selectbox("Pililh:", ("Jumlah Pencari Pekerjaan", "Jumlah Lowongan Pekerjaan", "Jumlah Penerimaan Karyawan"))
        if option_keterangan == "Jumlah Pencari Pekerjaan":
            with st.container(border=True):
                st.subheader('Tabel Jumlah Pencari Kerja Tiap Provinsi')
                data_pencari_kerja_laki_2018 = data_lowongan_2018[['Provinsi', 'Pencari Kerja Terdaftar - Laki-Laki']]
                data_pencari_kerja_laki_2019 = data_lowongan_2019[['Provinsi', 'Pencari Kerja Terdaftar - Laki-Laki']]
                data_pencari_kerja_laki_2020 = data_lowongan_2020[['Provinsi', 'Pencari Kerja Terdaftar - Laki-Laki']]
                data_pencari_kerja_laki_2021 = data_lowongan_2021[['Provinsi', 'Pencari Kerja Terdaftar - Laki-Laki']]

                data_pencari_kerja_perempuan_2018 = data_lowongan_2018[['Provinsi', 'Pencari Kerja Terdaftar - Perempuan']]
                data_pencari_kerja_perempuan_2019 = data_lowongan_2019[['Provinsi', 'Pencari Kerja Terdaftar - Perempuan']]
                data_pencari_kerja_perempuan_2020 = data_lowongan_2020[['Provinsi', 'Pencari Kerja Terdaftar - Perempuan']]
                data_pencari_kerja_perempuan_2021 = data_lowongan_2021[['Provinsi', 'Pencari Kerja Terdaftar - Perempuan']]
                st.write("Tahun :")
        
                tab_t3, tab_t4, tab_t5, tab_t6 = st.tabs(['2018', '2019', '2020', '2021'])
                with tab_t3:
                    col_t5, col_t6 = st.columns(2)
                    with col_t5:
                        st.write("Data Laki-Laki")
                        st.write(data_pencari_kerja_laki_2018)
                    with col_t6:
                        st.write("Data Perempuan")
                        st.write(data_pencari_kerja_perempuan_2018)
                with tab_t4:
                    col_t7, col_t8 = st.columns(2)
                    with col_t7:
                        st.write("Data Laki-Laki")
                        st.write(data_pencari_kerja_laki_2019)
                    with col_t8:
                        st.write("Data Perempuan")
                        st.write(data_pencari_kerja_perempuan_2019)
                with tab_t5:
                    col_t9, col_t10 = st.columns(2)
                    with col_t9:
                        st.write("Data Laki-Laki")
                        st.write(data_pencari_kerja_laki_2020)
                    with col_t10:
                        st.write("Data Perempuan")
                        st.write(data_pencari_kerja_perempuan_2020)
                with tab_t6:
                    col_t11, col_t12 = st.columns(2)
                    with col_t11:
                        st.write("Data Laki-Laki")
                        st.write(data_pencari_kerja_laki_2021)
                    with col_t12:
                        st.write("Data Perempuan")
                        st.write(data_pencari_kerja_perempuan_2021)
        
        elif option_keterangan == "Jumlah Lowongan Pekerjaan":
            with st.container(border=True):
                st.subheader('Tabel Jumlah Lowongan Pekerjaan Tiap Provinsi')
                data_lowongan_kerja_laki_2018 = data_lowongan_2018[['Provinsi', 'Lowongan Kerja Terdaftar - Laki-Laki']]
                data_lowongan_kerja_laki_2019 = data_lowongan_2019[['Provinsi', 'Lowongan Kerja Terdaftar - Laki-Laki']]
                data_lowongan_kerja_laki_2020 = data_lowongan_2020[['Provinsi', 'Lowongan Kerja Terdaftar - Laki-Laki']]
                data_lowongan_kerja_laki_2021 = data_lowongan_2021[['Provinsi', 'Lowongan Kerja Terdaftar - Laki-Laki']]

                data_lowongan_kerja_perempuan_2018 = data_lowongan_2018[['Provinsi', 'Lowongan Kerja Terdaftar - Perempuan']]
                data_lowongan_kerja_perempuan_2019 = data_lowongan_2019[['Provinsi', 'Lowongan Kerja Terdaftar - Perempuan']]
                data_lowongan_kerja_perempuan_2020 = data_lowongan_2020[['Provinsi', 'Lowongan Kerja Terdaftar - Perempuan']]
                data_lowongan_kerja_perempuan_2021 = data_lowongan_2021[['Provinsi', 'Lowongan Kerja Terdaftar - Perempuan']]

                tab_t7, tab_t8, tab_t9, tab_t10 = st.tabs(['2018', '2019', '2020', '2021'])
                with tab_t7:
                    col_t13, col_t14 = st.columns(2)
                    with col_t13:
                        st.write("Data Laki-Laki")
                        st.write(data_lowongan_kerja_laki_2018)
                    with col_t14:
                        st.write("Data Perempuan")
                        st.write(data_lowongan_kerja_perempuan_2018)
                with tab_t8:
                    col_t15, col_t16 = st.columns(2)
                    with col_t15:
                        st.write("Data Laki-Laki")
                        st.write(data_lowongan_kerja_laki_2019)
                    with col_t16:
                        st.write("Data Perempuan")
                        st.write(data_lowongan_kerja_perempuan_2019)
                with tab_t9:
                    col_t17, col_t18 = st.columns(2)
                    with col_t17:
                        st.write("Data Laki-Laki")
                        st.write(data_lowongan_kerja_laki_2020)
                    with col_t18:
                        st.write("Data Perempuan")
                        st.write(data_lowongan_kerja_perempuan_2020)
                with tab_t10:
                    col_t19, col_t20 = st.columns(2)
                    with col_t19:
                        st.write("Data Laki-Laki")
                        st.write(data_lowongan_kerja_laki_2021)
                    with col_t20:
                        st.write("Data Perempuan")
                        st.write(data_lowongan_kerja_perempuan_2021)

        elif option_keterangan == "Jumlah Penerimaan Karyawan":
            with st.container(border=True):
                st.subheader('Tabel Jumlah Pemenuhan / Penempatan Pekerjaan Tiap Provinsi')
                data_pemenuhan_pekerjaan_laki_2018 = data_lowongan_2018[['Provinsi', 'Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki']]
                data_pemenuhan_pekerjaan_laki_2019 = data_lowongan_2019[['Provinsi', 'Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki']]
                data_pemenuhan_pekerjaan_laki_2020 = data_lowongan_2020[['Provinsi', 'Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki']]
                data_pemenuhan_pekerjaan_laki_2021 = data_lowongan_2021[['Provinsi', 'Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki']]
                data_pemenuhan_pekerjaan_perempuan_2018 = data_lowongan_2018[['Provinsi', 'Penempatan/Pemenuhan Tenaga Kerja - Perempuan']]
                data_pemenuhan_pekerjaan_perempuan_2019 = data_lowongan_2019[['Provinsi', 'Penempatan/Pemenuhan Tenaga Kerja - Perempuan']]
                data_pemenuhan_pekerjaan_perempuan_2020 = data_lowongan_2020[['Provinsi', 'Penempatan/Pemenuhan Tenaga Kerja - Perempuan']]
                data_pemenuhan_pekerjaan_perempuan_2021 = data_lowongan_2021[['Provinsi', 'Penempatan/Pemenuhan Tenaga Kerja - Perempuan']]

                tab_t11, tab_t12, tab_t13, tab_t14 = st.tabs(['2018', '2019', '2020', '2021'])
                with tab_t11:
                    col_t21, col_t22 = st.columns(2)
                    with col_t21:
                        st.write("Data Laki-Laki")
                        st.write(data_pemenuhan_pekerjaan_laki_2018)
                    with col_t22:
                        st.write("Data Perempuan")
                        st.write(data_pemenuhan_pekerjaan_perempuan_2018)
                with tab_t12:
                    col_23, col_t24 = st.columns(2)
                    with col_23:
                        st.write("Data Laki-Laki")
                        st.write(data_pemenuhan_pekerjaan_laki_2019)
                    with col_t24:
                        st.write("Data Perempuan")
                        st.write(data_pemenuhan_pekerjaan_perempuan_2019)
                with tab_t13:
                    col_25, col_t26 = st.columns(2)
                    with col_25:
                        st.write("Data Laki-Laki")
                        st.write(data_pemenuhan_pekerjaan_laki_2020)
                    with col_t26:
                        st.write("Data Perempuan")
                        st.write(data_pemenuhan_pekerjaan_perempuan_2020)
                with tab_t14:
                    col_t27, col_t28 = st.columns(2)
                    with col_t27:
                        st.write("Data Laki-Laki")
                        st.write(data_pemenuhan_pekerjaan_laki_2021)
                    with col_t28:
                        st.write("Data Perempuan")
                        st.write(data_pemenuhan_pekerjaan_perempuan_2021)

    with st.container(border=True):
        st.subheader('Tabel Jumlah Penduduk Berdasarkan Status Pekerjaan Tiap Provinsi')
        tab_k1, tab_k2, tab_k3, tab_k4 = st.tabs(["2018", "2019", "2020", "2021"])
        with tab_k1:
            st.write('2018')
            st.write(data_status_pekerjaan_2018)

        with tab_k2:
            st.write('2019')
            st.write(data_status_pekerjaan_2019)

        with tab_k3:
            st.write('2020')
            st.write(data_status_pekerjaan_2020)
        
        with tab_k4:
            st.write('2021')
            st.write(data_status_pekerjaan_2021)





elif option_menu == "Home":
    data_max_perkotaan_laki= [
        data_gender_pertahun_perkotaan['2018_laki-laki'].max(),
        data_gender_pertahun_perkotaan['2019_laki-laki'].max(),
        data_gender_pertahun_perkotaan['2020_laki-laki'].max(),
        data_gender_pertahun_perkotaan['2021_laki-laki'].max()
    ]

    data_min_perkotaan_laki = [
        data_gender_pertahun_perkotaan['2018_laki-laki'].min(),
        data_gender_pertahun_perkotaan['2019_laki-laki'].min(),
        data_gender_pertahun_perkotaan['2020_laki-laki'].min(),
        data_gender_pertahun_perkotaan['2021_laki-laki'].min()
    ]

    data_mean_perkotaan_laki = [
        data_gender_pertahun_perkotaan['2018_laki-laki'].mean(),
        data_gender_pertahun_perkotaan['2019_laki-laki'].mean(),
        data_gender_pertahun_perkotaan['2020_laki-laki'].mean(),
        data_gender_pertahun_perkotaan['2021_laki-laki'].mean()
    ]


    data_max_perkotaan_perempuan = [
        data_gender_pertahun_perkotaan['2018_perempuan'].max(),
        data_gender_pertahun_perkotaan['2019_perempuan'].max(),
        data_gender_pertahun_perkotaan['2020_perempuan'].max(),
        data_gender_pertahun_perkotaan['2021_perempuan'].max()
    ]

    data_min_perkotaan_perempuan = [
        data_gender_pertahun_perkotaan['2018_perempuan'].min(),
        data_gender_pertahun_perkotaan['2019_perempuan'].min(),
        data_gender_pertahun_perkotaan['2020_perempuan'].min(),
        data_gender_pertahun_perkotaan['2021_perempuan'].min()
    ]

    data_mean_perkotaan_perempuan = [
        data_gender_pertahun_pedesaan['2019_perempuan'].mean(),
        data_gender_pertahun_perkotaan['2020_perempuan'].mean(),
        data_gender_pertahun_perkotaan['2021_perempuan'].mean(),
        data_gender_pertahun_perkotaan['2021_perempuan'].mean()
    ]



    data_max_pedesaan_laki = [
        data_gender_pertahun_perkotaan['2018_laki-laki'].max(),
        data_gender_pertahun_perkotaan['2019_laki-laki'].max(),
        data_gender_pertahun_perkotaan['2020_laki-laki'].max(),
        data_gender_pertahun_perkotaan['2021_laki-laki'].max()
    ]

    data_min_pedesaan_laki = [
        data_gender_pertahun_pedesaan['2018_laki-laki'].min(),
        data_gender_pertahun_pedesaan['2019_laki-laki'].min(),
        data_gender_pertahun_pedesaan['2020_laki-laki'].min(),
        data_gender_pertahun_pedesaan['2021_laki-laki'].min()
    ]

    data_mean_pedesaan_laki = [
        data_gender_pertahun_pedesaan['2018_laki-laki'].mean(),
        data_gender_pertahun_pedesaan['2019_laki-laki'].mean(),
        data_gender_pertahun_pedesaan['2020_laki-laki'].mean(),
        data_gender_pertahun_pedesaan['2021_laki-laki'].mean()
    ]


    data_max_pedesaan_perempuan = [
        data_gender_pertahun_pedesaan['2018_perempuan'].max(),
        data_gender_pertahun_pedesaan['2019_perempuan'].max(),
        data_gender_pertahun_pedesaan['2020_perempuan'].max(),
        data_gender_pertahun_pedesaan['2021_perempuan'].max()
    ]

    data_min_pedesaan_perempuan = [
        data_gender_pertahun_pedesaan['2018_perempuan'].min(),
        data_gender_pertahun_pedesaan['2019_perempuan'].min(),
        data_gender_pertahun_pedesaan['2020_perempuan'].min(),
        data_gender_pertahun_pedesaan['2021_perempuan'].min()
    ]

    data_mean_pedesaan_perempuan = [
        data_gender_pertahun_pedesaan['2018_perempuan'].mean(),
        data_gender_pertahun_pedesaan['2019_perempuan'].mean(),
        data_gender_pertahun_pedesaan['2020_perempuan'].mean(),
        data_gender_pertahun_pedesaan['2021_perempuan'].mean()
    ]

    


    col_hh1, col_hh2= st.columns(2)
    with col_hh1:
        with st.container(border=True):
            st.header('Hello Everyone!')
            with st.expander("Vido Dokumentasi"):
                VIDEO_URL = "https://www.youtube.com/watch?v=MqMzgqL3MiI"
                st.video(VIDEO_URL)


    with st.container(border=True):
        st.header("Analsis Persentase Penduduk Tahun 2018 - 2021")
        st.subheader('Data Set Penduduk :')

        options = st.selectbox(
            'Pilih', ["Perkotaan", "Pedesaan"]
        )

        if options == "Perkotaan":
            df_max_perkotaan_laki = pd.DataFrame(data_max_perkotaan_laki)
            df_min_perkotaan_laki = pd.DataFrame(data_min_perkotaan_laki)
            df_mean_perkotaan_laki = pd.DataFrame(data_mean_perkotaan_laki)

            df_max_perkotaan_perempuan = pd.DataFrame(data_max_perkotaan_perempuan)
            df_min_perkotaan_perempuan = pd.DataFrame(data_min_perkotaan_perempuan)
            df_mean_perkotaan_perempuan = pd.DataFrame(data_mean_perkotaan_perempuan)

            max_value_perkotaan_laki = df_max_perkotaan_laki.max()
            min_value_perkotaan_laki = df_min_perkotaan_laki.min()
            avg_value_perkotaan_laki = df_mean_perkotaan_laki.mean()

            max_value_perkotaan_perempuan = df_max_perkotaan_perempuan.max()
            min_value_perkotaan_perempuan = df_min_perkotaan_perempuan.min()
            avg_value_perkotaan_perempuan = df_mean_perkotaan_perempuan.mean()

            option_gender_perkotaan = st.radio("Gender :", ['Laki-Laki', 'Perempuan'])
            if option_gender_perkotaan == "Laki-Laki":
                with st.container():
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        with st.container(border=True):
                            st.metric(label="Jumlah Terkecil", value=min_value_perkotaan_laki)
                            
                    with col2:
                        with st.container(border=True):
                            st.metric(label="Rata-Rata", value=round(avg_value_perkotaan_laki, 2))

                    with col3:
                        with st.container(border=True):
                            st.metric(label="Jumlah Terbesar", value=max_value_perkotaan_laki)

            elif option_gender_perkotaan == 'Perempuan':
                with st.container():
                    col11, col12, col13 = st.columns(3)
                    with col11:
                        with st.container(border=True):
                            st.metric(label="Jumlah Terkecil", value=min_value_perkotaan_perempuan)
                        
                    with col12:
                        with st.container(border=True):
                            st.metric(label="Rata-Rata", value=round(avg_value_perkotaan_perempuan, 2))

                    with col13:
                        with st.container(border=True):
                            st.metric(label="Jumlah Terbesar", value=max_value_perkotaan_perempuan)


        elif options == "Pedesaan":
            df_max_pedesaan_laki = pd.DataFrame(data_max_pedesaan_laki)
            df_min_pedesaan_laki = pd.DataFrame(data_min_pedesaan_laki)
            df_mean_pedesaan_laki = pd.DataFrame(data_mean_pedesaan_laki)

            df_max_pedesaan_perempuan = pd.DataFrame(data_max_pedesaan_perempuan)
            df_min_pedesaan_perempuan = pd.DataFrame(data_min_pedesaan_perempuan)
            df_mean_pedesaan_perempuan = pd.DataFrame(data_mean_pedesaan_perempuan)

            max_value_pedesaan_laki = df_max_pedesaan_laki.max()
            min_value_pedesaan_laki = df_min_pedesaan_laki.min()
            avg_value_pedesaan_laki = df_mean_pedesaan_laki.mean()

            max_value_pedesaan_perempuan = df_max_pedesaan_perempuan.max()
            min_value_pedesaan_perempuan = df_min_pedesaan_perempuan.min()
            avg_value_pedesaan_perempuan = df_mean_pedesaan_perempuan.mean()

            option_gender_pedesaan = st.radio("Gender :", ['Laki-Laki', 'Perempuan'])
            if option_gender_pedesaan == 'Laki-Laki':
                col4, col5, col6 = st.columns(3)
                with col4:
                    with st.container(border=True):
                        st.metric(label="Jumlah Terkecil", value=min_value_pedesaan_laki)
                        
                with col5:
                    with st.container(border=True):
                        st.metric(label="Rata-Rata", value=round(avg_value_pedesaan_laki, 2))

                with col6:
                    with st.container(border=True):
                        st.metric(label="Jumlah Terbesar", value=max_value_pedesaan_laki)

            elif option_gender_pedesaan == 'Perempuan':
                col9, col10, col11 = st.columns(3)
                with col9:
                    with st.container(border=True):
                        st.metric(label="Jumlah Terkecil", value=min_value_pedesaan_perempuan)
                        
                with col10:
                    with st.container(border=True):
                        st.metric(label="Rata-Rata", value=round(avg_value_pedesaan_perempuan, 2))
                
                with col11:
                    with st.container(border=True):
                        st.metric(label="Jumlah Terbesar", value=max_value_pedesaan_perempuan)

    with st.container(border=True):
        
        col7, col8 = st.columns(2)
        with col7:
            if options == "Perkotaan":
                    with st.container(border=True):
                        st.subheader('Data Persentase Jumlah Penduduk')
                        tab_h1, tab_h2, tab_h3, tab_h4 = st.tabs(['2018', '2019', '2020', '2021'])
                        with tab_h1:
                            perkotaan_2018 = data_gender_pertahun_perkotaan[['Provinsi', '2018_laki-laki', '2018_perempuan']]
                            st.write(perkotaan_2018)

                        with tab_h2:
                            perkotaan_2019 = data_gender_pertahun_perkotaan[['Provinsi', '2019_laki-laki', '2019_perempuan']]
                            st.write(perkotaan_2019)
                        
                        with tab_h3:
                            perkotaan_2020 = data_gender_pertahun_perkotaan[['Provinsi', '2020_laki-laki', '2020_perempuan']]
                            st.write(perkotaan_2020)

                        with tab_h4:
                            perkotaan_2021 = data_gender_pertahun_perkotaan[['Provinsi', '2021_laki-laki', '2021_perempuan']]
                            st.write(perkotaan_2021)
                    

            elif options == "Pedesaan":
                with st.container(border=True):
                    st.subheader('Data Persentase Jumlah Penduduk')
                    tab_h5, tab_h6, tab_h7, tab_h8 = st.tabs(['2018', '2019', '2020', '2021'])
                    with tab_h5:
                        pedesaan_2018 = data_gender_pertahun_pedesaan[['Provinsi', '2018_laki-laki', '2018_perempuan']]
                        st.write(pedesaan_2018)

                    with tab_h6:
                        pedesaan_2019 = data_gender_pertahun_pedesaan[['Provinsi', '2019_laki-laki', '2019_perempuan']]
                        st.write(pedesaan_2019)
                    
                    with tab_h7:
                        pedesaan_2020 = data_gender_pertahun_pedesaan[['Provinsi', '2020_laki-laki', '2020_perempuan']]
                        st.write(pedesaan_2020)

                    with tab_h8:
                        pedesaan_2021 = data_gender_pertahun_pedesaan[['Provinsi', '2021_laki-laki', '2021_perempuan']]
                        st.write(pedesaan_2021)



        with col8:
            with st.container(border=True):
                st.subheader('Grafik')
                
                tab_h9, tab_h10, tab_h11 = st.tabs(['Pencari Kerja', 'Jumlah Lowongan', 'Jumlah Penerimaan'])
                with tab_h9:
                    option_radio_pencari = st.radio("Gender :", ['Laki-Laki', 'Perempuan'], key="radio_pencari")
                    
                    if option_radio_pencari == 'Laki-Laki':
                        tahun = ['2018', '2019', '2020', '2021']
                        pencari_average_laki = {
                            "Pencari_2018": data_lowongan_2018['Pencari Kerja Terdaftar - Laki-Laki'].mean(),
                            "Pencari_2019": data_lowongan_2019['Pencari Kerja Terdaftar - Laki-Laki'].mean(),
                            "Pencari_2020": data_lowongan_2020['Pencari Kerja Terdaftar - Laki-Laki'].mean(),
                            "Pencari_2021": data_lowongan_2021['Pencari Kerja Terdaftar - Laki-Laki'].mean()
                        }

                        pencari_laki_perkotaan = [
                            pencari_average_laki["Pencari_2018"],
                            pencari_average_laki["Pencari_2019"],
                            pencari_average_laki["Pencari_2020"],
                            pencari_average_laki["Pencari_2021"]
                        ]

                        fig, ax = plt.subplots(figsize=(8,4.3))
                        sns.scatterplot(x=tahun, y=pencari_laki_perkotaan, color="green", s=100, marker='d')
                        plt.plot(tahun, pencari_laki_perkotaan, color="green", linestyle='-')

                        for i, jumlah in enumerate(pencari_laki_perkotaan):
                            ax.text(tahun[i], jumlah + 0.5, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')

                        ax.set_title("Pertumbuhan Pencari Kerja Terdaftar Laki-Laki")
                        ax.set_xlabel("Tahun")
                        ax.set_ylabel("Rata-Rata Pencari Kerja")

                        st.pyplot(fig)

                    elif option_radio_pencari == 'Perempuan':
                        tahun = ['2018', '2019', '2020', '2021']
                        pencari_average_perempuan = {
                            "Pencari_2018" : data_lowongan_2018['Pencari Kerja Terdaftar - Perempuan'].mean(),
                            "Pencari_2019" : data_lowongan_2019['Pencari Kerja Terdaftar - Perempuan'].mean(),
                            "Pencari_2020" : data_lowongan_2020['Pencari Kerja Terdaftar - Perempuan'].mean(),
                            "Pencari_2021" : data_lowongan_2021['Pencari Kerja Terdaftar - Perempuan'].mean()    
                        }

                        pencari_perempuan_perkotaan = [
                            pencari_average_perempuan["Pencari_2018"],
                            pencari_average_perempuan["Pencari_2019"],
                            pencari_average_perempuan["Pencari_2020"],
                            pencari_average_perempuan["Pencari_2021"]
                        ]

                        fig, ax = plt.subplots(figsize=(8,4.3))
                        sns.scatterplot(x=tahun, y=pencari_perempuan_perkotaan, color="green", s=100, marker='d')
                        plt.plot(tahun, pencari_perempuan_perkotaan, color="green", linestyle='-')

                        for i, jumlah in enumerate(pencari_perempuan_perkotaan):
                            ax.text(tahun[i], jumlah + 0.5, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')

                        ax.set_title("Pertumbuhan Pencari Kerja Terdaftar Perempuan")
                        ax.set_xlabel("Tahun")
                        ax.set_ylabel("Rata-Rata Pencari Kerja")

                        st.pyplot(fig)

                with tab_h10:
                    option_radio_lowongan = st.radio('Gender :', ['Laki-Laki', 'Perempuan'], key="radio_lowongan")
                    if option_radio_lowongan == 'Laki-Laki':
                        tahun = ['2018', '2019', '2020', '2021']
                        lowongan_average_laki = {
                            "Lowongan_2018" : data_lowongan_2018['Lowongan Kerja Terdaftar - Laki-Laki'].mean(),
                            "Lowongan_2019" : data_lowongan_2019['Lowongan Kerja Terdaftar - Laki-Laki'].mean(),
                            "Lowongan_2020" : data_lowongan_2020['Lowongan Kerja Terdaftar - Laki-Laki'].mean(),
                            "Lowongan_2021" : data_lowongan_2021['Lowongan Kerja Terdaftar - Laki-Laki'].mean()    
                        }

                        lowongan_laki_perkotaan = [
                            lowongan_average_laki["Lowongan_2018"],
                            lowongan_average_laki["Lowongan_2019"],
                            lowongan_average_laki["Lowongan_2020"],
                            lowongan_average_laki["Lowongan_2021"]
                        ]

                        fig, ax = plt.subplots(figsize=(8,4.3))
                        sns.scatterplot(x=tahun, y=lowongan_laki_perkotaan, color="red", s=100, marker='d')
                        plt.plot(tahun, lowongan_laki_perkotaan, color="red", linestyle='-')

                        for i, jumlah in enumerate(lowongan_laki_perkotaan):
                                ax.text(tahun[i], jumlah + 0.5, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')

                        ax.set_title("Pertumbuhan Lowongan Kerja Terdaftar (Laki-Laki)")
                        ax.set_xlabel("Tahun")
                        ax.set_ylabel("Rata-Rata Lowongan Kerja")

                        st.pyplot(fig)

                    elif option_radio_lowongan == 'Perempuan':
                        tahun = ['2018', '2019', '2020', '2021']
                        lowongan_average_perempuan = {
                            "Lowongan_2018" : data_lowongan_2018['Lowongan Kerja Terdaftar - Perempuan'].mean(),
                            "Lowongan_2019" : data_lowongan_2019['Lowongan Kerja Terdaftar - Perempuan'].mean(),
                            "Lowongan_2020" : data_lowongan_2020['Lowongan Kerja Terdaftar - Perempuan'].mean(),
                            "Lowongan_2021" : data_lowongan_2021['Lowongan Kerja Terdaftar - Perempuan'].mean()    
                        }

                        lowongan_perempuan_perkotaan = [
                            lowongan_average_perempuan["Lowongan_2018"],
                            lowongan_average_perempuan["Lowongan_2019"],
                            lowongan_average_perempuan["Lowongan_2020"],
                            lowongan_average_perempuan["Lowongan_2021"]
                        ]

                        fig, ax = plt.subplots(figsize=(8,4.3))
                        sns.scatterplot(x=tahun, y=lowongan_perempuan_perkotaan, color="red", s=100, marker='d', label='Data')
                        plt.plot(tahun, lowongan_perempuan_perkotaan, color="red", linestyle='-', label='Trend Line')

                        for i, jumlah in enumerate(lowongan_perempuan_perkotaan):
                                ax.text(tahun[i], jumlah + 0.5, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')

                        ax.set_title("Pertumbuhan Lowongan Kerja Terdaftar Perempuan")
                        ax.set_xlabel("Tahun")
                        ax.set_ylabel("Rata-Rata Lowongan Kerja")

                        st.pyplot(fig)

                with tab_h11:
                    option_radio_penerimaan = st.radio('Gender :', ['Laki-Laki', 'Perempuan'], key="radio_penerimaan")
                    if option_radio_penerimaan == 'Laki-Laki':
                        tahun = ['2018', '2019', '2020', '2021']
                        penempatan_average_laki = {
                            "Penempatan_2018" : data_lowongan_2018['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki'].mean(),
                            "Penempatan_2019" : data_lowongan_2019['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki'].mean(),
                            "Penempatan_2020" : data_lowongan_2020['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki'].mean(),
                            "Penempatan_2021" : data_lowongan_2021['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki'].mean()    
                        }

                        penempatan_laki_perkotaan = [
                            penempatan_average_laki["Penempatan_2018"],
                            penempatan_average_laki["Penempatan_2019"],
                            penempatan_average_laki["Penempatan_2020"],
                            penempatan_average_laki["Penempatan_2021"]
                        ]

                        fig, ax = plt.subplots(figsize=(8,4.3))
                        sns.scatterplot(x=tahun, y=penempatan_laki_perkotaan, color="blue", s=100, marker='d')
                        plt.plot(tahun, penempatan_laki_perkotaan, color="blue", linestyle='-')

                        for i, jumlah in enumerate(penempatan_laki_perkotaan):
                            ax.text(tahun[i], jumlah + 0.5, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')

                        ax.set_title("Pertumbuhan Penerimaan Tenaga kerja Laki-Laki")
                        ax.set_xlabel("Tahun")
                        ax.set_ylabel("Rata-Rata Lowongan Kerja")

                        st.pyplot(fig)
                    
                    elif option_radio_penerimaan == 'Perempuan':
                        tahun = ['2018', '2019', '2020', '2021']
                        penempatan_average_perempuan = {
                            "Penempatan_2018" : data_lowongan_2018['Penempatan/Pemenuhan Tenaga Kerja - Perempuan'].mean(),
                            "Penempatan_2019" : data_lowongan_2019['Penempatan/Pemenuhan Tenaga Kerja - Perempuan'].mean(),
                            "Penempatan_2020" : data_lowongan_2020['Penempatan/Pemenuhan Tenaga Kerja - Perempuan'].mean(),
                            "Penempatan_2021" : data_lowongan_2021['Penempatan/Pemenuhan Tenaga Kerja - Perempuan'].mean()    
                        }

                        penempatan_perempuan_perkotaan = [
                            penempatan_average_perempuan["Penempatan_2018"],
                            penempatan_average_perempuan["Penempatan_2019"],
                            penempatan_average_perempuan["Penempatan_2020"],
                            penempatan_average_perempuan["Penempatan_2021"]
                        ]

                        fig, ax = plt.subplots(figsize=(8,4.3))
                        sns.scatterplot(x=tahun, y=penempatan_perempuan_perkotaan, color="blue", s=100, marker='d')
                        plt.plot(tahun, penempatan_perempuan_perkotaan, color="blue", linestyle='-')

                        for i, jumlah in enumerate(penempatan_perempuan_perkotaan):
                                ax.text(tahun[i], jumlah + 0.5, f"{jumlah:.2f}", ha='center', fontsize=10, color='black')

                        ax.set_title("Pertumbuhan Penerimaan Tenaga kerja Perempuan")
                        ax.set_xlabel("Tahun")
                        ax.set_ylabel("Rata-Rata Lowongan Kerja")

                        st.pyplot(fig)
                    

    with st.container(border=True):
        st.subheader("Perbandingan Index Kualitas Industri Tiap Tahun")
        tab_h12, tab_h13, tab_h14, tab_h15 = st.tabs(['2018', '2019', '2020', '2021'])

        with tab_h12:
            
            data_persiapan_2018 = {
                'Provinsi': data_lowongan_2018['Provinsi'],
                'Pencari Kerja 2018' : data_lowongan_2018['Pencari Kerja Terdaftar - Laki-Laki'],
                'Jumlah Lowongan 2018' : data_lowongan_2018['Lowongan Kerja Terdaftar - Laki-Laki'],
                'Penempatan Tenaga Kerja 2018' : data_lowongan_2018['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki']
            }
            df =  pd.DataFrame(data_persiapan_2018)
            
            df['Rasio Penyerapan'] = df['Penempatan Tenaga Kerja 2018'] / df['Pencari Kerja 2018']
            df['Rasio Ketersediaan Lowongan'] = df['Jumlah Lowongan 2018'] / df['Pencari Kerja 2018']
            df['Efisiensi Penyerapan'] = df['Penempatan Tenaga Kerja 2018'] / df['Jumlah Lowongan 2018']

            # Normalisasi indikator
            df['Rasio Penyerapan (Normalisasi)'] = (df['Rasio Penyerapan'] - df['Rasio Penyerapan'].min()) / (df['Rasio Penyerapan'].max() - df['Rasio Penyerapan'].min())
            df['Rasio Ketersediaan Lowongan (Normalisasi)'] = (df['Rasio Ketersediaan Lowongan'] - df['Rasio Ketersediaan Lowongan'].min()) / (df['Rasio Ketersediaan Lowongan'].max() - df['Rasio Ketersediaan Lowongan'].min())
            df['Efisiensi Penyerapan (Normalisasi)'] = (df['Efisiensi Penyerapan'] - df['Efisiensi Penyerapan'].min()) / (df['Efisiensi Penyerapan'].max() - df['Efisiensi Penyerapan'].min())

            # Kombinasi indikator dengan bobot
            w1, w2, w3 = 0.5, 0.3, 0.2
            df['Indeks Kualitas Industri'] = (w1 * df['Rasio Penyerapan (Normalisasi)'] +
                                            w2 * df['Rasio Ketersediaan Lowongan (Normalisasi)'] +
                                            w3 * df['Efisiensi Penyerapan (Normalisasi)'])

            fig, ax = plt.subplots(figsize=(4,2))
            sns.barplot(x='Provinsi', y=df['Indeks Kualitas Industri'], data=df, color='lightblue')
            for i, jumlah in enumerate(df['Indeks Kualitas Industri']):
                ax.text(i, jumlah + 0.01, f"{jumlah:.2f}", ha='center', fontsize=3, color='black')  # Posisi teks sedikit di atas bar


            plt.xlabel('Provinsi', fontsize=4)
            plt.xticks(rotation=45, ha='right', fontsize=4)
            plt.ylabel('Indeks Kualitas Industri', fontsize=4)
            plt.yticks(fontsize=4)

            st.pyplot(fig)

        with tab_h13:
            data_persiapan_2019 = {
                'Provinsi': data_lowongan_2019['Provinsi'],
                'Pencari Kerja 2019' : data_lowongan_2019['Pencari Kerja Terdaftar - Laki-Laki'],
                'Jumlah Lowongan 2019' : data_lowongan_2019['Lowongan Kerja Terdaftar - Laki-Laki'],
                'Penempatan Tenaga Kerja 2019' : data_lowongan_2019['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki']
            }
            df_2019 =  pd.DataFrame(data_persiapan_2019)
            
            df_2019['Rasio Penyerapan'] = df_2019['Penempatan Tenaga Kerja 2019'] / df_2019['Pencari Kerja 2019']
            df_2019['Rasio Ketersediaan Lowongan'] = df_2019['Jumlah Lowongan 2019'] / df_2019['Pencari Kerja 2019']
            df_2019['Efisiensi Penyerapan'] = df_2019['Penempatan Tenaga Kerja 2019'] / df_2019['Jumlah Lowongan 2019']

            df_2019['Rasio Penyerapan (Normalisasi)'] = (df_2019['Rasio Penyerapan'] - df_2019['Rasio Penyerapan'].min()) / (df_2019['Rasio Penyerapan'].max() - df_2019['Rasio Penyerapan'].min())
            df_2019['Rasio Ketersediaan Lowongan (Normalisasi)'] = (df_2019['Rasio Ketersediaan Lowongan'] - df_2019['Rasio Ketersediaan Lowongan'].min()) / (df_2019['Rasio Ketersediaan Lowongan'].max() - df_2019['Rasio Ketersediaan Lowongan'].min())
            df_2019['Efisiensi Penyerapan (Normalisasi)'] = (df_2019['Efisiensi Penyerapan'] - df_2019['Efisiensi Penyerapan'].min()) / (df_2019['Efisiensi Penyerapan'].max() - df_2019['Efisiensi Penyerapan'].min())

            w1, w2, w3 = 0.5, 0.3, 0.2
            df_2019['Indeks Kualitas Industri 2019'] = (w1 * df_2019['Rasio Penyerapan (Normalisasi)'] +
                                            w2 * df_2019['Rasio Ketersediaan Lowongan (Normalisasi)'] +
                                            w3 * df_2019['Efisiensi Penyerapan (Normalisasi)'])

            fig, ax = plt.subplots(figsize=(4,2))
            sns.barplot(x='Provinsi', y=df_2019['Indeks Kualitas Industri 2019'], data=df_2019, color='lightblue')
            for i, jumlah in enumerate(df_2019['Indeks Kualitas Industri 2019']):
                ax.text(i, jumlah + 0.01, f"{jumlah:.2f}", ha='center', fontsize=3, color='black')


            plt.xlabel('Provinsi', fontsize=4)
            plt.xticks(rotation=45, ha='right', fontsize=4)
            plt.ylabel('Indeks Kualitas Industri', fontsize=4)
            plt.yticks(fontsize=4)

            st.pyplot(fig)

        with tab_h14:
            data_persiapan_2020 = {
                'Provinsi': data_lowongan_2020['Provinsi'],
                'Pencari Kerja 2020' : data_lowongan_2020['Pencari Kerja Terdaftar - Laki-Laki'],
                'Jumlah Lowongan 2020' : data_lowongan_2020['Lowongan Kerja Terdaftar - Laki-Laki'],
                'Penempatan Tenaga Kerja 2020' : data_lowongan_2020['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki']
            }
            df_2020 =  pd.DataFrame(data_persiapan_2020)
            
            df_2020['Rasio Penyerapan'] = np.where(df_2020['Pencari Kerja 2020'] > 0,  df_2020['Penempatan Tenaga Kerja 2020'] / df_2020['Pencari Kerja 2020'], 0)
            df_2020['Rasio Ketersediaan Lowongan'] = df_2020['Jumlah Lowongan 2020'] / df_2020['Pencari Kerja 2020']
            df_2020['Efisiensi Penyerapan'] = df_2020['Penempatan Tenaga Kerja 2020'] / df_2020['Jumlah Lowongan 2020']

            df_2020['Rasio Penyerapan (Normalisasi)'] = (df_2020['Rasio Penyerapan'] - df_2020['Rasio Penyerapan'].min()) / (df_2020['Rasio Penyerapan'].max() - df_2020['Rasio Penyerapan'].min())
            df_2020['Rasio Ketersediaan Lowongan (Normalisasi)'] = (df_2020['Rasio Ketersediaan Lowongan'] - df_2020['Rasio Ketersediaan Lowongan'].min()) / (df_2020['Rasio Ketersediaan Lowongan'].max() - df_2020['Rasio Ketersediaan Lowongan'].min())
            df_2020['Efisiensi Penyerapan (Normalisasi)'] = (df_2020['Efisiensi Penyerapan'] - df_2020['Efisiensi Penyerapan'].min()) / (df_2020['Efisiensi Penyerapan'].max() - df_2020['Efisiensi Penyerapan'].min())

            w1, w2, w3 = 0.5, 0.3, 0.2
            df_2020['Indeks Kualitas Industri 2020'] = (w1 * df_2020['Rasio Penyerapan (Normalisasi)'] +
                                            w2 * df_2020['Rasio Ketersediaan Lowongan (Normalisasi)'] +
                                            w3 * df_2020['Efisiensi Penyerapan (Normalisasi)'])

            fig, ax = plt.subplots(figsize=(4,2))
            sns.barplot(x='Provinsi', y=df_2020['Indeks Kualitas Industri 2020'], data=df_2020, color='lightblue')
            for i, jumlah in enumerate(df_2020['Indeks Kualitas Industri 2020']):
                ax.text(i, jumlah + 0.01, f"{jumlah:.2f}", ha='center', fontsize=3, color='black')


            plt.xlabel('Provinsi', fontsize=4)
            plt.xticks(rotation=45, ha='right', fontsize=4)
            plt.ylabel('Indeks Kualitas Industri', fontsize=4)
            plt.yticks(fontsize=4)

            st.pyplot(fig)

        with tab_h15:
            data_persiapan_2021 = {
                'Provinsi': data_lowongan_2021['Provinsi'],
                'Pencari Kerja 2021' : data_lowongan_2021['Pencari Kerja Terdaftar - Laki-Laki'],
                'Jumlah Lowongan 2021' : data_lowongan_2021['Lowongan Kerja Terdaftar - Laki-Laki'],
                'Penempatan Tenaga Kerja 2021' : data_lowongan_2021['Penempatan/Pemenuhan Tenaga Kerja - Laki-Laki']
            }
            df_2021 =  pd.DataFrame(data_persiapan_2021)
            
            df_2021['Rasio Penyerapan'] = df_2021['Penempatan Tenaga Kerja 2021'] / df_2021['Pencari Kerja 2021']
            df_2021['Rasio Ketersediaan Lowongan'] = df_2021['Jumlah Lowongan 2021'] / df_2021['Pencari Kerja 2021']
            df_2021['Efisiensi Penyerapan'] = df_2021['Penempatan Tenaga Kerja 2021'] / df_2021['Jumlah Lowongan 2021']
            
            df_2021['Rasio Penyerapan (Normalisasi)'] = (df_2021['Rasio Penyerapan'] - df_2021['Rasio Penyerapan'].min()) / (df_2021['Rasio Penyerapan'].max() - df_2021['Rasio Penyerapan'].min())
            df_2021['Rasio Ketersediaan Lowongan (Normalisasi)'] = (df_2021['Rasio Ketersediaan Lowongan'] - df_2021['Rasio Ketersediaan Lowongan'].min()) / (df_2021['Rasio Ketersediaan Lowongan'].max() - df_2021['Rasio Ketersediaan Lowongan'].min())
            df_2021['Efisiensi Penyerapan (Normalisasi)'] = (df_2021['Efisiensi Penyerapan'] - df_2021['Efisiensi Penyerapan'].min()) / (df_2021['Efisiensi Penyerapan'].max() - df_2021['Efisiensi Penyerapan'].min())
            
            w1, w2, w3 = 0.5, 0.3, 0.2
            df_2021['Indeks Kualitas Industri 2021'] = (w1 * df_2021['Rasio Penyerapan (Normalisasi)'] +
                                              w2 * df_2021['Rasio Ketersediaan Lowongan (Normalisasi)'] +
                                              w3 * df_2021['Efisiensi Penyerapan (Normalisasi)'])
            
            fig, ax = plt.subplots(figsize=(4,2))
            sns.barplot(x='Provinsi', y=df_2021['Indeks Kualitas Industri 2021'], data=df_2021, color='lightblue')
            for i, jumlah in enumerate(df_2021['Indeks Kualitas Industri 2021']):
                ax.text(i, jumlah + 0.01, f"{jumlah:.2f}", ha='center', fontsize=3, color='black')
            
            plt.xlabel('Provinsi', fontsize=4)
            plt.xticks(rotation=45, ha='right', fontsize=4)
            plt.ylabel('Indeks Kualitas Industri', fontsize=4)
            plt.yticks(fontsize=4)

            st.pyplot(fig)
