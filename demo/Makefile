all: demo

demo: demo_plots.pdf

clean:
	latexmk -c

distclean: clean
	rm -f demo_plots.pdf
	rm -f stopping-power-mpl.pdf stopping-power.tex
	rm -f shower-front.tex
	rm -f eas-lateral.tex
	rm -f histogram-fit.tex
	rm -f spectrum.tex
	rm -f sciencepark.tex
	rm -f multiplot.tex
	rm -f polar_histogram.tex
	rm -f discrete_directions.tex
	rm -f histogram2d.tex

demo_plots.pdf: demo_plots.tex \
		stopping-power-mpl.pdf stopping-power.tex \
		shower-front.tex eas-lateral.tex histogram-fit.tex \
		spectrum.tex sciencepark.tex multiplot.tex polar_histogram.tex \
		discrete_directions.tex histogram2d.tex multi_histogram2d.tex
	latexmk -pdf demo_plots.tex

stopping-power-mpl.pdf stopping-power.tex: demo_stopping_power.py
	python $?

shower-front.tex: demo_shower_front.py
	python $?

eas-lateral.tex: demo_eas_ldf.py
	python $?

histogram-fit.tex: demo_histogram_fit.py
	python $?

spectrum.tex: demo_spectrum.py
	python $?

sciencepark.tex: demo_sciencepark.py
	python $?

multiplot.tex: demo_multiplot.py
	python $?

polar_histogram.tex: demo_polar_histogram.py
	python $?

discrete_directions.tex: demo_discrete_directions.py
	python $?

histogram2d.tex multi_histogram2d.tex: demo_histogram2d.py
	python $?
