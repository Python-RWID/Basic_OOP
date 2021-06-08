# cumlecase di java, class di awal huruf kapital
class Rectangle():  # class
    def __init__(self,p,l):
        #fungsi yang dipanggil pertama kali
        self.p = p
        self.l = l

    def info(self):  # self object class rectangle
        return f'Ini adalah hasil hitung dari rectangle dengan panjang {self.p} dan lebar {self.l}'
    def result_wide(self):
        return self.p * self.l