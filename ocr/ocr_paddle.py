from paddleocr import PaddleOCR
 
def ocr_with_paddleocr(image_path, lang='ch'):
    """
    使用PaddleOCR进行OCR识别
    
    参数:
        image_path: 图片路径
        lang: 语言 (默认中文 'ch', 英文 'en')
    
    返回:
        识别出的文本
    """
    try:
        # 初始化OCR
        ocr = PaddleOCR(use_angle_cls=True, lang=lang)
        
        # 读取图片
        result = ocr.ocr(image_path, cls=True)
        
        # 提取文本
        texts = [line[1][0] for line in result[0]]
        
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
