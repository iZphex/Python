# Install all the lib needed
# create a func that collects a text and converts it to a QR code
# Save QR code as img
# run the function
import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")

url = input("Enter the URL you want a QR Code for: ")
generate_qrcode(url)
