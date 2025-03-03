<template>
  <div class="jarvis-container">
    <div class="date-display">
      <h2>今日日期: {{ currentDate }}</h2>
    </div>

    <div class="stats-table">
      <table>
        <tr>
          <td>全息视频素材</td>
          <td>0（免费）</td>
        </tr>
        <tr>
          <td>总计</td>
          <td>15-25</td>
        </tr>
      </table>
    </div>

    <div class="notice-section">
      <h3>注意事项</h3>
      <ol>
        <li>透明材料选择：尽量选择高透明度、无划痕的材料，效果更好。</li>
        <li>视频质量：使用高分辨率视频，避免模糊。</li>
        <li>环境光线：在暗环境中观看，效果更佳。</li>
        <li>金字塔尺寸：根据手机屏幕大小调整金字塔尺寸，确保视频内容完全覆盖投影面。</li>
      </ol>
    </div>

    <div class="improvement-section">
      <h3>进阶改进（可选）</h3>
      <p>如果预算充许，可以尝试以下改进：</p>
      <ol>
        <li>使用LED灯带（20-30元）：在金字塔底部添加LED灯带，增强视觉效果。</li>
        <li>3D打印支架（如果有3D打印机）：制作更精确的金字塔支架。</li>
        <li>更高亮度设备：使用平板电脑或小型投影仪，提升亮度。</li>
      </ol>
    </div>

    <div class="summary">
      <p>通过以上方法，你可以在100元以内制作一个简易的全息数字人投影设备，体验全息技术的魅力！如果需要更复杂的效果，可以逐步升级硬件和内容。</p>
    </div>

    <div class="input-section">
      <div class="input-group">
        <input type="text" placeholder="聊聊吧，可再次划词..." />
        <span class="help-text">#标签 保存笔记，`help 详细了解`</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'JarvisView',
  data() {
    return {
      currentDate: '25年3月3日'
    }
  }
}
</script>

<style scoped>
.jarvis-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  border-radius: 15px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.date-display {
  text-align: center;
  margin-bottom: 20px;
}

.date-display h2 {
  color: #007bff;
  font-size: 1.5em;
}

.stats-table {
  margin-bottom: 20px;
}

.stats-table table {
  width: 100%;
  border-collapse: collapse;
}

.stats-table td {
  padding: 10px;
  border: 1px solid #ddd;
}

.notice-section,
.improvement-section {
  margin-bottom: 20px;
}

.notice-section h3,
.improvement-section h3 {
  color: #333;
  margin-bottom: 10px;
}

ol {
  padding-left: 20px;
}

li {
  margin-bottom: 8px;
  line-height: 1.5;
}

.summary {
  background-color: #f8f9fa;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 20px;
}

.input-section {
  margin-top: 20px;
}

.input-group {
  display: flex;
  align-items: center;
  gap: 10px;
  background-color: #f8f9fa;
  padding: 10px;
  border-radius: 8px;
}

.input-group input {
  flex: 1;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.help-text {
  color: #6c757d;
  font-size: 14px;
}
</style>