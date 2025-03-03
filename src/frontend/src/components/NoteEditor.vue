<template>
  <div class="note-editor">
    <div class="editor-container">
      <textarea
        v-model="noteContent"
        placeholder="输入笔记内容，使用 #标签 来添加标签"
        @input="handleInput"
      ></textarea>
    </div>
    <div class="tags-container" v-if="tags.length > 0">
      <span class="tag" v-for="tag in tags" :key="tag">
        {{ tag }}
      </span>
    </div>
    <div class="button-container">
      <button @click="saveNote" :disabled="!noteContent.trim()">保存笔记</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NoteEditor',
  data() {
    return {
      noteContent: '',
      tags: []
    }
  },
  methods: {
    handleInput() {
      // 提取标签
      this.tags = (this.noteContent.match(/#\w+/g) || []).map(tag => tag.slice(1))
    },
    async saveNote() {
      try {
        const response = await fetch('http://localhost:5000/api/notes', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            content: this.noteContent,
            tags: this.tags.map(tag => '#' + tag)
          })
        })

        const data = await response.json()
        if (data.status === 'success') {
          this.$emit('note-saved', data.note)
          this.noteContent = ''
          this.tags = []
        } else {
          console.error('保存笔记失败:', data.error)
        }
      } catch (error) {
        console.error('保存笔记时发生错误:', error)
      }
    }
  }
}
</script>

<style scoped>
.note-editor {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.editor-container {
  margin-bottom: 15px;
}

textarea {
  width: 100%;
  min-height: 150px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  resize: vertical;
}

.tags-container {
  margin-bottom: 15px;
}

.tag {
  display: inline-block;
  padding: 4px 8px;
  margin-right: 8px;
  margin-bottom: 8px;
  background-color: #e1f5fe;
  color: #0288d1;
  border-radius: 4px;
  font-size: 14px;
}

button {
  padding: 8px 16px;
  background-color: #2196f3;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

button:hover:not(:disabled) {
  background-color: #1976d2;
}
</style>