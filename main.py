import sys, getopt
from moviepy.editor import VideoFileClip
import numpy as np
import cv2

input_file = None
output_file = None

video_left = 20
video_right = -30

video_shift = 20


def process_frame(frame):
    global video_left, video_right, video_shift

    right = frame[:, video_left:video_right]
    left = frame[:, video_left+video_shift:video_right+video_shift]

    return np.concatenate((left, right), axis=1)


def generate():
    global input_file, output_file

    video = VideoFileClip(input_file)
    processed = video.fl_image(process_frame)
    processed.write_videofile(output_file, audio=True)


def main(argv):
    global input_file, output_file, video_left, video_right, video_shift

    try:
        opts, args = getopt.getopt(argv, "hi:o:l:r:s:", ["help", "input", "output", "left", "right", "shift"])
    except getopt.GetoptError:
        print('python main.py -i <inputfile> -o <outputfile> -l <left> -r <right> -s <shift>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('python main.py -i <inputfile> -o <outputfile> -l <left> -r <right> -s <shift>')
            sys.exit()
        elif opt in ('-i', '--input'):
            input_file = arg
        elif opt in ('-o', '--output'):
            output_file = arg
        elif opt in ('-l', '--left'):
            video_left = int(arg)
        elif opt in ('-r', '--right'):
            video_right = int(arg)
        elif opt in ('-s', '--shift'):
            video_shift = int(arg)

    if input_file is None:
        print("-i must be set.")
        sys.exit()

    if output_file is None:
        print("-0 must be set.")
        sys.exit()

    if video_left is None:
        print("-l must be set.")
        sys.exit()

    if video_right is None:
        print("-r must be set.")
        sys.exit()

    print("start generate...")
    generate()
    print("generate success to {}".format(output_file))


if __name__ == '__main__':
    main(sys.argv[1:])
