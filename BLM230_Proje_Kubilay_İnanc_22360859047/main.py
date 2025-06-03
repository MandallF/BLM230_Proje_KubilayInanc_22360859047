import tkinter as tk
from hamming import calculate_parity_bits, detect_and_correct

def encode_data():
    data = data_entry.get()
    if not set(data).issubset({'0', '1'}):
        result_label.config(text="Hatalı giriş! Sadece 0 ve 1 giriniz.")
        return
    encoded = calculate_parity_bits(data)
    encoded_label.config(text=f"Hamming Kodlu Veri: {encoded}")
    memory_entry.delete(0, tk.END)
    memory_entry.insert(0, encoded)

def introduce_error():
    memory = memory_entry.get()
    try:
        pos = int(error_pos_entry.get())
        if pos < 1 or pos > len(memory):
            result_label.config(text="Geçersiz bit pozisyonu!")
            return
        memory = list(memory)
        memory[pos - 1] = '1' if memory[pos - 1] == '0' else '0'
        memory = ''.join(memory)
        memory_entry.delete(0, tk.END)
        memory_entry.insert(0, memory)
    except ValueError:
        result_label.config(text="Pozisyon sayısal olmalı.")

def decode_data():
    memory = memory_entry.get()
    corrected, error_pos = detect_and_correct(memory)
    result_label.config(text=f"Düzeltilmiş Veri: {corrected}\nHata Pozisyonu: {error_pos}")

root = tk.Tk()
root.title("Hamming SEC-DED Simülatörü")

tk.Label(root, text="Giriş Verisi (0-1):").pack()
data_entry = tk.Entry(root)
data_entry.pack()

tk.Button(root, text="Veriyi Kodla", command=encode_data).pack()
encoded_label = tk.Label(root, text="")
encoded_label.pack()

tk.Label(root, text="Bellekteki Veri:").pack()
memory_entry = tk.Entry(root)
memory_entry.pack()

tk.Label(root, text="Hata Pozisyonu (1-N):").pack()
error_pos_entry = tk.Entry(root)
error_pos_entry.pack()

tk.Button(root, text="Yapay Hata Oluştur", command=introduce_error).pack()
tk.Button(root, text="Veriyi Doğrula", command=decode_data).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
