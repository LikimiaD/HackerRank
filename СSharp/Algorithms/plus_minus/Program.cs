using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Result
{

    /*
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<int> arr)
    {
        var plus = 0;
        var minus = 0;
        var zero = 0;
        foreach (var item in arr)
        {
            if (item > 0)
                plus++;
            if (item < 0)
                minus++;
            if (item == 0)
                zero++;
        }
        Console.WriteLine($"{Math.Round((double)plus / (double)arr.Count, 5)}\n{Math.Round((double)minus / (double)arr.Count, 5)}\n{Math.Round((double)zero / (double)arr.Count, 5)}");
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        int n = Convert.ToInt32(Console.ReadLine().Trim());

        List<int> arr = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(arrTemp => Convert.ToInt32(arrTemp)).ToList();

        Result.plusMinus(arr);
    }
}
