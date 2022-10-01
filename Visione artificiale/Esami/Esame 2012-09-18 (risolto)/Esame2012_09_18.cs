using BioLab.Common;
using BioLab.ImageProcessing;
using BioLab.ImageProcessing.Topology;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PRLab
{
    [AlgorithmInfo("Esercizio4 2012", Category ="FEI")]
    public class Esercizio4 : TopologyOperation<Image<double>>
    {
        public override void Run()
        {
            var connImg = new ConnectedComponentsLabeling(InputImage, 255, MetricType.CityBlock).Execute();
            int[] perimetro = new int[connImg.ComponentCount];
            int[] area = new int[connImg.ComponentCount];
            int[] n1 = new int[connImg.ComponentCount];
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
            for (int i = 0; i < connImg.ComponentCount; i++)
            {
                n1[i] = area[i] - perimetro[i];
            }
            Result = new Image<double>(InputImage.Width, InputImage.Height);
            for (int i = 0; i < Result.PixelCount; i++)
            {
                if (connImg[i] == -1)
                {
                    Result[i] = -1;
                }
                else
                {
                    Result[i] = n1[connImg[i]] / perimetro[connImg[i]];
                }
            }
        }
    }

    [AlgorithmInfo("Esercizio5 2012", Category ="FEI")]
    public class Esercizio5 : TopologyOperation<Image<byte>>
    {
        public override void Run()
        {
            var connImg = new ConnectedComponentsLabeling(InputImage, 255, MetricType.CityBlock).Execute();
            int[] perimetro = new int[connImg.ComponentCount];
            int[] area = new int[connImg.ComponentCount];
            int[] n1 = new int[connImg.ComponentCount];
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
            int somma = 0;
            for (int i = 0; i < connImg.ComponentCount; i++)
            {
                n1[i] = area[i] - perimetro[i];
                somma += n1[i];
            }
            int media = somma / connImg.ComponentCount;
            Result = InputImage.Clone();
            for (int i = 0; i < Result.PixelCount; i++)
            {
                if (connImg[i] >= 0 && n1[connImg[i]] < media)
                {
                    Result[i] = InputImage[i];
                }
                else
                {
                    Result[i] = 0;
                }
            }
        }
    }
}
