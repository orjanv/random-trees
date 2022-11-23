# Bruk dette scriptet for å lage 40 trær og sett sammen til en kollasj

mkdir $1
for f in {1..40}; do python3 alternative_trees.py $f $1; done
cd $1
for f in *.ps; do convert $f ${f%.ps}.png; done
montage -background "#d1cbba" -geometry +0+0 -tile 6x *.png collage.jpg

