# Import everything needed to edit video clips
from moviepy.editor import *

def main():

	input_file = open('./sampleinput.txt').read()
	times = input_file.split(' ')

	ct = 0
	new_times = []
	for i in times:
		if (ct%2==0):
			new_times.append(i)
		ct = ct + 1

	#hardcode num videos
	num_videos = 2

	
	intervals = []
	for i in range(0, len(new_times)-1):
		start = float(new_times[i])
		end = float(new_times[i+1])
		intervals.append(end-start)
		#ct = ct +1

	print intervals
	intervals = intervals[0:8]

	final_clips = []
	ct = 0					

	while(intervals):

		num = ct%num_videos
		video = getVideo(num)

		print video

		clip = VideoFileClip(video).subclip(0, intervals.pop(0))


		final_clips.append(clip)

		ct = ct+1

	print final_clips
	final_clip = concatenate_videoclips(final_clips)

	final_clip.write_videofile("my_concatenation2.mp4")
	

def getVideo(num):
	videos = ['./catvideos/after.mp4', './catvideos/cat2.mp4']
	#videos = './catvideos/cat2.mp4'
	return videos[num]
	#return videos

main()