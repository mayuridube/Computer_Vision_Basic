# Overview of structure and usages

|--- image_Manipulation<br>
|    |---SIFT_algo(Scale Invariant Feature Transform (SIFT) is a very popular keypoint detection algorithm)<br>
|    |---edge_detection.py (Detect edges from image,edges are nothing but point where pixel get change)<br>
|    |---height_width_image.py (gives dimension of image i.e height.width.channel)<br>
|    |---image_rotation.py (gives dimension of image i.e height.width.channel)<br>
|    |---img_read_write_display.py (simply read an image display it and storing with new name & extension)<br>
|    |---resize_image.py (various methods to resize the image)<br><br>



|--- video_Manipulation<br>
|    |---extract_image_from_video.py(read video and convert into images and save it)<br>
|    |---line & roi selection_on_video.py (select ROI an draw Line on video Feed )<br>
|    |---video_playback_rtsp.py (stream rtsp feed using opencv)<br>
|    |---video_writer_usb_csmera.py (stream and record video from usb camera)<br>


<h5>Issue Faced:</h5>
1.IN resize_image.py Matplotlip not showing plot for that make sure python3-tk is installed<br>
otherwise do:<h6 style="background-color:lightgrey">sudo apt-get install python3-tk<br>
   
  
