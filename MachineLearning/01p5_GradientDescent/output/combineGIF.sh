#convert animation_fits.gif animation_J.gif +append  animation3.gif
#convert animation_fits.gif animation_J.gif +append -layer optimize animation3.gif



convert animation_fits.gif -coalesce a-%04d.gif                         # separate frames of 1.gif
convert animation_J.gif -coalesce b-%04d.gif                         # separate frames of 2.gif
for f in a-*.gif; do convert $f ${f/a/b} +append $f; done  # append frames side-by-side
convert -loop 0 -delay 20 a-*.gif result.gif               # rejoin frames
