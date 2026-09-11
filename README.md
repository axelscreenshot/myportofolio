Nama  : Axel Sebastian Saragih \
NPM   : 2506590063 \
Kelas : PBP B

# <div align="center">My Portofolio: Progress</div>
Website: https://axel-sebastian-myportofolio.pws.cs.ui.ac.id


## Week 2
Implementasi Model-View-Template (MVT) pada Django

**-- Tidak menggunakan AI --** \
Masih 0% dalam penggunaan AI, saya yang akhirnya sudah cukup nyaman dengan HTML dan CSS dapat mengerjakan tugas 2 ini dengan kesulitan minimal, walau sebenarnya cukup banyak bagian dari tugas ini ditulis menggunakan python (mungkin juga karena tidak banyak pengaturan grid dan/atau tampilan lainnya). Konsep MVT yang dipersiapkan dan dipelajari juga cukup mudah dipahami dan diimplementasikan. Bagian _testing_ juga tidak mengalami kesulitan karena mirip dengan _unit testing_ pada DDP2 silam. Sebagai tambahan, saya buat template dan model sedemikian rupa sehingga dapat mengecek apakah disediakan _thumbnail_ atau tidak untuk Experience dan Project, mengisinya dengan _placeholder_ apabila kosong. _Not bad but could definitely be better_ (ex: halaman detail/slug untuk yang lebih spesifik).


### Tugas 2

1. Ketika pengguna membuka halaman portofolio baru, proyek portofolio Django akan menerima _request_ tersebut dan akan memetakan URL tersebut ke View (`views.py`) melalui `urls.py` proyek (dan jika perlu akan dipetakan lagi melalui `urls.py` aplikasi). Semuanya lalu diproses melalui View, mengambil dan mengolah data dari Model (`models.py`) yang telah dibuat jika diperlukan, di mana data-data tersebut telah di-_manage_. Setelah itu, View akan mengirimkan semua konteks yang diperlukan ke Template (`index.html`, `experience.html`, etc.). Template HTML yang telah diproses dan diisi otomatis dengan data ini adalah _response_ akhir yang akan diberikan Django kepada pengguna sehingga data yang diminta dapat ditampilkan pada browser.
2. Dengan menyimpan data bagian portofolio baru pada Model, pengaturan data akan menjadi lebih mudah. Tugas _managing_ dipisahkan ke bagian khusus sehingga tidak menjadi "berserakan" di berbagai tempat. Dengan begitu, pemeliharaan dan pengembangan aplikasi akan menjadi jauh lebih mudah: hanya perlu menambahkan dan merubah data langsung dari Model, memanggil objek dan atribut yang sesuai jika diperlukan pada suatu Template.
3. `makemigrations` berfungsi untuk menciptakan berkas migrasi, mendeskripsikan  _command-command_ SQL berdasarkan perubahan model yang telah kita lakukan. Ketika kita `migrate` lah baru _command_ tersebut dibaca dan data yang telah diubah lalu diaplikasikan ke dalam _database_. Sebagai contoh, model saya yang bernama "Projects" akan ditampilkan sebagai "Projectss" di halaman admin database Django akibat pluralisai otomatisnya. Oleh karena itu, saya ubah kembali nama model tersebut menjadi "Project". `makemigrations` kemudian akan menyusun perintah pengubahan nama tersebut dan kemudian akan dijalankan dan diimplementasi ke basis data setelah saya `migrate`. Akhirnya, model saya ditampilkan dengan nama "Projects" yang sesuai.


## Week 1
Static Web with HTML5 and CSS3

**-- Tidak menggunakan AI --** \
Karena ini pertama kali saya membuat proyek serius menggunakan HTML dan CSS, saya awalnya perlu mempelajari dari awal _mostly_ menggunakan W3Schools. Setelah cukup memahami kode yang telah ada dari tutorial, lalu saya coba kembangkan dengan kemampuan saya sendiri—seperti yang akan di bahas di bagian tugas—penuh dengan _trial-and-error_. Meskipun begitu, saya mengusahakan agar tidak menggunakan bantuan AI sama sekali untuk minggu pertama ini agar dapat lebih terlatih. Setelah semuanya berjalan dengan baik, hal terakhir yang dilakukan adalah _polishing_ web dengan detail-detail kecil. Untungnya, selain dalam memikirkan desain dan pengaturan _display_, kebebasan tugas minggu pertama ini membuat saya belum banyak mengalami masalah dan halangan yang benar-benar menghambat.


### Tugas 1
1. Saya menggunakan elemen semantik HTML5 berupa `<section>` untuk membantu membagi web menjadi _section-section_ yang lebih jelas, mengelompokkannya sesuai dengan jenis konten yang ingin disampaikan. Dengan begitu, dokumen tidak dikerumuni dengan tag `<div>` yang cenderung lebih general.
2. Kebanyakan waktu pengerjaan dimakan oleh pengaturan `display: grid`/`flex` termasuk berbagai pengaturan _padding_, _margin_, dan _align_ yang dimiliki. Pada akhirnya, diperlukan banyak _trial-and-error change-and-refresh_ yang dilakukan sehingga mendapatkan hasil yang diharapkan. _Section 'skills'_ yang saya buat tidak terlalu rumit strukturnya, sehingga tidak memerlukan pengubahan posisi/ukuran yang drastis untuk perihal responsivitas web.
3. Web _static_, seperti namanya, bersifat statis dan perlu diganti manual setiap ada perlu perubahan. Walau sederhana dan cocok digunakan untuk web portofolio, mereka memiliki keterbatasan pada sisi _backend_, membuat fitur seperti _scaling_, mengolah dan menyampaikan informasi menggunakan database dan fitur dinamis lainnya sulit diimplementasikan. Sesuai tema _assignment_ selanjutnya, fungsionalitas dinamis yang ingin ditambahkan dan perlu dipersiapkan berupa database dan model MVT: konsep arsitektur yang digunakan dalam _web development_ untuk memisahkan manajemen data, _request handling_, serta logika presentasi data dengan tujuan pengelolaan kode dengan lebih terstruktur dan mudah dirawat dalam jangka panjang.


## Resources
1. [Coolors](https://coolors.co/160c28-efcb68-e1efe6-aeb7b3-000411), for color palette
2. [Canva](https://www.canva.com), for photo editing
3. [W3Schools](https://www.w3schools.com)/tags; /cssref; /howto, for tutorials regarding frontend development
4. [Font Awesome](https://fontawesome.com), for brand icons
5. [Optimistic Web](www.youtube.com/@OptimisticWeb/), for css endless scroll
6. [Stack Overflow](https://stackoverflow.com/questions), for other—more specific—needs
7. [GeeksforGeeks](https://www.geeksforgeeks.org), for more theoretical questions
8. [django Documentation](https://docs.djangoproject.com/en/6.1/), for details about models and making queries
