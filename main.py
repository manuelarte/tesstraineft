from PIL import Image, ImageDraw, ImageFont

DATA_DIR = "data"
OFT_FONT_DIR = "./fonts/Bender/Jovanny Lemonad - Bender.otf"


def main():
    # Load the Word document
    with open("input.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    font_path = OFT_FONT_DIR  # Specify the path to your fonts file
    font_size = 40  # Specify the fonts size
    font = ImageFont.truetype(font_path, font_size)
    padding = 5
    background_color = (255, 255, 255)  # White background
    text_color = (0, 0, 0)  # Black text

    from pathlib import Path

    Path(DATA_DIR).mkdir(parents=True, exist_ok=True)
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
        filename = f"line_{i+1}"
        image.save(f"./{DATA_DIR}/{filename}.tiff")
        with open(f"./{DATA_DIR}/{filename}.gt.txt", "w+") as file:
            file.write(line)

    print("TIFF images generated successfully.")


if __name__ == "__main__":
    main()
