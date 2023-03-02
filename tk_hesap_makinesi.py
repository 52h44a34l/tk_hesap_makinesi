
# HESAP MAKİNESİ 

# 4 işlem


import tkinter as tk


class app(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("650x600")
        self.title("HESAP MAKİNESİ")

        # gelen sayı
        self.etiket1 = tk.Label(text="İŞLEM: \t",bg="grey")
        self.etiket1.grid(row=0, column=0)
        self.sayı1 = tk.Entry()
        self.sayı1.grid(row=0,column=1)

        #sonuc etiket
        self.cevap = tk.Label(text="--",bg="red")
        self.cevap.grid(row=0,column=2)

        #butonlar
        self.sonuc = tk.Button(text ="SONUÇ",bg="grey", command=self.islem)
        self.sonuc.grid(row=1, column=0)

        self.temizle = tk.Button(text="TEMİZLE",bg="grey", command=self.f_temizle)
        self.temizle.grid(row=1,column=1)

        self.kapat = tk.Button(text="KAPAT",bg="grey", command=self.cikis)
        self.kapat.grid(row=1,column=2)

        # uyarı etiket
        self.uyarı1 = tk.Label(text="",bg="white",fg="red")
        self.uyarı1.grid(row=3, column=3)


    # gelen değeri düzenleyip işlem yapma
    def islem(self):
        gelen = self.sayı1.get()
        self.cevap["bg"] = "green"


        if "+" in gelen:
            sayılar = gelen.split("+")
            sayılar = self.ayıkla("+",gelen)
            self.cevap["text"] = sayılar[0] + sayılar[1]

        elif "-" in gelen:
            sayılar = gelen.split("-")
            sayılar = self.ayıkla("-",gelen)
            self.cevap["text"] = sayılar[0] - sayılar[1]

        elif "/" in gelen:
            sayılar = gelen.split("/")
            sayılar = self.ayıkla("/",gelen)
            self.cevap["text"] = sayılar[0] / sayılar[1]

        elif "*" in gelen:
            sayılar = gelen.split("*")
            sayılar = self.ayıkla("*",gelen)
            self.cevap["text"] = sayılar[0] * sayılar[1]

        else:
            self.uyarı1["text"]  = "UYARI!\n sayı girmediniz yada işleç te sorun var..."


    # hatalı gelen ifadeyi ayıklama işlemi
    def ayıkla(self,imlec,gelen):
        w = "1234567890"
        s1 = ""
        s2 = ""
        i1,i2 = gelen.split(imlec)

        for i in i1:
            if i in w:
                s1+=i

        for i in i2:
            if i in w:
                s2+=i

        s1 = int(s1)
        s2 = int(s2)

        return s1,s2
    
    # ekranı temizleme
    def f_temizle(self):
        self.uyarı1["text"] = ""
        self.cevap["text"] = "--"
        self.sayı1.delete(0,"end")
        self.cevap["bg"] = "red"

        self.after(600)

    # uygulamadan çıkış
    def cikis(self):
        self.cevap["text"] = ""
        self.sayı1.delete(0,"end")
        self.kapat["state"] = "disabled"
        self.uyarı1["text"] = "  :)  "
        self.after(1000, self.destroy)





a1 = app()
a1.mainloop()