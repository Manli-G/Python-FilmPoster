#!/usr/bin/env python

# Hello World in GIMP Python

from gimpfu import *

def poster_wgb(colorB,colorF,text,file1,file2,file3,file4,size,font):
       gimp.message("poster script started")
       posterW = 2480
       posterH = 3508
       poster = gimp.Image(posterW, posterH)
       gimp.message("image is created")

       # make the background
       background = gimp.Layer(poster, "background", posterW, posterH, RGB_IMAGE, 100, NORMAL_MODE)
       #colorB = gimpcolor.RGB(255,255, 255)
       pdb.gimp_context_set_background(colorB)
       pdb.gimp_context_set_foreground(colorF)
       background.fill(BACKGROUND_FILL)
       poster.add_layer(background)
       gimp.message("background is created")

       # make the text 1------------------------------
       textLayer = pdb.gimp_text_fontname(poster, None, posterW/2, posterH/10, "A NETFLIX ORIGINAL SERIES",
                                          10, True, size, PIXELS, font)

       textLayer.translate(-textLayer.width/2, -200)
       gimp.message("text layer is created")
       # make the text 2------------------------------
       textLayer = pdb.gimp_text_fontname(poster, None, posterW/2, posterH/10, "A NETFLIX ORIGINAL SERIES",
                                          10, True, size, PIXELS, font)

       textLayer.translate(-textLayer.width/2, 2600)
       gimp.message("text layer is created")
  
       # make 1st Image Layer--------------------------------

       # open image and resize it
       
       image1 = pdb.gimp_file_load(file1,file1)
       pdb.gimp_image_resize(image1, posterW, posterH, 0, 0)
       
       # make a new layer with the right sizes
       layer1 = gimp.Layer(poster,"Image Layer 1",2480,1910,RGBA_IMAGE,100,NORMAL_MODE)
       poster.add_layer(layer1,0)
       # copy the image and paste it to the new layer
       pdb.gimp_edit_copy(image1.layers[0])
       floatingLayer = pdb.gimp_edit_paste(layer1,True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       

       # eventually translate the layer
       layer1.translate(0,600)
       gimp.message("Layer 1 done")
       


       # make 2st Image Layer----------------------------

       # open image and resize it
       
       image2 = pdb.gimp_file_load(file2,file2)
       pdb.gimp_image_resize(image2, posterW/3, posterH/3, 0, 0)
       
       # make a new layer with the right sizes
       layer2 = gimp.Layer(poster,"Image Layer 2",1770,2780,RGBA_IMAGE,100,NORMAL_MODE)
       poster.add_layer(layer2,0)
       # copy the image and paste it to the new layer
       pdb.gimp_edit_copy(image2.layers[0])
       floatingLayer = pdb.gimp_edit_paste(layer2,True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       
       # eventually translate the layer
       layer2.translate(716,0)
       
       gimp.message("Layer 2 done")

       # make 2st Image Layer----------------------------

       # open image and resize it
       
       image3 = pdb.gimp_file_load(file3,file3)
       pdb.gimp_image_resize(image3, posterW/3, posterH/3, 0, 0)
       
       # make a new layer with the right sizes
       layer3 = gimp.Layer(poster,"Image Layer 3",1770,2780,RGBA_IMAGE,100,NORMAL_MODE)
       poster.add_layer(layer3,0)
       # copy the image and paste it to the new layer
       pdb.gimp_edit_copy(image3.layers[0])
       floatingLayer = pdb.gimp_edit_paste(layer3,True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       
       # eventually translate the layer
       layer3.translate(716,0)
       
       gimp.message("Layer 3 done")

       # make 4st Image Layer----------------------------

       # open image and resize it
       
       image4 = pdb.gimp_file_load(file4,file4)
       pdb.gimp_image_resize(image4, posterW/3, posterH/3, 0, 0)
       
       # make a new layer with the right sizes
       layer4 = gimp.Layer(poster,"Image Layer 4",1405,posterH/24,RGBA_IMAGE,100,NORMAL_MODE)
       poster.add_layer(layer4,0)
       # copy the image and paste it to the new layer
       pdb.gimp_edit_copy(image4.layers[0])
       floatingLayer = pdb.gimp_edit_paste(layer4,True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       
       # eventually translate the layer
       layer4.translate(580,1306)
       
       gimp.message("Layer 4 done")
       
       

              


       gimp.Display(poster)
            

register(
              "python_fu_poster_wgb",
              "Black Mirror Series Poster",      # short description
              "Create a new poster with some wgb images and one text",       # long description
              "ST",         # author
              "Copyright@ST", 
              "2016",       
              "Poster (Python)", # menu name    
              "", # Create a new image, don't work on an existing one
              [
                     (PF_COLOR,"colorB","Background Color", (255,255,255)),
                     (PF_COLOR,"colorF","Forground Color",(0,0,0)),
                     (PF_STRING,"text","Copyright:","Python Assignment By Manli Gao"),
                     (PF_FILE,"file1","Open Image 1:",""),
                     (PF_FILE,"file2","Open Image 2:",""),
                     (PF_FILE,"file3","Open Image 3:",""),
                     (PF_FILE,"file4","Open Image 4:",""),
                     (PF_INT,"size","Font Size","70"),
                     (PF_FONT,"font","Font","Courier")
              ],
              [],
              poster_wgb,menu="<Image>/File/Create/Assign2/"
)

main()
