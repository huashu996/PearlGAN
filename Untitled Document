import cv2
import numpy as np

if __name__ == "__main__":
    img_path = "/home/seucar/wjh/PearlGAN/res_FLIR/FLIR_NTIR2DC/test_80/images/11.png"
    img = cv2.imread(img_path)
    #获取图片的宽和高
    width,height = img.shape[:2][::-1]
    #将图片缩小便于显示观看
    img_resize = cv2.resize(img,
    (int(width*0.5),int(height*0.5)),interpolation=cv2.INTER_CUBIC)
#    cv2.imshow("img",img_resize)
    print("img_reisze shape:{}".format(np.shape(img_resize)))

    #读取灰度图
    img_gray = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    
    cv2.imwrite('hd.jpeg', img_gray)
    #将图片缩小便于显示观看
#    img_gray = cv2.resize(img_gray,
#    (int(width*0.5),int(height*0.5)),interpolation=cv2.INTER_CUBIC)
    cv2.imshow("img_gray",img_gray)
    print("img_gray shape:{}".format(np.shape(img_gray)))
    cv2.waitKey()


