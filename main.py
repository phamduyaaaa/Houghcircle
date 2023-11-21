import cv2
import numpy as np

# Read image.
img = cv2.imread("R.png")
# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (8, 8))

# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred,
				cv2.HOUGH_GRADIENT, 1, 20, param1 = 100,
			param2 = 30, minRadius = 1, maxRadius = 100)

# Điều kiện
if detected_circles is not None:

	# Convert
	detected_circles = np.uint16(np.around(detected_circles))

	for pt in detected_circles[0, :]:
		a, b, r = pt[0], pt[1], pt[2]

		# Vẽ hình tròn bao quanh xác định được
		cv2.circle(img, (a, b), r, (0, 255, 0), 2)

		# Vẽ Tâm hình tròn
		cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
		cv2.imshow("Detected Circle", img)
		cv2.waitKey(0)

