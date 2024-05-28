import argparse

def parser_args():
    parser = argparse.ArgumentParser(
        description='Tracks mice.'
    )

    parser.add_argument(
        '--path', type=str,help='path to project data'
    )
    
    parser.add_argument(
        '--name', type=str, help="Project name"
    )
    
    parser.add_argument(
        "--video", type=str, help="Video pasth"
    )
    
    parser.add_argument(
        "--framerate", type=str, help="Frame rate video", default=30
    )
    
    return parser.parse_args()

def open_data(path,video_path,frame_rate):
    import json
    if path == None:
        if video_path==None:
            print("Error: No video path")
            exit()
        return {
            "video_path":video_path,
            "frame_rate":frame_rate,
            "rois":[],
            "type":0,
            "fecal_bolus":0,
            "rearings":0,
            "freezing":0,
            "ambulations":0,
            "rearings_time":0.0,
            "freezing_rearings":0.0,
            "ambulations_time":0.0,
            "grooming_time":0.0,
            "time_spent_center":0.0,
            "time_spent_periphery":0.0
        }
    try:   
        return json.load(open(path, encoding='utf-8'))
    except:
        print("Error: couldn't open project data")
        exit()
        
def save_project(path,data):
    import json
    import os
    segmented_path =  path.split("\\")
    path_to_file = "\\".join(segmented_path[:len(segmented_path)-1])
    if not os.path.exists(path_to_file):
        os.mkdir(path_to_file)
      
    with open(path, "w") as outfile:
        json.dump(data,outfile)