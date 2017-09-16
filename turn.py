import cv2
import numpy as np 

img=cv2.imread('F:/deal_pic/test5.jpg',0)
ret ,thresh1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
coords=np.column_stack(np.where(thresh1>0))
angle=cv2.minAreaRect(coords)[-1]
print angle
h,w=thresh1.shape
center=(w//2,h//2) #there are (col//2,row//2)
print center
M=cv2.getRotationMatrix2D(center,-20,0.5)#-(90+angle)
rotated=cv2.warpAffine(thresh1,M,(w,h))# the lastest one is also (col//2,row//2)
# #print(angle)
cv2.imwrite('F:/deal_pic/test2_1.jpg',rotated)






# img=cv2.imread('F:/deal_pic/test2.jpg',0)
# h,w=img.shape
# center=(w//2,h//2)
# M=cv2.getRotationMatrix2D(center,-75,1)
# rotated=cv2.warpAffine(img,M,(w,h))
# cv2.imwrite('F:/deal_pic/test2_3.jpg',rotated)

