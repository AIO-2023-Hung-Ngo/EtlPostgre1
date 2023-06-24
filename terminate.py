import psycopg2

# Kết nối đến cơ sở dữ liệu
hostname = "localhost"
db = "sparkifydb"
usr = "postgres"
port = 5432
conn = None
cur = None
pws = "342002"
conn = psycopg2.connect(host=hostname, dbname=db, user=usr, password=pws, port=port)
# Tạo cursor
cur = conn.cursor()

# Truy vấn để lấy thông tin về các phiên đang chạy
cur.execute(
    "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = current_database()"
)

# Commit các thay đổi
conn.commit()

# Đóng cursor và kết nối
cur.close()
conn.close()
