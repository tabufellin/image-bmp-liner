from render import Render

#creating object
gl = Render()										#glinit is in the constructor of the class

#just image with noting in it
gl.finish('test1.bmp')							

#now modified to have 600x300 dimensions p
gl.CreateWindow(600,300)								
gl.finish('test2.bmp')										

#from x1 y1 --> to x2 y2 and make a rectangle
gl.viewPort(0, 0, 600, 300)					#ViewPort should be the fourth quadrant of the image
gl.vertex(0,0)
gl.color(1,0,0)	
gl.line(0,0,1,1)									#Should draw a line in the left top corner of the view port. 
gl.line(0,0,1,0)	
gl.line(0,0,1,-1)
gl.line(0,0,0,-1)
gl.line(0,0,-1,0)
gl.line(0,0,-1,-1)
gl.line(0,0,-1,1)
gl.line(0,0,1,0)
gl.line(0,0,0,1)

gl.finish('test.bmp')	
