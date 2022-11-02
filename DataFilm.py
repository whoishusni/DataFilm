{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMRAa2hz/bNWKhkOK2gBbfH",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/whoishusni/DataFilm/blob/main/DataFilm.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "kode"
      ],
      "metadata": {
        "id": "U8nesPFGmvOm"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "package to install:\n",
        "1.   requests\n",
        "2.   pyfiglet\n",
        "\n"
      ],
      "metadata": {
        "id": "dGWek-dYPbLN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import requests as rq\n",
        "import datetime as dt\n",
        "from pyfiglet import Figlet\n",
        "import os\n",
        "import time\n",
        "import sys\n",
        "import pip\n",
        "import importlib\n",
        "\n",
        "#variable film\n",
        "API_KEY = ''\n",
        "BASE_URL = 'https://api.themoviedb.org/3'\n",
        "\n",
        "banner = Figlet(font='big')\n",
        "banner_show = banner.renderText('DataFilm')\n",
        "\n",
        "# Fungsi Menampilkan Film Trending Mingguan\n",
        "# TODO : Genre masih mau diperbaiki, mau dibuatkan kelas\n",
        "def trending():\n",
        "    os.system('cls')\n",
        "    os.system('clear')\n",
        "    print(banner_show)\n",
        "    TRENDING_ENDPOINT = f'/trending/movie/week?api_key={API_KEY}&language=id-ID'\n",
        "    sekarang = dt.date.today()\n",
        "    response = rq.get(BASE_URL+TRENDING_ENDPOINT)\n",
        "    res = response.json()\n",
        "    print(\"Film Box Office yang Trending Minggu Ini \" + str(sekarang))\n",
        "    for json in res['results']:\n",
        "        print(f\"\"\"\n",
        "        Judul    = {json['original_title']}\n",
        "        Rilis    = {json['release_date']}\n",
        "        Genre    = {json['genre_ids']}\n",
        "        Skor     = {json['vote_average']}\n",
        "        Sinopsis = {json['overview']}\n",
        "        \"\"\")\n",
        "# fungsi pencarian Film\n",
        "def cari():\n",
        "    os.system('cls')\n",
        "    os.system('clear')\n",
        "    keyword = input('Masukkan Judul Film Yang Mau Dicari ? ')\n",
        "    SEARCH_ENDPOINT = f'/search/movie?api_key={API_KEY}&language=id-ID&query={keyword}&page=1&include_adult=false'\n",
        "    response = rq.get(BASE_URL+SEARCH_ENDPOINT)\n",
        "    res = response.json()\n",
        "    for i in res['results']:\n",
        "        print(f\"\"\"\n",
        "        Judul    = {i['original_title']}\n",
        "        Rilis    = {i['release_date']}\n",
        "        Genre    = {i['genre_ids']}\n",
        "        Skor     = {i['vote_average']}\n",
        "        Sinopsis = {i['overview']}\n",
        "        \"\"\")\n",
        "    \n",
        "    \n",
        "# Main Function\n",
        "def main():\n",
        "    os.system('cls')\n",
        "    os.system('clear')\n",
        "    print(banner_show)\n",
        "    print('created by : Husni\\n\\n')\n",
        "    print(' Menu Utama '.center(50,'='))\n",
        "    print('1. Daftar Film Trending Mingguan')\n",
        "    print('2. Pencarian Film')\n",
        "    print('3. Exit')\n",
        "    print('\\n')\n",
        "    menu = input('Pilih Menu : ')\n",
        "    if menu == '1':\n",
        "        trending()\n",
        "    elif menu == '2':\n",
        "        cari()\n",
        "    elif menu == '3':\n",
        "        print('Exit....')\n",
        "        time.sleep(0.5)\n",
        "        os._exit(os.EX_OK)\n",
        "    else:\n",
        "        print(f'Menu Nomor {menu} Tidak Ditemukan\\nSilahkan Coba Lagi')\n",
        "        time.sleep(2)\n",
        "        main()\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()"
      ],
      "metadata": {
        "id": "cvSjtH4KGlwi"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}