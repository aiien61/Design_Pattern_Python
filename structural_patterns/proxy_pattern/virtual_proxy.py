class Bitmap:
    def __init__(self, filename: str):
        self.filename = filename
        print(f'Loading image from {self.filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')


class LazyBitmap:
    def __init__(self, filename: str):
        self.filename = filename
        self.bitmap = None

    def draw(self):
        if not self.bitmap:
            self.bitmap = Bitmap(self.filename)
        self.bitmap.draw()


def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')
    print('-------')


class TestDrive:
    @staticmethod
    def standard_image_drawing(*args, **kwargs):
        bmp = Bitmap('kitty.jpg')
        draw_image(bmp)

    @staticmethod
    def instantiate_but_unnecessary_loading(*args, **kwargs):
        bmp = Bitmap('kitty.jpg')

    @staticmethod
    def proxy_to_prevent_unnecessary_loading(*args, **kwargs):
        bmp = LazyBitmap('kitty.jpg')
        draw_image(bmp)
    
    @staticmethod
    def proxy_to_cache_when_multiple_drawing_same_image(*args, **kwargs):
        bmp = LazyBitmap('kitty.jpg')
        draw_image(bmp)
        draw_image(bmp)

if __name__ == '__main__':
    # TestDrive.standard_image_drawing()
    
    # loading should be avoided
    # TestDrive.instantiate_but_unnecessary_loading()

    # TestDrive.proxy_to_prevent_unnecessary_loading()
    
    # only loading once
    TestDrive.proxy_to_cache_when_multiple_drawing_same_image()
