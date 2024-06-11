from BarcodeReader import BarcodeRead

def main():
    bc = BarcodeRead("./test_images/plain_barcodes/barcode1.png")
    print(bc.readBarcodeString())

if __name__ == '__main__':
    main()