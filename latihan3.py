#memanggil librai opencv
import cv2 
from cv2 import waitKey 

#menyimpan gambar dengan fungsi imread dari openCV
img=cv2.imread("boy.1.webp")

#menampilkan gambar dengan fungsi  cv2_imshow
cv2.imshow("boy.1", img)
waitKey(0)

#lihat tipe data img.disimpan sebagai apa?
print(type(img))

print(img.shape)#menampilkan resolusi
print(img.size)#menampilkan ukuran data pada media penyimpan
print(img.size)#mage datatype (kedalam bit)

#band blu .green dan red masing masing disimpan pada variabel b,g,r
b,g,r=cv2.split(img)
#blue channel
b=img[...,0]
g=img[...,1]
r=img[...,2]
#menampilkan bend biru
cv2.imshow("pepe", img); 
cv2.imshow("blue", b); 
cv2.imshow("gren", g); 
cv2.imshow("red", r); 
waitKey(0)