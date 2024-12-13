using System;

namespace GeometryLibrary
{
    public class Triangle : Polygon
    {
        public Triangle((double X, double Y)[] vertices)
        {
            if (vertices.Length != 3)
                throw new ArgumentException("Triangle must have 3 vertices.");
            Vertices = vertices;
        }

        public override double CalculateArea()
        {
            double a = Vertices[0].X * (Vertices[1].Y - Vertices[2].Y);
            double b = Vertices[1].X * (Vertices[2].Y - Vertices[0].Y);
            double c = Vertices[2].X * (Vertices[0].Y - Vertices[1].Y);
            return Math.Abs((a + b + c) / 2.0);
        }

        public override double CalculatePerimeter()
        {
            double a = Distance(Vertices[0], Vertices[1]);
            double b = Distance(Vertices[1], Vertices[2]);
            double c = Distance(Vertices[2], Vertices[0]);
            return a + b + c;
        }

        private double Distance((double X, double Y) p1, (double X, double Y) p2)
        {
            return Math.Sqrt(Math.Pow(p1.X - p2.X, 2) + Math.Pow(p1.Y - p2.Y, 2));
        }

        public override void DisplayInfo()
        {
            string info = $"Triangle: Color={Color}, Area={CalculateArea()}, Perimeter={CalculatePerimeter()}";
            PrintColoredText(info, Color);
        }
    }
}