import numpy as np
import cv2

from time import sleep
from picamera import PiCamera

red =   [0  ,255,255]
orange =[15 ,255,255]
yellow =[30 ,255,255]
lime   =[45 ,255,255]
green = [60, 255,255]
marine =[75 ,255,255]
cyan =  [90 ,255,255]
navy =  [105,255,255]
blue =  [120,255,255]
lila =  [135,255,255]
magenta=[150,255,255]
pink =  [165,255,255]
gray =  [30 ,0  ,50 ]

colors=['red','orange','yellow','lime','green','marine','cyan','navy','blue','lila','magenta','pink','gray']
colorlist =[red,orange,yellow,lime,green,marine,cyan,navy,blue,lila,magenta,pink,gray]

camera = PiCamera()
camera.resolution = (640, 480)
lowb =[0,0,0]
highb=[0,0,0]

def color_bounds(mcolor):
       if mcolor in colors:
          diff=10
          saturation=50
          if mcolor == 'blue':
             diff = 20
             saturation=150

          pickedcolor=colorlist[colors.index(mcolor)]
          lowb[0]=max(0, pickedcolor[0]-diff)
          lowb[1]=50
          lowb[2]=saturation
          highb[0]=pickedcolor[0]+diff
          highb[1]=255
          highb[2]=255
          return  lowb,highb

class snapandanalyse:
    ROBOT_LIBRARY_SCOPE = "TEST SUITE"
    def __init__(self):
       self.red_bound = ([15, 15, 100], [125, 125, 255])
       self.blue_bound = ([100, 15, 15], [255, 125, 125])
       self.green_bound = ([15, 100, 15], [125, 255, 125])
       self.white_bound = ([103, 86, 65], [145, 133, 128])

    def take_picture(self, picture_name="foo.png"):
        camera.start_preview()
        # Camera warm-up time
        sleep(3)
#        camera.exposure_mode= 'off'
        camera.shutter_speed = int(900) # set shutter speed based on light meter reading
        camera.ISO = 64
#        camera.framerate = 50
#        camera.image_effect = 'deinterlace1'

#        camera.brightness = 20      #JP
#	camera.contrast = 10        #JP
        camera.capture(picture_name)

    def mask_from_color_image(self, picture="foo.png",mask_color=None):
        img=cv2.imread(picture)
        img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        print(mask_color)

        if mask_color != None:
           lowb, highb = color_bounds(mask_color)
           print lowb
           print highb
           color_min = np.array(lowb,np.uint8)
           color_max = np.array(highb,np.uint8)
           bw = cv2.inRange(img_hsv,color_min,color_max)
           if mask_color ==  'red':
                color_min = np.array([170,50,50],np.uint8)
                color_max = np.array([180,255,255],np.uint8)
                bw2 = cv2.inRange(img_hsv,color_min,color_max)
                bw=bw+bw2
        else:
           th, bw = cv2.threshold(img_hsv[:, :, 2], 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        morph = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
	morph2 = cv2.bitwise_not(morph)
	des = cv2.bitwise_not(morph2)
	im3, contour,hier = cv2.findContours(morph,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

	for cnt in contour:
	    cv2.drawContours(des,[cnt],0,255,-1)

	morph = des
        kernel = np.ones((3, 3), np.uint8)
        dilation = cv2.dilate(morph,kernel,iterations = 1)
        cv2.imwrite("mask_"+picture, dilation)

##########
# Copy the thresholded image.
        im_floodfill = dilation.copy()
 
# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
        h, w = dilation.shape[:2]
        mask = np.zeros((h+2, w+2), np.uint8)
 
# Floodfill from point (0, 0)
        cv2.floodFill(im_floodfill, mask, (0,0), 255);
 
# Invert floodfilled image
        im_floodfill_inv = cv2.bitwise_not(im_floodfill)
 
# Combine the two images to get the foreground.
        morph = dilation | im_floodfill_inv


    def analyse_color_mask(self, picture="foo.png", expected_result=None):
        im = cv2.imread(picture,0)

        dist = cv2.distanceTransform(im, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)
#       borderSize = 75
        borderSize = 25
        distborder = cv2.copyMakeBorder(dist, borderSize, borderSize, borderSize, borderSize, cv2.BORDER_CONSTANT | cv2.BORDER_ISOLATED, 0)
        gap = 10
        kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*(borderSize-gap)+1, 2*(borderSize-gap)+1))
        kernel2 = cv2.copyMakeBorder(kernel2, gap, gap, gap, gap, cv2.BORDER_CONSTANT | cv2.BORDER_ISOLATED, 0)
        distTempl = cv2.distanceTransform(kernel2, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)
        nxcor = cv2.matchTemplate(distborder, distTempl, cv2.TM_CCOEFF_NORMED)
        mn, mx, _, _ = cv2.minMaxLoc(nxcor)
        th, peaks = cv2.threshold(nxcor, mx*0.5, 255, cv2.THRESH_BINARY)
        peaks8u = cv2.convertScaleAbs(peaks)
        im2, contours, hierarchy = cv2.findContours(peaks8u, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        peaks8u = cv2.convertScaleAbs(peaks)    # to use as mask

        for i in range(len(contours)):
            x, y, w, h = cv2.boundingRect(contours[i])
            _, mx, _, mxloc = cv2.minMaxLoc(dist[y:y+h, x:x+w], peaks8u[y:y+h, x:x+w])
            cv2.circle(im, (int(mxloc[0]+x), int(mxloc[1]+y)), int(mx), (255, 0, 0), 2)
            print(int(mx))
            cv2.imwrite("circled_"+picture, im)
            cv2.rectangle(im, (x, y), (x+w, y+h), (0, 255, 255), 2)
            cv2.drawContours(im, contours, i, (0, 0, 255), 2)

        if expected_result:
            if int(expected_result) != int(len(contours)):
                raise Exception("%s out of %s leds was lit." % (len(contours), expected_result))
#                raise Exception("%s out of %s leds was lit." % (len(circles[0,:]), expected_result))
            else:
                print("All OK. %s out of %s leds was lit." % (len(contours), expected_result))

