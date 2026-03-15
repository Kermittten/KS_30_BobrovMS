import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

time_file = os.path.join(script_dir, 'time_results.csv')
swap_file = os.path.join(script_dir, 'swap_results.csv')
pass_file = os.path.join(script_dir, 'pass_results.csv')

print("Поиск файлов в директории:", script_dir)
print("\nПроверка наличия файлов:")
print(f"time_results.csv: {'✅ Найден' if os.path.exists(time_file) else '❌ Не найден'}")
print(f"swap_results.csv: {'✅ Найден' if os.path.exists(swap_file) else '❌ Не найден'}")
print(f"pass_results.csv: {'✅ Найден' if os.path.exists(pass_file) else '❌ Не найден'}")

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

plt.style.use('seaborn-v0_8-darkgrid')

all_sizes = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000]

graphs_dir = os.path.join(script_dir, 'graphs')
os.makedirs(graphs_dir, exist_ok=True)

plt.figure(figsize=(14, 9))

first_size = time_data['Size'].iloc[0]
first_time = time_data['WorstTime'].iloc[0]
first_bigo = time_data['BigO'].iloc[0]

scale_factor = first_time / first_bigo
normalized_bigO = time_data['BigO'] * scale_factor

plt.plot(time_data['Size'], time_data['WorstTime'], 'ro-', 
         label='Худшее время (реальное)', linewidth=2, markersize=8, 
         markerfacecolor='white', markeredgewidth=1.5)

plt.plot(time_data['Size'], normalized_bigO, 'b--', 
         label=f'O(n²) (масштабированная: {scale_factor:.2e} * n²)', 
         linewidth=2, alpha=0.7)

plt.xlabel('Размер массива', fontsize=14, fontweight='bold')
plt.ylabel('Время (мс)', fontsize=14, fontweight='bold')
plt.title('Сравнение худшего времени сортировки с теоретической сложностью O(n²)', 
          fontsize=16, fontweight='bold', pad=20)
plt.legend(fontsize=12, framealpha=0.9)
plt.grid(True, alpha=0.3, linestyle='--')

plt.xticks(all_sizes, [f'{size:,}'.replace(',', ' ') for size in all_sizes], 
           rotation=45, fontsize=10)

plt.annotate(f'Коэффициент масштабирования: {scale_factor:.2e}', 
             xy=(0.02, 0.98), xycoords='axes fraction',
             fontsize=10, bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, 'complexity_comparison_fixed.png'), dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(14, 9))
plt.plot(time_data['Size'], time_data['BestTime'], 'g^-', 
         label='Лучшее время', linewidth=2, markersize=8, markerfacecolor='white',
         markeredgewidth=1.5)
plt.plot(time_data['Size'], time_data['AvgTime'], 'bs-', 
         label='Среднее время', linewidth=2, markersize=8, markerfacecolor='white',
         markeredgewidth=1.5)
plt.plot(time_data['Size'], time_data['WorstTime'], 'ro-', 
         label='Худшее время', linewidth=2, markersize=8, markerfacecolor='white',
         markeredgewidth=1.5)
plt.xlabel('Размер массива', fontsize=14, fontweight='bold')
plt.ylabel('Время (мс)', fontsize=14, fontweight='bold')
plt.title('Лучшее, среднее и худшее время сортировки вставками', 
          fontsize=16, fontweight='bold', pad=20)
plt.legend(fontsize=12, framealpha=0.9)
plt.grid(True, alpha=0.3, linestyle='--')

plt.xticks(all_sizes, [f'{size:,}'.replace(',', ' ') for size in all_sizes], 
           rotation=45, fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, 'time_comparison.png'), dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(14, 9))
plt.plot(swap_data['Size'], swap_data['AvgSwaps'], 'o-', 
         linewidth=2, markersize=8, color='purple', markerfacecolor='white', 
         markeredgecolor='purple', markeredgewidth=1.5)
plt.xlabel('Размер массива', fontsize=14, fontweight='bold')
plt.ylabel('Среднее количество обменов', fontsize=14, fontweight='bold')
plt.title('Среднее количество обменов элементов', 
          fontsize=16, fontweight='bold', pad=20)
plt.grid(True, alpha=0.3, linestyle='--')

plt.xticks(all_sizes, [f'{size:,}'.replace(',', ' ') for size in all_sizes], 
           rotation=45, fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, 'swaps.png'), dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(14, 9))
plt.plot(pass_data['Size'], pass_data['AvgPasses'], 'o-', 
         linewidth=2, markersize=8, color='orange', markerfacecolor='white', 
         markeredgecolor='orange', markeredgewidth=1.5)
plt.xlabel('Размер массива', fontsize=14, fontweight='bold')
plt.ylabel('Среднее количество проходов', fontsize=14, fontweight='bold')
plt.title('Среднее количество проходов по массиву', 
          fontsize=16, fontweight='bold', pad=20)
plt.grid(True, alpha=0.3, linestyle='--')

plt.xticks(all_sizes, [f'{size:,}'.replace(',', ' ') for size in all_sizes], 
           rotation=45, fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, 'passes.png'), dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(14, 9))

norm_sizes = time_data['Size'] / time_data['Size'].iloc[0]
norm_worst = time_data['WorstTime'] / time_data['WorstTime'].iloc[0]
norm_bigo = time_data['BigO'] / time_data['BigO'].iloc[0]

plt.plot(norm_sizes, norm_worst, 'ro-', 
         label='Худшее время (нормализованное)', linewidth=2, markersize=8,
         markerfacecolor='white', markeredgewidth=1.5)
plt.plot(norm_sizes, norm_bigo, 'b--', 
         label='O(n²) (нормализованное)', linewidth=2, alpha=0.7)
plt.plot(norm_sizes, norm_sizes**2, 'g:', 
         label='Теоретическая n²', linewidth=2, alpha=0.5)

plt.xlabel('Относительный размер массива (n/n₀)', fontsize=14, fontweight='bold')
plt.ylabel('Относительное время (T/T₀)', fontsize=14, fontweight='bold')
plt.title('Проверка квадратичной зависимости (нормализованные данные)', 
          fontsize=16, fontweight='bold', pad=20)
plt.legend(fontsize=12, framealpha=0.9)
plt.grid(True, alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, 'normalized_comparison.png'), dpi=300, bbox_inches='tight')
plt.show()

print("\n" + "="*70)
print("СТАТИСТИКА ТЕСТИРОВАНИЯ")
print("="*70)

print("\n" + "-"*70)
print("ВРЕМЕННЫЕ ХАРАКТЕРИСТИКИ:")
print("-"*70)
for i, row in time_data.iterrows():
    print(f"\nРазмер массива: {row['Size']:,}".replace(',', ' '))
    print(f"  Лучшее время: {row['BestTime']:.3f} мс")
    print(f"  Среднее время: {row['AvgTime']:.3f} мс")
    print(f"  Худшее время: {row['WorstTime']:.3f} мс")

print("\n" + "-"*70)
print("ПРОВЕРКА КВАДРАТИЧНОЙ ЗАВИСИМОСТИ:")
print("-"*70)
print(f"\nКоэффициент масштабирования для O(n²): {scale_factor:.2e}")
print("\nСоотношение роста времени и теоретического O(n²):")
print(f"{'Размер':>10} | {'T(n)/T(1000)':>15} | {'(n/1000)²':>15} | {'Отклонение':>15}")
print("-"*70)

first_worst = time_data['WorstTime'].iloc[0]
first_size = time_data['Size'].iloc[0]

for i, row in time_data.iterrows():
    time_ratio = row['WorstTime'] / first_worst
    size_ratio = row['Size'] / first_size
    theoretical = size_ratio ** 2
    deviation = (time_ratio / theoretical - 1) * 100
    
    print(f"{row['Size']:>10,} | {time_ratio:>15.2f} | {theoretical:>15.2f} | {deviation:>14.1f}%".replace(',', ' '))

print("\n" + "-"*70)
print("СРЕДНЕЕ КОЛИЧЕСТВО ОБМЕНОВ:")
print("-"*70)
for i, row in swap_data.iterrows():
    print(f"  {row['Size']:>8,}: {row['AvgSwaps']:>12,.0f}".replace(',', ' '))

print("\n" + "-"*70)
print("СРЕДНЕЕ КОЛИЧЕСТВО ПРОХОДОВ:")
print("-"*70)
for i, row in pass_data.iterrows():
    print(f"  {row['Size']:>8,}: {row['AvgPasses']:>12,.0f}".replace(',', ' '))

print(f"\n Графики сохранены: {graphs_dir}")