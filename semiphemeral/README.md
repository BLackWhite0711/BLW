![Logo](/img/logo-small.png)

# Semiphemeral

Ada banyak alat yang memungkinkan Anda membuat umpan Twitter Anda sesaat, secara otomatis menghapus tweet yang lebih lama dari batas tertentu, seperti satu bulan.

Semiphemeral melakukan ini, tetapi juga memungkinkan Anda secara otomatis mengecualikan tweet berdasarkan kriteria: berapa banyak RT atau suka yang dimiliki, dan jika mereka bagian dari utas di mana salah satu tweet Anda memiliki banyak RT atau suka. Ini juga memungkinkan Anda secara manual memilih tweet yang ingin Anda kecualikan dari penghapusan.

~~ Ini juga dapat secara otomatis menghapus pesan langsung lama Anda. ~~ (Dukungan DM saat ini [rusak] (https://github.com/tweepy/tweepy/issues/1081) dalam tweepy, aku akan menunggu sampai diperbaiki pertama.)

_Baca selengkapnya di posting blog: [Semiphemeral: Secara otomatis menghapus tweet lama Anda, kecuali yang Anda ingin pertahankan] (https://micahflee.com/2019/06/semiphemeral-automatically-delete-your-old-tweets- Kecuali-untuk-yang-Anda-ingin-untuk-menjaga /) _


## Installation

```
pip3 install semiphemeral
```

## Bagaimana itu bekerja

Semiphemeral adalah alat baris perintah yang Anda jalankan secara lokal di komputer Anda, atau di server.

```
$ semiphemeral
Usage: semiphemeral [OPTIONS] COMMAND [ARGS]...

  Secara otomatis menghapus tweet lama Anda, kecuali yang Anda ingin pertahankan

Options:
  --help  Show this message and exit.

Commands:
  configure  Start the web server to configure semiphemeral
  delete     Delete tweets that aren't automatically or manually excluded
  fetch      Download all tweets
  stats      Show stats about tweets in the database
```

Mulailah dengan menjalankan `semiphemeral configure`, yang memulai server web lokal di http://127.0.0.1:8080/. Muat situs web itu di browser.

Anda harus memberikan kredensial API Twitter di sini, yang bisa Anda peroleh dengan mengikuti [panduan ini] (https://python-twitter.readthedocs.io/en/latest/getting_started.html). Pada dasarnya, Anda harus masuk ke https://developer.twitter.com/ dan membuat "aplikasi Twitter" baru yang hanya akan Anda gunakan (saat membuat aplikasi, Anda boleh menggunakan https://github.com / micahflee / semiphemeral sebagai URL situs web untuk aplikasi Anda).
From the settings page you also tell semiphemeral which tweets to exclude from deletion:

![Settings](/img/settings.png)

Setelah Anda mengkonfigurasi semiphemeral, ambil semua tweet dari akun Anda dengan menjalankan `semiphemeral fetch`. (Mungkin butuh waktu lama jika Anda memiliki banyak tweet - ketika semiphemeral mencapai batas tingkat Twitter, ia hanya menunggu jumlah waktu tersingkat yang diizinkan hingga dapat melanjutkan pengambilan.)

Kemudian kembali ke aplikasi web konfigurasi dan lihat halaman tweet. Dari sini, Anda dapat melihat semua tweet yang akan dihapus saat berikutnya Anda menjalankan `semiphemeral delete`, dan memilih untuk secara manual mengecualikan beberapa dari mereka dari penghapusan. Antarmuka ini memberi peringkat pada semua tweet yang dipentaskan untuk dihapus, dan memungkinkan Anda untuk memfilternya dengan mencari frasa dalam teks tweet Anda.

Setelah Anda memilih semua tweet yang ingin Anda kecualikan, Anda mungkin ingin [mengunduh arsip Twitter Anda] (https://help.twitter.com/en/managing-your-account/how-to-download-your-twitter- arsip) untuk catatan Anda.

Kemudian jalankan `semiphemeral delete` (ini juga mengambil tweet terbaru sebelum menghapus). Pertama kali mungkin butuh waktu lama. Seperti halnya dengan mengambil, ia akan menunggu ketika mencapai batas tingkat Twitter. Biarkan berjalan sekali dulu sebelum mengotomatiskannya.

Setelah Anda menghapus secara manual sekali, Anda dapat secara otomatis menghapus tweet lama Anda dengan menjalankan `semiphemeral delete` sekali sehari dalam pekerjaan cron.

Pengaturan disimpan di `~ / .semiphemeral / settings.json`. Semua tweets (termasuk pengecualian, dan tweet yang dihapus) disimpan dalam database sqlite `~ / .semiphemeral / tweets.db`.

## Development

Pastikan Anda memiliki [pipenv] (https://pipenv.readthedocs.io/en/latest/). Kemudian instal dependensi:

```sh
pipenv install --dev
```

And run the program like this:

```sh
pipenv run python ./app.py --help
```
