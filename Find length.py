# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 13:53:33 2021

@author: Adminstrator
"""

import cv2,math
#Don`t forget to put the refernce length

#initate ref lengths
#ex=[W1,H1,W2,H2.....]
#belt of the diver is 9.6 cm approx
#the length of the diver is 178 cm
reflen_Actual=[10]

points=[]
ref_point = []

def shape_selection(event, x, y, flags, param):

    global ref_point
    
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being performed
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point=[(x, y)]
        points.append((x,y))
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        ref_point.append((x, y))
        points.append((x,y))
        
        # draw a rectangle around the region of interest
        if len(reflen_Actual)==4:
            cv2.rectangle(image, ref_point[0], ref_point[1], (50, 50, 250), 2)
        if len(reflen_Actual)==1:
            cv2.line(image, ref_point[0], ref_point[1], (50, 50, 250), 2)
        '''
        width=abs(ref_point[0][0]-ref_point[1][0])
        height=abs(ref_point[0][1]-ref_point[1][1])
        print(width,height)
        '''
        cv2.imshow("image", image)
                

image = cv2.imread("G:\\1.png")
# resize image
heightimg,widthimg,no_ch=image.shape
widthimg = int(widthimg*0.7)
heightimg = int(heightimg*0.7)
dim = (widthimg, heightimg)
image= cv2.resize(image, dim)

cv2.namedWindow("image")
cv2.setMouseCallback("image", shape_selection)

while True: 
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    # ref_point.append(ref_point)
print(points)    
cv2.destroyAllWindows()
for dim in ref_point:
#For Diver
    if len(points)/2==2:
#ref for head
        
        W_ref_px=abs(points[0][0] - points[1][0])
        # print(W_ref_px)
        # H_ref_px=abs(ref_point[0][1] - ref_point[1][1])
        W_obj_px=abs(points[2][0] - points[3][0])
        print(W_obj_px)
    
        W_Actual_Head=reflen_Actual[0]
#px per cm
        ratio=W_ref_px / W_Actual_Head
        Avgratio=ratio
        # print(Avgratio)

#Actual Length Diver length
        # Actual_len=W_obj_px / Avgratio
        Actual_len=round((W_obj_px / Avgratio),2)
        
        text=f'length is {Actual_len} cm'
        # print(f'length:{Actual_len}')
        image=cv2.putText(image,text,(points[2][0],points[2][1]+15),cv2.FONT_HERSHEY_SIMPLEX,1,(100,50,100),2,cv2.LINE_AA)


    
cv2.imshow("image",image)
# cv2.imwrite(image,"img")
print(math.ceil(Actual_len))
