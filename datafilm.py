import requests as rq
import datetime as dt
from pyfiglet import Figlet
import os
import time
import csv
import platform

#variable film
API_KEY = 'ea01ca5302449a0f3a35a38947ef180f'
BASE_URL = 'https://api.themoviedb.org/3'
IMAGE_URL = 'https://image.tmdb.org/t/p/w500'

banner = Figlet(font='big')
banner_show = banner.renderText('DataFilm')

def write_trending():
    writer = csv.writer(open('trending.csv','w', newline=''))
    header =['Judul','rilis','Skor','Sinopsis','Image']
    writer.writerow(header)

def write_search(keyword):
    writer = csv.writer(open('{}.csv'.format(keyword),'w', newline=''))
    header =['judul','rilis','skor','plot','image']
    writer.writerow(header)

def terminal_clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
  
def trending():
    write_trending()
    terminal_clear()
    print(banner_show)
    TRENDING_ENDPOINT = f'/trending/movie/week?api_key={API_KEY}&language=id-ID'
    sekarang = dt.date.today()
    response = rq.get(BASE_URL+TRENDING_ENDPOINT)
    res = response.json()
    print('Daftar 10 Film Box Office yang Trending Minggu Ini {}' .format(str(sekarang)))
    for i in res['results']:
        print('Judul: {}'.format(i['title']))
        writer = csv.writer(open('trending.csv','a', newline=''))
        data =[i['title'],i['release_date'],i['vote_average'],i['overview'],IMAGE_URL+i['poster_path']]
        writer.writerow(data)
      
def cari(query):
    terminal_clear()
    print(banner_show)
    write_search(query)
    # kayaknya  masih mau diperbaiki URL dibawah
    SEARCH_ENDPOINT = f'/search/movie?api_key={API_KEY}&language=id-ID&query={query}&page=1&include_adult=false'
    response = rq.get(BASE_URL+SEARCH_ENDPOINT)
    res = response.json()
    print('tersedia 1 dari {} Halaman'.format(res['total_pages']))
    for hal in range(1,res['total_pages']+1):
        SEARCH_ENDPOINT2 = f'/search/movie?api_key={API_KEY}&language=id-ID&query={query}&page={hal}&include_adult=false'
        response = rq.get(BASE_URL+SEARCH_ENDPOINT2)
        ress = response.json()
        for j in ress['results']:
            print('Judul: {}'.format(j['title']))
    #         writer = csv.writer(open('{}.csv'.format(query),'a', newline=''))
    #         data =[j['title'],j['release_date'],j['vote_average'],j['overview'],IMAGE_URL+j['poster_path']]
    #         writer.writerow(data)
    # return query

def main():
    terminal_clear()
    print(banner_show)
    print('created by : Husni\n\n')
    print(' Menu Utama '.center(50,'='))
    print('1. Daftar Film Trending Mingguan')
    print('2. Pencarian Film')
    print('3. Exit')
    print('\n')
    menu = input('Pilih Menu : ')
    if menu == '1':
        trending()
    elif menu == '2':
        query = input('Masukkan Judul Film yang mau dicari ? ')
        cari(query)
    elif menu == '3':
        print('Exit....')
        time.sleep(0.5)
        os._exit(os.EX_OK)
    else:
        print('Menu Nomor {} Tidak Ditemukan\nSilahkan Coba Lagi'.format(menu))
        time.sleep(2)
        main()

if __name__ == '__main__':
    main()