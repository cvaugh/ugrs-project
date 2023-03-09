import cv2
import numpy as np
from tqdm import tqdm

def read_video_frames(path, linear=False, count=None):
    capture = cv2.VideoCapture(path)
    frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    if count is None:
        count = frame_count
    else:
        count = min(count, frame_count)
    success, frame = capture.read()
    index = 0
    frames = []
    with tqdm(total=frame_count, leave=False) as progress:
        progress.set_description("Reading frames")
        while success and index < count:
            frames.append(frame.reshape(-1) if linear else frame)
            success, frame = capture.read()
            index += 1
            progress.update()
    capture.release()
    return frames

def count_frames(path):
    capture = cv2.VideoCapture(path)
    frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    capture.release()
    return frame_count
