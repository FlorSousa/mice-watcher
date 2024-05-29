import cv2 as cv

def drawRois(frame,rois)-> numpy.darray:
    for roi in rois:
       cv.rectangle(frame, (roi[0],roi[1]), (roi[0]+roi[2],roi[1]+roi[3]), (255,0,0), 2)
    print(type(frame))
    return frame
   
def check_mice_posi(frame,rois,mice_posi)-> numpy.darray:
   pass

def draw_contour(frame,object_posi)-> umpy.darray:
   pass

def open_capture(video_path)-> cv.VideoCapture:
    if video_path == None:
        print("Erro")
        exit()
    return cv.VideoCapture(video_path)

def selectionRoi(back_frame)-> numpy.darray:
    return cv.selectROIs("Select Regions Of Interesse", back_frame)