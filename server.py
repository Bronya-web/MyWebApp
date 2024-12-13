import http.server
import socketserver
import webbrowser

# 端口号
PORT = 8000

# 定义 HTTP 请求处理程序
Handler = http.server.SimpleHTTPRequestHandler

# 启动服务器
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")

    # 自动打开默认浏览器访问本地服务器
    webbrowser.open(f"http://localhost:{PORT}")

    # 开始服务
    httpd.serve_forever()
