print('-----------------------------------------------------')
print('Aplikasi Ini Dibuat oleh Gabriel Cesar Hutagalung')
print('-----------------------------------------------------')

while True:
    print('\nKeterangan:')
    print('\nTekan 1 untuk perkalian!')
    print('Tekan 2 untuk pembagian!')
    print('Tekan 3 untuk penjumlahan!')
    print('Tekan 4 untuk pengurangan!')
    print('Tekan 5 untuk mencari sisa!')
    print('Tekan 6 untuk membulatkan ke bawah!')
    print('Tekan 7 untuk memangkatkan!')
    print('Jika ingin keluar, tekan Ctrl+C')

    z = input('\nOperator: ')
    x = int(input('Masukkan angka pertama: '))
    y = int(input('Masukkan angka kedua: '))
    hasil = '\nHasilnya adalah: '

    if z == '1':
        print(hasil, + int(x) * int(y))

    if z == '2':
        print(hasil, + int(x) / int(y))

    if z == '3':
        print(hasil, + int(x) + int(y))

    if z == '4':
        print(hasil, + int(x) - int(y))

    if z == '5':
        print('\nSisanya adalah: ', + int(x) % int(y))

    if z == '6':
        print('\nHasil pembulatan ke bawahnya adalah: ', + int(x) // int(y))

    if z == '7':
        print(hasil, + int(x) ** int(y))

    if int(z) > 8:
        print('\nMaaf, operator salah :(')

    if int(z) < 1:
        print('\nMaaf, operator salah :(')

        print('\nTerima kasih telah menggunakan :)')
        
