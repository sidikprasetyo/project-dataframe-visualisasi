import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64

# Menambahkan gambar ke sidebar
st.sidebar.markdown(
    """
    <div style='display: flex; justify-content: center;'>
        <img class='sidebar-img' src='https://businesstalentgroup.com/wp-content/uploads/2018/02/data-science_circle_rgb.png' />
    </div>
    """,
    unsafe_allow_html=True
)

# Menambahkan CSS
st.markdown(
    """
    <style>
        @media only screen and (max-width: 600px) {
                .sidebar .stButton {
                    width: 100%;
                }
            }
        .sidebar-img {
            max-width: 175px;
            display: block;
            margin-left: 0px;
            margin-top: -75px;
            margin-bottom: 20px;
        }
        .sidebar .sidebar-content {
            width: 250px;
        }
        .hae {
            margin-top: -35px;
            margin-bottom: 20px;
        }
        div.stButton > button:first-child {
            background-color: #4CAF50;
            color: white;
            padding: 5px 10px;
            text-align: left;
            text-decoration: none;
            display: inline-block;
            font-size: 15px;
            margin: 0px 0px;
            cursor: pointer;
            border-radius: 5px;
            border: none;
            width: 100%;
        }
        div.stButton > button:first-child:hover {
            background-color: #45a049;
            color: #FFFF00;
        }
        div.stButton > button:first-child:active {
            background-color: #45a049;
        }
    </style>
""",
    unsafe_allow_html=True
)

st.sidebar.markdown("<h1 class='hae' style='text-align: center;'>Data Frame and Visualization</h1>", unsafe_allow_html=True)

selected_option = 'op1'

if st.sidebar.button('Dashboard', key='op1'):
    selected_option = 'op1'

if st.sidebar.button('Data Frame', key='op2'):
    selected_option = 'op2'

if st.sidebar.button('Data Visualization', key='op3'):
    selected_option = 'op3'


if selected_option == 'op1':
    st.markdown("<h1 style='text-align: center;'>Project Pemrograman Python Data Frame and Visualization Health Insurance</h1>", unsafe_allow_html=True)
    st.write('1. Azkha Brilliant Firdaus (210103126)\n2. Christian Imanuel Munaiseche (210103128)\n3. Sidik Prasetyo (210103142)\n4. Vincensius Gilang Pramudito (210103144)')
    # Baca file CSV
    data = pd.read_csv("insurance.csv")  

    # Fungsi untuk mengunduh file CSV
    def download_csv(data):
        csv_file = data.to_csv(index=False)
        b64 = base64.b64encode(csv_file.encode()).decode()  # Konversi file CSV ke base64
        href = "Download Data Set : "f'<a href="data:file/csv;base64,{b64}" download="insurance.csv">Unduh file CSV</a>'
        return href

    # Menampilkan tombol unduh
    st.markdown(download_csv(data), unsafe_allow_html=True)

elif selected_option == 'op2':
    st.markdown("<h1 style='text-align: center;'>Data Frame Health Insurance</h1>", unsafe_allow_html=True)
    df = pd.read_csv("insurance.csv")

    st.markdown("<h3 style='text-left: center;'>Data Frame</h3>", unsafe_allow_html=True)
    st.dataframe(df)


    # In[4]:

    st.markdown("<h3 style='text-left: center;'>Daftar 5 data teratas dalam dataset</h3>", unsafe_allow_html=True)
    st.dataframe(df.head())


    # ##### fungsi describe di pandas

    # In[5]:
    st.markdown("<h3 style='text-left: center;'>Statistik ringkasan dari data frame</h3>", unsafe_allow_html=True)
    st.write(df.describe())


    # In[11]:


    umur = df[df['age'] < 21]
    filtered = umur['age'].count()
    st.markdown(f"<h3 style='text-left: center;'>Peserta asuransi berumur kurang dari 21 tahun : {filtered} orang</h3>", unsafe_allow_html=True)
    st.write(umur)

    # ##### pengindeksan ulang

    # In[12]:


    df_indexed = df.set_index('age')
    st.markdown("<h3 style='text-left: center;'>Data frame setelah diindeks ulang :</h3>", unsafe_allow_html=True)
    st.write(df_indexed)


    # ##### grouping

    # In[13]:


    grouped_data = df.groupby('region')['charges'].mean()
    st.markdown("<h3 style='text-left: center;'>Penggabungan data charges berdasarkan wilayah :</h3>", unsafe_allow_html=True)
    st.write(grouped_data)


    # ##### sortir data

    # In[14]:


    sorted_data = df.sort_values('charges', ascending=False)
    st.markdown("<h3 style='text-left: center;'>Pengurutan data berdasarkan biaya charges terbesar :</h3>", unsafe_allow_html=True)
    st.write("")
    st.write(sorted_data)

elif selected_option == 'op3':
    st.markdown("<h1 style='text-align: center;'>Visualization Data Health Insurance</h1>", unsafe_allow_html=True)
    df = pd.read_csv("insurance.csv")
    dfn = np.genfromtxt("insurance.csv", delimiter=",", skip_header=1)

    average_age = np.mean(dfn[:, 0])

    average_age_rounded = round(average_age, 2)

    # In[18]:

    st.markdown("<h3 style='text-left: center;'>Distribusi Usia Peserta Asuransi</h3>", unsafe_allow_html=True)
    plot1 = plt.figure(figsize=(8, 6))
    plt.hist(df['age'], bins=30, color='skyblue', edgecolor='black')
    plt.xlabel('Usia')
    plt.ylabel('Frekuensi')
    plt.xlabel(f"Rata-rata usia peserta asuransi : {average_age_rounded}")
    plt.title('Distribusi Usia')
    st.pyplot(plot1)


    # In[19]:
    st.markdown("<h3 style='text-left: center;'>Distribusi Gender Peserta Asuransi</h3>", unsafe_allow_html=True)
    dfn = np.genfromtxt("insurance.csv", delimiter=",", dtype=str, skip_header=1)

    count_male = np.count_nonzero(dfn[:, 1] == 'male')
    count_female = np.count_nonzero(dfn[:, 1] == 'female')

    keterangan_gender = [f"Jumlah peserta asuransi laki-laki : {count_male}", f"Jumlah peserta asuransi perempuan : {count_female}"]

    sex_count = df['sex'].value_counts()
    plot2 = plt.figure(figsize=(8, 6))
    wedges, texts, autotexts = plt.pie(sex_count, labels=sex_count.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
    plt.legend(wedges, keterangan_gender, title="Gender",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1.5))
    plt.title('Distribusi Gender')
    st.pyplot(plot2)

    # In[20]:

    st.markdown("<h3 style='text-left: center;'>Distribusi Biaya Asuransi</h3>", unsafe_allow_html=True)
    plot3 = sns.displot(data=df, x='charges')
    plt.title('Distribusi Biaya Asuransi')
    st.pyplot(plot3)


    # In[33]:

    st.markdown("<h3 style='text-left: center;'>Biaya Asuransi Berdasarkan Gender</h3>", unsafe_allow_html=True)
    plot4 = sns.catplot(data=df, x='sex', y='charges',  hue='sex', palette="deep", legend=False)
    plt.title('Biaya Asuransi vs Gender')
    st.pyplot(plot4)


    # In[34]:
    dfn = np.genfromtxt("insurance.csv", delimiter=",", dtype=str, skip_header=1)

    count_nochildren = np.count_nonzero(dfn[:, 3] == '0')
    count_1children = np.count_nonzero(dfn[:, 3] == '1')
    count_2children = np.count_nonzero(dfn[:, 3] == '2')
    count_3children = np.count_nonzero(dfn[:, 3] == '3')
    count_4children = np.count_nonzero(dfn[:, 3] == '4')
    count_5children = np.count_nonzero(dfn[:, 3] == '5')

    keterangan =[   f"Jumlah peserta asuransi yang tidak memiliki anak : {count_nochildren}",
        f"Jumlah peserta asuransi yang memiliki anak 1 : {count_1children}",
        f"Jumlah peserta asuransi yang memiliki anak 2 : {count_2children}",
        f"Jumlah peserta asuransi yang memiliki anak 3 : {count_3children}",
        f"Jumlah peserta asuransi yang memiliki anak 4 : {count_4children}",
        f"Jumlah peserta asuransi yang memiliki anak 5 : {count_5children}"]

    st.markdown("<h3 style='text-left: center;'>Distribusi Peserta Asuransi yang Memiliki Anak</h3>", unsafe_allow_html=True)
    children_counts = df['children'].value_counts()
    plot5 = plt.figure(figsize=(8, 6))
    wedges, texts, autotexts = plt.pie(children_counts, labels=children_counts.index, autopct='%1.1f%%', startangle=0, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'silver','aqua'])
    plt.legend(wedges, keterangan, title="Jumlah Anak yang Dimiliki",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1))
    plt.title('Distribusi Anak')
    st.pyplot(plot5)

    # ##### mencari jumlah peserta yang memiliki anak

    # In[35]:

    st.markdown("<h3 style='text-left: center;'>Biaya Asuransi Berdasarkan Jumlah Anak</h3>", unsafe_allow_html=True)
    plot6 = sns.catplot(data=df, x='children', y='charges',  hue='children', palette="deep", legend=False)
    plt.title('Biaya Asuransi vs Anak')
    st.pyplot(plot6)

    # In[24]:

    st.markdown("<h3 style='text-left: center;'>Distribusi Peserta Asuransi Perokok dan Non-Perokok</h3>", unsafe_allow_html=True)
    smoker_counts = df['smoker'].value_counts()
    plot7 = plt.figure(figsize=(8, 6))
    plt.pie(smoker_counts, labels=smoker_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
    plt.title('Persentase Peserta Asuransi yang merokok dan tidak')
    st.pyplot(plot7)


    # In[37]:

    st.markdown("<h3 style='text-left: center;'>Biaya Asuransi Berdasarkan Perokok dan Non-Perokok</h3>", unsafe_allow_html=True)
    plot8 = sns.catplot(df, x='smoker', y='charges',  hue='smoker', palette="deep", legend=False)
    plt.title('Biaya Asuransi vs Perokok')
    st.pyplot(plot8)


    # In[38]:
    st.markdown("<h3 style='text-left: center;'>Distribusi Peserta Asuransi Berdasarkan Wilayah</h3>", unsafe_allow_html=True)
    region_counts = df['region'].value_counts()
    plot13 = plt.figure(figsize=(8, 6))
    plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightyellow'])
    plt.title('Persentase Peserta Asuransi Berdasarkan Wilayah')
    st.pyplot(plot13)


    st.markdown("<h3 style='text-left: center;'>Biaya Asuransi Berdasarkan Wilayah</h3>", unsafe_allow_html=True)
    plot9 = sns.catplot(df, x='region', y='charges',  hue='region', palette="deep", legend=False)
    plt.title('Biaya Asuransi Vs Wilayah')
    st.pyplot(plot9)


    # In[27]:

    st.markdown("<h3 style='text-left: center;'>Distribusi BMI Peserta Asuransi</h3>", unsafe_allow_html=True)
    plot10 = plt.figure(figsize=(8, 6))
    plt.hist(df['bmi'], bins=30, color='skyblue', edgecolor='black')
    plt.title('Histogram BMI')
    plt.xlabel('BMI')
    plt.ylabel('Frekuensi')
    st.pyplot(plot10)


    # In[28]:

    st.markdown("<h3 style='text-left: center;'>Biaya Asuransi Berdasarkan Usia</h3>", unsafe_allow_html=True)
    plot11 = plt.figure(figsize=(8, 6))
    plt.scatter(df['age'], df['charges'], alpha=0.5, color='b')
    plt.title('Usia vs Biaya Asuransi')
    plt.xlabel('Age')
    plt.ylabel('Charges')
    st.pyplot(plot11)


    # In[29]:


    # Menambahkan anotasi ke dalam scatter plot
    st.markdown("<h3 style='text-left: center;'>Biaya Asuransi Berdasarkan BMI</h3>", unsafe_allow_html=True)
    plot12 = plt.figure(figsize=(8, 6))
    plt.scatter(df['bmi'], df['charges'], alpha=0.5, color='b', label='Data Asuransi')
    plt.title('BMI vs Biaya Asuransi', fontsize=16)
    plt.xlabel('BMI', fontsize=12)
    plt.ylabel('Charges', fontsize=12)
    plt.legend()
    plt.annotate('Anomali di sini', xy=(35, 45000), xytext=(30, 50000), arrowprops=dict(facecolor='black', shrink=0.05))
    st.pyplot(plot12)

    # In[31]:

    st.markdown("<h3 style='text-left: center;'>BOX PLOT</h3>", unsafe_allow_html=True)
    plot14 = plt.figure(figsize=(8, 6))
    df[['age', 'bmi', 'children']].boxplot()
    plt.title('Box Plot Usia, BMI, dan Jumlah Anak')
    st.pyplot(plot14)