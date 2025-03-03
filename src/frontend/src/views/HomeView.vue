<template>
  <div class="home-container">
    <div class="chat-section">
      <div class="chat-header">
        <h2>AI对话</h2>
      </div>
      <div class="chat-messages" ref="messagesContainer">
        <div v-for="(message, index) in messages" :key="index" :class="['message', message.type]">
          <div class="message-content">{{ message.content }}</div>
          <div class="message-time">{{ message.time }}</div>
        </div>
      </div>
      <div class="chat-input">
        <textarea
          v-model="userInput"
          placeholder="输入问题或#标签 内容来记录笔记"
          @keyup.enter.ctrl="sendMessage"
        ></textarea>
        <button @click="sendMessage" class="send-button">发送</button>
      </div>
    </div>

    <div class="notes-preview">
      <h2>最近笔记</h2>
      <div class="notes-list">
        <div v-for="note in recentNotes" :key="note.id" class="note-item">
          <div class="note-tags">
            <span v-for="tag in note.tags" :key="tag" class="tag">{{ tag }}</span>
          </div>
          <div class="note-content">{{ note.content }}</div>
          <div class="note-time">{{ note.time }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      userInput: '',
      messages: [],
      recentNotes: []
    }
  },
  methods: {
    async sendMessage() {
      if (!this.userInput.trim()) return

      const now = new Date().toLocaleTimeString()
      const content = this.userInput.trim()
      this.userInput = ''

      // 检查是否是笔记（以#开头）
      if (content.startsWith('#')) {
        await this.saveNote(content)
      } else {
        // 添加用户消息
        this.messages.push({
          type: 'user',
          content,
          time: now
        })

        try {
          const response = await fetch('http://localhost:5000/api/chat', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: content })
          })
          const data = await response.json()
          
          // 添加AI响应
          this.messages.push({
            type: 'ai',
            content: data.message,
            time: new Date().toLocaleTimeString()
          })

          this.$nextTick(() => {
            this.scrollToBottom()
          })
        } catch (error) {
          console.error('Error:', error)
        }
      }
    },
    async saveNote(content) {
      try {
        const response = await fetch('http://localhost:5000/api/notes', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            content,
            tags: content.match(/#\w+/g) || []
          })
        })
        const data = await response.json()
        if (data.status === 'success') {
          this.loadRecentNotes()
        }
      } catch (error) {
        console.error('Error saving note:', error)
      }
    },
    async loadRecentNotes() {
      try {
        const response = await fetch('http://localhost:5000/api/notes')
        const data = await response.json()
        this.recentNotes = data.notes
      } catch (error) {
        console.error('Error loading notes:', error)
      }
    },
    scrollToBottom() {
      const container = this.$refs.messagesContainer
      container.scrollTop = container.scrollHeight
    }
  },
  mounted() {
    this.loadRecentNotes()
  }
}
</script>

<style scoped>
.home-container {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 20px;
  height: calc(100vh - 200px);
}

.chat-section {
  display: flex;
  flex-direction: column;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.chat-header {
  padding: 1rem;
  border-bottom: 1px solid #eee;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
}

.message {
  margin-bottom: 1rem;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  max-width: 80%;
}

.message.user {
  margin-left: auto;
  background-color: #007bff;
  color: white;
}

.message.ai {
  margin-right: auto;
  background-color: #f8f9fa;
  color: #333;
}

.message-time {
  font-size: 0.8rem;
  opacity: 0.7;
  margin-top: 0.25rem;
}

.chat-input {
  padding: 1rem;
  border-top: 1px solid #eee;
  display: flex;
  gap: 1rem;
}

.chat-input textarea {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  resize: none;
  height: 60px;
}

.send-button {
  padding: 0 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.send-button:hover {
  background-color: #0056b3;
}

.notes-preview {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  padding: 1rem;
}

.notes-list {
  overflow-y: auto;
  height: calc(100% - 40px);
}

.note-item {
  padding: 0.5rem;
  border-bottom: 1px solid #eee;
}

.note-tags {
  margin-bottom: 0.5rem;
}

.tag {
  background-color: #e9ecef;
  color: #495057;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  margin-right: 0.5rem;
  font-size: 0.8rem;
}

.note-time {
  font-size: 0.8rem;
  color: #6c757d;
  margin-top: 0.25rem;
}
</style>