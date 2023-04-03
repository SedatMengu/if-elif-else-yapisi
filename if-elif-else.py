#if - elif - else yapısı

#parola ve kullanıcı adı kontrol 

Kullanici_Adi="Admin"
Parola = 1234

Kullanici_Adi1 = input("Kullanıcı Adı Giriniz: ")
Parola1 = int(input("Parola Giriniz : "))
if (Kullanici_Adi == Kullanici_Adi1 and Parola == Parola1):
    print("Kullanıcı Adı ve Parola Doğru")
elif (Kullanici_Adi!=Kullanici_Adi1 and Parola==Parola1):
    print("Girilen Kullanıcı Adı Hatalı : {}".format(Kullanici_Adi1))
elif (Kullanici_Adi==Kullanici_Adi1) and (Parola!=Parola1):
    print("Girilen Parola Hatalı : {}".format(Parola1))
else:
    print("Girilen {} kullanıcı adı ve {} Parola Hatalı.".format(Kullanici_Adi1,Parola1))
    

# Girilen Notlara Göre Harf Notu Belirleme

# 100 - 90 / AA
# 89 - 80 / BA
# 79 - 70 / BB
# 69 - 60 / CB
# 59 - 50 / CC
# 49 - 40 / DC
# 39 - 30 / DD
# 29 - 00 / FF

Vize1 = float(input("1.Vize Notu Giriniz : "))
Vize2 = float(input("2.Vize Noru Giriniz : "))
Final = float(input("Final Notu Giriniz: "))

ortalama = Vize1*0.3 + Vize2*0.3 + Final*0.4
print("Ortalama {}".format(ortalama))

if Final <= 60:
    print("Finalde {} Aldığını İçin Kaldınız.".format(Final))
else:
    if ortalama >=90 : 
        print("Geçtiniz Harf Notunuz AA")
    elif (ortalama >=80) : 
        print("Geçtiniz Harf Notunuz BA")
    elif (ortalama >=70) :
        print("Geçtiniz Harf Notunuz BB")
    elif (ortalama >=60 ): 
        print("Geçtiniz Harf Notunuz CB")
    elif (ortalama >=50 ): 
        print("Geçtiniz Harf Notunuz CC")
    elif (ortalama >=40 ): 
        print("Geçtiniz Harf Notunuz DD")
    elif (ortalama >=30 ): 
        print("Geçtiniz Harf Notunuz DC")
    else:
        print("Kaldınız Harf Notunuz FF")
 


# Kullanıcının girdiği sayı sıfırdan küçükse negatif uyarısı veren kodu yazınız.

sayi = int(input("Lütfen Bir Sayi Giriniz : "))

if sayi < 0 :
    print("Girilen Sayı Negatiftir.")
else: 
    print("Girilen Sayı Poztiftir.")


# Kullanıcı tarafından girilen sayının işaretine göre pozitif, negatif yada nötr yazdıran uygulamayı yapınız.

sayi = int(input("Lütfen Bir Sayi Giriniz : "))

if sayi > 0 :
    print("girilen sayı pozitiftir..")
elif sayi == 0:
    print("girilen sayı nötürdür.")
else:
    print("girilen sayı negatiftir.")


# Kullanıcı yaşını girecek ve ehliyet almaya uygun olup olmadığı ekrana yazdırılacaktır.

yas = int(input("Yaşınızı giriniz : "))

if yas < 18 :
    print("Ehliyet Alamazsınız")
else:
    print("Ehliyet Alabilirsiniz.")

liste = [1,2,3,4,5,6,7,8,9]

yeni_eleman= int(input("Lütfen yeni Bir eleman girin : "))

if yeni_eleman in liste:
    print("eleman listede mevcut")
else:
    print("yeni eleman listede bulumuyor")
    liste.append(yeni_eleman)
    print("yeni eleman listeye eklendi")
    print(liste)


string = "Hello World!"

aranan_harf = input("lütfen Bir Harf giriniz : ")
if aranan_harf in string:
    print("harf ifadede mevcut")
else: 
    print("harf ifadede mevcut değil")

# not : Büyük harf ile küçük harf aynı değildir.

# "is" anahtar kelimesi bellekte aynı yerde olup olmadığını kontrol eder. İD leri farklı 
a = "Python"
b = "Pytho"
b = b+ "n"
print(a)
print(b)

if a is b:
    print("a = b")
else:
    print("a != b")
    print(id(a))
    print(id(b))

# tek satırda if else yazma

yas = 18 

durum = "Oy kullanabilir" if yas >=18 else "Oy kullanamaz"
print(durum)