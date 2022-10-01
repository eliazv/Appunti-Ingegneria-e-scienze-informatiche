using BioLab.Common;
using BioLab.ImageProcessing;
using BioLab.ImageProcessing.Topology;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PRLab
{
    [AlgorithmInfo("Binarizza 2012", Category ="FEI")]
    public class Binarizza : ImageOperation<Image<byte>, Image<byte>>
    {
        public Binarizza(Image<byte> inputImage)
        {
            InputImage = inputImage;
        }

        public override void Run()
        {
            int tmp = 0;
            foreach (byte p in InputImage)
            {
                tmp += p;
            }
            int mediaGlobale = tmp / InputImage.PixelCount;
            Result = InputImage.Clone();
            for (int y = 0; y < InputImage.Height; y++)
            {
                for (int x = 0; x < InputImage.Width; x++)
                {
                    int somma = 0;
                    for (int i = -2; i <= 2; i++)
                    {
                        for (int j = -2; j <= 2; j++)
                        {
                            int yIndex = y + i;
                            int xIndex = x + j;
                            if (yIndex >= 0 && xIndex >= 0 && yIndex < InputImage.Height &&
                              xIndex < InputImage.Width)
                            {
                                somma += InputImage[yIndex, xIndex];
                            }
                        }
                    }
                    int mediaLocale = somma / (5 * 5);
                    int min = Math.Min(mediaGlobale, mediaLocale);
                    if (InputImage[y, x] < min)
                    {
                        Result[y, x] = 0;
                    }
                    else
                    {
                        Result[y, x] = 255;
                    }
                }
            }
        }

        int Esercizio5(Image<byte> InputImage)
        {
            var binImg = new Binarizza(InputImage).Execute();
            var connImg = new ConnectedComponentsLabeling(binImg, 255, MetricType.CityBlock).Execute();
            int[] area = new int[connImg.ComponentCount];
            int[] perimetro = new int[connImg.ComponentCount];
            var cursor = new ImageCursor(connImg);
            do
            {
                if (connImg[cursor] >= 0)
                {
                    area[connImg[cursor]]++;
                    if (connImg[cursor.North] == -1 || connImg[cursor.East] == -1 ||
                      connImg[cursor.South] == -1 || connImg[cursor.West] == -1)
                    {
                        perimetro[connImg[cursor]]++;
                    }
                }
            } while (cursor.MoveNext());
            int contatore = 0;
            for (int i = 0; i < connImg.ComponentCount; i++)
            {
                if (perimetro[i] < area[i] / 2)
                {
                    contatore++;
                }
            }
            return contatore;
        }
    }
}
