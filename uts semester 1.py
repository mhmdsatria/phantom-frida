#dekorasi
print("=====================================================")
print("===============|UJIAN TENGAH SEMESTER|===============")
print("=====================================================")
print("===================|MUHAMAD SATRIA|==================")
print("\n-----------------------------------------------------")
#pembukaan dan pilihan
nama = input("> Username :")
print("\n-----------------------------------------------------")
print ("Hai,",nama,"silahkan pilih Langkah-langkah dibawah ini")
print("-----------------------------------------------------")
while True:
    pilihan = ["[a]Menghitung umur saat ini","[b]Menghitung sisa tahun cicilan","[c]Menghitung BMI berat badan","[d]Quit"]
    for x in pilihan:
        print(x)
    print("-----------------------------------------------------")
    z = input("> Masukan pilihan:") 
    if z == "a":
        #kelahiran

        print("\n------------------------------------------------------")
        print("[a] Menghitung umur saat ini")
        print("-----------------------------------------------------")
        print("isi beberapa pertanyaan dibawah ini dengan baik".center(50))
        print("Format input tanggal lahir wajib 'dd mm yyyy', contoh '07 03 2004' ")
        print("-----------------------------------------------------")
        #tanggal kelahiran
        tl=int(input(" 1.masukan tanggal kelahiran anda :")) 
        #bulan kelahiran
        bl=int(input(" 2.masukan bulan kelahiran anda :")) 
        #tahun kelahiran
        th=int(input(" 2.masukan tahun kelahiran  anda :"))
        
        #datetime sekarang

        print("-----------------------------------------------------")
        print("isi beberapa pertanyaan dibawah ini dengan baik".center(50))
        print("Format input tanggal lahir wajib 'dd mm yyyy', contoh '07 03 2004' ")
        print("-----------------------------------------------------")
        ts=int(input(" 1.masukan tanggal sekarang :")) 
        bs=int(input(" 2.masukan bulan sekarang :")) 
        ths=int(input(" 3.masukan tahun sekarang :")) 

        #deskripsi umur

        tanggal= ts - tl
        bulan= bs - bl
        tahun= ths - th

        #deskripsi hidup

        des_bulan=12 * tahun + bulan
        des_minggu = int(des_bulan / 12 * 48) 
        des_hari=int(des_minggu * 7) 

        #print rumus umur

        print("=====================================================")
        ("hallo", nama, "kini anda berusia", tahun,"tahun ,",bulan, " bulan, ",tanggal, " hari")

        #print rumus deskripsi umur

        print("Kini anda berusia:")
        des_umur="{} tahun {} bulan {} hari"
        print(des_umur.format(tahun,bulan, tanggal))

        #print rumus deskrips hidup

        print("-----------------------------------------------------")
        print("Anda sudah hidup:")
        des_hidup="{} tahun {} bulan {} minggu {} hari"
        print(des_hidup.format(tahun, des_bulan, des_minggu, des_hari))
        print("semoga sehat selalu ya..",nama)
        print("=====================================================")
        penutup_umur = input("apakah mau melanjutkan.. y or n ?")
        if penutup_umur == "y":
            continue
        elif penutup_umur =="n":
            print("baik,terima kasih",nama,"semoga sehat selalu ya..")
            break
        else:
            print("maaf kode yang anda masukan salah")
            continue
    elif z == "b":
        print(" \n-----------------------------------------------------")
        print("[b] Menghitung sisa tahun cicilan")
        print("-----------------------------------------------------")
        while True:
            
            n_barang=input(" 1.masukan nama barang : ") 
            h_barang=int(input(" 2.masukan harga barang : "))
            print("-----------------------------------------------------")
            print("Barang tersebut bisa di kredit dengan tempo:")
            tempo=["> 4 Bulan","> 8 Bulan","> 12 Bulan"]
            for k in tempo:
                print(k)
            j_waktu=input("Berapa kredit yang anda ambil : 4/8/12 Bulan ? ")
            #harga barang
            if j_waktu == "4":
                b_bunga4="15%"
                bunga4=int(h_barang*15/100)
                total4=int(bunga4+h_barang)
                #rumus angsuran
                angsuran4=int(total4/12)
                #deskripsi kredit
                print(nama,"anda membeli",n_barang,"dengan harga",total4," jangka waktu",j_waktu,"bulan dengan bunga",b_bunga4)
                print ("maka angsuran perbulannya sebesar Rp.",angsuran4)
                #cicilan
                print("-----------------------------------------------------")
                t_bulan=input("> Berapa bulan yang telah dibayar :")
                if t_bulan == "1":
                    sisa1=int(total4-angsuran4) 
                    print("Sisa waktu pembayaran anda 11 bulan dengan tagihan", sisa1)
                elif t_bulan=="2":
                    sisa2=int(total4-angsuran4)
                    print("Sisa waktu pembayaran anda 10 bulan dengan tagihan", sisa2)
                elif t_bulan=="3":
                    sisa3=int(total4-angsuran4)
                    print("Sisa waktu pembayaran anda 9 bulan dengan tagihan", sisa3)
                elif t_bulan=="4":
                    sisa4=int(total4-angsuran4)
                    print("Sisa waktu pembayaran anda 8 bulan dengan tagihan", sisa4)
                elif t_bulan=="5":
                    sisa5=int(total4-angsuran4)
                    print("Sisa waktu pembayaran anda 7 bulan dengan tagihan", sisa5)
                elif t_bulan=="6":
                    sisa6=int(total4-angsuran4)
                    print("Sisa waktu pembayaran anda 6 bulan dengan tagihan", sisa6)
                elif t_bulan=="7":
                    sisa7=int(total4-angsuran4)
                    print("Sisa waktu pembayaran anda 5 bulan dengan tagihan", sisa7)
                elif t_bulan=="8":
                    sisa8=int(total4-angsuran4)
                    print("Sisa waktu pembayaran anda 4 bulan dengan tagihan", sisa8)
                elif t_bulan=="9":
                    sisa9=int(total4-angsuran4)
                    print("Sisa waktu pembayaran anda 3 bulan dengan tagihan", sisa9)
                elif t_bulan=="10":
                    sisa10=int(total4-angsuran4)
                    print("Sisa waktu pembayaran anda 2 bulan dengan tagihan", sisa10)
                elif t_bulan=="11":
                    sisa11=int(total4-angsuran4)
                    print("Sisa waktu pembayaran anda 1 bulan dengan tagihan", sisa11)
                elif t_bulan=="12":
                    sisa12=int(total4-angsuran4)
                    print("Tidak ada lagi pembayaran, anda sudah melunasi semua cicilan")
                else:
                    print("Mohon maaf,input yang anda masukan salah")
                lanjut4=input("apakah lanjut menghitung cicilan...y or n ?")
                if lanjut4 == "y":
                    continue
                elif lanjut4 =="n":
                    break
                else:
                    print("Mohon maaf,input yang anda masukan salah")
                    continue
            
            elif j_waktu == "8":
                b_bunga8="17%"
                bunga8=int(h_barang*17/100)
                total8=int(bunga8+h_barang)
                #rumus angsuran
                angsuran8=int(total8/12)
                #deskripsi kredit
                print(nama,"anda membeli",n_barang,"dengan harga",total8," jangka waktu",j_waktu,"bulan dengan bunga",b_bunga8)
                print ("maka angsuran perbulannya sebesar Rp.",angsuran8)
                #cicilan
                print("-----------------------------------------------------")
                t_bulan=input("> Berapa bulan yang telah dibayar :")
                if t_bulan == "1":
                    sisa1=int(total8-angsuran8) 
                    print("Sisa waktu pembayaran anda 11 bulan dengan tagihan", sisa1)
                elif t_bulan=="2":
                    sisa2=int(total8-angsuran8)
                    print("Sisa waktu pembayaran anda 10 bulan dengan tagihan", sisa2)
                elif t_bulan=="3":
                    sisa3=int(total8-angsuran8)
                    print("Sisa waktu pembayaran anda 9 bulan dengan tagihan", sisa3)
                elif t_bulan=="4":
                    sisa4=int(total8-angsuran8)
                    print("Sisa waktu pembayaran anda 8 bulan dengan tagihan", sisa4)
                elif t_bulan=="5":
                    sisa5=int(total8-angsuran8)
                    print("Sisa waktu pembayaran anda 7 bulan dengan tagihan", sisa5)
                elif t_bulan=="6":
                    sisa6=int(total8-angsuran8)
                    print("Sisa waktu pembayaran anda 6 bulan dengan tagihan", sisa6)
                elif t_bulan=="7":
                    sisa7=int(total8-angsuran8)
                    print("Sisa waktu pembayaran anda 5 bulan dengan tagihan", sisa7)
                elif t_bulan=="8":
                    sisa8=int(total8-angsuran8)
                    print("Sisa waktu pembayaran anda 4 bulan dengan tagihan", sisa8)
                elif t_bulan=="9":
                    sisa9=int(total8-angsuran8)
                    print("Sisa waktu pembayaran anda 3 bulan dengan tagihan", sisa9)
                elif t_bulan=="10":
                    sisa10=int(total8-angsuran8)
                    print("Sisa waktu pembayaran anda 2 bulan dengan tagihan", sisa10)
                elif t_bulan=="11":
                    sisa11=int(total8-angsuran8)
                    print("Sisa waktu pembayaran anda 1 bulan dengan tagihan", sisa11)
                elif t_bulan=="12":
                    sisa12=int(total8-angsuran8)
                    print("Tidak ada lagi pembayaran, anda sudah melunasi semua cicilan")
                else:
                    print("Mohon maaf,input yang anda masukan salah")
                lanjut8=input("apakah lanjut menghitung cicilan...y or n ?")
                if lanjut8 == "y":
                    continue
                elif lanjut8 =="n":
                    break
                else:
                    print("Mohon maaf,input yang anda masukan salah")
                    continue
            
            elif j_waktu == "12":
                b_bunga12="25%"
                bunga8=int(h_barang*25/100)
                total12=int(bunga8+h_barang)
                #rumus angsuran
                angsuran12=int(total12/12)
                #deskripsi kredit
                print(nama,"anda membeli",n_barang,"dengan harga",total12," jangka waktu",j_waktu,"bulan dengan bunga",b_bunga12)
                print ("maka angsuran perbulannya sebesar Rp.",angsuran12)
                #cicilan
                print("-----------------------------------------------------")
                t_bulan=input("> Berapa bulan yang telah dibayar :")
                if t_bulan == "1":
                    sisa1=int(total12-angsuran12) 
                    print("Sisa waktu pembayaran anda 11 bulan dengan tagihan", sisa1)
                elif t_bulan=="2":
                    sisa2=int(total12-angsuran12)
                    print("Sisa waktu pembayaran anda 10 bulan dengan tagihan", sisa2)
                elif t_bulan=="3":
                    sisa3=int(total12-angsuran12)
                    print("Sisa waktu pembayaran anda 9 bulan dengan tagihan", sisa3)
                elif t_bulan=="4":
                    sisa4=int(total12-angsuran12)
                    print("Sisa waktu pembayaran anda 8 bulan dengan tagihan", sisa4)
                elif t_bulan=="5":
                    sisa5=int(total12-angsuran12)
                    print("Sisa waktu pembayaran anda 7 bulan dengan tagihan", sisa5)
                elif t_bulan=="6":
                    sisa6=int(total12-angsuran12)
                    print("Sisa waktu pembayaran anda 6 bulan dengan tagihan", sisa6)
                elif t_bulan=="7":
                    sisa7=int(total12-angsuran12)
                    print("Sisa waktu pembayaran anda 5 bulan dengan tagihan", sisa7)
                elif t_bulan=="8":
                    sisa8=int(total12-angsuran12)
                    print("Sisa waktu pembayaran anda 4 bulan dengan tagihan", sisa8)
                elif t_bulan=="9":
                    sisa9=int(total12-angsuran12)
                    print("Sisa waktu pembayaran anda 3 bulan dengan tagihan", sisa9)
                elif t_bulan=="10":
                    sisa10=int(total12-angsuran12)
                    print("Sisa waktu pembayaran anda 2 bulan dengan tagihan", sisa10)
                elif t_bulan=="11":
                    sisa11=int(total12-angsuran12)
                    print("Sisa waktu pembayaran anda 1 bulan dengan tagihan", sisa11)
                elif t_bulan=="12":
                    sisa12=int(total12-angsuran12)
                    print("Tidak ada lagi pembayaran, anda sudah melunasi semua cicilan")
                else:
                    print("Mohon maaf,input yang anda masukan salah")
                    continue
                lanjut12=input("apakah lanjut menghitung cicilan...y or n ?")
                if lanjut12== "y":
                    continue
                elif lanjut12 =="n":
                    break
                else:
                    print("Mohon maaf,input yang anda masukan salah")
                    continue
            else:
                print("Mohon maaf,input yang anda masukan salah")
                continue
    elif z == "c":
        print(" \n-----------------------------------------------------")
        print("[c] Menghitung BMI berat badan")
        print("-----------------------------------------------------")
        bmi_berat=input("Masukan berat badan anda : ")
        bmi_tinggi=input("Masukan tinggi badan anda : ")
        print("-----------------------------------------------------")
        #rumus bmi
        tinggi_badan=float(bmi_tinggi)/100
        r_bmi=int(bmi_berat)/float(tinggi_badan)
        #deskripsi bmi
        if r_bmi <=18.5:
            print("anda kekurangan berat badan")
        elif r_bmi <=24.9:
            print("anda memiliki badan ideal(normal)")
        elif r_bmi <=29.9:
            print("anda kelebihan berat badan")
        elif r_bmi >=30.0:
            print("anda memiliki badan obesitas(kegemukan)")
        else:
            print("Mohon maaf,input yang anda masukan salah")
            continue
        penutup_bmi = input("apakah mau melanjutkan.. y or n ?")
        if penutup_bmi == "y":
            continue
        elif penutup_umur =="n":
            print("baik,terima kasih",nama,"semoga sehat selalu ya..")
            break
        else:
            print("Mohon maaf,input yang anda masukan salah")
            continue
    elif z == "d":
        print("Terama kasih..","\nselamat beraktivitas kembali",nama,"semoga sehat selalu.")
        break
    else:
        print("Mohon maaf,input yang anda masukan salah")
        continue
