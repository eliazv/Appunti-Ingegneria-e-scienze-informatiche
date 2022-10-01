using BioLab.Common;
using BioLab.ImageProcessing;
using BioLab.ImageProcessing.Topology;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PRLab
{
    [AlgorithmInfo("Esame FEI 2013_09_17", Category = "FEI")]
    public class esame2013_09_17 : ImageOperation<Image<byte>, Image<byte>>
    {
        public override void Run()
        {
            int somma = 0;
            int contatoreMax = 0;
            int media = 0;
            for (int y = 0; y < InputImage.Height; y++)
            {
                for (int x = 0; x < InputImage.Width; x++)
                {
                    bool verifica = true;
                    for (int i = -1; i <= 1; i++)
                    {
                        for (int j = -1; j <= 1; j++)
                        {
                            int yIndex = y + i;
                            int xIndex = x + j;
                            if (yIndex >= 0 && xIndex >= 0 && yIndex < InputImage.Height && xIndex < InputImage.Width)
                            {
                                if (InputImage[yIndex, xIndex] > InputImage[y, x])
                                {
                                    verifica = false;
                                }
                            }
                        }
                    }
                    if(verifica)
                    {
                        somma += InputImage[y, x];
                        contatoreMax++;
                    }
                }
            }
            if (contatoreMax > 0)
            {
                media = somma / contatoreMax;
            }
            else
            {
                media = 128;
            }
            Image<byte> binImg = InputImage.Clone();
            for (int i = 0; i < InputImage.PixelCount; i++)
            {
                if (InputImage[i] < media)
                {
                    binImg[i] = 0;
                }
                else
                {
                    binImg[i] = 255;      //Risultato es1
                }
            }

            Image<byte> element = MorphologyStructuringElement.CreateSquare(7);
            Image<byte> C = new MorphologyDilation(new MorphologyErosion(binImg, element, 255).Execute(), element, 255).Execute();
            //Risultato es2

            Image<byte> Ceroso = new MorphologyErosion(C, MorphologyStructuringElement.CreateCircle(3), 255).Execute();
            Image<byte> es3 = C.Clone();
            for (int i = 0; i < C.PixelCount; i++)
            {
                es3[i] = (C[i] - Ceroso[i]).ClipToByte();    //Risultato es3
            }

            Image<byte> es4 = C.Clone();
            Image<int> distanceImg = new DistanceTransform(C, 255, MetricType.Chessboard).Execute();
            for (int i = 0; i < distanceImg.PixelCount; i++)
            {
                if (C[i] == 255 && distanceImg[i] >= 9)
                {
                    es4[i] = 255;
                }
                else
                {
                    es4[i] = 0;   //Risultato es4
                }
            }

            Result = InputImage.Clone();
            for (int i = 0; i < InputImage.PixelCount; i++)
            {
                if (es3[i] == 255)
                {
                    Result[i] = 255;
                }
                else if (es4[i] == 255)
                {
                    Result[i] = 128;
                }
                else
                {
                    Result[i] = (InputImage[i] / 2).ClipToByte();
                }
            }
        }
    }
}
