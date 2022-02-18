import cv2
import numpy as np
import time

#cap = cv2.VideoCapture(r"C:\Users\Sandhya Sudi\Desktop\python\fan1.mp4")
if __name__ == '__main__' :
    cap = cv2.VideoCapture(r"C:\Users\Sandhya Sudi\Desktop\python\fan1.mp4")
    i=0
    
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    if int(major_ver)  < 3 :
        fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
        print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else:
        fps = cap.get(cv2.CAP_PROP_FPS)
        print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))




    


while(True):
    ret, frame=cap.read()
    cv2.imshow('output',frame)
    if ret:
        # if video is still left continue creating images
        name = (r'C:\Users\Sandhya Sudi\Desktop\python' + str(i) + '.jpg')
        print ('Creating...' + name)
  
        # writing the extracted images
        cv2.imwrite(name, frame)
  
        # increasing counter so that it will
        # show how many frames are created
        i += 1
        
    if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
    




 
cap.release()
cv2.destroyAllWindows()














	 

	# Check if camera opened successfully

#if (cap.isOpened()== False):

	  #print("Error opening video stream or file")
#while(cap.isOpened()):
    #ret, frame = cap.read()
    #if ret == True:
        #cv2.imshow('Frame',frame)
        # Press Q on keyboard to  exit
        #if cv2.waitKey(10000) & 0xFF == ord('q'):
            #break
        #else:
            #break
#cap.release()
#cv2.destroyAllWindows()