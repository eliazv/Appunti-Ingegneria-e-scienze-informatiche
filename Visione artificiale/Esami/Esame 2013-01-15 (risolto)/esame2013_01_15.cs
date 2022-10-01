using BioLab.Common;
using BioLab.ImageProcessing;
using BioLab.ImageProcessing.Topology;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PRLab
{
    [AlgorithmInfo("Esame 2013 gennaio", Category ="FEI")]
    public class esame2013_01_15 : ImageOperation<Image<byte>, Image<byte>>
    {
        public override void Run()
        {
            ConvolutionFilter<int> filtroX = new ConvolutionFilter<int>(new int[] { 1, 0, -1, 1, 0, -1, 1, 0, -1 }, 3);
            Image<int> gradienteX = new ByteToIntConvolution(InputImage, filtroX, 3 / 2).Execute();
            ConvolutionFilter<int> filtroY = new ConvolutionFilter<int>(new int[] { 1, 1, 1, 0, 0, 0, -1, -1, -1 }, 3);
            Image<int> gradienteY = new ByteToIntConvolution(InputImage, filtroY, 3 / 2).Execute();

            Image<int> es2 = gradienteX.Clone();
            for (int i = 0; i < es2.PixelCount; i++)
            {
                es2[i] = (int)Math.Round(Math.Atan2(gradienteY[i], gradienteX[i]));
            }

            int somma = 0;
            foreach (byte p in InputImage)
            {
                somma += p;
            }
            int media = somma / InputImage.PixelCount;
            Image<byte> binImg = InputImage.Clone();
            for (int i = 0; i < InputImage.PixelCount; i++)
            {
                if (InputImage[i] < media)
                {
                    binImg[i] = 0;
                }
                else
                {
                    binImg[i] = 255;
                }
            }

            ConnectedComponentImage es4 = new ConnectedComponentsLabeling(binImg, 255, MetricType.CityBlock).Execute();

            int[] area = new int[es4.ComponentCount];
            int[] contatore = new int[es4.ComponentCount];
            for (int i = 0; i < InputImage.PixelCount; i++)
            {
                if (es4[i] >= 0)
                {
                    area[es4[i]]++;
                    if (es2[i] >= -Math.PI / 4 && es2[i] <= Math.PI / 4)
                    {
                        contatore[es4[i]]++;
                    }
                }
            }
            Image<byte> es5 = binImg.Clone();
            for (int i = 0; i < es5.PixelCount; i++)
            {
                if (es4[i] >= 0 && contatore[es4[i]] / area[es4[i]] >= 0.15)
                {
                    es5[i] = 255;
                }
                else
                {
                    es5[i] = 0;
                }
            }

            Result = InputImage.Clone();
            for (int i = 0; i < InputImage.PixelCount; i++)
            {
                if (es5[i] == 255)
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
