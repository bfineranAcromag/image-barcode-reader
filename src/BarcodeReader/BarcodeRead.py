import zxingcpp
import cv2

class BarcodeRead:
    def __init__(self, img_to_test):
        self.img_to_read = img_to_test
    
    def readBarcodeString(self):
        result = zxingcpp.read_barcodes(self.img_to_read)
        return result
