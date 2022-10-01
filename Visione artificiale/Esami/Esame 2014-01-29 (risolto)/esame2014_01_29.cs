using BioLab.Common;
using BioLab.ImageProcessing;
using BioLab.ImageProcessing.Topology;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PRLab.FEI
{
    [AlgorithmInfo("Esame", Category = "FEI")]
    public class esame2014_01_29 : ImageOperation<Image<byte>, Image<int>>
    {
        public override void Run()
        {
            int[] rowSums = new int[InputImage.Height];
            for (int i = 0; i < InputImage.Height; i++)
            {    //scorro righe
                int tot = 0;
                for (int j = 0; j < InputImage.Width; j++)
                {   //scorro colonne di una riga
                    tot += InputImage[i, j];
                }
                rowSums[i] = tot;
            }
            int maxValue = 0;
            int ym = 0;
            for (int i = 0; i < rowSums.Length; i++)
            {
                if (rowSums[i] > maxValue)
                {
                    maxValue = rowSums[i];
                    ym = i;
                }
            }


            int media = rowSums[ym] / InputImage.Width;
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


            Image<byte> C = new MorphologyErosion(binImg, MorphologyStructuringElement.CreateCircle(7), 255).Execute();


            Image<byte> erosion = new MorphologyErosion(binImg, MorphologyStructuringElement.CreateCircle(3), 255).Execute();
            Image<byte> bordo = C.Clone();
            for (int i = 0; i < C.PixelCount; i++)
            {
                bordo[i] = (C[i] - erosion[i]).ClipToByte();
            }


            Image<int> distanza = new DistanceTransform(C, 0, MetricType.Chessboard).Execute();
            Image<byte> es5 = C.Clone();
            for (int i = 0; i < distanza.PixelCount; i++)
            {
                if (distanza[i] < 9)
                {
                    es5[i] = 255;
                }
                else
                {
                    es5[i] = 0;
                }
            }


            Result = new Image<int>(InputImage.Width, InputImage.Height);
            for (int i = 0; i < Result.PixelCount; i++)
            {
                if (bordo[i] == 255)
                {
                    Result[i] = -1;
                }
                else if (es5[i] == 255)
                {
                    Result[i] = 0;
                }
                else
                {
                    Result[i] = InputImage[i] * InputImage[i];
                }
            }
        }
    }
}
