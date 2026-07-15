# 竞争法监控项目（Competition Law Monitor）

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

一个自动化监控 **欧盟、美国、澳大利亚** 竞争法（反垄断）监管动态的项目。每天北京时间 15:00 通过飞书机器人推送更新。

## 功能特点

- **监控地区**：欧盟（EU）、美国（US）、澳大利亚（AU）
- **重点来源**：政府官网 + 官方媒体（FTC、DOJ、EUR-Lex、ACCC 等）
- **监控板块**：
  - Legislation（立法）
  - Sanctions and Suppression Actions（制裁与执法行动）
  - Research Reports & Public Opinion（研究报告与舆情）
- **事件分级**：
  - **最高级别**：直接涉及中国企业
  - **中等级别**：具有全球影响力
  - **低级别**：仅本地影响
- **每日自动推送**：飞书群机器人 + 附带原文链接
- **基于 GitHub Actions** 免费运行，无需服务器

## 项目结构
