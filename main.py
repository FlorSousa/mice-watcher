import cv2 as cv
from tqdm import tqdm
from utils.parser import parser_args,open_data,save_project

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
    
    if args.path == None:
        save_project(f"{args.name}.json",project_data)
        exit()
        
    save_project(args.path,project_data)