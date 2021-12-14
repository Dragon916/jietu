"""
    此脚本用于从视频中截取图片
"""
#
# import cv2
# import time
#
# mp4 = cv2.VideoCapture(r"C:\Users\龙升\Desktop\炮筒识别\Video_2021-09-01_142228.wmv")  # 读取视频
# is_opened = mp4.isOpened()  # 判断是否打开
# print(is_opened)
# fps = mp4.get(cv2.CAP_PROP_FPS)  # 获取视频的帧率
# print(fps)
# widght = mp4.get(cv2.CAP_PROP_FRAME_WIDTH)  # 获取视频的宽度
# height = mp4.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 获取视频的高度
# print(str(widght) + "x" + str(height))
# i = 0
# while is_opened:
#     if i == 120:  # 截取图片的数量
#         break
#     else:
#         i += 1
#     time.sleep(3)  # 如果图像不清晰从这里修改以下参数
#     (flag, frame) = mp4.read()  # 读取图片
#     file_name = "iamge" + str(i) + ".jpg"
#     print(file_name)
#     if flag:
#         cv2.imwrite(file_name, frame, [cv2.IMWRITE_JPEG_QUALITY])  # 保存图片
# print("转换完成")


import cv2
import argparse
import os


def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Process pic')
    parser.add_argument('--input', help='video to process', dest='input', default=None, type=str)
    parser.add_argument('--output', help='pic to store', dest='output', default=None, type=str)
    # default为间隔多少帧截取一张图片
    parser.add_argument('--skip_frame', dest='skip_frame', help='skip number of video', default=2, type=int)
    # input为输入视频的路径 ，output为输出存放图片的路径
    args = parser.parse_args(['--input', r'C:\Users\龙升\Desktop\paotong\Video_2021-09-01_143715.wmv', '--output',
                              r'D:\jietu\video3'])
    return args


def process_video(i_video, o_video, num):
    cap = cv2.VideoCapture(i_video)
    num_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    expand_name = '.jpg'
    if not cap.isOpened():
        print("Please check the path.")
    cnt = 0
    count = 0
    while 1:
        ret, frame = cap.read()
        cnt += 1
        # how
        # many
        # frame
        # to
        # cut
        if cnt % num == 0:
            count += 1
            cv2.imwrite(os.path.join(o_video, str(count) + expand_name), frame)

        if not ret:
            break


if __name__ == '__main__':
    args = parse_args()
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    print('Called with args:')
    print(args)
    process_video(args.input, args.output, args.skip_frame)
