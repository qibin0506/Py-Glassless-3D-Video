import sys, getopt
from moviepy.editor import VideoFileClip

try:
    input_file = None
    opts, args = getopt.getopt(sys.argv[1:], "hi:", ["help", "input"])

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('python video_info.py -i <inputfile>')
        if opt in ('-i', '--help'):
            input_file = arg

    video = VideoFileClip(input_file)
    print("video width: {}, video_height: {}".format(video.w, video.h))
except getopt.GetoptError:
    print('python video_info.py -i <inputfile>')
    sys.exit(2)
