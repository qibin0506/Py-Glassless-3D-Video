# Py-Glassless-3D-Video

## 裸眼3D观看方法
1. 眼睛保持放松状态 平行靠近手机 将脸无限贴近屏幕 鼻子对准中线让眼睛虚焦
2. 直到画面上两个人物重合为一个人物时 保持虚焦状态 盯着那个虚影 需要反复找角度尝试
3.然后慢慢拉开距离 直到出现三个画面 就成功了
4.
参考：[https://www.bilibili.com/video/av94669451/](https://www.bilibili.com/video/av94669451/)


## 裸眼3D视频制作
1. 下载本项目
2. 安装python: [https://blog.csdn.net/nerissa_lou/article/details/78300839](https://blog.csdn.net/nerissa_lou/article/details/78300839)
3. 定位到项目目录，执行`pip install -r requirements.txt`
4. 执行`python video_info.py -i test.mp4` 查看视频信息，输入：`video width: 544, video_height: 960`
5. 执行`python main.py -i test.mp4 -o 3d.mp4`，等待制作完成。

## 详细参数说明
1. -i 输入文件
2. -o 输出文件
3. -l 可选，自定义视频左边界
4. -r 可选，自定义视频右边界
5. -s 可选，视频偏移量
