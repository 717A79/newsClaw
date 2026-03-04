#!/usr/bin/env python3
"""
newsClaw - 时间显示页面
简单的 Flask 应用，显示当前时间
"""

from flask import Flask, render_template_string
from datetime import datetime
import pytz

app = Flask(__name__)

# HTML 模板
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>newsClaw - 当前时间</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #ffffff;
        }
        
        .container {
            text-align: center;
            padding: 40px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }
        
        h1 {
            font-size: 48px;
            margin-bottom: 20px;
            text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }
        
        .time {
            font-size: 72px;
            font-weight: 700;
            margin: 20px 0;
            text-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        }
        
        .date {
            font-size: 24px;
            opacity: 0.9;
            margin-bottom: 30px;
        }
        
        .timezone {
            font-size: 16px;
            opacity: 0.7;
        }
        
        .footer {
            margin-top: 40px;
            font-size: 14px;
            opacity: 0.6;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🦞 newsClaw</h1>
        <div class="time">{{ time }}</div>
        <div class="date">{{ date }}</div>
        <div class="timezone">时区：{{ timezone }}</div>
        <div class="footer">
            <p>自动刷新 · 每秒更新</p>
        </div>
    </div>
    
    <script>
        // 每秒自动刷新
        setInterval(() => {
            location.reload();
        }, 1000);
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """显示当前时间页面"""
    tz = pytz.timezone('Asia/Shanghai')
    now = datetime.now(tz)
    
    return render_template_string(HTML_TEMPLATE,
        time=now.strftime('%H:%M:%S'),
        date=now.strftime('%Y年%m月%d日 %A'),
        timezone='Asia/Shanghai (UTC+8)'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
