import os
import shutil

# Настройки
LOG_DIR = "/var/log"
# Порог свободного места в процентах (например, удалять логи, если свободно меньше 15%)
THRESHOLD_PERCENT = 15
# Или порог в гигабайтах (например, если свободно меньше 5 ГБ)
THRESHOLD_GB = 5


def check_disk_space(path):
  """Возвращает кортеж: (всего ГБ, свободно ГБ, процент свободного места)."""
  total, used, free = shutil.disk_usage(path)

  total_gb = total / (2**30)
  free_gb = free / (2**30)
  free_percent = (free / total) * 100

  return total_gb, free_gb, free_percent


def clean_logs(log_dir):
  """Удаляет лог-файлы из указанной директории."""
  if not os.path.exists(log_dir):
    print(f"Директория {log_dir} не найдена.")
    return

  print(f"Начинаю очистку логов в {log_dir}...")

  for root, dirs, files in os.walk(log_dir):
    for file in files:
      # Удаляем файлы с расширением .log или сжатые логи .gz / старые с суффиксами .1, .2 и т.д.
      if file.endswith(".log") or file.endswith(".gz") or ".log." in file:
        file_path = os.path.join(root, file)
        try:
          # Пропускаем, если это не обычный файл (например, симлинк)
          if os.path.isfile(file_path):
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
            os.remove(file_path)
            print(f"Удален файл: {file_path} ({file_size_mb:.2f} MB)")
        except Exception as e:
          print(f"Не удалось удалить файл {file_path}: {e}")


def main():
  total_gb, free_gb, free_percent = check_disk_space(LOG_DIR)

  print(f"Диск с {LOG_DIR}:")
  print(f"  Всего: {total_gb:.2f} GB")
  print(f"  Свободно: {free_gb:.2f} GB ({free_percent:.1f}%)")

  # Условие срабатывания: места меньше заданного процента ИЛИ меньше заданного объема в ГБ
  if free_percent < THRESHOLD_PERCENT or free_gb < THRESHOLD_GB:
    print(
        "Внимание: Свободного места на диске мало! Запускаю очистку"
        " логов..."
    )
    clean_logs(LOG_DIR)

    # Повторная проверка после очистки
    _, new_free_gb, new_free_percent = check_disk_space(LOG_DIR)
    print(
        f"Очистка завершена. Теперь свободно: {new_free_gb:.2f} GB"
        f" ({new_free_percent:.1f}%)."
    )
  else:
    print("Места на диске достаточно. Очистка не требуется.")


if __name__ == "__main__":
  main()
