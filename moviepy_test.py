# Import everything needed to edit video clips
from moviepy.editor import *

def main():

	input_file = open('./sampleinput.txt').read()
	times = input_file.split(' ')

	#not too crazy
	times = times[0:9]

	#hardcode num videos
	num_videos = 3

	ct = 0

	# first one

	final_clips = []


	
	time_start = times.pop(0)
	time_end = float(times.pop(0)) - float(time_start)
	#interval = times.pop(0) - time_end
	time_start = 0


	#time1 = times.pop(0)
	#time2 = float(times.pop(0)) - float(time1)
	#print time2

	# rest
	while(times):
		#time = times.pop(0)
		num = ct%num_videos
		video = getVideo(num)
		print video

		print time_start, ", ", time_end
		clip = VideoFileClip(video).subclip(time_start, time_end)
		
		if (ct%num_videos == 0):
			time_start = time_end
			time_end = float(times.pop(0)) - float(time_start)			

		final_clips.append(clip)
		#time_start = time_end
		++ct

	final_clip = concatenate_videoclips(final_clips)

	final_clip.write_videofile("my_concatenation.mp4")


def getVideo(num):
	videos = ['./catvideos/cat1.mp4', './catvideos/cat2.mp4', 
	'./catvideos/cat3.mp4']
	return videos[num]

main()