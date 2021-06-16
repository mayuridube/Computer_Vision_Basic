# Overview of structure and usages

<h5>image_manipulation</h5>
1.edge_detection.py<br>
Detect edges from image,edges are nothing but point where pixel get change<br>
Usage: python3 edge_detection.py<br><br>
2.height_width_image.py<br>
Gives dimension of image i.e height,width,channel<br>
Usage: python3 height_width_image.py<br>
3.image_rotation.py<br>
Rotate the image in anticlockwise.<br> 
Usage: python3 image_rotation.py<br>
4.img_read_write_display.py<br>
simply read an image display it and storing with new name & extension<br>
Usage: python3 img_read_write_display<br>
5.img_thresholding.py<br>
Different method for thresholding the image,used to divide the image into it’s foreground and background.<br>
usage: python3 img_thresholding.py<br>
6.resize_image.py<br>
various methods to resize the image<br>
Usage: python3 resize_image.py<br><br>



<h5>video_manipulation</h5>
1.extract_image_from_video.py<br>
read video and convert into images and save it in data folder<br>
Usage:add video file path in script & Run python3 extract_image_from_video.py<br>
2.line and roi selection_on_video.py<br>
select ROI and draw Line on video Feed<br>
Usage: python3 line_and_roi selection_on_video.py<br>
3.video_playback_rtsp.py<br>
stream rtsp feed using opencv<br>
Usage:add rtsp link in script & Run python3 video_playback_rtsp.py<br>
4.video_writer_usb_camera.py<br>
stream and record video from usb camera<br>
Usage:python3 video_writer_usb_csmera.py<br>


<h5>Issue Faced:</h5>
1.IN resize_image.py Matplotlip not showing plot for that make sure python3-tk is installed<br>
otherwise do:<h6 style="background-color:lightgrey">sudo apt-get install python3-tk<br>
   
  
