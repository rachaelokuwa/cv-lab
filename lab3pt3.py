import cv2
import numpy as np

#global variables for trackbar 
min_red, max_red = 0, 255
min_green, max_green = 0, 255
min_blue, max_blue = 0, 255
has_changed=True



def set_min_red(x):
    global min_red, has_changed
    min_red = x
    has_changed = True

def set_max_red(x):
    global max_red, has_changed
    max_red = x
    has_changed = True

def set_min_green(x):
    global min_green, has_changed
    min_green = x
    has_changed = True

def set_max_green(x):
    global max_green, has_changed
    max_green = x
    has_changed = True


def set_min_blue(x):
    global min_blue, has_changed
    min_blue = x
    has_changed = True


def set_max_blue(x):
    global max_blue, has_changed
    max_blue = x
    has_changed = True



#Load Image
img=cv2.imread('data/robot_010_sm.png', cv2.IMREAD_COLOR)
# Now convert the image to RGB rather than BGR, for convenience when plotting it
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #for some reason it screws up the colour


# Create a window, and give it a name
cv2.namedWindow('Tracker sample', cv2.WINDOW_AUTOSIZE)




# Create a trackbar
# - give it a name ('Red')
# - attach it to the named window ('Tracker sample')
# - set its minimum and maximum values (0 and 255)
# - give it the name of a function to call when it changes (set_m...)
cv2.createTrackbar('Min Red', 'Tracker sample', 0, 255, set_min_red)
cv2.createTrackbar('Max Red', 'Tracker sample', 255, 255, set_max_red)
cv2.createTrackbar('Min Green', 'Tracker sample', 0, 255, set_min_green)
cv2.createTrackbar('Max Green', 'Tracker sample', 255, 255, set_max_green)
cv2.createTrackbar('Min Blue', 'Tracker sample', 0, 255, set_min_blue)
cv2.createTrackbar('Max Blue', 'Tracker sample', 255, 255, set_max_blue)



while True:
    if has_changed:
        has_changed = False
        
        # new image to store the results
        new_img=np.zeros(img.shape, np.uint8)


        # Iterate over the pixels in the image
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):

                blue = img[i, j, 0] #because the colours are all mixed 
                green = img[i, j, 1] #be wary of the colour channnels based on what library is being used. 
                red = img[i, j, 2]


                # Check if the pixel is within the selected range
                if (min_red <= red <= max_red and 
                    min_green <= green <= max_green and 
                    min_blue <= blue <= max_blue):
                    new_img[i, j] = [blue, green, red]  # Keep the original colour
                else:
                    new_img[i, j] = [0, 0, 0]  # Set to black


        cv2.imshow('Tracker sample', new_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



    # so i only change colour to rgb when using matplotlib to display, as that uses rgb. otherwise, like here where were just using the builtin imshow(), we just work with bgr. 

# to isolate yellow, change only min red 150, min blue green 150 and max blue to 100



cv2.destroyAllWindows()



