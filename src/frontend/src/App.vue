<template>
  <div class="app-container">
    <header class="app-header">
      <nav>
        <router-link to="/">首页</router-link> |
        <router-link to="/notes">笔记</router-link> |
        <router-link to="/review">复习</router-link> |
        <router-link to="/jarvis">JARVIS</router-link>
      </nav>
    </header>

    <main class="app-main">
      <router-view></router-view>
    </main>

    <!-- 划词选择悬浮窗组件 -->
    <text-selection-overlay
      v-if="showSelectionOverlay"
      :selection="selectedText"
      :position="selectionPosition"
      @close="closeSelectionOverlay"
      @ask="askAI"
    />
  </div>
</template>

<script>
import TextSelectionOverlay from './components/TextSelectionOverlay.vue'

export default {
  name: 'App',
  components: {
    TextSelectionOverlay
  },
  data() {
    return {
      showSelectionOverlay: false,
      selectedText: '',
      selectionPosition: { x: 0, y: 0 }
    }
  },
  mounted() {
    document.addEventListener('mouseup', this.handleTextSelection)
  },
  beforeUnmount() {
    document.removeEventListener('mouseup', this.handleTextSelection)
  },
  methods: {
    handleTextSelection() {
      const selection = window.getSelection()
      const text = selection.toString().trim()
      
      if (text) {
        const range = selection.getRangeAt(0)
        const rect = range.getBoundingClientRect()
        
        this.selectedText = text
        this.selectionPosition = {
          x: rect.left + window.scrollX,
          y: rect.bottom + window.scrollY
        }
        this.showSelectionOverlay = true
      }
    },
    closeSelectionOverlay() {
      this.showSelectionOverlay = false
      this.selectedText = ''
    },
    async askAI(question) {
      try {
        const response = await fetch('http://localhost:5000/api/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            text: this.selectedText,
            question
          })
        })
        const data = await response.json()
        // TODO: 处理AI响应
      } catch (error) {
        console.error('Error asking AI:', error)
      }
    }
  }
}
</script>

<style>
.app-container {
  font-family: Arial, sans-serif;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.app-header {
  background-color: #f8f9fa;
  padding: 1rem;
  margin-bottom: 2rem;
}

.app-header nav {
  text-align: center;
}

.app-header nav a {
  color: #495057;
  text-decoration: none;
  margin: 0 1rem;
  padding: 0.5rem 1rem;
  border-radius: 4px;
}

.app-header nav a:hover {
  background-color: #e9ecef;
}

.app-header nav a.router-link-active {
  color: #007bff;
  font-weight: bold;
}

.app-main {
  min-height: calc(100vh - 200px);
  padding: 1rem;
}
</style>