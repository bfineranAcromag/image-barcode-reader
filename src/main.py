from BarcodeReader import BarcodeReader

def main():
    bc = BarcodeReader.BarcodeReader("./test_images/p/pbarcode1.jpg", 7)
    print(bc.readBarcodeString())

if __name__ == '__main__':
    main()