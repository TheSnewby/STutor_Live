using System;
using System.Collections.Generic;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;
using SixLabors.ImageSharp.Processing;
using System.Threading;
/*
speak about some basics
compared C vs C# these topics
how arrays work in C vs C# (pointers vs pass-by-refernce (hidden pointers(?))) # read up passbyrefernce vs passbyvalues
consider finding a simple way to talk about physical memory management
ask ppl what their understanding in any languages they know of these topics as they come up
attempt to say things multiple different ways (diagrams, verbal, live-code)
*/
class Program
{
	static void Squares()
	{
		int i;
		int[] arr = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
		for (i = 0; i < arr.Length; i++)
		{
			Console.Write(arr[i] * arr[i] + "   ");
			Thread.Sleep(200);
		}
	}

	static void Fibonacci()
    {
        int[] fib = new int[25];
        fib[0] = 0;
        fib[1] = 1;

        for (int i = 2; i < fib.Length; i++)
		{
            fib[i] = fib[i - 1] + fib[i - 2];
			Console.Write(fib[i] + "   ");
			Thread.Sleep(200);
		}
    }

	static void ASCIIWave()
    {
		int modifier = 30;  //horizontal amplitude
        for (int i = 0; i < 100; i++)
        {
            int x = (int)(modifier * Math.Sin(i / 3.14));
            Console.WriteLine(new string(' ', x + modifier + 40) + "*");  //40 is horizontal offset
			Thread.Sleep(90);
        }
    }

	static void FallingStars()
    {
        Random rand = new Random();
        int width = 240;
        char[] stars = new char[width];
		int i = 90;

        while (i >= 0)
        {
            Array.Fill(stars, ' ');
            stars[rand.Next(width)] = '*';
            // Console.Clear();
            Console.WriteLine(new string(stars));
            Thread.Sleep(100);
			i--;
        }
    }

	static void ASCIISpiral()
    {
        int size = 25;
        for (int y = -size + 6; y < size; y++)
        {
			Console.Write(new string(' ', 40));
            for (int x = -size; x < size; x++)
            {
				Thread.Sleep(5);
                if (Math.Sqrt(x * x + y * y) % 2 < 1)
                    Console.Write("* ");
                else
                    Console.Write("  ");
            }
            Console.WriteLine();
        }
    }

	static void ASCIIImagePrinting(string imagePath)
    {
        using (Image<Rgba32> img = Image.Load<Rgba32>(imagePath))
        {
            img.Mutate(x => x.Resize(100, 50)); // Resize for terminal display
            for (int y = 0; y < img.Height; y++)
            {
				Console.Write(new string(' ', 30));  //offset
                for (int x = 0; x < img.Width; x++)
                {
                    var pixel = img[x, y];
                    int gray = (pixel.R + pixel.G + pixel.B) / 3;
                    char ascii = gray > 128 ? '#' : ' ';
                    Console.Write(ascii);
					Thread.Sleep(1);
                }
                Console.WriteLine();
            }
        }
    }
    static void Main(string[] args)
    {
		string userInput = "0";
		while (userInput != "9")
		{
			Console.WriteLine(@"
What would you like to run?
1) Squared Values
2) Fibonnaci Sequence
3) Wave
4) Star
5) Net Pattern
6) Print Lumi
7) Print Kitty
8) Print Pupper
9) Exit");
			Console.Write("\nEnter Here: ");
			userInput = Console.ReadLine() ?? "";
			Console.WriteLine("You entered {0}.", userInput);
			Thread.Sleep(500);
			Console.Clear();

			switch(userInput)
			{
				case "1":
					Squares();
					break;
				case "2":
					Fibonacci();
					break;
				case "3":
					ASCIIWave();
					break;
				case "4":
					FallingStars();
					break;
				case "5": 
					ASCIISpiral();
					break;
				case "6":
					ASCIIImagePrinting("Lumi.png");
					break;
				case "7":
					ASCIIImagePrinting("surprise_kitty.jpg");
					break;
				case "8":
					ASCIIImagePrinting("cute_pupper.jpg");
					break;
				case "9":
					Console.WriteLine(new string(' ', 80) + "Thank you for playing!!!\n");
					Thread.Sleep(1000);
					break;
				default:
					Console.WriteLine("Not a valid entry. Please enter a number between 1 and 7.\n");
					break;
			}
			Console.ReadKey();
			Console.Clear();
		}
    }
}