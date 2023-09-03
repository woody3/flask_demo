import base64
from io import BytesIO


class Convertors(object):
    @staticmethod
    def pil2base64(im):
        output_buffer = BytesIO()
        im.save(output_buffer, format="png")
        binary_data = output_buffer.getvalue()
        return base64.b64encode(binary_data)

    @staticmethod
    def base64_to_png(base64_str):
        pic_data = base64.b64decode(base64_str)
        with open("img123.png", "wb") as f:
            f.write(pic_data)
