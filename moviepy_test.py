# Import everything needed to edit video clips
from moviepy.editor import *


length = input("Enter length of video: ")

# Get subclip from 0 to (length) seconds
clip = VideoFileClip("catexample1.mp4").subclip(0,length)

# Reduce the audio volume (volume x 0.8)
clip = clip.volumex(0.8)

# Write the result to a file (many options available !)
clip.write_videofile("catexample1_1.mp4")

print "done!"