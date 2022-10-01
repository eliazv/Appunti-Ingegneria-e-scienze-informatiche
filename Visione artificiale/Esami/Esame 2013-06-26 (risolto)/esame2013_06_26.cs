using BioLab.Common;
using BioLab.ImageProcessing;
using BioLab.ImageProcessing.Topology;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PRLab
{
    [AlgorithmInfo("Esame 2013 giugno", Category ="FEI")]
    public class esame2013_06_26 : ImageOperation<Image<byte>, Image<byte>>
    {
        public override void Run()
        {
            Image<byte> es1 = InputImage.Clone();
            for (int y = 0; y < InputImage.Height; y++)
            {
                for (int x = 0; x < InputImage.Width; x++)
                {
                    int somma = 0;
                    for (int i = -25; i <= 25; i++)
                    {
                        for (int j = -25; j <= 25; j++)
                        {
                            int xIndex = x + i;
                            int yIndex = y + j;
                            if (xIndex >= 0 && yIndex >= 0 && xIndex < InputImage.Width && yIndex < InputImage.Height)
                            {
                                somma += InputImage[yIndex, xIndex];
                            }
                        }
                    }
                    es1[y, x] = (somma / (51 * 51)).ClipToByte();
                }
            }

            Image<byte> Diff = InputImage.Clone();
            for (int i = 0; i < InputImage.PixelCount; i++)
            {
                Diff[i] = (Math.Abs(InputImage[i] - es1[i])).ClipToByte();
            }

            int max = 0;
            int min = 255;
            for (int i = 0; i < InputImage.PixelCount; i++)
            {
                if (Diff[i] > max)
                {
                    max = Diff[i];
                }
                if (Diff[i] < min)
                {
                    min = Diff[i];
                }
            }
            int difference = max - min;
            Image<byte> es3 = Diff.Clone();
            for (int i = 0; i < es3.PixelCount; i++)
            {
                es3[i] = (255 * (Diff[i] - min) / difference).ClipToByte();
            }

            Image<byte> es4 = es3.Clone();
            for (int i = 0; i < es3.PixelCount; i++)
            {
                if (es3[i] < 128)
                {
                    es4[i] = 0;
                }
                else
                {
                    es4[i] = 255;
                }
            }

            ConnectedComponentImage connImg = new ConnectedComponentsLabeling(es4, 255, MetricType.CityBlock).Execute();
            int[] perimetri = new int[connImg.ComponentCount];
            ImageCursor cursor = new ImageCursor(connImg);
            do
            {
                if (connImg[cursor] >= 0)
                {
                    if (connImg[cursor.North] == -1 || connImg[cursor.East] == -1 ||
                      connImg[cursor.South] == -1 || connImg[cursor.West] == -1)
                    {
                        perimetri[connImg[cursor]]++;
                    }
                }
            } while (cursor.MoveNext());
            Image<byte> es5 = es4.Clone();
            for (int i = 0; i < es5.PixelCount; i++)
            {
                if (connImg[i] >= 0 && perimetri[connImg[i]] > 25)
                {
                    es5[i] = 255;
                }
                else
                {
                    es5[i] = 0;
                }
            }

            Result = es5;
        }
    }
}
