#!/usr/bin/env python
import subprocess as sb
import os
import time

#savingPathP = sb.Popen("xdg-user-dir VIDEOS", shell=True, stdout=sb.PIPE)
#savingPathP.wait()
#savingPath,_ = savingPathP.communicate()
#savingPath = savingPath.replace("\n","")
savingPath = os.popen("xdg-user-dir VIDEOS").read().replace("\n","")+"/"

isRecording = "/tmp/.screenrecording"

cmd = "ffmpeg -f x11grab -s wxga -r 25 -i :0.0 -qscale 0 "

def notify(title="", content="", icon="record"):
	os.popen("notify-send -i {} -t 1 {} {}".format(repr(icon), repr(title), repr(content)))
	return 0

def main():
	if not os.path.isfile(isRecording):
		saveName = savingPath+str(int(time.time()))+".mp4"

		#recording = sb.Popen("yes", shell=False, stdout=sb.PIPE)
		recording = sb.Popen( (cmd+saveName).split(" ") , shell=False, stdout=sb.PIPE, stderr=sb.PIPE)
		pid = recording.pid
		
		with open(isRecording,"w+") as f:
			f.write(saveName +"\n"+ str(pid))
			f.close()
		
		notify("Start recording","Saving at "+saveName)

		recording.wait()
	else:
		with open(isRecording,"r") as f:
			saveName,pid=f.read().split("\n")
		os.remove(isRecording)

		os.system("kill -2 "+pid)
		
		notify("Stop recording","Saved at "+saveName)
	
	return 0

if __name__ == "__main__":
	exit(main())
