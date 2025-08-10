import cv2

# Load the image
image = cv2.imread(&quot;image.jpg&quot;)
# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BG2GRAY)
# Apply Gaussian blur to reduce noise
blurred = cv2.GausianBlur(gray, (5, 5), 0)
# Thresholding the image (binary inverse)
_, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)
# Find contours
contours, _ = cv2.findContours(thrsh, cv2.RETR_EXTERNAL, cv2.CHIN_APPROX_SIMPLE)
# Draw bounding boxes around contours
for contour in contours:
y, w, h = cv2.boundingRect(contour)
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.putText(image, &quot;Object&quot;, (x, y - 10), cv2.FONTHERSHEYSIMPLEX, 0.5, (0, 255, 0), 1)
# Display results
cv2.imshow(&quot;Original with Bounding Boxes&quot;, image)
cv2.imshow(&quot;Threshold&quot;, thresh)
cv2.waitKey(0)
