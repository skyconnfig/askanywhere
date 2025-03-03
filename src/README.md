# 源代码目录结构说明

## 功能模块组织

### 划词功能模块 (selection/)
- selection_handler.py - 划词功能的核心处理逻辑
- floating_window.py - 悬浮窗口的UI实现
- text_processor.py - 文本处理和意图识别

### 笔记管理模块 (notes/)
- note_manager.py - 笔记的创建、存储和管理
- tag_processor.py - 标签处理和智能推荐
- note_search.py - 笔记搜索功能

### AI交互模块 (ai/)
- llm_interface.py - LLM接口封装
- chat_handler.py - 对话管理
- rag_processor.py - RAG检索增强生成
- summary_generator.py - AI总结生成器

### 复习系统模块 (review/)
- review_scheduler.py - 复习计划调度器
- forgetting_curve.py - 艾宾浩斯遗忘曲线实现
- review_reminder.py - 复习提醒系统

### 命令行功能模块 (cli/)
- command_parser.py - 命令解析器
- command_executor.py - 命令执行器
- command_help.py - 帮助信息管理

### 数据存储模块 (storage/)
- database.py - 数据库操作封装
- file_storage.py - 文件存储管理
- config_manager.py - 配置文件管理

### 系统托盘模块 (system/)
- tray_manager.py - 系统托盘管理
- app_controller.py - 应用程序控制

### 公共组件 (common/)
- utils.py - 通用工具函数
- constants.py - 常量定义
- exceptions.py - 异常类定义

## 代码迁移说明
现有的源代码文件将按照功能模块逐步迁移到对应的目录中，确保系统功能的平稳过渡和持续可用。