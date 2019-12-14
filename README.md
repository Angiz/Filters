# Filters
Project uses photo filters like median, sobel, dilatation, smooth, erosion

To run a program necessary are following libraries:
- PyQt
- OpenCV

Filters are uploaded by using OpenCV library for Python. First, you have to upload a picture by "Load Picture..." button. Afterwards you can 
choose particular filter. Every filter (except sobel) can be dynamically changed by trackbar. Kernel for trackbar can give odd value between 1
and 7.
