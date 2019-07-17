# Tor Browser Launcher

_ ** Apakah Anda mendapatkan kesalahan? ** Terkadang pembaruan di Tor Browser itu sendiri akan merusak Tor Browser Launcher. Ada kemungkinan besar bahwa masalah yang Anda alami telah diperbaiki di [versi terbaru] (https://github.com/micahflee/torbrowser-launcher/releases), tetapi distribusi Linux bisa lambat untuk menyediakan hingga paket -tanggal. Dalam hal ini, Anda dapat menginstal dari PPA (instruksi di bawah), atau [build from source] (/ BUILD.md) ._

Tor Browser Launcher dimaksudkan untuk membuat Tor Browser lebih mudah dipasang dan digunakan untuk pengguna GNU / Linux. Anda menginstal `` `torbrowser-launcher``` dari manajer paket distribusi Anda dan menangani semuanya:

* Mengunduh dan menginstal versi Tor Browser terbaru dalam bahasa Anda dan untuk arsitektur komputer Anda, atau meluncurkan Tor Browser jika sudah diinstal (Tor Browser akan secara otomatis memperbarui sendiri)
* Memverifikasi [tanda tangan] Tor Browser (https://www.torproject.org/docs/verifying-signatures.html.en) untuk Anda, untuk memastikan versi yang Anda unduh ditandatangani secara kriptografi oleh pengembang Tor dan tidak dirusak oleh
* Menambahkan peluncur aplikasi "Tor Browser" dan "Tor Browser Launcher Settings" ke menu lingkungan desktop Anda
* Termasuk profil AppArmor untuk membuat kompromi Browser Tor tidak seburuk itu
* Secara opsional memutar suara modem ketika Anda membuka Tor Browser (karena Tor sangat lambat)

Peluncur Peramban Tor termasuk dalam Ubuntu, Debian, dan Fedora. Untuk menginstalnya di distribusi lain, lihat [membangun instruksi] (/ BUILD.md)

Anda mungkin ingin memeriksa [dokumen desain keamanan] (/ security_design.md).

! [Tangkapan layar Tor Browser Launcher] (/ tangkapan layar.png)

# Menginstal dari PPA

Jika Anda ingin selalu memiliki versi terbaru dari paket `torbrowser-launcher` sebelum distribusi Anda mendapatkannya, Anda dapat menggunakan PPA saya:

```sh
sudo add-apt-repository ppa:micahflee/ppa
sudo apt-get update
sudo apt-get install torbrowser-launcher
```
