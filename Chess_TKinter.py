import tkinter as tk

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("بـــازی شــطــرنـــــج")

# اندازه خانه‌ها و تخته شطرنج
square_size = 80
board_color_1 = "#DDB88C"  # رنگ کرم
board_color_2 = "#A66D4F"  # رنگ قهوه‌ای

# موقعیت مهره‌ها
initial_pieces = {
    "rook": [(0, 0), (0, 7), (7, 0), (7, 7)],
    "knight": [(0, 1), (0, 6), (7, 1), (7, 6)],
    "bishop": [(0, 2), (0, 5), (7, 2), (7, 5)],
    "queen": [(0, 3), (7, 3)],
    "king": [(0, 4), (7, 4)],
    "pawn": [(1, i) for i in range(8)] + [(6, i) for i in range(8)]
}

# نوع مهره و رنگ آن
piece_colors = {
    "rook": "♖",
    "knight": "♘",
    "bishop": "♗",
    "queen": "♕",
    "king": "♔",
    "pawn": "♙"
}

# ایجاد صفحه شطرنج
canvas = tk.Canvas(root, width=8 * square_size, height=8 * square_size)
canvas.pack()

# رسم خانه‌های تخته
for row in range(8):
    for col in range(8):
        color = board_color_1 if (row + col) % 2 == 0 else board_color_2
        canvas.create_rectangle(
            col * square_size, row * square_size,
            (col + 1) * square_size, (row + 1) * square_size,
            fill=color
        )

# تابع برای رسم مهره‌ها
pieces = {}
def draw_piece(piece, row, col, color):
    text_color = "white" if color == "black" else "black"
    piece_id = canvas.create_oval(
        col * square_size + 10, row * square_size + 10,
        (col + 1) * square_size - 10, (row + 1) * square_size - 10,
        fill=color
    )
    canvas.create_text(
        col * square_size + square_size / 2,
        row * square_size + square_size / 2,
        text=piece_colors[piece],
        fill=text_color,
        font=("Arial", 24, "bold")
    )
    pieces[(row, col)] = (piece, piece_id, color)

# قرار دادن مهره‌ها در جای اولیه
for piece, positions in initial_pieces.items():
    for pos in positions:
        row, col = pos
        color = "black" if row < 2 else "white"
        draw_piece(piece, row, col, color)

# تابع برای انتخاب و حرکت مهره‌ها
selected_piece = None
def on_square_click(event):
    global selected_piece

    col = event.x // square_size
    row = event.y // square_size
    position = (row, col)

    # اگر مهره‌ای قبلاً انتخاب شده باشد
    if selected_piece:
        piece, piece_id, color = selected_piece
        canvas.delete(piece_id)
        del pieces[selected_piece[1]]
        draw_piece(piece, row, col, color)
        selected_piece = None
    # اگر مهره‌ای در این خانه وجود دارد، آن را انتخاب کن
    elif position in pieces:
        selected_piece = (pieces[position], position)

# اتصال کلیک به تابع
canvas.bind("<Button-1>", on_square_click)

# اجرای برنامه
root.mainloop()