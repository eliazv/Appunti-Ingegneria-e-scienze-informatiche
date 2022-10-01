using BioLab.Common;
using BioLab.ImageProcessing;
using BioLab.ImageProcessing.Topology;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PRLab
{
    [AlgorithmInfo("Equalizzazione 2011", Category = "FEI")]
    public class EqualizzazioneIstrogramma : ImageOperation<Image<byte>, Image<byte>>
    {
        public override void Run()
        {
            var histogram = new HistogramBuilder(InputImage).Execute();
            for (int i = 1; i < 256; i++)
            {
                histogram[i] += histogram[i - 1];
            }
            Result = InputImage.Clone();
            for (int i = 0; i < InputImage.PixelCount; i++)
            {
                Result[i] = (255 * histogram[InputImage[i]] / InputImage.PixelCount).ClipToByte();
            }
        }

        Image<byte> Esercizio5(Image<byte> InputImage, byte foreground)
        {
            byte background = (byte)~foreground;
            var connImg = new ConnectedComponentsLabeling(InputImage, background, MetricType.Chessboard).Execute();
            int[] area = new int[connImg.ComponentCount];
            for (int i = 0; i < connImg.PixelCount; i++)
            {
                if (connImg[i] >= 0)
                {
                    area[connImg[i]]++;
                }
            }
            int max = 0;
            for (int i = 0; i < connImg.ComponentCount; i++)
            {
                if (area[i] > area[max])
                {
                    max = i;
                }
            }
            var Result = InputImage.Clone();
            for (int i = 0; i < InputImage.PixelCount; i++)
            {
                if (connImg[i] == max)
                {
                    Result[i] = background;
                }
                else
                {
                    Result[i] = foreground;
                }
            }
            return Result;
        }
    }
}
