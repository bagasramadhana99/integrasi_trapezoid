import numpy as np
import time
import tkinter as tk
from tkinter import ttk

# Definisikan fungsi f(x)
def f(x):
    return 4 / (1 + x**2)

# Implementasikan metode integrasi trapezoid
def trapezoid_integration(f, a, b, N):
    h = (b - a) / N
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, N):
        integral += f(a + i * h)
    integral *= h
    return integral

# Hitung galat RMS
def calculate_rms_error(estimated_pi, true_pi=3.14159265358979323846):
    return np.sqrt((estimated_pi - true_pi)**2)

# Fungsi untuk menguji berbagai nilai N
def test_integration(f, a, b, N_values):
    true_pi = 3.14159265358979323846
    results = []

    for N in N_values:
        start_time = time.time()
        estimated_pi = trapezoid_integration(f, a, b, N)
        end_time = time.time()
        
        error = calculate_rms_error(estimated_pi, true_pi)
        execution_time = end_time - start_time
        
        results.append((N, estimated_pi, error, execution_time))
    
    return results

# Fungsi untuk menjalankan pengujian dan menampilkan hasil di GUI
def run_integration():
    N_values = [10, 100, 1000, 10000]
    results = test_integration(f, 0, 1, N_values)

    result_text.delete("1.0", tk.END)  # Clear previous results
    for result in results:
        N, estimated_pi, error, execution_time = result
        result_text.insert(tk.END, f"N = {N}, Estimated pi = {estimated_pi}, RMS Error = {error}, Execution Time = {execution_time} seconds\n")

# Setup GUI
root = tk.Tk()
root.title("Numerical Integration with Trapezoid Method")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

run_button = ttk.Button(frame, text="Run Integration", command=run_integration)
run_button.grid(row=0, column=0, pady=10)

result_text = tk.Text(frame, width=80, height=20)
result_text.grid(row=1, column=0, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
