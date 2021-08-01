<!--
.. title: GameBoy Thumbnails on Linux
.. slug: sameboy-thumbnailer
.. date: 2021-03-01 15:08:55 UTC+02:00
.. tags: 
.. category: 
.. link: 
.. description: pretty pictures
.. type: text
-->

# Where I started

My introduction to SameBoy came from stacksmashing's ["How to reverse engineer & patch a Game Boy ROM"](https://youtu.be/dQLp5i8oS3Y) video.

I'm not big on reverse engineering but I do enjoy a good GameBoy game when I see one.

and there it was

![](/images/sameboy/quicklook.png)

this is the type of integration I like to see from projects

but these kinds of features are almost never present on Linux be it because no one bothers or because each major DE supports a different method.

Despite that I was interested in it and started looking through the code

# pretty images for pretty games

the code was simple
it stored the framebuffer output in a bitmap image and composed that under the image for the cartridge case.

Seems simple

([source code](https://github.com/Jan200101/SameBoy/blob/bmp-thumbnailer/Thumbnailer/main.c))
```c
            bitmap* pbitmap  = malloc(sizeof(bitmap));
            pbitmap->fileheader.signature[0] = 0x42;
            pbitmap->fileheader.signature[1] = 0x4D;

            pbitmap->fileheader.filesize = sizeof(pixels) + sizeof(bitmap);
            pbitmap->fileheader.fileoffset_to_pixelarray = sizeof(bitmap);
            pbitmap->bitmapinfoheader.dibheadersize = sizeof(bitmapinfoheader);
            pbitmap->bitmapinfoheader.width = 160;
            pbitmap->bitmapinfoheader.height = -144;
            pbitmap->bitmapinfoheader.planes = 1;
            pbitmap->bitmapinfoheader.bitsperpixel = 32;
            pbitmap->bitmapinfoheader.compression = 0;
            pbitmap->bitmapinfoheader.imagesize = sizeof(pixels);
            pbitmap->bitmapinfoheader.ypixelpermeter = 0;
            pbitmap->bitmapinfoheader.xpixelpermeter = 0;
            pbitmap->bitmapinfoheader.numcolorspallette = 0;
            fwrite(pbitmap, 1, sizeof(bitmap),fp);
            fwrite(pixels, 1, sizeof(pixels),fp);
            fclose(fp);
            free(pbitmap);
```

I actually wanted to see the images in my filemanager though so I went to see how that is done and quickly changed my mind.

The way you creat ThumbCreator plugins for KDE was way too complicated to propose to the repository so I went [Freedesktop Thumbnailer standard](https://specifications.freedesktop.org/thumbnail-spec/thumbnail-spec-latest.html) instead

the biggest requirement was that the output format was a PNG so I started from scratch

writing my own png lib was too big of an undertaking so I simply chose to use lodepng, a free png library under zlib so it was fair to use

a simple conversion to PNG was completed and the resulting binary outputted pngs for any files you wanted

![](/images/sameboy/103683381-6b58e080-4f8a-11eb-97ec-a2859dc807be.png)

I was happy with this but it was a bit bare and having to specify the bootrom path wasn't very user friendly so I took suggestions from max-m and embedded everything needed in the binary itself

but the image does need to be resized if a differnt resolution was desired

so I implemented a basic scaling function with things like passable sample size

([source code](https://github.com/Jan200101/SameBoy/blob/thumbnailer/Thumbnailer/main.c#L70))
```c 
static void scale_image(const uint32_t* input, const signed input_width, const signed input_height,
                        uint32_t* output, const double multiplier, const signed samples)
{
    signed output_width = input_width * multiplier;
    uint32_t pixel;

    for (signed h = 0; h < input_height * multiplier; ++h) {
        for (signed w = 0; w < input_width * multiplier; ++w) {
            pixel = 0;

            signed h_input = h/multiplier;
            signed w_input = w/multiplier;

            signed h_input_max = (h+1)/multiplier-1;
            signed w_input_max = (w+1)/multiplier-1;

            signed h_step = h_input_max - h_input + 2;
            signed w_step = w_input_max - w_input + 2;

            for (signed xa = w_input; xa < w_input_max + 2 && xa < input_width; xa += w_step / samples)
                for (signed ya = h_input; ya < h_input_max + 2 && ya < input_width; ya += h_step / samples)
                    pixel = average(pixel, input[(signed)xa + ((signed)ya * input_width)]);

            output[w + (h * output_width)] = pixel;
        }
    }
}
```

with this I could also create thumbnails of any size that still looked correct

![](/images/sameboy/104072883-aa966400-520c-11eb-97ce-889af5328d5d.png)

the end result looks great and similar to the MacOS implementation which means I have achived my goal

![](/images/sameboy/104074209-cb13ed80-520f-11eb-915c-4ea99a2ca4c1.png)

[pull request](https://github.com/LIJI32/SameBoy/pull/320)