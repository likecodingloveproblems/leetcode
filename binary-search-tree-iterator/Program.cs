using System;

namespace binary_search_tree_iterator
{
    class Program
    {
        static void Main(string[] args)
        {
            foreach (var num in DividableNumbers.DividableBy(5, 2))
            {
                Console.WriteLine($"this is the result: {num}");
            }
        }
    }
    class DividableNumbers
    {
        public static IEnumerable<int> DividableBy(int num, int targetNumber)
        {
            Console.WriteLine(num);
            if (num > targetNumber)
                DividableBy(num - 1, targetNumber);
            yield return num;
        }
    }
}