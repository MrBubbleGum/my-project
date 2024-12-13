using System;

namespace GeometryLibrary
{
    public class Circle : GeometricFigure
    {
        public (double X, double Y) Center { get; set; }
        public double Radius { get; set; }

        public Circle((double X, double Y) center, double radius)
        {
            Center = center;
            Radius = radius;
        }

        public override double CalculateArea()
        {
            return Math.PI * Math.Pow(Radius, 2);
        }

        public override void DisplayInfo()
        {
            string info = $"Circle: Color={Color}, Center=({Center.X}, {Center.Y}), Radius={Radius}, Area={CalculateArea()}";
            PrintColoredText(info, Color);
        }
    }
}