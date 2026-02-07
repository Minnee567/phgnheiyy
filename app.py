html_content = """
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Shop Hoàng</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <img src="images/banner.png" alt="Banner cửa hàng">
    <h1>Chào mừng đến với Shop Hoàng</h1>
    <nav>
      <a href="#home">Trang chủ</a>
      <a href="#products">Sản phẩm</a>
      <a href="#contact">Liên hệ</a>
    </nav>
  </header>

  <section id="home">
    <h2>Giới thiệu</h2>
    <p>Shop Hoàng chuyên cung cấp sản phẩm chất lượng.</p>
  </section>

  <section id="products">
    <h2>Sản phẩm nổi bật</h2>
    <div class="product">
      <img src="ao-thun.jpg" alt="Áo thun">
      <h3>Áo thun nam</h3>
      <p>Giá: 120.000đ</p>
      <button>Mua ngay</button>
    </div>
    <div class="product">
      <img src="sach.jpg" alt="Sách">
      <h3>Sách Tin học 12</h3>
      <p>Giá: 80.000đ</p>
      <button>Mua ngay</button>
    </div>
  </section>

  <footer id="contact">
    <p>Liên hệ: hoangshop@gmail.com | 0123 456 789</p>
  </footer>

  <script>
    const buttons = document.querySelectorAll("button");
    buttons.forEach(btn => {
      btn.addEventListener("click", () => {
        alert("Cảm ơn bạn đã chọn sản phẩm!");
      });
    });
  </script>
</body>
</html>
"""

css_content = """
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

header {
  background: #2c3e50;
  color: white;
  padding: 15px;
  text-align: center;
}

header img {
  width: 100%;
  height: auto;
}

nav a {
  color: white;
  margin: 0 10px;
  text-decoration: none;
}

#products {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding: 20px;
}

.product {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 15px;
  width: 200px;
  text-align: center;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.product img {
  max-width: 100%;
  height: auto;
}

button {
  background: #27ae60;
  color: white;
  border: none;
  padding: 8px 12px;
  cursor: pointer;
  margin-top: 10px;
  border-radius: 4px;
}

button:hover {
  background: #2ecc71;
}

footer {
  background: #2c3e50;
  color: white;
  text-align: center;
  padding: 15px;
}
"""

# Tạo file index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# Tạo file style.css
with open("style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

print("Đã tạo xong index.html và style.css!")