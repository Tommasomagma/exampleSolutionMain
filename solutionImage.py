from PIL import Image, ImageDraw, ImageFont
import os


def getSolutionImage(solutionString, savePath):

    #font_path = "fonts/PatrickHand-Regular.ttf"
    font_path = "fonts/PlaypenSans-VariableFont_wght.ttf"
    font_size = 32

    # Check if output image already exists and delete it
    output_path = f'{savePath}'
    if os.path.exists(output_path):
        os.remove(output_path)

    # Create a temporary image to measure text size
    temp_img = Image.new('RGB', (1, 1))
    temp_draw = ImageDraw.Draw(temp_img)
    font = ImageFont.truetype(font_path, font_size)
    
    # Get text dimensions
    text_bbox = temp_draw.multiline_textbbox((0, 0), solutionString, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Add padding
    padding = 40
    image_width = text_width + (2 * padding)
    image_height = text_height + (2 * padding)

    # Make dimensions equal for square image
    image_size = max(image_width, image_height)
    
    # Load and resize background image
    img = Image.open("bgImage/bgImage.png")
    img = img.resize((int(image_size), int(image_size)))
    d = ImageDraw.Draw(img)

    # Calculate center position
    x = (image_size - text_width) / 2
    y = (image_size - text_height) / 2
    
    d.multiline_text((x, y), solutionString, font=font, fill=(60, 65, 70))

    img.save(f'{savePath}')

    return savePath