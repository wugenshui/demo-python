import easyocr
from PIL import Image
import numpy as np

def ocr_with_easyocr(image_input, langs=['ch_sim', 'en']):
    """
    使用EasyOCR进行OCR识别
    
    参数:
        image_input: 图片路径或PIL Image对象
        langs: 语言列表 (默认中文简体和英语)
    
    返回:
        识别出的文本
    """
    try:
        # 创建reader对象，指定语言
        reader = easyocr.Reader(langs)

        if isinstance(image_input, str):
            # 如果是字符串，则认为是图片路径
            result = reader.readtext(image_input)
        elif isinstance(image_input, Image.Image):
            # 如果是PIL Image对象，则转换为numpy数组
            img_array = np.array(image_input)
            result = reader.readtext(img_array)
        else:
            raise ValueError("输入必须是图片路径(str)或PIL Image对象")

        # 提取文本
        texts = [detection[1] for detection in result]

        return '\n'.join(texts)
    except Exception as e:
        print(f"OCR处理出错: {e}")
        return ""

# 使用示例
if __name__ == "__main__":
    # 示例1：使用图片路径
    image_path = "example.png"  # 替换为你的图片路径
    result = ocr_with_easyocr(image_path)
    print("识别结果:")
    print(result)

    # 示例2：使用PIL Image对象
    from PIL import Image
    pil_image = Image.open(image_path)
    result = ocr_with_easyocr(pil_image)
    print("预处理后识别结果:")
    print(result)