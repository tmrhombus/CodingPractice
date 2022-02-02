#convert animation_fits.gif animation_J.gif +append  animation3.gif
#convert animation_fits.gif animation_J.gif +append -layer optimize animation3.gif



convert animation_fits.gif -coalesce a-%04d.png                         # separate frames of 1.png
convert animation_Js.gif -coalesce b-%04d.png                         # separate frames of 2.png
for f in a-*.png; do convert $f ${f/a/b} +append $f; done  # append frames side-by-side
convert -loop 0 -delay 20 a-*.png result.gif               # rejoin frames
