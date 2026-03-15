#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <fstream>
#include <algorithm>
#include <iomanip>

using namespace std;
using namespace chrono;

void shakerSort(vector<double>& arr, long long& swaps, long long& passes) {
    swaps = 0;
    passes = 0;
    int n = arr.size();
    bool swapped = true;
    int start = 0;
    int end = n - 1;
    
    while (swapped) {
        swapped = false;
        passes++;

        for (int i = start; i < end; ++i) {
            if (arr[i] > arr[i + 1]) {
                swap(arr[i], arr[i + 1]);
                swaps++;
                swapped = true;
            }
        }
        
        if (!swapped) break;
        
        swapped = false;
        end--;
        passes++;
        
        for (int i = end - 1; i >= start; --i) {
            if (arr[i] > arr[i + 1]) {
                swap(arr[i], arr[i + 1]);
                swaps++;
                swapped = true;
            }
        }
        
        start++;
    }
}

vector<double> generateRandomArray(int size, mt19937& engine, uniform_real_distribution<double>& dist) {
    vector<double> arr(size);
    for (auto& el : arr) {
        el = dist(engine);
    }
    return arr;
}

struct TestResult {
    double time_ms;
    long long swaps;
    long long passes;
};

vector<TestResult> runTestSeries(int arraySize, int testsPerSeries, 
                                mt19937& engine, uniform_real_distribution<double>& dist) {
    vector<TestResult> results;
    
    for (int test = 0; test < testsPerSeries; ++test) {
        vector<double> arr = generateRandomArray(arraySize, engine, dist);
        long long swaps, passes;
        
        auto start = high_resolution_clock::now();
        shakerSort(arr, swaps, passes);
        auto end = high_resolution_clock::now();
        
        auto duration = duration_cast<microseconds>(end - start);
        
        results.push_back({
            static_cast<double>(duration.count()) / 1000.0,
            swaps,
            passes
        });
    }
    
    return results;
}

void calculateStatistics(const vector<TestResult>& results, 
                        double& bestTime, double& worstTime, double& avgTime,
                        double& avgSwaps, double& avgPasses) {
    bestTime = results[0].time_ms;
    worstTime = results[0].time_ms;
    double sumTime = 0;
    double sumSwaps = 0;
    double sumPasses = 0;
    
    for (const auto& result : results) {
        bestTime = min(bestTime, result.time_ms);
        worstTime = max(worstTime, result.time_ms);
        sumTime += result.time_ms;
        sumSwaps += result.swaps;
        sumPasses += result.passes;
    }
    
    avgTime = sumTime / results.size();
    avgSwaps = sumSwaps / results.size();
    avgPasses = sumPasses / results.size();
}

double bigO(int n, double c) {
    return c * n * n;
}

int main() 
{
    vector<int> sizes = {1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000};
    int testsPerSeries = 20;
    
    random_device rd;
    mt19937 engine(rd());
    uniform_real_distribution<double> dist(-1.0, 1.0);
    
    ofstream timeFile("time_results.csv");
    ofstream swapFile("swap_results.csv");
    ofstream passFile("pass_results.csv");
    
    timeFile << "Size,BestTime,WorstTime,AvgTime,BigO" << endl;
    swapFile << "Size,AvgSwaps" << endl;
    passFile << "Size,AvgPasses" << endl;
    
    cout << fixed << setprecision(3);
    cout << "Начало тестирования сортировки перемешиванием\n" << endl;
    
    double c = 0.0001; 
    
    for (int size : sizes) {
        cout << "Тестирование для размера массива: " << size << endl;
        
        auto seriesResults = runTestSeries(size, testsPerSeries, engine, dist);
        
        double bestTime, worstTime, avgTime, avgSwaps, avgPasses;
        calculateStatistics(seriesResults, bestTime, worstTime, avgTime, 
                          avgSwaps, avgPasses);
        
        timeFile << size << "," << bestTime << "," << worstTime << "," 
                << avgTime << "," << bigO(size, c) << endl;
        
        swapFile << size << "," << avgSwaps << endl;
        
        passFile << size << "," << avgPasses << endl;
        
        cout << "  Лучшее время: " << bestTime << " мс" << endl;
        cout << "  Худшее время: " << worstTime << " мс" << endl;
        cout << "  Среднее время: " << avgTime << " мс" << endl;
        cout << "  Среднее число обменов: " << avgSwaps << endl;
        cout << "  Среднее число проходов: " << avgPasses << endl;
        cout << endl;
    }
    
    timeFile.close();
    swapFile.close();
    passFile.close();
    
    cout << "Результаты сохранены в CSV файлы" << endl;
    
    return 0;
}