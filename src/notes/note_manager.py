from typing import List, Dict, Optional
from ..storage.database import Database
from datetime import datetime

class NoteManager:
    def __init__(self):
        self.db = Database()

    def create_note(self, content: str, tags: List[str] = None) -> Optional[Dict]:
        try:
            # 创建笔记
            result = self.db.execute_procedure('CreateNote', (content, None))
            if not result:
                return None
            
            note_id = result[0]['note_id']
            
            # 处理标签
            if tags:
                for tag in tags:
                    tag = tag.strip('#') if tag.startswith('#') else tag
                    self.db.execute_procedure('AddNoteTag', (note_id, tag))
            
            self.db.commit()
            return self.get_note(note_id)
            
        except Exception as e:
            print(f"创建笔记失败: {str(e)}")
            self.db.rollback()
            return None

    def get_note(self, note_id: int) -> Optional[Dict]:
        try:
            result = self.db.execute_query(
                "SELECT n.*, STRING_AGG(t.tag_name, ',') as tags "
                "FROM notes n "
                "LEFT JOIN note_tags nt ON n.note_id = nt.note_id "
                "LEFT JOIN tags t ON nt.tag_id = t.tag_id "
                "WHERE n.note_id = ? AND n.is_deleted = 0 "
                "GROUP BY n.note_id, n.content, n.vector_embedding, n.created_at, n.updated_at, n.is_deleted",
                (note_id,)
            )
            return result[0] if result else None
        except Exception as e:
            print(f"获取笔记失败: {str(e)}")
            return None

    def get_notes_by_tags(self, tags: List[str], combine_type: str = 'OR') -> List[Dict]:
        try:
            tags_str = ','.join(tag.strip('#') if tag.startswith('#') else tag for tag in tags)
            result = self.db.execute_procedure('GetNotesByTags', (tags_str, combine_type))
            return result if result else []
        except Exception as e:
            print(f"按标签获取笔记失败: {str(e)}")
            return []

    def delete_note(self, note_id: int) -> bool:
        try:
            result = self.db.execute_procedure('SoftDeleteNote', (note_id,))
            if result and result[0]['affected_rows'] > 0:
                self.db.commit()
                return True
            return False
        except Exception as e:
            print(f"删除笔记失败: {str(e)}")
            self.db.rollback()
            return False

    def get_all_tags(self) -> List[Dict]:
        try:
            result = self.db.execute_procedure('GetAllTags')
            return result if result else []
        except Exception as e:
            print(f"获取所有标签失败: {str(e)}")
            return []