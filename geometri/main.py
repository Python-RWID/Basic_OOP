# buat class dlu, baru object
# class tipe data, object var/nama = manusia , fauzan&farhan
from geometri.triangle import Triangle
from geometri.rectangle import Rectangle

print('menggunakan OOP')
P1 = Rectangle(10,5)
print(P1.info()) # result from encapsulation
print(f'dengan hasil {P1.result_wide()}')

T1 = Triangle(10,4)
print(T1.info()) # resulft from encapsulation
print(f'dengan hasil {T1.result_wide()}')