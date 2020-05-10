# Travelling-Salesman-Problem---Simulated-Annealing-
Solve Travelling Salesman Problem using Simulated Annealing Algorithm
<html>

<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
<meta name=Generator content="Microsoft Word 15 (filtered)">
<style>
<!--
 /* Font Definitions */
 @font-face
	{font-family:Helvetica;
	panose-1:2 11 6 4 2 2 2 2 2 4;}
@font-face
	{font-family:Wingdings;
	panose-1:5 0 0 0 0 0 0 0 0 0;}
@font-face
	{font-family:"Cambria Math";
	panose-1:2 4 5 3 5 4 6 3 2 4;}
@font-face
	{font-family:Calibri;
	panose-1:2 15 5 2 2 2 4 3 2 4;}
@font-face
	{font-family:"Century Gothic";
	panose-1:2 11 5 2 2 2 2 2 2 4;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{margin-top:0in;
	margin-right:0in;
	margin-bottom:8.0pt;
	margin-left:0in;
	line-height:107%;
	font-size:11.0pt;
	font-family:"Century Gothic",sans-serif;}
a:link, span.MsoHyperlink
	{color:blue;
	text-decoration:underline;}
p.MsoListParagraph, li.MsoListParagraph, div.MsoListParagraph
	{margin-top:0in;
	margin-right:0in;
	margin-bottom:8.0pt;
	margin-left:.5in;
	line-height:107%;
	font-size:11.0pt;
	font-family:"Century Gothic",sans-serif;}
p.MsoListParagraphCxSpFirst, li.MsoListParagraphCxSpFirst, div.MsoListParagraphCxSpFirst
	{margin-top:0in;
	margin-right:0in;
	margin-bottom:0in;
	margin-left:.5in;
	margin-bottom:.0001pt;
	line-height:107%;
	font-size:11.0pt;
	font-family:"Century Gothic",sans-serif;}
p.MsoListParagraphCxSpMiddle, li.MsoListParagraphCxSpMiddle, div.MsoListParagraphCxSpMiddle
	{margin-top:0in;
	margin-right:0in;
	margin-bottom:0in;
	margin-left:.5in;
	margin-bottom:.0001pt;
	line-height:107%;
	font-size:11.0pt;
	font-family:"Century Gothic",sans-serif;}
p.MsoListParagraphCxSpLast, li.MsoListParagraphCxSpLast, div.MsoListParagraphCxSpLast
	{margin-top:0in;
	margin-right:0in;
	margin-bottom:8.0pt;
	margin-left:.5in;
	line-height:107%;
	font-size:11.0pt;
	font-family:"Century Gothic",sans-serif;}
.MsoPapDefault
	{margin-bottom:8.0pt;
	line-height:107%;}
@page WordSection1
	{size:8.5in 11.0in;
	margin:1.0in 1.0in 1.0in 1.0in;}
div.WordSection1
	{page:WordSection1;}
 /* List Definitions */
 ol
	{margin-bottom:0in;}
ul
	{margin-bottom:0in;}
-->
</style>

</head>

<body lang=EN-US link=blue vlink="#954F72">

<div class=WordSection1>

<p class=MsoNormal><b><span style='font-size:12.0pt;line-height:107%'>Travelling
Salesman Problem - TSP:</span></b></p>

<p class=MsoNormal>“Given a list of cities and the distances between each pair
of cities, what is the shortest possible route that visits each city and
returns to the origin city?”</p>

<p class=MsoNormal>I have chosen Simulated Annealing Algorithm to solve the TSP,
because it has some parameters in which I can tweak to reach a reasonable
solution - <span style='color:#2C2C2C;background:white'>the goal of simulated
annealing is to minimize the energy of a system (minimizing a cost function)</span>.
</p>

<p class=MsoNormal><b><span style='font-size:12.0pt;line-height:107%'>Simulated
Annealing Algorithm in brief:</span></b></p>

<p class=MsoListParagraphCxSpFirst style='text-indent:-.25in'>1.<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp; </span><span
dir=LTR></span>Start from an initial solution, then at each iteration we
generate a slightly different solution. </p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-.25in'>2.<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp; </span><span
dir=LTR></span>If the iteration is better, then we accept it. Otherwise, we
accept it with a probability of metropolis.</p>

<p class=MsoListParagraphCxSpLast style='text-indent:-.25in'>3.<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp; </span><span
dir=LTR></span>We repeat the iteration process until a stopping criterion is
reached.</p>

<div style='border:solid windowtext 1.0pt;padding:1.0pt 1.0pt 1.0pt 1.0pt;
background:#D9D9D9'>

<p class=MsoNormal style='background:#D9D9D9;border:none;padding:0in'><span
style='color:black'>Let&nbsp;</span><i><span style='font-size:11.5pt;
line-height:107%;color:black'>s</span></i><span style='font-size:11.5pt;
line-height:107%;color:black'>&nbsp;=&nbsp;<i>s</i></span><sub><span
style='font-size:9.0pt;line-height:107%;color:black'>0</span></sub></p>

<p class=MsoNormal style='background:#D9D9D9;border:none;padding:0in'><span
style='color:black'>For&nbsp;</span><i><span style='font-size:11.5pt;
line-height:107%;color:black'>k</span></i><span style='font-size:11.5pt;
line-height:107%;color:black'>&nbsp;= 0</span><span style='color:black'>&nbsp;through&nbsp;</span><i><span
style='font-size:11.5pt;line-height:107%;color:black'>k</span></i><sub><span
style='font-size:9.0pt;line-height:107%;color:black'>max</span></sub><span
style='color:black'>&nbsp;(exclusive):</span></p>

<p class=MsoNormal style='text-indent:.5in;background:#D9D9D9;border:none;
padding:0in'><i><span style='font-size:11.5pt;line-height:107%;color:black'>T</span></i><span
style='font-size:11.5pt;line-height:107%;color:black'>&nbsp;&#8592;
temperature(&nbsp;<i>(k+1)</i>/<i>k</i></span><sub><span style='font-size:9.0pt;
line-height:107%;color:black'>max</span></sub><span style='font-size:11.5pt;
line-height:107%;color:black'>&nbsp;)</span></p>

<p class=MsoNormal style='text-indent:.5in;background:#D9D9D9;border:none;
padding:0in'><span style='color:black'>Pick a random neighbour,&nbsp;</span><i><span
style='font-size:11.5pt;line-height:107%;color:black'>s</span></i><sub><span
style='font-size:9.0pt;line-height:107%;color:black'>new</span></sub><span
style='font-size:11.5pt;line-height:107%;color:black'>&nbsp;&#8592; neighbour(<i>s</i>)</span></p>

<p class=MsoNormal style='text-indent:.5in;background:#D9D9D9;border:none;
padding:0in'><span style='color:black'>If&nbsp;</span><i><span
style='font-size:11.5pt;line-height:107%;color:black'>P</span></i><span
style='font-size:11.5pt;line-height:107%;color:black'>(<i>E</i>(<i>s</i>),&nbsp;<i>E</i>(<i>s</i></span><sub><span
style='font-size:9.0pt;line-height:107%;color:black'>new</span></sub><span
style='font-size:11.5pt;line-height:107%;color:black'>),&nbsp;<i>T</i>) &#8805;
random(0, 1)</span><span style='color:black'>:</span></p>

<p class=MsoNormal style='text-indent:.5in;background:#D9D9D9;border:none;
padding:0in'><i><span style='font-size:11.5pt;line-height:107%;color:black'>        
s</span></i><span style='font-size:11.5pt;line-height:107%;color:black'>&nbsp;&#8592;&nbsp;<i>s</i></span><sub><span
style='font-size:9.0pt;line-height:107%;color:black'>new</span></sub></p>

<p class=MsoNormal style='background:#D9D9D9;border:none;padding:0in'><span
style='color:black'>Output: the final state&nbsp;</span><i><span
style='font-size:11.5pt;line-height:107%;color:black'>s</span></i></p>

<p class=MsoNormal style='background:#D9D9D9;border:none;padding:0in'><sup><span
style='color:black'>from: <a
href="https://en.wikipedia.org/wiki/Simulated_annealing">https://en.wikipedia.org/wiki/Simulated_annealing</a></span></sup></p>

</div>

<p class=MsoNormal><b>Parameters that I have used in this simulation are:</b></p>

<p class=MsoListParagraphCxSpFirst style='text-indent:-.25in'><span
style='font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span dir=LTR></span>Initial Temperature: starting temperature </p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-.25in'><span
style='font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span dir=LTR></span>Stopping Temperature: min value of the
temperature where to stop</p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-.25in'><span
style='font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span dir=LTR></span>Alpha - <span
style='font-size:11.0pt;line-height:107%;font-family:"Calibri",sans-serif;
position:relative;top:4.0pt'><img width=10 height=18
src="TSP%20travelling%20salesman%20problem_files/image001.png"></span>: it is
the <span style='color:#2C2C2C;background:white'>learning rate (ranges between
0 and 1)</span></p>

<p class=MsoListParagraphCxSpLast style='text-indent:-.25in'><span
style='font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span dir=LTR></span>Stopping Iteration: max iteration </p>

<p class=MsoNormal>Something worth mentioning is that we decrease the
temperature at each iteration, by multiplying the temperature by &#945; rate
(known as Cooling Schedule).</p>

<p class=MsoNormal>Also, in the case of decreasing the learning rate, one
should consider reducing the initial and stopping temperature, as well as
stopping iteration, to fine-tune the result.</p>

<p class=MsoNormal><b>Study cases: </b></p>

<p class=MsoNormal>In our case I used “Djibouti - 38 Cities” and “Qatar - 194
Cities” from <a href="http://www.math.uwaterloo.ca/tsp/world/countries.html">http://www.math.uwaterloo.ca/tsp/world/countries.html</a></p>

<p class=MsoNormal>In both cases, I have repeated the simulated annealing 5
times to produce the best solution by using the same parameters at each repetition.
The best solution and fitness generated was:</p>

<p class=MsoListParagraphCxSpFirst style='margin-bottom:0in;margin-bottom:.0001pt;
text-indent:-.25in;line-height:normal'>1.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;
</span><span dir=LTR></span>Djibouti - 38 Cities:</p>

<p class=MsoListParagraphCxSpLast style='margin-bottom:0in;margin-bottom:.0001pt;
line-height:normal'>&nbsp;</p>

<p class=MsoNormal>The best solution is (6660.8366) KM for the TSP journey with
a total execution time - for 5 repetitions, equals to 0 seconds.</p>

<div style='border:solid windowtext 1.0pt;padding:1.0pt 4.0pt 1.0pt 4.0pt;
background:#D9D9D9'>

<p class=MsoListParagraphCxSpFirst style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'>.............................................</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'>Starting Annealing ...</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'>Total Execution Time in
seconds: 0</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New"'>&nbsp;</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'>-- Resulted Fitness:</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'>Simulated Annealing 1,
best fitness is 6660.8366</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'>Simulated Annealing 2,
best fitness is 6973.0018</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'>Simulated Annealing 3,
best fitness is 7133.8403</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'>Simulated Annealing 4,
best fitness is 7179.9864</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'>Simulated Annealing 5,
best fitness is 7249.409</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New"'>&nbsp;</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'>Best Solution: </span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'> ++++++++++++++++++++++++++++++++++++++++++++++++++</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'> Initial
Temperature                 : 1000.000</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'> Learning Rate -
Alpha               : 0.999</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'> Stopping
Temperature                : 1e-05</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'> Stopping
Iteration                  : 500000.000</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'> Best Fitness - Greedy
Search        : 8167.403 </span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'> Best Fitness -
Simulated Annealing  : 6660.837</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'> Annealing improvement
over Greedy   : 18.400%</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'> Annealing Execution
Time in seconds : 0</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin:0in;margin-bottom:.0001pt;
background:#D9D9D9;border:none;padding:0in'><span style='font-size:9.0pt;
line-height:107%;font-family:"Courier New";color:black'>++++++++++++++++++++++++++++++++++++++++++++++++++</span></p>

</div>

<p class=MsoListParagraphCxSpMiddle style='margin-bottom:0in;margin-bottom:
.0001pt'>&nbsp;</p>

<p class=MsoListParagraphCxSpMiddle align=center style='margin-left:0in;
text-align:center'><img border=0 width=623 height=306 id="Picture 3"
src="TSP%20travelling%20salesman%20problem_files/image002.jpg"></p>

<p class=MsoListParagraphCxSpMiddle align=center style='margin-top:12.0pt;
text-align:center'><b><i><span style='font-size:10.0pt;line-height:107%'>“The fitness
curves - </span></i></b><b><i><span style='font-size:10.0pt;line-height:107%'>The
convergence curve”</span></i></b></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in'>&nbsp;</p>

<p class=MsoListParagraphCxSpMiddle>&nbsp;</p>

<p class=MsoListParagraphCxSpMiddle align=center style='margin-left:0in;
text-align:center'><img border=0 width=432 height=334 id="Picture 1"
src="TSP%20travelling%20salesman%20problem_files/image003.jpg"></p>

<p class=MsoListParagraphCxSpMiddle align=center style='text-align:center'><b><i><span
style='font-size:10.0pt;line-height:107%'>Best Route</span></i></b></p>

<p class=MsoListParagraphCxSpMiddle align=center style='margin-left:0in;
text-align:center'>&nbsp;</p>

<p class=MsoListParagraphCxSpLast style='text-indent:-.25in'>2.<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp; </span><span
dir=LTR></span>Qatar - 194 Cities:</p>

<p class=MsoNormal>In this case, I have tweaked the learning rate (<span
style='font-size:11.0pt;line-height:107%;font-family:"Century Gothic",sans-serif;
position:relative;top:4.0pt'><img width=10 height=18
src="TSP%20travelling%20salesman%20problem_files/image004.png"></span>) and both
initial and stopping temperatures, hence the best solution is (9832.537) KM for
the TSP journey with a total execution time - for 5 repetitions, equals to 0.</p>

<div style='border:solid windowtext 1.0pt;padding:1.0pt 4.0pt 1.0pt 4.0pt;
background:#D9D9D9'>

<p class=MsoListParagraphCxSpFirst style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'>.............................................</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'>Starting Annealing ...</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'>Total Execution Time in seconds: 244</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New"'>&nbsp;</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'>-- Resulted Fitness:</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'>Simulated Annealing 1, best fitness is
9832.5367</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'>Simulated Annealing 2, best fitness is
9888.1638</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'>Simulated Annealing 3, best fitness is
9980.0555</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'>Simulated Annealing 4, best fitness is
10001.9822</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'>Simulated Annealing 5, best fitness is
10162.5029</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New"'>&nbsp;</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'>Best Solution: </span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'> ++++++++++++++++++++++++++++++++++++++++++++++++++</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'> Initial Temperature                 :
100.000</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'> Learning Rate - Alpha               :
0.99999</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'> Stopping Temperature                :
0.001</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'> Stopping Iteration                  :
500000.000</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'> Best Fitness - Greedy Search        :
11559.790 </span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'> Best Fitness - Simulated Annealing  :
9832.537</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'> Annealing improvement over Greedy   :
14.900%</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'> Annealing Execution Time in seconds :
49</span></p>

<p class=MsoListParagraphCxSpMiddle style='margin-left:0in;background:#D9D9D9;
border:none;padding:0in'><span style='font-size:9.0pt;line-height:107%;
font-family:"Courier New";color:black'>++++++++++++++++++++++++++++++++++++++++++++++++++</span></p>

</div>

<p class=MsoListParagraphCxSpMiddle align=center style='margin-left:0in;
text-align:center'>&nbsp;</p>

<p class=MsoListParagraphCxSpMiddle align=center style='margin-left:0in;
text-align:center'>&nbsp;</p>

<p class=MsoListParagraphCxSpMiddle align=center style='margin-left:0in;
text-align:center'><img border=0 width=624 height=320 id="Picture 5"
src="TSP%20travelling%20salesman%20problem_files/image005.jpg"></p>

<p class=MsoListParagraphCxSpMiddle align=center style='margin-top:12.0pt;
text-align:center'><b><i><span style='font-size:10.0pt;line-height:107%'>“The fitness
curves - </span></i></b><b><i><span style='font-size:10.0pt;line-height:107%'>The
convergence curve”</span></i></b></p>

<p class=MsoListParagraphCxSpMiddle align=center style='margin-left:0in;
text-align:center'>&nbsp;</p>

<p class=MsoListParagraphCxSpMiddle align=center style='margin-left:0in;
text-align:center'><img border=0 width=432 height=432 id="Picture 4"
src="TSP%20travelling%20salesman%20problem_files/image006.jpg"></p>

<p class=MsoListParagraphCxSpLast align=center style='margin-left:0in;
text-align:center'><b><i><span style='font-size:10.0pt;line-height:107%'>Best Route</span></i></b></p>

</div>

</body>

</html>
