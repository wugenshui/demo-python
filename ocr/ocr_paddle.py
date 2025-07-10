from paddleocr import PaddleOCR
from PIL import Image
import numpy as np

def ocr_with_paddleocr(image_input, lang='ch'):
    """
    使用PaddleOCR进行OCR识别
    
    参数:
        image_input: 图片路径、PIL Image对象或numpy数组
        lang: 语言 (默认中文 'ch', 英文 'en')
    
    返回:
        识别出的文本
    """
    try:
        # 初始化OCR模型
        ocr = PaddleOCR(use_angle_cls=True, lang=lang)

        # 处理输入类型
        if isinstance(image_input, str):
            # 如果是字符串，则认为是图片路径
            result = ocr.predict(img=image_input)
        elif isinstance(image_input, np.ndarray):
            # 如果是numpy数组（OpenCV图像）
            result = ocr.predict(img=image_input)
        elif isinstance(image_input, Image.Image):
            # 如果是PIL Image对象
            img_array = np.array(image_input)
            result = ocr.predict(img=img_array)
        else:
            raise ValueError("不支持的输入类型。请输入路径(str)、numpy数组或PIL.Image")

        # 提取文本
        texts = [line[1][0] for line in result]

        return '\n'.join(texts)
    except Exception as e:
        print(f"OCR处理出错: {e}")
        return ""

# 使用示例
if __name__ == "__main__":
    image_path = "example.png"  # 替换为你的图片路径
    result = ocr_with_paddleocr(image_path)
    print("识别结果:")
    print(result)