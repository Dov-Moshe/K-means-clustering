import matplotlib.pyplot as plt
import numpy as np
import sys


def get_closest_cent_index(cents, pixel):
    current_dist, index_cent = 195075, None

    # calculate 
    for p in range(num_of_cent):
        dist = np.linalg.norm(cents[p] - pixel)
        if dist < current_dist:
            current_dist = dist
            index_cent = p
    return index_cent


def create_cent_by_average(pixels_list, centroids):
    new_cents = np.empty((0, 3))
    for i in range(num_of_cent):

        sum = pixels_list[i].sum(axis=0)

        if pixels_list[i].size != 0:
            average = np.divide(sum, pixels_list[i].size / LENGTH_OF_VECTOR)
        else:
            average = centroids[i]

        average = average.round(4)
        new_cents = np.concatenate((new_cents, [average]))
    return new_cents


if __name__ == "__main__":

    MAX_ITERATIONS = 20
    LENGTH_OF_VECTOR = 3

    ##############################
    image_fname, centroids_fname, out_fname = sys.argv[1], sys.argv[2], sys.argv[3]
    z = np.loadtxt(centroids_fname)
    orig_pixels = plt.imread(image_fname)
    pixels = orig_pixels.astype(float)/255
    pixels = pixels.reshape(-1, 3)
    ##############################

    num_of_cent = z.shape[0]
    num_of_pixels = pixels.shape[0]

    f = open(out_fname, "w")

    for iter in range(MAX_ITERATIONS):

        # creating 2d list for the pixels that will be classified
        pixels_cent_list = []
        for i in range(num_of_cent):
            pixels_cent_list.append(np.empty((0, 3)))

        for k in range(num_of_pixels):
            current_pixel = pixels[k]
            closest_cent_index = get_closest_cent_index(z, current_pixel)
            pixels_cent_list[closest_cent_index] = np.concatenate((pixels_cent_list[closest_cent_index], [current_pixel]))

        new_z = create_cent_by_average(pixels_cent_list, z)

        f.write(f"[iter {iter}]:{','.join([str(i) for i in new_z])}" + "\n")

        if np.array_equal(z, new_z):
            break

        z = new_z

    f.close()
