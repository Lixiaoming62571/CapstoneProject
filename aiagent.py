from flask import Flask, render_template, request, jsonify

# 初始化 Flask 应用
app = Flask(__name__)

# 【场景1】后端渲染 HTML 页面（直接返回整个页面）
@app.route('/')  # 访问根路径（http://localhost:5000）时触发
def index():
    # 渲染 templates 文件夹下的 index.html（需提前创建 templates 目录）
    return render_template('index.html', name="用户")  # 可传参数给 HTML

# 【场景2】后端接收前端请求（AJAX/表单），返回数据（JSON）
@app.route('/api/handle', methods=['POST'])  # 仅接收 POST 请求
def handle_data():
    # 1. 获取前端传参（两种方式）
    # 方式A：表单提交（form-data）
    # username = request.form.get('username')
    # 方式B：AJAX/JSON 传参
    data = request.get_json()  # 获取 JSON 数据
    username = data.get('user_text')
    
    # 2. 后端处理逻辑（示例：拼接字符串）
    result = f"你好，{username}！后端已收到你的请求"
    
    # 3. 返回 JSON 数据给前端
    return jsonify({"code": 200, "msg": result})

if __name__ == '__main__':
    app.run(debug=True)  # 启动服务，debug=True 调试模式（修改代码自动重启）