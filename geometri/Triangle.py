class Triangle():
    def __init__(self,a,t):
        self.a = a
        self.t = t

    def info(self):  # self object class rectangle
        return f'Ini adalah hasil hitung dari rectangle dengan alas {self.a} dan tinggi {self.t} dibagi 2'

    def result_wide(self):
        return self.a * self.t / 2
