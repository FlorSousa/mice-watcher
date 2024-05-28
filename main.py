import cv2 as cv
from tqdm import tqdm
from utils.parser import parser_args,open_data,save_project
from ultralytics import YOLO

def open_capture(video_path):
    if video_path == None:
        exit()
    capture = cv.VideoCapture(video_path)
    if not capture.isOpened():
        print("Error: couldn't open video")
        exit()
    return capture
                  
if __name__ == "__main__":
    args = parser_args()
    project_data = open_data(args.path,args.video,args.framerate)
    capture = open_capture(args.video)
    model = YOLO("model/yolov8n.pt")
    frameIndex = 0
    frame_rate_ms = int((1/project_data["frame_rate"])*1000)
    pbar = tqdm(total=int(capture.get(cv.CAP_PROP_FRAME_COUNT)))
    
    while(capture.isOpened()):
        ret,frame = capture.read()
        #results = model(frame,stream=True)
       
        if not ret:
            print("Error: Couldn't open frame %d" % (frameIndex))
            exit()

        cv.imshow("Watching",frame)
        if cv.waitKey(frame_rate_ms) & 0xFF == ord("q"):
            break
        pbar.update(1)
        frameIndex+=1
    
    capture.release()
    cv.destroyAllWindows()
    if args.path == None:
        save_project(f"{args.name}.json",project_data)
        exit()
    
    save_project(args.path,project_data)    
    