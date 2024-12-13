using System;

namespace GeometryLibrary
{
    public abstract class GeometricFigure
    {
        public string Color { get; set; }
        public abstract double CalculateArea();
        public abstract void DisplayInfo();

        protected void PrintColoredText(string text, string color)
        {
            ConsoleColor consoleColor;
            if (Enum.TryParse(color, true, out consoleColor))
            {
                Console.ForegroundColor = consoleColor;
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.White; // Default color
            }

            Console.WriteLine(text);
            Console.ResetColor();
        }
    }
}