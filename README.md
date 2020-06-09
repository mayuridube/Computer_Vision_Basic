# Over_view of structuring and usages of script

|--- Image_Manipulation
|    |---height_width_image.py (gives dimension of image i.e height.width.channel)
|    |---img_read_write_display.py (simply read an image display it and stroning with new name & extension)
|    |---resize_image.py (various methods to resize the image) 



|--- Video_Manipulation
|    |---line & roi selection_on_video.py (select ROI an draw Line on video Feed )
|    |---video_playback_rtsp.py (stream rtsp field using opencv)
|    |---video_writer_usb_csmera.py (stream and record video from usb camera) 


#Issue Faced:
1.IN resize_image.py Matplotlip not showing plot for that make sure python3-tk is installed
otherwise do:
sudo apt-get install python3-tk
  
