# Training Tesseract With Bender Font

This project's goal is to generate training data for [Tesseract](https://github.com/tesseract-ocr/tesseract) using the font Bender [./fonts/Bender](fonts/Bender)

## Generate gt.txt and TIFF images from input.txt

First run `pip install -r requirements.txt`, and then run `python3 main.py`. 
This will generate the .gt.txt and .tiff images in the [data](./data) folder

## Train Tesseract

[tesstrain](https://github.com/tesseract-ocr/tesstrain/)
TODO