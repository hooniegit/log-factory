import psutil

# 1초 간격으로 CPU 사용량 측정
cpu_percent = psutil.cpu_percent(interval=1)
memory_percent = psutil.virtual_memory().percent

print(f"CPU Usage: {cpu_percent}% / MEM Usage: {memory_percent}")
