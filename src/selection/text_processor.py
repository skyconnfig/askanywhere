from enum import Enum
from typing import Tuple

class TextIntent(Enum):
    """文本处理意图枚举"""
    TRANSLATION = "translation"
    CODE_EXPLANATION = "code_explanation"
    TEXT_CORRECTION = "text_correction"
    GENERAL_QUESTION = "general_question"

class TextProcessor:
    """文本处理和意图识别"""
    
    def __init__(self):
        self._code_indicators = [
            "def ", "class ", "import ", "from ", "return",
            "function", "var ", "const ", "let ",
            "{", "}", "[]", "()"
        ]
        
        self._translation_indicators = [
            "translate", "translation", "翻译",
            lambda text: any(ord(c) > 127 for c in text)  # 包含非ASCII字符
        ]
    
    def process_text(self, text: str) -> Tuple[str, TextIntent]:
        """处理文本并识别意图
        
        Args:
            text: 用户选中的文本
            
        Returns:
            Tuple[str, TextIntent]: 处理后的文本和识别出的意图
        """
        cleaned_text = self._clean_text(text)
        intent = self._identify_intent(cleaned_text)
        return cleaned_text, intent
    
    def _clean_text(self, text: str) -> str:
        """清理和标准化文本
        
        Args:
            text: 原始文本
            
        Returns:
            str: 清理后的文本
        """
        # 移除多余的空白字符
        text = " ".join(text.split())
        return text.strip()
    
    def _identify_intent(self, text: str) -> TextIntent:
        """识别文本意图
        
        Args:
            text: 清理后的文本
            
        Returns:
            TextIntent: 识别出的意图
        """
        # 检查是否是代码
        if any(indicator in text for indicator in self._code_indicators):
            return TextIntent.CODE_EXPLANATION
        
        # 检查是否需要翻译
        for indicator in self._translation_indicators:
            if callable(indicator):
                if indicator(text):
                    return TextIntent.TRANSLATION
            elif isinstance(indicator, str) and indicator.lower() in text.lower():
                return TextIntent.TRANSLATION
        
        # 默认为通用问题
        return TextIntent.GENERAL_QUESTION