import pymysql
try:
    conn = pymysql.connect(
        host='172.17.0.3',
        user='root',
        password='123456',
        database='login_db',
        port=3306,
        charset='utf8mb4'
    )
    print("连接成功!")
    conn.close()
except Exception as e:
    print(f"连接失败: {e}")