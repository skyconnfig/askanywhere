from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from notes.note_manager import NoteManager
from api_llm import ApiLLM

app = Flask(__name__)
CORS(app)

# 配置
app.config['SECRET_KEY'] = os.urandom(24)
note_manager = NoteManager()

# 路由
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

# AI交互路由
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        text = data.get('text')
        context = data.get('context', [])
        
        # 调用ApiLLM处理用户查询
        ApiLLM.handle_user_query(text, context=context, question=None, callback=None)
        
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 笔记管理路由
@app.route('/api/notes', methods=['GET', 'POST'])
def manage_notes():
    if request.method == 'POST':
        try:
            data = request.get_json()
            content = data.get('content')
            tags = data.get('tags', [])
            
            note = note_manager.create_note(content, tags)
            if note:
                return jsonify({'status': 'success', 'note': note})
            return jsonify({'error': '创建笔记失败'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        try:
            tags = request.args.getlist('tags[]')
            combine_type = request.args.get('combine_type', 'OR')
            
            if tags:
                notes = note_manager.get_notes_by_tags(tags, combine_type)
            else:
                notes = []
            return jsonify({'notes': notes})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

# 标签管理路由
@app.route('/api/tags', methods=['GET'])
def get_tags():
    try:
        tags = note_manager.get_all_tags()
        return jsonify({'tags': tags})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 复习提醒路由
@app.route('/api/review', methods=['GET'])
def get_review_items():
    # TODO: 实现复习项目获取逻辑
    return jsonify({'items': []})

if __name__ == '__main__':
    app.run(debug=True)