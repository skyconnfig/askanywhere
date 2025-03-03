<template>
  <div class="notes-container">
    <div class="search-section">
      <div class="search-input">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="搜索笔记内容或标签"
          @input="handleSearch"
        />
      </div>
      <div class="tag-filters" v-if="allTags.length">
        <span
          v-for="tag in allTags"
          :key="tag"
          :class="['tag', { active: selectedTags.includes(tag) }]"
          @click="toggleTag(tag)"
        >
          {{ tag }}
        </span>
      </div>
    </div>

    <div class="notes-grid">
      <div v-for="note in filteredNotes" :key="note.id" class="note-card">
        <div class="note-tags">
          <span v-for="tag in note.tags" :key="tag" class="tag">{{ tag }}</span>
        </div>
        <div class="note-content">{{ note.content }}</div>
        <div class="note-footer">
          <span class="note-time">{{ note.time }}</span>
          <button @click="deleteNote(note.id)" class="delete-button">删除</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotesView',
  data() {
    return {
      notes: [],
      searchQuery: '',
      selectedTags: [],
      allTags: []
    }
  },
  computed: {
    filteredNotes() {
      return this.notes.filter(note => {
        const matchesSearch = this.searchQuery
          ? note.content.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
            note.tags.some(tag =>
              tag.toLowerCase().includes(this.searchQuery.toLowerCase())
            )
          : true

        const matchesTags =
          this.selectedTags.length === 0 ||
          this.selectedTags.every(tag => note.tags.includes(tag))

        return matchesSearch && matchesTags
      })
    }
  },
  methods: {
    async loadNotes() {
      try {
        const response = await fetch('http://localhost:5000/api/notes')
        const data = await response.json()
        this.notes = data.notes
        this.updateAllTags()
      } catch (error) {
        console.error('Error loading notes:', error)
      }
    },
    async deleteNote(noteId) {
      if (!confirm('确定要删除这条笔记吗？')) return

      try {
        const response = await fetch(`http://localhost:5000/api/notes/${noteId}`, {
          method: 'DELETE'
        })
        if (response.ok) {
          this.notes = this.notes.filter(note => note.id !== noteId)
          this.updateAllTags()
        }
      } catch (error) {
        console.error('Error deleting note:', error)
      }
    },
    handleSearch() {
      // 防抖处理可以在这里添加
    },
    toggleTag(tag) {
      const index = this.selectedTags.indexOf(tag)
      if (index === -1) {
        this.selectedTags.push(tag)
      } else {
        this.selectedTags.splice(index, 1)
      }
    },
    updateAllTags() {
      const tagSet = new Set()
      this.notes.forEach(note => {
        note.tags.forEach(tag => tagSet.add(tag))
      })
      this.allTags = Array.from(tagSet)
    }
  },
  mounted() {
    this.loadNotes()
  }
}
</script>

<style scoped>
.notes-container {
  padding: 1rem;
}

.search-section {
  margin-bottom: 2rem;
}

.search-input input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.tag-filters {
  margin-top: 1rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  background-color: #e9ecef;
  color: #495057;
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
}

.tag.active {
  background-color: #007bff;
  color: white;
}

.notes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.note-card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  padding: 1rem;
  display: flex;
  flex-direction: column;
}

.note-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.note-content {
  flex: 1;
  font-size: 0.9rem;
  line-height: 1.5;
  margin-bottom: 1rem;
}

.note-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.note-time {
  font-size: 0.8rem;
  color: #6c757d;
}

.delete-button {
  padding: 0.25rem 0.75rem;
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.8rem;
}

.delete-button:hover {
  background-color: #c82333;
}
</style>