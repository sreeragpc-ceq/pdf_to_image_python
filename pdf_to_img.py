from pdf2image import convert_from_bytes

#converting pdf to PIL object
images = convert_from_bytes(open('sample.pdf', 'rb').read())

# images.save('output.png', 'PNG')
for i, image in enumerate(images):
    image.save(f'page_{i+1}.jpg', 'JPEG')