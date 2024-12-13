using System;

namespace GeometryLibrary
{
    public class Rectangle : Polygon
    {
        public Rectangle((double X, double Y)[] vertices)
        {
            if (vertices.Length != 4)
                throw new ArgumentException("Rectangle must have 4 vertices.");
            Vertices = vertices;
        }

        public override double CalculateArea()
        {
            double width = Math.Abs(Vertices[0].X - Vertices[1].X);
            double height = Math.Abs(Vertices[1].Y - Vertices[2].Y);
            return width * height;
        }

        public override double CalculatePerimeter()
        {
            double width = Math.Abs(Vertices[0].X - Vertices[1].X);
            double height = Math.Abs(Vertices[1].Y - Vertices[2].Y);
            return 2 * (width + height);
        }

        public override void DisplayInfo()
        {
            string info = $"Rectangle: Color={Color}, Area={CalculateArea()}, Perimeter={CalculatePerimeter()}";
            PrintColoredText(info, Color);
        }
    }
}