from PIL import Image
import pytesseract
 
# 如果Tesseract不在系统PATH中，需要指定路径
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
 
def ocr_with_tesseract(image_path, lang='eng'):
    """
    使用Tesseract进行OCR识别
    
    参数:
        image_path: 图片路径
        lang: 语言代码 (默认英语 'eng', 中文 'chi_sim' 或 'chi_tra')
    
    返回:
        识别出的文本
    """
    try:
        # 打开图片文件
        img = Image.open(image_path)
        
        # 使用Tesseract进行OCR识别
        text = pytesseract.image_to_string(img, lang=lang)
        
        return text.strip()
    except Exception as e:
        print(f"OCR处理出错: {e}")
        return ""
 
# 使用示例
if __name__ == "__main__":
    image_path = "example.png"  # 替换为你的图片路径
    result = ocr_with_tesseract(image_path, lang='chi_sim')  # 中文简体
    print("识别结果:")
    print(result)
