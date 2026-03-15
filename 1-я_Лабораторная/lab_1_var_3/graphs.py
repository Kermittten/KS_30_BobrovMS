import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Получаем путь к директории, где находится текущий скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# Формируем полные пути к файлам
time_file = os.path.join(script_dir, 'time_results.csv')
swap_file = os.path.join(script_dir, 'swap_results.csv')
pass_file = os.path.join(script_dir, 'pass_results.csv')

# Проверяем существование файлов
print("Поиск файлов в директории:", script_dir)
print("\nПроверка наличия файлов:")
print(f"time_results.csv: {'✅ Найден' if os.path.exists(time_file) else '❌ Не найден'}")
print(f"swap_results.csv: {'✅ Найден' if os.path.exists(swap_file) else '❌ Не найден'}")
print(f"pass_results.csv: {'✅ Найден' if os.path.exists(pass_file) else '❌ Не найден'}")

# Загрузка данных
try:
    time_data = pd.read_csv(time_file)
    swap_data = pd.read_csv(swap_file)
    pass_data = pd.read_csv(pass_file)
    print("\n✅ Все файлы успешно загружены!")
except FileNotFoundError as e:
    print(f"\n❌ Ошибка загрузки файлов: {e}")
    print("\nУбедитесь, что файлы находятся в той же директории, что и скрипт:")
    print(f"  {script_dir}")
    exit(1)

# Настройка стиля графиков
plt.style.use('seaborn-v0_8-darkgrid')

# Список всех размеров массивов
all_sizes = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000]

# Функция для форматирования подписей оси X
def format_ticks(x, p):
    if x in all_sizes:
        return f'{int(x):,}'.replace(',', ' ')
    return ''

# Создаем директорию для графиков, если её нет
graphs_dir = os.path.join(script_dir, 'graphs')
os.makedirs(graphs_dir, exist_ok=True)

# График 1: Сравнение с O(n²)
plt.figure(figsize=(14, 9))
plt.plot(time_data['Size'], time_data['WorstTime'], 'ro-', 
         label='Худшее время', linewidth=2, markersize=8, markerfacecolor='white')
plt.plot(time_data['Size'], time_data['BigO'], 'b--', 
         label='O(n²)', linewidth=2, alpha=0.7)
plt.xlabel('Размер массива', fontsize=14, fontweight='bold')
plt.ylabel('Время (мс)', fontsize=14, fontweight='bold')
plt.title('Сравнение худшего времени с теоретической сложностью O(n²)', 
          fontsize=16, fontweight='bold', pad=20)
plt.legend(fontsize=12, framealpha=0.9)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xscale('log')
plt.yscale('log')

# Настройка подписей оси X - показываем все размеры
plt.xticks(all_sizes, [f'{size:,}'.replace(',', ' ') for size in all_sizes], 
           rotation=45, fontsize=10)
plt.gca().tick_params(axis='x', labelsize=10)

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, 'complexity_comparison.png'), dpi=300, bbox_inches='tight')
plt.show()

# График 2: Лучшее, среднее и худшее время
plt.figure(figsize=(14, 9))
plt.plot(time_data['Size'], time_data['BestTime'], 'g^-', 
         label='Лучшее время', linewidth=2, markersize=8, markerfacecolor='white')
plt.plot(time_data['Size'], time_data['AvgTime'], 'bs-', 
         label='Среднее время', linewidth=2, markersize=8, markerfacecolor='white')
plt.plot(time_data['Size'], time_data['WorstTime'], 'ro-', 
         label='Худшее время', linewidth=2, markersize=8, markerfacecolor='white')
plt.xlabel('Размер массива', fontsize=14, fontweight='bold')
plt.ylabel('Время (мс)', fontsize=14, fontweight='bold')
plt.title('Лучшее, среднее и худшее время сортировки вставками', 
          fontsize=16, fontweight='bold', pad=20)
plt.legend(fontsize=12, framealpha=0.9)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xscale('log')
plt.yscale('log')

# Настройка подписей оси X - показываем все размеры
plt.xticks(all_sizes, [f'{size:,}'.replace(',', ' ') for size in all_sizes], 
           rotation=45, fontsize=10)
plt.gca().tick_params(axis='x', labelsize=10)

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, 'time_comparison.png'), dpi=300, bbox_inches='tight')
plt.show()

# График 3: Среднее количество обменов
plt.figure(figsize=(14, 9))
plt.plot(swap_data['Size'], swap_data['AvgSwaps'], 'o-', 
         linewidth=2, markersize=8, color='purple', markerfacecolor='white', 
         markeredgecolor='purple', markeredgewidth=1.5)
plt.xlabel('Размер массива', fontsize=14, fontweight='bold')
plt.ylabel('Среднее количество обменов', fontsize=14, fontweight='bold')
plt.title('Среднее количество обменов элементов', 
          fontsize=16, fontweight='bold', pad=20)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xscale('log')
plt.yscale('log')

# Настройка подписей оси X - показываем все размеры
plt.xticks(all_sizes, [f'{size:,}'.replace(',', ' ') for size in all_sizes], 
           rotation=45, fontsize=10)
plt.gca().tick_params(axis='x', labelsize=10)

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, 'swaps.png'), dpi=300, bbox_inches='tight')
plt.show()

# График 4: Среднее количество проходов
plt.figure(figsize=(14, 9))
plt.plot(pass_data['Size'], pass_data['AvgPasses'], 'o-', 
         linewidth=2, markersize=8, color='orange', markerfacecolor='white', 
         markeredgecolor='orange', markeredgewidth=1.5)
plt.xlabel('Размер массива', fontsize=14, fontweight='bold')
plt.ylabel('Среднее количество проходов', fontsize=14, fontweight='bold')
plt.title('Среднее количество проходов по массиву', 
          fontsize=16, fontweight='bold', pad=20)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xscale('log')
plt.yscale('log')

# Настройка подписей оси X - показываем все размеры
plt.xticks(all_sizes, [f'{size:,}'.replace(',', ' ') for size in all_sizes], 
           rotation=45, fontsize=10)
plt.gca().tick_params(axis='x', labelsize=10)

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, 'passes.png'), dpi=300, bbox_inches='tight')
plt.show()

# Вывод статистики
print("\n" + "="*60)
print("СТАТИСТИКА ТЕСТИРОВАНИЯ")
print("="*60)

for i, row in time_data.iterrows():
    print(f"\nРазмер массива: {row['Size']:,}".replace(',', ' '))
    print(f"  Лучшее время: {row['BestTime']:.3f} мс")
    print(f"  Среднее время: {row['AvgTime']:.3f} мс")
    print(f"  Худшее время: {row['WorstTime']:.3f} мс")
    print(f"  Теоретическое O(n²): {row['BigO']:.3f}")

print("\n" + "="*60)
print(f"Среднее количество обменов для разных размеров:")
for i, row in swap_data.iterrows():
    print(f"  {row['Size']:>8,}: {row['AvgSwaps']:>12,.0f}".replace(',', ' '))

print("\n" + "="*60)
print(f"Среднее количество проходов для разных размеров:")
for i, row in pass_data.iterrows():
    print(f"  {row['Size']:>8,}: {row['AvgPasses']:>12,.0f}".replace(',', ' '))

print(f"\n✅ Графики сохранены в директорию: {graphs_dir}")