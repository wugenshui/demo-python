from PIL import Image
import pytesseract

# 如果Tesseract不在系统PATH中，需要指定路径
pytesseract.pytesseract.tesseract_cmd = r'D:\lib\Tesseract-OCR\tesseract.exe'

def ocr_with_tesseract(image_input, lang='chi_sim'):
    """
    使用Tesseract进行OCR识别
    
    参数:
        image_input: 图片路径或PIL Image对象
        lang: 语言代码 (默认英语 'eng', 中文简体 'chi_sim' 或中文繁体 'chi_tra')
    
    返回:
        识别出的文本
    """
    try:
        # 判断输入是图片路径还是PIL Image对象
        if isinstance(image_input, str):
            # 如果是字符串，则认为是图片路径
            img = Image.open(image_input)
        elif isinstance(image_input, Image.Image):
            # 如果是PIL Image对象，则直接使用
            img = image_input
        else:
            raise ValueError("输入必须是图片路径(str)或PIL Image对象")

        # 使用Tesseract进行OCR识别
        text = pytesseract.image_to_string(img, lang=lang).strip()
        
        return text
    except Exception as e:
        print(f"OCR处理出错: {e}")
        return ""

# 使用示例
if __name__ == "__main__":
    image_path = "example.png"  # 替换为你的图片路径
    result = ocr_with_tesseract(image_path, lang='chi_sim')  # 中文简体
    print("识别结果:")
    print(result)