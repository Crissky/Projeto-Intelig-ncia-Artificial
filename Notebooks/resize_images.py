#Imports
from imutils import paths
from itertools import product
import os
import cv2

base_path = '..{}imagens'.format(os.sep)
base_folders = [os.path.join(base_path, folder) for folder in os.listdir(base_path)]
sizes = [(200, 150), (200, 267), (300, 400), (500, 667), (300, 300), (500, 500)]

for path, dimensions in list( product( base_folders, sizes ) ):
  print( "woking in", path, "with dimensions {}x{}".format(dimensions[0], dimensions[1]) )
  print("Get Images...")
  image_paths = list( paths.list_images( path ) )
  print("Loading Images...")
  images = list( map( cv2.imread, image_paths ) )
  print("Recolor Images...")
  images = [cv2.cvtColor(image, cv2.COLOR_BGR2RGB) for image in images]
  print("Resize Images...")
  images = [cv2.resize(image, dimensions) for image in images]
  
  new_path = base_path + "{}x{}".format(dimensions[0], dimensions[1])
  new_path = os.path.join(new_path, os.path.basename(path))
  os.makedirs(new_path, exist_ok=True)
  new_image_paths = [os.path.join(new_path, os.path.basename(image_path)) for image_path in image_paths]

  print("Saving Images in '{}'... \n\n".format(new_path))
  for index in range(len(image_paths)):
    cv2.imwrite(new_image_paths[index], images[index])
  
print("Finish!!!")
