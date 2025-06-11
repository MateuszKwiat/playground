namespace ConsoleCalculatorApp;
using System;

class Program
{
    static string GetInputWithExitOption(string message)
    {
        Console.Write(message);
        string input = Console.ReadLine();
        if (input == 'q'.ToString())
            Environment.Exit(0);
        
        return input;
    }
    static void ReadValues(ref float firstValue, ref float secondValue, ref char operation)
    {
        try
        {
            firstValue = float.Parse(GetInputWithExitOption("First value of an equation, q - to exit: "));
            secondValue = float.Parse(GetInputWithExitOption("Second value of an equation, q - to exit: "));
            operation = char.Parse(GetInputWithExitOption("Operation (+, -, *, /) q - to exit: "));
        }
        catch (Exception e)
        {
            Console.WriteLine("Incorrect input");
            operation = '\0';
        }
    }
    
    static float Add(float a, float b)
    {
        return a + b;
    }

    static float Sub(float a, float b)
    {
        return a - b;
    }

    static float Mult(float a, float b)
    {
        return a * b;
    }

    static float Div(float a, float b)
    { 
        float result = a / b;
        if (float.IsInfinity(result))
        {
            Console.WriteLine("Division by zero");
            return float.NaN;
        }
        return result;
    }
    
    static void Main(string[] args)
    {
        Console.WriteLine("Console Calculator App");
        float firstValue = 0.0f;
        float secondValue = 0.0f;
        char operation = '+';
        
        while (true)
        {
            ReadValues(ref firstValue, ref secondValue, ref operation);

            switch (operation)
            {
                case '+':
                    Console.WriteLine(Add(firstValue, secondValue));
                    break;
                
                case '-':
                    Console.WriteLine(Sub(firstValue, secondValue));
                    break;
                
                case '*':
                    Console.WriteLine(Mult(firstValue, secondValue));
                    break;
                
                case '/':
                    Console.WriteLine(Div(firstValue, secondValue));
                    break;
                
                case '\0':
                    break;
            }
            Console.WriteLine("\nPress any key to continue...");
            Console.ReadKey();
            Console.Clear();
        }
    }
}