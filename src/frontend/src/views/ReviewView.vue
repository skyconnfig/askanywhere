<template>
  <div class="review-container">
    <div class="review-header">
      <h2>今日复习</h2>
      <div class="review-stats">
        <span>待复习: {{ reviewItems.length }}</span>
        <span>已完成: {{ completedCount }}</span>
      </div>
    </div>

    <div class="review-list">
      <div v-for="item in reviewItems" :key="item.id" class="review-card">
        <div class="review-content">
          <div class="review-tags">
            <span v-for="tag in item.tags" :key="tag" class="tag">{{ tag }}</span>
          </div>
          <div class="content">{{ item.content }}</div>
          <div class="review-info">
            <span class="review-time">创建于: {{ item.createTime }}</span>
            <span class="review-count">复习次数: {{ item.reviewCount }}</span>
          </div>
        </div>
        <div class="review-actions">
          <button @click="markAsReviewed(item.id)" class="review-button">
            标记已复习
          </button>
          <button @click="postponeReview(item.id)" class="postpone-button">
            稍后复习
          </button>
        </div>
      </div>
    </div>

    <div v-if="reviewItems.length === 0" class="empty-state">
      <p>今天没有需要复习的内容</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReviewView',
  data() {
    return {
      reviewItems: [],
      completedCount: 0
    }
  },
  methods: {
    async loadReviewItems() {
      try {
        const response = await fetch('http://localhost:5000/api/review')
        const data = await response.json()
        this.reviewItems = data.items
      } catch (error) {
        console.error('Error loading review items:', error)
      }
    },
    async markAsReviewed(itemId) {
      try {
        const response = await fetch(`http://localhost:5000/api/review/${itemId}/complete`, {
          method: 'POST'
        })
        if (response.ok) {
          this.reviewItems = this.reviewItems.filter(item => item.id !== itemId)
          this.completedCount++
        }
      } catch (error) {
        console.error('Error marking item as reviewed:', error)
      }
    },
    async postponeReview(itemId) {
      try {
        const response = await fetch(`http://localhost:5000/api/review/${itemId}/postpone`, {
          method: 'POST'
        })
        if (response.ok) {
          this.reviewItems = this.reviewItems.filter(item => item.id !== itemId)
        }
      } catch (error) {
        console.error('Error postponing review:', error)
      }
    }
  },
  mounted() {
    this.loadReviewItems()
  }
}
</script>

<style scoped>
.review-container {
  padding: 1rem;
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.review-stats {
  display: flex;
  gap: 1rem;
}

.review-stats span {
  padding: 0.5rem 1rem;
  background-color: #f8f9fa;
  border-radius: 4px;
  font-size: 0.9rem;
}

.review-list {
  display: grid;
  gap: 1rem;
}

.review-card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  padding: 1rem;
}

.review-content {
  margin-bottom: 1rem;
}

.review-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.tag {
  background-color: #e9ecef;
  color: #495057;
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  font-size: 0.8rem;
}

.content {
  font-size: 1rem;
  line-height: 1.5;
  margin-bottom: 0.5rem;
}

.review-info {
  display: flex;
  justify-content: space-between;
  font-size: 0.8rem;
  color: #6c757d;
}

.review-actions {
  display: flex;
  gap: 1rem;
}

.review-button,
.postpone-button {
  flex: 1;
  padding: 0.5rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: background-color 0.2s;
}

.review-button {
  background-color: #28a745;
  color: white;
}

.review-button:hover {
  background-color: #218838;
}

.postpone-button {
  background-color: #6c757d;
  color: white;
}

.postpone-button:hover {
  background-color: #5a6268;
}

.empty-state {
  text-align: center;
  padding: 2rem;
  color: #6c757d;
}
</style>