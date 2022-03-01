
# for f in input*.png; do convert $f ${f/input/output} +append $f; done  # append frames side-by-side
convert -loop 0 -delay 500 input*.png result.gif 
