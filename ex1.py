import matplotlib.pyplot as plt
import numpy as np
import sys


def get_closest_cent_index(pixel):
    current_dist, index_cent = 195075, None
    for p in range(num_of_cent):
        #print(pow(z[p][0]+pixel[0], 2) + pow(z[p][1]+pixel[1], 2) + pow(z[p][2]+pixel[2], 2))
        dist = pow(z[p][0]+pixel[0], 2) + pow(z[p][1]+pixel[1], 2) + pow(z[p][2]+pixel[2], 2)
        if dist < current_dist:
            current_dist = dist
            index_cent = p
    return index_cent

def create_cent_by_average():
    first, second, third = 0.0, 0.0, 0.0
    new_cent = []
    for i in range(num_of_cent):
        for m in range(len(pixels_cent_list[i])):

            #print("iteration " + str(m))
            first, second, third = first + pixels_cent_list[i][m][0],\
                                   second + pixels_cent_list[i][m][1], \
                                   third + pixels_cent_list[i][m][2]

        #print(i)
        if len(pixels_cent_list[i]) != 0:
            new_cent.append([first / len(pixels_cent_list[i]), second / len(pixels_cent_list[i]), third / len(pixels_cent_list[i])])
    return np.array(new_cent)

image_fname, centroids_fname, out_fname = sys.argv[1], sys.argv[2], sys.argv[3]
z = np.loadtxt(centroids_fname)
#print(z)
orig_pixels = plt.imread(image_fname)
pixels = orig_pixels.astype(float)/255
#print(pixels)
pixels = pixels.reshape(-1, 3)


#print(pixels)
#print(z[0])
#print(pixels[0])
num_of_cent = z.shape[0]
num_of_pixels = pixels.shape[0]

# # creating 2d list for the pixels that will be classified
pixels_cent_list = []
#print("num_of_cent = " + str(num_of_cent))
for i in range(num_of_cent):
    #print("i = " + str(i))
    pixels_cent_list.append([])

MAX_ITERATIONS = 20

for j in range(MAX_ITERATIONS):
    for k in range(num_of_pixels):
        current_pixel = pixels[k]
        #if k == 0 and j == 1:
        #    print(k)
        closest_cent_index = get_closest_cent_index(current_pixel)
        pixels_cent_list[closest_cent_index].append(current_pixel)
    av = create_cent_by_average()

    z = av
    print(z)