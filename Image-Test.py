"""This application demonstrates how to perform basic operations with the
Google Cloud Vision API.
Example Usage:
python detect.py text ./resources/wakeupcat.jpg
python detect.py labels ./resources/landmark.jpg
python detect.py web ./resources/landmark.jpg
python detect.py web-uri http://wheresgus.com/dog.JPG
python detect.py web-geo ./resources/city.jpg
python detect.py faces-uri gs://your-bucket/file.jpg
python detect_pdf.py ocr-uri gs://python-docs-samples-tests/HodgeConj.pdf \
gs://BUCKET_NAME/PREFIX/
For more information, the documentation at
https://cloud.google.com/vision/docs.
"""


import io

from google.cloud import vision
from google.protobuf import json_format


# [START def_detect_document]
def detect_document(path):
    """Detects document features in an image."""
    client = vision.ImageAnnotatorClient()

    # [START migration_document_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.types.Image(content=content)
    print(image)
    response = client.document_text_detection(image=image)
    print(response)    
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:

                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

                    for symbol in word.symbols:
                        print('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))
    # [END migration_document_text_detection]
# [END def_detect_document]


if __name__ == '__main__':
   detect_document('/home/professional_ravi_singh/googleapi/Invoice-3.jpeg')