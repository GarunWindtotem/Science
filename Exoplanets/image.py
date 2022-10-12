
def image_resize_append():

    from PIL import Image

    image_paths = [
        'D:\\Github\\Science\\Exoplanets\\Exoplanets_1.png', 
        'D:\\Github\\Science\\Exoplanets\\Exoplanets_2.png',
        'D:\\Github\\Science\\Exoplanets\\Exoplanets_3.png',
        'D:\\Github\\Science\\Exoplanets\\Exoplanets_4.png',
        ]


    images = [Image.open(x) for x in image_paths]
    widths, heights = zip(*(i.size for i in images))

    # resizing images
    i=0
    for im in images:
        new_width = 1920
        new_height = int(new_width / im.width * im.height)
        print(new_height)
        new_size = im.resize((new_width, new_height))
        new_size.save(image_paths[i])
        i=i+1

    # images = [Image.open(x) for x in image_paths]
    # widths, heights = zip(*(i.size for i in images))

    # max_width = max(widths)
    # total_height = sum(heights)

    # new_im = Image.new('RGB', (max_width, total_height))

    # y_offset = 0
    # for im in images:
    #     new_im.paste(im, (0, y_offset))
    #     y_offset += im.size[1] +42

    images = [Image.open(x) for x in image_paths]
    widths, heights = zip(*(i.size for i in images))

    anzahlCharts= len(image_paths)
    OffsetZwischenCharts = 10
    summeOffset = anzahlCharts * OffsetZwischenCharts

    max_width = max(widths)
    total_height = sum(heights) + summeOffset

    new_im = Image.new('RGB', (max_width, total_height))

    y_offset = 0
    for im in images:
        new_im.paste(im, (0, y_offset))
        y_offset += im.size[1] + OffsetZwischenCharts


    new_im.save('D:\\Github\\Science\\Exoplanets\\test.png')


    new_im = Image.open(r'D:\\Github\\Science\\Exoplanets\\test.png')
    im_1 = new_im.convert('RGB')
    im_1.save(r'D:\\Github\\Science\\Exoplanets\\test.pdf')
    print("fertig :)")
