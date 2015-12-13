# Import everything needed to edit video clips
from moviepy.editor import *
import glob

def main():
	videos = glob.glob("./catvideos/*.mp4")
	audio = AudioFileClip('./barbiegirl.mp3')

	input_file = open('./sampleinput.txt').read()
	times = input_file.split(' ')

	ct = 0
	new_times = []
	for i in times:
		if (ct%2==0):
			new_times.append(i)
		ct = ct + 1

	#hardcode num videos
	num_videos = 4

	
	intervals = []
	for i in range(0, len(new_times)-1):
		start = float(new_times[i])
		end = float(new_times[i+1])
		intervals.append(end-start)
		#ct = ct +1

	intervals = intervals[0:8]

	final_clips = []
	ct = 0					

	
	while(intervals):

		num = ct%num_videos
		video = videos[num]

		print video

		clip = VideoFileClip(video).subclip(0, intervals.pop(0))

		clip.fps = 24
		final_clips.append(clip)

		ct = ct+1

	final_clip = concatenate_videoclips(final_clips)
	final_clip = final_clip.set_audio(audio)

	final_clip.write_videofile("conCATenate.mp4")
	

main()