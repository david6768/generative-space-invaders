from glob import glob
from PIL import Image, ImageDraw, ImageChops, ImageOps
import random
import colorsys

palete1 = ['#042940','#005C53','#9FC131','#DBF227','#D6D58E']
palete2 = ['#524A4E','#FDEFF4','#FFC0D3','#FF5C8D']
palete3 = ['#03045E','#00B4D8','#90E0EF','#CAF0F8']
palete4 = ['#D3ECA7','#A1B57D','#B33030','#19282F']
palete5 = ['#24A19C','#FAEEE7','#325288','#D96098']
palete6 = ['#FFF89A','#FFC900','#086E7D','#1A5F7A']
palete7 = ['#F5F5F5','#F05454','#DBF227','#30475E']
palete8 = ['#1A374D','#406882','#6998AB','#B1D0E0']
palete9 = ['#97BFB4','#F5EEDC','#DD4A48','#4F091D']
palete10 = ['#2E4C6D','#396EB0','#DADDFC','#FC997C']
palete11 = ['#E23E57','#88304E','#522546','#311D3F']
palete12 = ['#1B262C','#0F4C75','#3282B8','#BBE1FA']
palete13 = ['#364F6B','#3FC1C9','#F5F5F5','#FC5185']
palete14 = ['#FFB6B9','#FAE3D9','#BBDED6','#61C0BF']
palete15 = ['#F9F7F7','#DBE2EF','#3F72AF','#112D4E']
palete16 = ['#2B2E4A','#E84545','#903749','#53354A']
palete17 = ['#F67280','#C06C84','#6C5B7B','#355C7D']
palete18 = ['#F4EEFF','#DCD6F7','#A6B1E1','#424874']
palete19 = ['#A8E6CF','#DCEDC1','#FFD3B6','#FFAAA5']
palete20 = ['#FFD5CD','#EFBBCF','#C3AED6','#8675A9']

paletes = [palete1,palete2,palete3,palete4,palete5,palete6,palete7,palete8,palete9,palete10,palete11,palete12,palete13,palete14,palete15,palete16,palete17,palete18,palete19,palete20]

def generate_art():
    print("Generating art")

    # Set size parameters.
    rescale = 1
    image_size_px = int(6000 * rescale)
    # Create the directory and base image.
    bg_color = (0, 0, 0, 0)
    image = Image.new("RGBA", (image_size_px, image_size_px), bg_color)
    step_number_y = 0
    step_number_x = 0


    # Set size parameters.
    padding = int(image_size_px/random.randrange(10,15) * rescale)
    padding = 0

    # How many lines do we want to draw?
    num_lines = int(random.randrange(8, 16))
    
    palete = random.choice(paletes)
    line_color = random.choice(palete)
    palete.append('#000000')
    palete.append('#000000')
    palete.append('#000000')
    palete.append('#000000')

    #Draw Grid
    step_count = num_lines
    step_size = int((image_size_px - (padding*2)) / step_count)
    y_start = padding
    y_end = padding+step_size
    while step_count > step_number_y:
        step_number_x = 0
        x_start = padding
        x_end = padding+step_size
        while step_count > step_number_x:
            thickness = random.randrange(10,100) * rescale
            #thickness = 1
            # Draw some lines
            overdraw = random.randrange(1,100)
            overdraw = 1
            draw = ImageDraw.Draw(image, "RGBA")
            #transp = Image.new("RGBA", (image_size_px, image_size_px), (0,0,0,0))
            #draw = ImageDraw.Draw(transp, "RGBA")
            while overdraw > 0:
                black = 0
                line_color = random.choice(palete)
                if line_color == '#000000':
                    black += 1
                if black > step_count/4:
                    palete.remove('#000000')
                point1 = (x_start, y_start)
                point2 = (x_end, y_end)
                line = (point1, point2)
                draw.rectangle(line, fill=line_color, outline=line_color)
                overdraw -= 1
            x_start += step_size
            x_end += step_size
            step_number_x +=1
        y_start += step_size
        y_end += step_size
        step_number_y +=1

    #delete half
    point1 = (0, 0)
    point2 = ((image_size_px/2)-1, image_size_px)
    line = (point1, point2)
    draw.rectangle(line, fill=(0, 0, 0, 0), outline=(0, 0, 0, 0))

    # Image is done! Now resize it to be smooth.
    image = image.resize(
        (image_size_px // rescale, image_size_px // rescale), resample=Image.ANTIALIAS
    )

    # Flip
    mirrored = ImageOps.mirror(image)
    image.paste(Image.alpha_composite(image,mirrored))

    # Save the image.
    image.save(str(number)+'.png')

number = 0

while number >= 0:

    overdraw = random.randrange(1,50)

    generate_art()

    number += 1