import os

from PIL import Image, ImageDraw, ImageFont

MODEL_NAME = 'eft'
DATA_DIR = "./data"
OFT_NORMAL_FONT_DIR = "./fonts/Bender/Jovanny Lemonad - Bender.otf"
OFT_ITALIC_FONT_DIR = "./fonts/Bender/Jovanny Lemonad - Bender-Italic.otf"
OFT_BOLD_FONT_DIR = "./fonts/Bender/Jovanny Lemonad - Bender-Bold.otf"


def main():
    # Load the Word document
    with open("input.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    # for each font
    for the_font, suffix in [(OFT_NORMAL_FONT_DIR, ''), (OFT_BOLD_FONT_DIR, '-bld'), (OFT_ITALIC_FONT_DIR, '-ita')]:
        font_path = the_font  # Specify the path to your fonts file
        font_size = 40  # Specify the fonts size
        font = ImageFont.truetype(font_path, font_size)
        padding = 5
        background_color = (255, 255, 255)  # White background
        text_color = (0, 0, 0)  # Black text

        from pathlib import Path
        Path(DATA_DIR).mkdir(parents=True, exist_ok=True)

        model_name = f'{MODEL_NAME}{suffix}'
        # Iterate through each paragraph in the document
        for i, line in enumerate(lines):
            # Create a new image with a white background
            image_dummy = Image.new("RGB", (1, 1))  # Dummy image to calculate text size
            draw_dummy = ImageDraw.Draw(image_dummy)
            text_bbox = draw_dummy.textbbox((0, 0), line, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]

            # Add padding to the image size
            image_width = text_width + 2 * padding
            image_height = text_height + 2 * padding

            # Create a new image with the calculated size
            image = Image.new("RGB", (image_width, image_height), background_color)
            draw = ImageDraw.Draw(image)

            # Calculate text position (centered with padding)
            text_position = (padding, 0)

            # Draw the text onto the image
            draw.text(text_position, line, font=font, fill=text_color)

            # Save the image as a TIFF file
            training_dir = f"{DATA_DIR}/{model_name}-ground-truth"

            if not os.path.exists(training_dir):
                os.makedirs(training_dir)

            filename = f"line_{i+1}"
            the_filename = f"{training_dir}/{filename}"
            image.save(f"{the_filename}.tif")
            with open(f"{the_filename}.gt.txt", "w+") as file:
                file.write(line)


        print(f"TIF images generated successfully for {model_name}.")




if __name__ == "__main__":
    main()
