print("KISI-COOKIES")
print()
nama = str(input("Siapa nama Anda? "))
alamat = str(input("Masukkan alamat Anda: "))
nomor_telepon = str(input("Masukkan nomor telepon Anda: "))
kode_pemesanan = nama[:3].upper() + nomor_telepon[-3:]

print("--------------------------------------------------")
print("DD-MM-YYYY")
hari = int(input("Masukkan tanggal pesanan: "))
bulan = int(input("Masukkan bulan pesanan: "))
tahun = int(input("Masukkan tahun pesanan: "))
tanggal = f"{hari}-{bulan}-{tahun}"
print()
print("Detail Tanggal Pesanan:", tanggal)
print("Kode Pemesanan:", kode_pemesanan)
member = input("Apakah Anda member? (Y/N): ").upper()

biaya_member = 0
if member == "N":
    daftar_member = input("Daftar member seharga Rp5.500? (Y/N): ").upper()
    if daftar_member == "Y":
        member = "Y"
        biaya_member = 5500
        print("Anda menjadi member!")
    else:
        print("Anda non-member.")
elif member == "Y":
    print("Cashback sebesar 8%")
else:
    print("Status non-member.")
    member = "N"

# Pesanan Pertama

print("\nPesanan pertama")
print("PILIH MENU:")
print("A. Nastar")
print("B. Lidah Kucing")
print("C. Sagu")
jenis_produk = input("Pilih produk (A/B/C): ").upper()

harga = 0
nama_produk = ""
nama_rasa = ""
nama_ukuran = ""

if jenis_produk == "A":
    nama_produk = "Nastar"
    print("\nA. Original")
    print("B. Keju")
    rasa_nastar = input("Pilih rasa (A/B): ").upper()
    if rasa_nastar == "A":
        nama_rasa = "Original"
        print("\nA. Kecil")
        print("B. Besar")
        ukuran_nastar = input("Pilih ukuran (A/B): ").upper()
        if ukuran_nastar == "A":
            nama_ukuran = "Small"
            harga = 45000
        elif ukuran_nastar == "B":
            nama_ukuran = "Large"
            harga = 65000
        else:
            print("Ukuran tidak tersedia")
    elif rasa_nastar == "B":
        nama_rasa = "Keju"
        print("\nA. Kecil")
        print("B. Besar")
        ukuran_nastar = input("Pilih ukuran (A/B): ").upper()
        if ukuran_nastar == "A":
            nama_ukuran = "Small"
            harga = 55000
        elif ukuran_nastar == "B":
            nama_ukuran = "Large"
            harga = 80000
        else:
            print("Ukuran tidak tersedia")
    else:
        print("Rasa tidak tersedia")

elif jenis_produk == "B":
    nama_produk = "Lidah Kucing"
    nama_rasa = "Original"
    print("\nA. Kecil")
    print("B. Besar")
    ukuran_lidah_kucing = input("Pilih ukuran (A/B): ").upper()
    if ukuran_lidah_kucing == "A":
        nama_ukuran = "Small"
        harga = 50000
    elif ukuran_lidah_kucing == "B":
        nama_ukuran = "Large"
        harga = 75000
    else:
        print("Ukuran tidak tersedia")
elif jenis_produk == "C":
    nama_produk = "Sagu"

    print("\nA. Original")
    print("B. Keju")
    rasa_sagu = input("Pilih rasa (A/B): ").upper()

    if rasa_sagu == "A":
        nama_rasa = "Original"
        print("\nA. Kecil")
        print("B. Besar")
        ukuran_sagu = input("Pilih ukuran (A/B): ").upper()
        if ukuran_sagu == "A":
            nama_ukuran = "Small"
            harga = 35000
        elif ukuran_sagu == "B":
            nama_ukuran = "Large"
            harga = 45000
        else:
            print("Ukuran tidak tersedia")
    elif rasa_sagu == "B":
        nama_rasa = "Keju"
        print("\nA. Kecil")
        print("B. Besar")
        ukuran_sagu = input("Pilih ukuran (A/B): ").upper()
        if ukuran_sagu == "A":
            nama_ukuran = "Small"
            harga = 55000
        elif ukuran_sagu == "B":
            nama_ukuran = "Large"
            harga = 85000
        else:
            print("Ukuran tidak tersedia")
    else:
        print("Rasa tidak tersedia!")
else:
    print("Jenis produk tidak tersedia")


# Jumlah toples pesanan 1

jumlah = 0
subtotal1 = 0

if harga > 0:
    print("\nJUMLAH TOPLES PESANAN PERTAMA")
    print(f"Harga per toples: Rp{harga:,.0f}")
    jumlah = int(input("Masukkan jumlah toples: "))
    if jumlah > 0:
        subtotal1 = harga * jumlah
        print(f"Subtotal pesanan pertama: Rp{subtotal1:,.2f}")
    else:
        print("Jumlah toples tidak valid!")

# Pesanan Kedua

harga2 = 0
nama_produk2 = ""
nama_rasa2 = ""
nama_ukuran2 = ""
jumlah2 = 0
subtotal2 = 0

if subtotal1 > 0:
    tambah_pesanan = input(
        "\nApakah ingin menambah pesanan kedua? (Y/N): "
    ).upper()
else:
    tambah_pesanan = "N"

if tambah_pesanan == "Y":

    print("\nPESANAN KEDUA")
    print("PILIH MENU:")
    print("A. Nastar")
    print("B. Lidah Kucing")
    print("C. Sagu")
    jenis_produk2 = input("Pilih produk (A/B/C): ").upper()

    if jenis_produk2 == "A":
        nama_produk2 = "Nastar"
        print("\nA. Original")
        print("B. Keju")
        rasa_nastar2 = input("Pilih rasa (A/B): ").upper()
        if rasa_nastar2 == "A":
            nama_rasa2 = "Original"
            print("\nA. Kecil")
            print("B. Besar")
            ukuran_nastar2 = input("Pilih ukuran (A/B): ").upper()

            if ukuran_nastar2 == "A":
                nama_ukuran2 = "Small"
                harga2 = 45000
            elif ukuran_nastar2 == "B":
                nama_ukuran2 = "Large"
                harga2 = 65000
            else:
                print("Ukuran tidak tersedia")

        elif rasa_nastar2 == "B":
            nama_rasa2 = "Keju"

            print("\nA. Kecil")
            print("B. Besar")
            ukuran_nastar2 = input("Pilih ukuran (A/B): ").upper()

            if ukuran_nastar2 == "A":
                nama_ukuran2 = "Small"
                harga2 = 55000
            elif ukuran_nastar2 == "B":
                nama_ukuran2 = "Large"
                harga2 = 80000
            else:
                print("Ukuran tidak tersedia")
        else:
            print("Rasa tidak tersedia")
    elif jenis_produk2 == "B":
        nama_produk2 = "Lidah Kucing"
        nama_rasa2 = "Original"
        print("\nA. Kecil")
        print("B. Besar")
        ukuran_lidah_kucing2 = input("Pilih ukuran (A/B): ").upper()

        if ukuran_lidah_kucing2 == "A":
            nama_ukuran2 = "Small"
            harga2 = 50000
        elif ukuran_lidah_kucing2 == "B":
            nama_ukuran2 = "Large"
            harga2 = 75000
        else:
            print("Ukuran tidak tersedia")

    elif jenis_produk2 == "C":
        nama_produk2 = "Sagu"

        print("\nA. Original")
        print("B. Keju")
        rasa_sagu2 = input("Pilih rasa (A/B): ").upper()
        if rasa_sagu2 == "A":
            nama_rasa2 = "Original"
            print("\nA. Kecil")
            print("B. Besar")
            ukuran_sagu2 = input("Pilih ukuran (A/B): ").upper()
            if ukuran_sagu2 == "A":
                nama_ukuran2 = "Small"
                harga2 = 35000
            elif ukuran_sagu2 == "B":
                nama_ukuran2 = "Large"
                harga2 = 45000
            else:
                print("Ukuran tidak tersedia")
        elif rasa_sagu2 == "B":
            nama_rasa2 = "Keju"

            print("\nA. Kecil")
            print("B. Besar")
            ukuran_sagu2 = input("Pilih ukuran (A/B): ").upper()
            if ukuran_sagu2 == "A":
                nama_ukuran2 = "Small"
                harga2 = 55000
            elif ukuran_sagu2 == "B":
                nama_ukuran2 = "Large"
                harga2 = 85000

            else:
                print("Ukuran tidak tersedia!")
        else:
            print("Rasa tidak tersedia")
    else:
        print("Jenis produk tidak tersedia")

    # Jumlah toples pesanam 2

    if harga2 > 0:
        print("\nJUMLAH TOPLES PESANAN KEDUA")
        print(f"Harga per toples: Rp{harga2:,.0f}")
        jumlah2 = int(input("Masukkan jumlah toples: "))
        if jumlah2 > 0:
            subtotal2 = harga2 * jumlah2
            print(f"Subtotal pesanan kedua: Rp{subtotal2:,.2f}")
        else:
            print("Jumlah toples tidak valid")
elif tambah_pesanan == "N":
    print("Tidak menambah pesanan kedua.")
else:
    print("Pilihan tidak valid.")


# subtotal

subtotal = subtotal1 + subtotal2
if subtotal > 0:
    print("\nDISKON")
    if subtotal > 120000:
        diskon = subtotal * 0.06
    else:
        diskon = 0
    total_setelah_diskon = subtotal - diskon
    print("CASHBACK")
    if member == "Y":
        cashback = total_setelah_diskon * 0.08
    else:
        cashback = 0
    print("PAJAK")
    pajak = total_setelah_diskon * 0.095
    print("TOTAL BAYAR")
    total_transaksi = total_setelah_diskon + pajak + biaya_member

    # Pembayaran

    print("\nPilih Metode Pembayaran:")
    print("A. Cash")
    print("B. Debit")
    metode = input("Pilih metode pembayaran (A/B): ").upper()
    pembayaran_berhasil = False
    uang_bayar = 0
    kembalian = 0

    if metode == "A":
        metode_pembayaran = "Cash"
        print(f"Total pembayaran: Rp{total_transaksi:,.2f}")
        uang_bayar = float(input("Masukkan jumlah uang: Rp"))
        if uang_bayar >= total_transaksi:
            kembalian = uang_bayar - total_transaksi
            pembayaran_berhasil = True
            print("Pembayaran berhasil")
        else:
            print("Uang tidak cukup")
    elif metode == "B":
        metode_pembayaran = "Debit"
        pembayaran_berhasil = True
        print("Pembayaran debit berhasil")
    else:
        print("Pembayaran gagal")

    # Struk Pembelian

    print()
    if pembayaran_berhasil:
        print(" STRUK ANDA:")
        print(f"Kode Pemesanan  : {kode_pemesanan}")
        print(f"Tanggal         : {tanggal}")
        print(f"Nama            : {nama}")
        print(f"Alamat          : {alamat}")
        print(f"Nomor Telepon   : {nomor_telepon}")
        print(f"Status Member   : {member}")
        print("Pesanan Pertama")
        print(f"Produk          : {nama_produk}")
        print(f"Rasa            : {nama_rasa}")
        print(f"Ukuran          : {nama_ukuran}")
        print(f"Jumlah Toples   : {jumlah}")
        print(f"Harga Satuan    : Rp{harga:,.2f}")
        print(f"Subtotal        : Rp{subtotal1:,.2f}")
        if subtotal2 > 0:
            print("Pesanan Kedua")
            print(f"Produk          : {nama_produk2}")
            print(f"Rasa            : {nama_rasa2}")
            print(f"Ukuran          : {nama_ukuran2}")
            print(f"Jumlah Toples   : {jumlah2}")
            print(f"Harga Satuan    : Rp{harga2:,.2f}")
            print(f"Subtotal        : Rp{subtotal2:,.2f}")
        print(f"Subtotal Belanja: Rp{subtotal:,.2f}")
        print(f"Diskon          : Rp{diskon:,.2f}")
        print(f"Cashback Member : Rp{cashback:,.2f}")
        print(f"Pajak 9.5%      : Rp{pajak:,.2f}")
        print(f"Biaya Member    : Rp{biaya_member:,.2f}")
        print(f"Total Transaksi : Rp{total_transaksi:,.2f}")
        print(f"Metode Bayar    : {metode_pembayaran}")
        print("_______________________________________________")
        if metode == "A":
            print(f"Uang Bayar      : Rp{uang_bayar:,.2f}")
            print(f"Kembalian       : Rp{kembalian:,.2f}")

            # Kembalian
            sisa = int(kembalian)

            uang_20000 = sisa // 20000
            sisa = sisa % 20000

            uang_10000 = sisa // 10000
            sisa = sisa % 10000

            uang_5000 = sisa // 5000
            sisa = sisa % 5000

            uang_2000 = sisa // 2000
            sisa = sisa % 2000

            uang_1000 = sisa // 1000
            sisa = sisa % 1000

            print("\nKembalian:")
            print(f"Rp20.000 : {uang_20000} lembar")
            print(f"Rp10.000 : {uang_10000} lembar")
            print(f"Rp5.000  : {uang_5000} lembar")
            print(f"Rp2.000  : {uang_2000} lembar")
            print(f"Rp1.000  : {uang_1000} lembar")
            print(f"Sisa     : Rp{sisa}")

        print("TERIMA KASIH TELAH MEMBELI :)")
else:
    print("Transaksi gagal :( ")
