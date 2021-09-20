import cv2
import os
import time

start = time.time()
path = 'images/1'
olcek = 50

def Panorama():
    images = []
    myList = os.listdir(path)
    print(f' resim sayısı {len(myList)}')
    for imgN in myList:
        curImg = cv2.imread(f'{path}/{imgN}')
        images.append(curImg)
    stitcher = cv2.Stitcher_create()
    (status, result) = stitcher.stitch(images)

    if (status == cv2.Stitcher_OK):
        print('Panorama basarili')
    else:
        print('Panorama basarisiz')
    return result

def skala(result = Panorama()):
    h, w = result.shape[:2]
    new_h = int(h * olcek / 100)
    new_w = int((w * olcek) / 100)
    dim = (new_w, new_h)
    resize = cv2.resize(result, dim, interpolation=cv2.INTER_AREA)
    return resize

#def Clipping_image():
    #h,w = resim.shape[:2]
    #start_row, start_col=int(h * .20), int(w * .20)
    #end_row, end_col=int(h * .80), int(w * .80)
    #crop=resim[start_row:end_row , start_col:end_col]


resized = Panorama()

cv2.imshow(path,resized)
#cv2.imwrite("Result/"+path+".jpg", resized)
cv2.imwrite("full.jpg", resized)
end = time.time()
gcnsure = end-start
sure = f"gecen sure :{gcnsure:.2f}s"
print(sure)

cv2.waitKey(0)
cv2.destroyAllWindows()
