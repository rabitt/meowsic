# Import everything needed to edit video clips
from moviepy.editor import *

def main():

	input_file = open('./sampleinput.txt').read()
	times = input_file.split(' ')

	#not too crazy
	times = times.slice(0, 9)

	#hardcode num videos
	num_videos = 4

	ct = 0

	# first one

	final_clips = []
	time1 = 0

	# rest
	while(times):
		time = times.pop(0)
		num = ct%num_videos
		video = getVideo(num)

		clip = VideoFileClip(video).subclip(time1, time)
		if (ct%4 == 0):
			time1 = time1 + time

		final_clips.append(clip)
		++ct

	final_clip = concatenate_videoclips(final_clips)

	final_clip.write_videofile("my_concatenation.mp4")


def getVideo(num):
	videos = ['./catvideos/cat1.mp4', './catvideos/cat1.mp4', 
	'./catvideos/cat1.mp4', './catvideos/cat1.mp4']
	return videos[num]

main()