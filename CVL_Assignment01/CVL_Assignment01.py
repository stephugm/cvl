import cv2
import numpy as np

def histogram_equalization(img):
  height, width = img.shape
  total_pixels = height * width

  histogram = [0] * 256
  for i in range(height):
      for j in range(width):
          pixel_value = img[i, j]
          histogram[pixel_value] += 1
  
  cdf = [0] * 256
  cdf[0] = histogram[0]
  for i in range(1, 256):
      cdf[i] = cdf[i - 1] + histogram[i]
  
  cdf_min = next((val for val in cdf if val > 0), 0)

  equalized_map = [0] * 256
  for i in range(256):
      equalized_map[i] = round(((cdf[i] - cdf_min) / (total_pixels - cdf_min)) * 255)

  equalized_img = np.zeros_like(img, dtype=np.uint8)
  for i in range(height):
      for j in range(width):
          old_value = img[i, j]
          equalized_img[i, j] = equalized_map[old_value]
  
  return equalized_img

if __name__ == '__main__':
    input_file = 'dark_image.jpg'
    output_file = 'enhanced_dark_image.jpg'
    img = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print(f"Error: Could not load image from {input_file}")
        exit()

    enhanced_img = histogram_equalization(img)
    
    cv2.imwrite(output_file, enhanced_img)
    print(f"Enhanced image saved to {output_file}")
    
    cv2.imshow('Original Image', img)
    cv2.imshow('Enhanced Image', enhanced_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
