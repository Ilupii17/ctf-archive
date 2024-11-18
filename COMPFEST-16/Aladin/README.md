# aladin
### Category: Binary Exploitation

**Deskripsi:**
>terkadang sebuah perjuangan tidak hanya memerlukan usaha, tapi memerlukan bantuan dari dunia gaib, hehehe...
>
>Author: nabilmuafa

## Penyelesaian
Pada Chall ini kita di berikan sebuah file binary, dikarenakan ini chall pwn/binary exploitation maka hal yang pertama kita lakukan yaitu 
melakukan checksec, untuk mengecek keamanan dari file tersebut

![Preview](images/1.png)

Disebutkan di sini no canary found yang artinya tidak ada byte random sebelum saved rbp, dan no pie yang artinya tidak ada pengacakan address
di dalam binary, maka dari itu kita bisa dengan mudah mengoverflow file ini.
