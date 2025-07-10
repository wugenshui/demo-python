from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import cv2
from ocr_paddle import ocr_with_paddleocr
from ocr_easyocr import ocr_with_easyocr
from ocr_pytesseract import ocr_with_tesseract

 
def preprocess_image(image_path):
    """
    图像预处理
    
    参数:
        image_path: 图片路径
    
    返回:
        预处理后的PIL Image对象
    """
    try:
        # 打开图片
        img = Image.open(image_path)
        
        # 转换为灰度图
        img = img.convert('L')
        
        # 增强对比度
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)
        
        # 锐化
        img = img.filter(ImageFilter.SHARPEN)
        
        # 使用OpenCV进行二值化 (可选)
        # img_cv = np.array(img)
        # _, img_cv = cv2.threshold(img_cv, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # img = Image.fromarray(img_cv)
        
        return img
    except Exception as e:
        print(f"图像预处理出错: {e}")
        return None
 
# 使用预处理后的图片进行OCR
if __name__ == "__main__":
    image_path = "example.png"
    preprocessed_img = preprocess_image(image_path)
    if preprocessed_img:
        # result = ocr_with_easyocr(preprocessed_img)
        result = ocr_with_paddleocr(preprocessed_img)
        print("预处理后识别结果:")
        print(result)
