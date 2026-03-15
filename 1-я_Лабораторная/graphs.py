import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

time_data = pd.read_csv('time_results.csv')
swap_data = pd.read_csv('swap_results.csv')
pass_data = pd.read_csv('pass_results.csv')

# Настройка стиля графиков
plt.style.use('seaborn-v0_8-darkgrid')

# График 1: Сравнение с O(n²)
plt.figure(figsize=(12, 8))
plt.plot(time_data['Size'], time_data['WorstTime'], 'ro-', 
         label='Худшее время', linewidth=2, markersize=8)
plt.plot(time_data['Size'], time_data['BigO'], 'b--', 
         label='O(n²)', linewidth=2, alpha=0.7)
plt.xlabel('Размер массива', fontsize=12)
plt.ylabel('Время (мс)', fontsize=12)
plt.title('Сравнение худшего времени с теоретической сложностью O(n²)', 
          fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xscale('log')
plt.yscale('log')
plt.savefig('complexity_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# График 2: Лучшее, среднее и худшее время
plt.figure(figsize=(12, 8))
plt.plot(time_data['Size'], time_data['BestTime'], 'g^-', 
         label='Лучшее время', linewidth=2, markersize=8)
plt.plot(time_data['Size'], time_data['AvgTime'], 'bs-', 
         label='Среднее время', linewidth=2, markersize=8)
plt.plot(time_data['Size'], time_data['WorstTime'], 'ro-', 
         label='Худшее время', linewidth=2, markersize=8)
plt.xlabel('Размер массива', fontsize=12)
plt.ylabel('Время (мс)', fontsize=12)
plt.title('Лучшее, среднее и худшее время сортировки перемешиванием', 
          fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xscale('log')
plt.yscale('log')
plt.savefig('time_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# График 3: Среднее количество обменов
plt.figure(figsize=(12, 8))
plt.plot(swap_data['Size'], swap_data['AvgSwaps'], 'mo-', 
         linewidth=2, markersize=8, color='purple')
plt.xlabel('Размер массива', fontsize=12)
plt.ylabel('Среднее количество обменов', fontsize=12)
plt.title('Среднее количество обменов элементов', 
          fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.xscale('log')
plt.yscale('log')
plt.savefig('swaps.png', dpi=300, bbox_inches='tight')
plt.show()

# График 4: Среднее количество проходов
plt.figure(figsize=(12, 8))
plt.plot(pass_data['Size'], pass_data['AvgPasses'], 'co-', 
         linewidth=2, markersize=8, color='orange')
plt.xlabel('Размер массива', fontsize=12)
plt.ylabel('Среднее количество проходов', fontsize=12)
plt.title('Среднее количество проходов по массиву', 
          fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.xscale('log')
plt.yscale('log')
plt.savefig('passes.png', dpi=300, bbox_inches='tight')
plt.show()