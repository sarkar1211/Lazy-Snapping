# Lazy-Snapping

Basic Algorithm Graph Cut:
The algorithm for lazy snapping is implemented using (1) extraction of seed pixels, (2) K-means clustering and
(3) Probability calculation. It takes the main image, stroke image and k value as input and displays foreground
and background extraction of image by implementing the following functions: -
- Seed Pixel extraction: Each pixel of stroke is traversed to check if it belongs to red or blue pixels, and
placed in separate arrays
- K means Clustering: In this clustering technique, centroids and indices are assigned randomly. They
are updated by taking average of seed pixels for each index of centroids. The computation is done
iteratively until old and new centroids become equal or total iteration exceeds 200.
- Calculation of probability: In this function, the likelihood of the pixels with respect to foreground
and background region is calculated and a binary image is formed with 1 for higher probability of
belonging to foreground pixel and 0 for background pixel

# Results

![Results]()