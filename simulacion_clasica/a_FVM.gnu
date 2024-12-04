reset session

# PARÁMETROS ------------------------------------------------------------------
arch_centered = 'centered_FVM.txt'
arch_forward = 'forward_FVM.txt'

# AJUSTES Y GRÁFICOS ----------------------------------------------------------
set grid
set size 0.9
set origin 0.07,0.05
set border 31

unset label
unset arrow
unset logscale
set xtics auto
set ytics auto

set key font "Times New Roman, 20"
set tics font "Times New Roman, 22"
set xtics offset 0,-1
set ytics offset -1,0

set terminal gif animate delay 1           # Formato de salida GIF animado
set output 'evolucion_FVM.gif'                  # Nombre del archivo de salida

set xrange [0:128]                           # Ajustar rango x
set yrange [-0.5:1.5]                       # Ajustar rango y
set grid                                    # Mostrar cuadrícula

set xlabel "x" font "Times New Roman, 22" offset 0,-2
set ylabel "u(x, t)" font "Times New Roman, 22" offset -2,0

do for [i=0:2000:1] {                           # Itera sobre los archivos
    set label sprintf("t = %d", i/100) font "Times New Roman, 20" at graph 0.75, 0.65
    plot arch_centered using 1:2 every :::i::i with lines lw 2 linecolor "blue" title "Centered" at graph 0.75, 0.85, \
        arch_forward using 1:2 every :::i::i with lines lw 2 linecolor "sienna1" title "Forward" at graph 0.75, 0.75
    unset label
}
unset output