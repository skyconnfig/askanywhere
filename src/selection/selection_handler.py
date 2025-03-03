from typing import Optional

class SelectionHandler:
    """划词功能的核心处理逻辑"""
    
    def __init__(self):
        self._is_active: bool = True
        self._last_selection: Optional[str] = None
    
    def handle_selection(self, selected_text: str) -> bool:
        """处理用户划词选中的文本
        
        Args:
            selected_text: 用户选中的文本内容
            
        Returns:
            bool: 处理是否成功
        """
        if not self._is_active or not selected_text:
            return False
            
        self._last_selection = selected_text
        return True
    
    def toggle_active_state(self) -> None:
        """切换划词功能的激活状态"""
        self._is_active = not self._is_active
    
    @property
    def is_active(self) -> bool:
        """获取划词功能的当前激活状态"""
        return self._is_active
    
    @property
    def last_selection(self) -> Optional[str]:
        """获取最后一次选中的文本内容"""
        return self._last_selection