# Importing
from bs4 import BeautifulSoup
import pandas as pd
import requests
import openpyxl


# Functions
def prestasi_2022():
    url = 'https://ditmawa.ugm.ac.id/sang-juara-2022/'
    html = requests.get(url)
    html_content = html.content
    soup = BeautifulSoup(html_content, 'html.parser')

    tables = soup.find_all('table')
    table = tables[1]
 
    data_mahasiswa = pd.DataFrame(columns=['No','Nama Mahasiswa','Fakultas Ketua','Prestasi','Tingkat Kegiatan','Nama Kegiatan'])

    for row in table.find('tbody').find_all('tr'):
        col = row.find_all('td')
        no = col[0].text
        nama = col[1].text
        fakultas = col[2].text
        prestasi = col[3].text
        tingkat = col[4].text
        kegiatan = col[5].text
        if input_lomba in tingkat:
            data_mahasiswa = data_mahasiswa.append({'No':no,'Nama Mahasiswa':nama,'Fakultas Ketua':fakultas,'Prestasi':prestasi,'Tingkat Kegiatan':tingkat,'Nama Kegiatan':kegiatan}, ignore_index=True)
    
    data_mahasiswa.to_excel('data_prestasi_2022.xlsx', index=False, header=False)

    return data_mahasiswa

def prestasi_2021():
    url = 'https://ditmawa.ugm.ac.id/sang-juara-2021/'
    html = requests.get(url)
    html_content = html.content
    soup = BeautifulSoup(html_content, 'html.parser')

    tables = soup.find_all('table')
    table = tables[1]
 
    data_mahasiswa = pd.DataFrame(columns=['Nama Mahasiswa','Fakultas Ketua','Prestasi','Tingkat Kegiatan','Nama Kegiatan'])

    for row in table.find('tbody').find_all('tr'):
        col = row.find_all('td')
        nama = col[0].text
        fakultas = col[1].text
        prestasi = col[2].text
        tingkat = col[3].text
        kegiatan = col[4].text
        if input_lomba in tingkat:
            data_mahasiswa = data_mahasiswa.append({'Nama Mahasiswa':nama,'Fakultas Ketua':fakultas,'Prestasi':prestasi,'Tingkat Kegiatan':tingkat,'Nama Kegiatan':kegiatan}, ignore_index=True)
    
    data_mahasiswa.to_excel('data_prestasi_2021.xlsx', index=False, header=False)

    return data_mahasiswa



#User Page
while(True) :
    print("SELAMAT DATANG DI PROGRAM WEBSCRAPING DATA PRESTASI UNIVERSITAS GADJAH MADA")
    print("===========================================================================")
    print(f"1. Prestasi Tahun 2022")
    print(f"2. Prestasi Tahun 2021")

    user_option = input("Masukan opsi: ")
    if user_option == "1":
        input_lomba = input("Tingkat Perlombaan: ")
        prestasi_2022()
    if user_option == "2":
        input_lomba = input("Tingkat Perlombaan: ")
        prestasi_2021()
    is_done = input("Mau tambah lagi? (y/n):")
    if is_done == "n":
        break