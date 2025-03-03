<template>
  <div
    class="selection-overlay"
    :style="{
      left: `${position.x}px`,
      top: `${position.y}px`
    }"
  >
    <div class="overlay-content">
      <div class="selected-text">{{ selection }}</div>
      <div class="action-buttons">
        <button @click="handleAskDirectly" class="action-button primary">
          直接询问
        </button>
        <div class="input-group">
          <input
            v-model="question"
            type="text"
            placeholder="输入你的问题"
            @keyup.enter="handleAskWithQuestion"
          />
          <button @click="handleAskWithQuestion" class="action-button">
            提问
          </button>
        </div>
        <button @click="$emit('close')" class="action-button close">
          关闭
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TextSelectionOverlay',
  props: {
    selection: {
      type: String,
      required: true
    },
    position: {
      type: Object,
      required: true,
      default: () => ({ x: 0, y: 0 })
    }
  },
  data() {
    return {
      question: ''
    }
  },
  methods: {
    handleAskDirectly() {
      this.$emit('ask', '')
      this.$emit('close')
    },
    handleAskWithQuestion() {
      if (this.question.trim()) {
        this.$emit('ask', this.question)
        this.question = ''
        this.$emit('close')
      }
    }
  }
}
</script>

<style scoped>
.selection-overlay {
  position: absolute;
  z-index: 1000;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.15);
  padding: 12px;
  min-width: 300px;
  max-width: 400px;
}

.overlay-content {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.selected-text {
  font-size: 14px;
  color: #333;
  padding: 8px;
  background: #f5f5f5;
  border-radius: 4px;
  max-height: 100px;
  overflow-y: auto;
}

.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.input-group {
  display: flex;
  gap: 8px;
}

.input-group input {
  flex: 1;
  padding: 6px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.action-button {
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.2s;
}

.action-button.primary {
  background-color: #007bff;
  color: white;
}

.action-button.primary:hover {
  background-color: #0056b3;
}

.action-button:not(.primary) {
  background-color: #e9ecef;
  color: #495057;
}

.action-button:not(.primary):hover {
  background-color: #dde2e6;
}

.action-button.close {
  background-color: #dc3545;
  color: white;
}

.action-button.close:hover {
  background-color: #c82333;
}
</style>