import cv2
import os

img_dir = "./images"
img_ls = os.listdir(img_dir)
#print(img_ls)
i = 0
for img in img_ls:
    img_read = cv2.imread(os.path.join(img_dir,img))
    img_out = cv2.resize(img_read,(1242,375), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("./images/"+img[:-11]+".png",img_out)
    
