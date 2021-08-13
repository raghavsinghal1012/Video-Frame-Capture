import cv2
from moviepy.editor import VideoFileClip
from tkinter import filedialog

Video_name=filedialog.askopenfilename()
name=Video_name.split("/")[-1]
name=name.split(".")[0]
Vc = cv2.VideoCapture(Video_name)
for_video_duration = VideoFileClip(Video_name)
c = 0
count=1


if (Vc.isOpened()):
    rval, frame = Vc.read()
else:
    rval = False

print("Duration of video in sec is :",for_video_duration.duration )
fps = Vc.get(cv2.CAP_PROP_FPS)
print("FPS : ",fps)
seconds=float(input("enter time intervals in second:"))

location=filedialog.askdirectory()

timeF =fps*seconds
timeF=int(timeF)
 
while (rval): 
    rval, frame = Vc.read()
    if (c % timeF == 0): 
        cv2.imencode('.jpg', frame)[1].tofile(location+'/'+name+'_'+str(count)+'.jpg')
        count+=1
                 
    c = c + 1
    
    cv2.waitKey(1)
 
 
Vc.release()
