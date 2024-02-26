using System;
using System.Diagnostics;

class InsertionSortRunningTime
{
    static void InsertionSort(int[] arr)
    {
        for (int i = 1; i < arr.Length; i++)
        {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && key < arr[j])
            {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    static void Main()
    {
        Stopwatch stopwatch = new Stopwatch();

        // Test case 1
        int[] array1 = { 2, 4, 7, 3, 5, 5, 88, 44, 6, 2, 44, 66 };
        stopwatch.Start();
        InsertionSort(array1);
        stopwatch.Stop();
        Console.WriteLine(stopwatch.Elapsed.TotalSeconds);

        // Test case 2
        int[] array2 = { 2, 4, 75, 5, 1, 6, 2, 6 };
        stopwatch.Reset();
        stopwatch.Start();
        InsertionSort(array2);
        stopwatch.Stop();
        Console.WriteLine(stopwatch.Elapsed.TotalSeconds);
    }
}
