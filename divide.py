import cv2
import numpy as np 
#from matplotlib import pyplot as plt
def num_of_black(thresh1,w,h):
	width_black=[]
	for i in range(0,w):
		num=0
		for j in range(0,h):
			if thresh1[j,i]==255:
				num=num+1
		width_black.append(num)
	return width_black

def num_of_h_black(thresh1,h,w):
	width_black=[]
	for i in range(0,h):
		num=0
		for j in range(0,w):
			if thresh1[i,j]==255:
				num=num+1
		width_black.append(num)
	return width_black

def seq(width_black,w):
	index=[];flag=1
	for i in range(0,w):
		if flag==1 and width_black[i]!=0:
			index.append(i)
			flag=0

		if flag==0 and width_black[i]==0:
			index.append(i)
			flag=1
	return index



img=cv2.imread('F:/deal_pic/test2_1.jpg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#print(np.unique(thresh1))
h,w=thresh1.shape
print('h=%d w=%d'%(h,w))

width_black=num_of_black(thresh1,w,h)
#print(width_black)
index=seq(width_black,w)
k=0
for i in range(1,len(index)):#
	if i%2==1:
		part=thresh1[:,index[i-1]:index[i]]
		pt_h,pt_w=part.shape
		height_black=num_of_h_black(part,pt_h,pt_w)
		height_index=seq(height_black,pt_h)
		if len(height_index)==2:
			part1=part[height_index[0]:height_index[1],:]
			path='F:/deal_pic/divide1/'+str(k)+'.jpg'
			print(path)
			cv2.imwrite(path,part1)
			k=k+1


			


		


#the num of black point in every col 


#print(width_black)

#draw the picture
# new_one=np.zeros((h,w))
# for i in range(0,w):
# 	new_one[h-1-width_black[i]:h,i]=255

#divide into small pic

		
#print(index)








# cv2.namedWindow("Contours", cv2.WINDOW_NORMAL)
# cv2.imshow("Contours", new_one)
# cv2.waitKey(0)
# cv2.destroyAllWindows()