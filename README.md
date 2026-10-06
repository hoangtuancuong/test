## Cấu trúc thư mục

```
test/
├── app.py              # khởi tạo Flask app và các route
├── run.py              # file chạy chương trình
├── requirements.txt    # khai báo thư viện
├── README.md           # giới thiệu project
├── .gitignore          # các file không đưa lên Git
├── templates/
│   └── index.html      # giao diện
└── instance/           # dữ liệu cục bộ (không đưa lên Git)
```

## Cài đặt

```bash
pip install -r requirements.txt
```

## Chạy chương trình

```bash
python run.py
```

Sau đó mở trình duyệt tại http://127.0.0.1:5000
