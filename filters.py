from PIL import ImageFilter

class Filter:
    def apply_to_pixel(self, red, green, blue):
        raise NotImplementedError

    def apply_filter(self, img):
        width, height = img.size
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                r, g, b = self.apply_filter(r, g, b)
                img.putpixel((x, y), (r, g, b))
        img.show()
        return img


class GreenFilter(Filter):
    def __init__(self, change_value = 100):
        self.change_value = change_value

    # определить метод apply_filter для изменения значения green
    def apply_to_pixel(self, red: int, green: int, blue: int) -> tuple[int, int, int]:
        green = min(255, green + self.change_value)
        return (red, green, blue)


class RedFilter(Filter):
    def __init__(self, change_value = 100):
        self.change_value = change_value

    # определить метод apply_filter для изменения значения red
    def apply_to_pixel(self, red: int, green: int, blue: int) -> tuple[int, int, int]:
        red = min(255, red + self.change_value)
        return (red, green, blue)


class BlueFilter(Filter):
    def __init__(self, change_value = 100):
        self.change_value = change_value

    # определить метод apply_filter для изменения значения blue
    def apply_to_pixel(self, red: int, green: int, blue: int) -> tuple[int, int, int]:
        blue = min(255, blue + self.change_value)
        return (red, green, blue)


class Inversion(Filter):
    # определить метод apply_filter для инверсии значений r,g,b
    def apply_to_pixel(self, red: int, green: int, blue: int) -> tuple[int, int, int]:
        return (255 - red, 255 - green, 255 - blue)


class Intensifier(Filter):
    def __init__(self, border_value: int):
        self.border_value = border_value

    # переназначение цвета на 0 и 255 в зависимости от границы
    def color_checker(self, color) -> int:
        return 0 if color <= self.border_value else 255

    def apply_to_pixel(self, red: int, green: int, blue: int) -> tuple:
        return (self.color_checker(red), self.color_checker(green), self.color_checker(blue))


class Blur(Filter):
    def apply_filter(self, img):
        im1 = img.filter(ImageFilter.BLUR)
        im1.show()
        return im1


class Contour(Filter):
    def apply_filter(self, img):
        im1 = img.filter(ImageFilter.CONTOUR)
        im1.show()
        return im1

