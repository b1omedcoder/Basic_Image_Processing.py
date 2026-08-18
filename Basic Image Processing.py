import pydicom as dicom
import numpy as np
import matplotlib.pyplot as plt

file_path = r"C:\Users\zhaid\OneDrive\Pycharm Projects\DICOM\CT Data Files\stageii_colorectal_ct\StageII-Colorectal-CT-001\12095\8d622732-746b-47dd-b5b8-41b04c5bb0eb.dcm"

img_data = dicom.dcmread(file_path)

img_array = img_data.pixel_array

slope = getattr(img_data, "RescaleSlope")
intercept = getattr(img_data, "RescaleIntercept")
hounsfield_array = (img_array * slope) + intercept

def IsolateBone(hf_array):

    arr = hf_array.copy()
    for row in range(arr.shape[0]):
        for col in range(arr.shape[1]):
            hu_unit = arr[row, col]

            if (hu_unit < 2000) and (hu_unit > 300):
                 arr[row,col] = 1
            else:
                arr[row,col] = 0


    final_array = np.uint8(arr * 255)
    plt.figure(1)
    plt.imshow(final_array, cmap="gray")
    plt.title("Isolating Bone")


plt.figure(2)
plt.imshow(img_array, cmap="gray")
plt.title("Original Image")

print(IsolateBone(hounsfield_array))

plt.show()
