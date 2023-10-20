import cv2
import numpy as np
from math import exp
import matplotlib.pyplot as plt
from math import sqrt
from scipy.ndimage import uniform_filter

from skimage import draw
# img1 = cv2.imread("trial_15.png",0)

# img2 = cv2.imread("trial_16.png",0)

# base_folder = "/home/mohan/backup_xeon_decoding_server_sep_21_2022/experiment7/group_0"

# base_folder = "/home/mohan/backup_xeon_decoding_server_sep_21_2022/experiment7/group_1"

# base_folder = "/home/mohan/backup_xeon_decoding_server_sep_21_2022/experiment8/group_0"

base_folder = "/home/mohan/backup_xeon_decoding_server_sep_21_2022/experiment9/group_1"


# base_folder = "/home/mohan/backup_xeon_decoding_server_sep_21_2022/experiment9/group_0"

# img1_name = "semi_img_no_1_crop_no_2.png"

# img2_name = "semi_img_no_2_crop_no_2.png"

# img1_name = "semi_img_no_14_crop_no_1.png"

# img2_name = "semi_img_no_15_crop_no_1.png"

# img1_name = "semi_img_no_1_crop_no_1.png"

# img2_name = "semi_img_no_2_crop_no_1.png"

img1_name = "semi_img_no_6_crop_no_2.png"

img2_name = "semi_img_no_7_crop_no_1.png"

# img1_name = "semi_img_no_11_crop_no_3.png"

# img2_name = "semi_img_no_12_crop_no_3.png"

hsv_img1 = cv2.cvtColor(cv2.imread(base_folder+"/"+img1_name), cv2.COLOR_BGR2HSV)/255.0

hsv_img2 = cv2.cvtColor(cv2.imread(base_folder+"/"+img2_name), cv2.COLOR_BGR2HSV)/255.0

print(hsv_img2.max(),hsv_img2.shape)
# from scipy import ndimage

def f(x):
    b = np.full_like(x,0.11,dtype=np.double)

    return (1 - 1/(1 + np.exp(-100 * (x - b))))
    # return 

def I(f,H,S,V) :
    H_c = np.full_like(H,0.083,dtype=np.double)
    # print(f (np.minimum(abs(H_c - H), 1 - abs(H_c - H))).shape,H.shape)
    return  f (np.minimum(abs(H_c - H), 1 - abs(H_c - H))) * S * V
h1,s1,v1 = cv2.split(hsv_img1)
h2,s2,v2 = cv2.split(hsv_img2)

# f=np.vectorize(f)

img1  = I(f,h1,s1,v1)

img2  = I(f,h2,s2,v2)


cv2.imwrite("ayyayo_6.png",img2*255)
print(img2.shape)


ksize = 3

# gX = cv2.Sobel(img1, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
# gY = cv2.Sobel(img1, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)

I_mean  = 0.5*(img2+img1)

gX = cv2.Sobel(img1, cv2.CV_64F, 1, 0)
gY = cv2.Sobel(img1, cv2.CV_64F, 0, 1)

I_x = gX

I_y = gY

# cv2.imshow("gradient",I_y)

I_t = img1-img2

I_mean  = 0.5*(img2+img1)

b = -1*I_t

blur = cv2.GaussianBlur(I_mean,(3,3),0)

# Apply Laplacian operator in some higher datatype
I_delta = cv2.Laplacian(blur,cv2.CV_64F)

# But this tends to localize the edge towards the brighter side.
I_delta = I_delta/I_delta.max()
alpha = 0.4

I_delta_L2_NORM =  np.linalg.norm(I_delta, ord=2)**2
print(I_delta_L2_NORM+alpha)
# # I_delta = np.append(np.expand_dims(I_x,axis=0), np.expand_dims(I_y, axis= 0) , axis= 0)
# # I_delta = np.moveaxis(np.stack([I_x,I_y],axis=0),0,-1)
# # print(I_delta.shape)
# # print((I_delta.transpose().dot(I_delta)).shape)

u = -1*(I_x * I_t)/(I_delta_L2_NORM+alpha)
v = -1*(I_y * I_t)/(I_delta_L2_NORM+alpha)
print(u.shape,v.shape)

# # hsv = np.zeros_like(cv2.imread("trial_1.png"))
# # hsv[..., 1] = 255
# # mag, ang = cv2.cartToPolar(u, v)

# # hsv[..., 0] = ang*180/np.pi/2
# # hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
# # bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
# # cv2.imshow('frame2', bgr)


# # cv2.waitKey(0) 

# # cv2.destroyAllWindows() 


# # np.norm(())
# # flow = np.array([u,v])
flow = np.moveaxis(np.append(np.expand_dims(u,axis=0), np.expand_dims(v, axis= 0) , axis= 0),0,-1)
print(flow.shape)
step = 3
# plt.quiver(np.arange(0, flow.shape[1], step), np.arange(flow.shape[0], -1, -step), 
#            flow[::step, ::step, 0], flow[::step, ::step, 1])

# plt.show()

def hof(flow, orientations=9, pixels_per_cell=(8, 8),
        cells_per_block=(3, 3), visualise=False, normalise=False, motion_threshold=1.):

    """Extract Histogram of Optical Flow (HOF) for a given image.
    Key difference between this and HOG is that flow is MxNx2 instead of MxN
    Compute a Histogram of Optical Flow (HOF) by
        1. (optional) global image normalisation
        2. computing the dense optical flow
        3. computing flow histograms
        4. normalising across blocks
        5. flattening into a feature vector
    Parameters
    ----------
    Flow : (M, N) ndarray
        Input image (x and y flow images).
    orientations : int
        Number of orientation bins.
    pixels_per_cell : 2 tuple (int, int)
        Size (in pixels) of a cell.
    cells_per_block  : 2 tuple (int,int)
        Number of cells in each block.
    visualise : bool, optional
        Also return an image of the hof.
    normalise : bool, optional
        Apply power law compression to normalise the image before
        processing.
    static_threshold : threshold for no motion
    Returns
    -------
    newarr : ndarray
        hof for the image as a 1D (flattened) array.
    hof_image : ndarray (if visualise=True)
        A visualisation of the hof image.
    References
    ----------
    * http://en.wikipedia.org/wiki/Histogram_of_oriented_gradients
    * Dalal, N and Triggs, B, Histograms of Oriented Gradients for
      Human Detection, IEEE Computer Society Conference on Computer
      Vision and Pattern Recognition 2005 San Diego, CA, USA
    """
    flow = np.atleast_2d(flow)

    """ 
    -1-
    The first stage applies an optional global image normalisation
    equalisation that is designed to reduce the influence of illumination
    effects. In practice we use gamma (power law) compression, either
    computing the square root or the log of each colour channel.
    Image texture strength is typically proportional to the local surface
    illumination so this compression helps to reduce the effects of local
    shadowing and illumination variations.
    """

    if flow.ndim < 3:
        raise ValueError("Requires dense flow in both directions")

    if normalise:
        flow = sqrt(flow)

    """ 
    -2-
    The second stage computes first order image gradients. These capture
    contour, silhouette and some texture information, while providing
    further resistance to illumination variations. The locally dominant
    colour channel is used, which provides colour invariance to a large
    extent. Variant methods may also include second order image derivatives,
    which act as primitive bar detectors - a useful feature for capturing,
    e.g. bar like structures in bicycles and limbs in humans.
    """

    if flow.dtype.kind == 'u':
        # convert uint image to float
        # to avoid problems with subtracting unsigned numbers in np.diff()
        flow = flow.astype('float')

    gx = np.zeros(flow.shape[:2])
    gy = np.zeros(flow.shape[:2])
    # gx[:, :-1] = np.diff(flow[:,:,1], n=1, axis=1)
    # gy[:-1, :] = np.diff(flow[:,:,0], n=1, axis=0)

    gx = flow[:,:,1]
    gy = flow[:,:,0]
    print(gx.shape)



    """ 
    -3-
    The third stage aims to produce an encoding that is sensitive to
    local image content while remaining resistant to small changes in
    pose or appearance. The adopted method pools gradient orientation
    information locally in the same way as the SIFT [Lowe 2004]
    feature. The image window is divided into small spatial regions,
    called "cells". For each cell we accumulate a local 1-D histogram
    of gradient or edge orientations over all the pixels in the
    cell. This combined cell-level 1-D histogram forms the basic
    "orientation histogram" representation. Each orientation histogram
    divides the gradient angle range into a fixed number of
    predetermined bins. The gradient magnitudes of the pixels in the
    cell are used to vote into the orientation histogram.
    """

    magnitude = np.sqrt(gx**2 + gy**2)
    orientation = np.arctan2(gy, gx) * (180 / np.pi) % 180

    sy, sx = flow.shape[:2]
    cx, cy = pixels_per_cell
    bx, by = cells_per_block

    n_cellsx = int(np.floor(sx // cx))  # number of cells in x
    n_cellsy = int(np.floor(sy // cy))  # number of cells in y

    # compute orientations integral images
    orientation_histogram = np.zeros((n_cellsy, n_cellsx, orientations))
    subsample = np.index_exp[cy // 2:cy * n_cellsy:cy, cx // 2:cx * n_cellsx:cx]
    for i in range(orientations-1):
        #create new integral image for this orientation
        # isolate orientations in this range

        temp_ori = np.where(orientation < 180 / orientations * (i + 1),
                            orientation, -1)
        temp_ori = np.where(orientation >= 180 / orientations * i,
                            temp_ori, -1)
        # select magnitudes for those orientations
        cond2 = (temp_ori > -1) * (magnitude > motion_threshold)
        temp_mag = np.where(cond2, magnitude, 0)

        temp_filt = uniform_filter(temp_mag, size=(cy, cx))
        print(subsample,"subsample ---")
        orientation_histogram[:, :, i] = temp_filt[subsample]

    ''' Calculate the no-motion bin '''
    temp_mag = np.where(magnitude <= motion_threshold, magnitude, 0)

    temp_filt = uniform_filter(temp_mag, size=(cy, cx))
    orientation_histogram[:, :, -1] = temp_filt[subsample]

    # now for each cell, compute the histogram
    hof_image = None

    if visualise:
        

        radius = min(cx, cy) // 2 - 1
        hof_image = np.zeros((sy, sx), dtype=float)
        for x in range(n_cellsx):
            for y in range(n_cellsy):
                for o in range(orientations-1):
                    centre = tuple([y * cy + cy // 2, x * cx + cx // 2])
                    dx = int(radius * np.cos(float(o) / orientations * np.pi))
                    dy = int(radius * np.sin(float(o) / orientations * np.pi))
                    rr, cc = draw.line(centre[0] - dy, centre[1] - dx,
                                            centre[0] + dy, centre[1] + dx)
                    hof_image[rr, cc] += orientation_histogram[y, x, o]

    """
    The fourth stage computes normalisation, which takes local groups of
    cells and contrast normalises their overall responses before passing
    to next stage. Normalisation introduces better invariance to illumination,
    shadowing, and edge contrast. It is performed by accumulating a measure
    of local histogram "energy" over local groups of cells that we call
    "blocks". The result is used to normalise each cell in the block.
    Typically each individual cell is shared between several blocks, but
    its normalisations are block dependent and thus different. The cell
    thus appears several times in the final output vector with different
    normalisations. This may seem redundant but it improves the performance.
    We refer to the normalised block descriptors as Histogram of Oriented
    Gradient (hog) descriptors.
    """

    n_blocksx = (n_cellsx - bx) + 1
    n_blocksy = (n_cellsy - by) + 1
    normalised_blocks = np.zeros((n_blocksy, n_blocksx,
                                  by, bx, orientations))

    for x in range(n_blocksx):
        for y in range(n_blocksy):
            block = orientation_histogram[y:y+by, x:x+bx, :]
            eps = 1e-5
            normalised_blocks[y, x, :] = block / sqrt(block.sum()**2 + eps)

    """
    The final step collects the hof descriptors from all blocks of a dense
    overlapping grid of blocks covering the detection window into a combined
    feature vector for use in the window classifier.
    """

    if visualise:
        return orientation_histogram.ravel(), hof_image
    else:
        return orientation_histogram.ravel()

vector,image = hof(flow, orientations=9, pixels_per_cell=(20, 20),
        cells_per_block=(4, 4), visualise=True, normalise=False, motion_threshold=0.0)

print(vector)
print(image)
print(vector.shape,flow.shape,20*4)
# print(list(vector))
cv2.imwrite("hof_image_fire.png",image*255)
# def plot_quiver(plt,ax, flow, spacing, margin=0, **kwargs):
#     """Plots less dense quiver field.

#     Args:
#         ax: Matplotlib axis
#         flow: motion vectors
#         spacing: space (px) between each arrow in grid
#         margin: width (px) of enclosing region without arrows
#         kwargs: quiver kwargs (default: angles="xy", scale_units="xy")
#     """
#     h, w, *_ = flow.shape

#     nx = int((w - 2 * margin) / spacing)
#     ny = int((h - 2 * margin) / spacing)

#     x = np.linspace(margin, w - margin - 1, nx, dtype=np.int64)
#     y = np.linspace(margin, h - margin - 1, ny, dtype=np.int64)

#     flow = flow[np.ix_(y, x)]
#     u = flow[:, :, 0]
#     v = flow[:, :, 1]

#     kwargs = {**dict(angles="xy", scale_units="xy"), **kwargs}
#     ax.quiver(x, y, u, v, **kwargs)

#     ax.set_ylim(sorted(ax.get_ylim(), reverse=True))
#     ax.set_aspect("equal")
#     plt.show()

# # flow = cv2.calcOpticalFlowFarneback(
# #     img1, img2, None, 0.5, 3, 15, 3, 5, 1.2, 0
# # )
# print(flow.shape)
# fig, ax = plt.subplots()
# # # plot_quiver(plt,ax, flow, spacing=10, scale=1, color="#ff44ff")
# # # plt.show()
# margin = 0
# spacing = 1
# scale = 1 
# color = "#ff44ff"
# # h, w, *_ = flow.shape
# h,w = 512,512
# nx = int((w - 2 * margin) / spacing)
# ny = int((h - 2 * margin) / spacing)

# x = np.linspace(margin, w - margin - 1, nx, dtype=np.int64)
# y = np.linspace(margin, h - margin - 1, ny, dtype=np.int64)

# # # flow = flow[np.ix_(y, x)]
# # # u = flow[:, :, 0]
# # # v = flow[:, :, 1]
# u = u[np.ix_(y,x)]
# v = v[np.ix_(y,x)]

# print(u.shape,v.shape)
# kwargs = {**dict(angles="xy", scale_units="xy")}
# ax.quiver(x, y, u, v, **kwargs)

# ax.set_ylim(sorted(ax.get_ylim(), reverse=True))
# ax.set_aspect("equal")
# plt.show()