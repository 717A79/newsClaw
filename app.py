#!/usr/bin/env python3
"""
newsClaw - 时间显示和随机数生成
简单的 Flask 应用
"""

from flask import Flask, render_template_string
from datetime import datetime
import pytz
import random

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
        
        .nav {
            margin-top: 30px;
        }
        
        .nav a {
            display: inline-block;
            margin: 0 10px;
            padding: 10px 20px;
            background: rgba(255, 255, 255, 0.2);
            color: #ffffff;
            text-decoration: none;
            border-radius: 25px;
            transition: all 0.3s;
        }
        
        .nav a:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
        }
        
        .random-number {
            font-size: 96px;
            font-weight: 700;
            margin: 30px 0;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: none;
        }
        
        .range {
            font-size: 18px;
            opacity: 0.8;
            margin-bottom: 20px;
        }
        
        .refresh-btn {
            display: inline-block;
            margin-top: 20px;
            padding: 15px 40px;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: #ffffff;
            text-decoration: none;
            border-radius: 30px;
            font-weight: 600;
            transition: all 0.3s;
            box-shadow: 0 10px 30px rgba(245, 87, 108, 0.4);
        }
        
        .refresh-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(245, 87, 108, 0.5);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🦞 newsClaw</h1>
        <div class="time">{{ time }}</div>
        <div class="date">{{ date }}</div>
        <div class="timezone">时区：{{ timezone }}</div>
        <div class="nav">
            <a href="/">⏰ 时间</a>
            <a href="/random">🎲 随机数</a>
        </div>
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

# 随机数页面 HTML 模板
RANDOM_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>newsClaw - 随机数生成器</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
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
        
        .random-number {
            font-size: 96px;
            font-weight: 700;
            margin: 30px 0;
            text-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        }
        
        .range {
            font-size: 18px;
            opacity: 0.9;
            margin-bottom: 20px;
        }
        
        .nav {
            margin-top: 30px;
        }
        
        .nav a {
            display: inline-block;
            margin: 0 10px;
            padding: 10px 20px;
            background: rgba(255, 255, 255, 0.2);
            color: #ffffff;
            text-decoration: none;
            border-radius: 25px;
            transition: all 0.3s;
        }
        
        .nav a:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
        }
        
        .refresh-btn {
            display: inline-block;
            margin-top: 20px;
            padding: 15px 40px;
            background: rgba(255, 255, 255, 0.3);
            color: #ffffff;
            text-decoration: none;
            border-radius: 30px;
            font-weight: 600;
            transition: all 0.3s;
        }
        
        .refresh-btn:hover {
            background: rgba(255, 255, 255, 0.4);
            transform: translateY(-3px);
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
        <h1>🎲 随机数生成器</h1>
        <div class="range">范围：{{ min_val }} - {{ max_val }}</div>
        <div class="random-number">{{ random_num }}</div>
        <a href="/random" class="refresh-btn">🔄 生成新的随机数</a>
        <div class="nav">
            <a href="/">⏰ 时间</a>
            <a href="/random">🎲 随机数</a>
        </div>
        <div class="footer">
            <p>点击按钮或刷新页面生成新随机数</p>
        </div>
    </div>
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

@app.route('/random')
def random_number():
    """显示随机数页面"""
    min_val = 1
    max_val = 1000
    random_num = random.randint(min_val, max_val)
    
    return render_template_string(RANDOM_TEMPLATE,
        random_num=random_num,
        min_val=min_val,
        max_val=max_val
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
