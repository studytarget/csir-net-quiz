from h import *

Q_C2 = [
# C38
Q("C", 10, [P("The table below gives the avian community composition of three communities (X, Y, Z), where '1' indicates the presence of the species in the community and '0' indicates its absence."),
  TBL(["Species", "X", "Y", "Z"], [["Red-vented bulbul", "1", "0", "1"], ["Purple sunbird", "0", "0", "1"], ["Common Babbler", "0", "1", "1"], ["Rufous treepie", "1", "1", "1"], ["Red-naped Ibis", "1", "1", "0"], ["Scarlet minivet", "0", "0", "1"], ["Spotted Owlet", "0", "1", "0"]]),
  P("Select the option that lists the correct order of similarity between pairs of communities based on Sorensen's coefficient of similarity.")],
  ["(X,Y) &gt; (Y,Z) &gt; (X,Z)", "(X,Y) &gt; (X,Z) &gt; (Y,Z)", "(Y,Z) &gt; (X,Z) &gt; (X,Y)", "(X,Y) = (X,Z) = (Y,Z)"],
  E("Sørensen's index is QS = 2C/(A + B), where A and B are the species counts of the two communities and C the number shared. X has 3 species, Y has 4 and Z has 5. Every pair shares 2 species (X–Y: treepie and ibis; X–Z: bulbul and treepie; Y–Z: babbler and treepie). So QS(X,Y) = 4/7 = 0.57, QS(X,Z) = 4/8 = 0.50 and QS(Y,Z) = 4/9 = 0.44.",
    {"1": "(Y,Z) is the least similar pair, not the middle one.", "3": "This is the reverse order.", "4": "The shared count is equal, but the denominators differ."})),
# C39
Q("C", 8, [P("In <i>Drosophila melanogaster</i>, a cross was performed, and the resulting progeny are indicated below."),
  TBL(["", "Females", "Males"], [["P", "Mutant: yellow body colour and sepia eye colour", "Wild type: gray body colour and red eye colour"], ["F<sub>1</sub>", "Gray body colour and red eye colour", "Yellow body colour and red eye colour"]]),
  P("The F<sub>1</sub> progeny were sib-mated and the F<sub>2</sub> progeny were analysed. The following statements were made based on the above crosses and analysis of the progeny:"),
  P("A. The mutation leading to sepia eye color is located on an autosome.<br>B. Yellow body is a dominant phenotype.<br>C. One fourth of the F<sub>2</sub> progeny will be males with yellow body color.<br>D. In this dihybrid cross, as the F<sub>2</sub> progeny do not show a 9:3:3:1 typical Mendelian ratio, the two genes can be assumed to be linked."),
  P("Which one of the following options correctly identifies each statement as True (T) or False (F) from A to D, respectively?")],
  ["T, F, T, F", "F, T, T, F", "T, T, F, F", "F, F, T, T"],
  E("<b>Body colour</b> shows crisscross inheritance: mutant mothers give yellow sons and wild-type daughters, so <i>yellow</i> is X-linked recessive. <b>Eye colour</b> is wild type in both F₁ sexes, so <i>sepia</i> is autosomal recessive (A true). Yellow is not dominant, since F₁ daughters are gray (B false). In F₂ (X<sup>y</sup>X<sup>+</sup> × X<sup>y</sup>Y), half the sons are yellow, i.e. 1/2 × 1/2 = 1/4 of all progeny are yellow males (C true). The deviation from 9:3:3:1 is due to X-linkage of one gene, not to linkage between the two genes, which lie on different chromosomes (D false).",
    {"2": "A is true and B is false.", "3": "C is true and B is false.", "4": "A is true and D is false."})),
# C40
Q("C", 6, [P("A researcher placed plant cells in a hypertonic solution to cause the cells to shrink. The following statements are made regarding the plasmolysed cells."),
  P("A. Microtubules are lost in the plasmolysed cells.<br>B. Protoplasts are retracted in the plasmolysed cells.<br>C. Hechtian strands are lost during plasmolysis.<br>D. Patches of plasma membrane remain affixed to the wall."),
  P("Which one of the following options represents the combination of all correct statements?")],
  ["A, B and C", "B and C only", "A, C and D", "B and D"],
  E("In plasmolysis the protoplast pulls away from the wall (B). It stays tethered at wall–membrane attachment sites, where patches of plasma membrane remain stuck to the wall (D). These attachments are drawn out into <b>Hechtian strands</b>, membranous threads containing cytoskeletal elements, which <i>form</i> during plasmolysis and help the protoplast re-expand on deplasmolysis (Oparka 1994, <i>New Phytol</i> 126:571).",
    {"1": "A and C are false: the cortical cytoskeleton is retained and reorganised, and Hechtian strands appear rather than disappear.", "2": "C is false, and D is omitted.", "3": "A and C are false."})),
# C41
Q("C", 5, [P("Gradient formation of Fgf8 is governed by both diffusion from a localized source and removal of Fgf8 ligand through endocytosis. Both Rab5C and dynamin promote endocytosis. What would happen to the Fgf8 concentration gradient when Rab5C is overexpressed or dynamin is inhibited?"),
  IMG("C41", "Four panels A to D of Fgf8 concentration against distance from source, each with a normal gradient, a dynamin-inhibition curve and a Rab5C-overexpression curve. A: both curves above normal. B: both below normal. C: dynamin inhibition above normal and shallower, Rab5C overexpression below normal and steeper. D: Rab5C overexpression above, dynamin inhibition below")],
  ["A", "B", "C", "D"],
  E("Fgf8 forms a source–sink gradient: free diffusion from the source, with receptor-mediated endocytosis acting as the sink (Yu et al. 2009, <i>Nature</i> 461:533). Blocking endocytosis (dominant-negative dynamin) removes the sink, so Fgf8 spreads further: a higher, shallower gradient. Enhancing endocytosis (Rab5C overexpression) increases clearance, giving a lower, steeper, shorter-range gradient (Scholpp &amp; Brand 2004, <i>Curr Biol</i> 14:1834). Panel C shows exactly this.",
    {"1": "Rab5C overexpression cannot raise the gradient.", "2": "Dynamin inhibition cannot lower the gradient.", "4": "The effects of the two manipulations are reversed."})),
# C42
Q("C", 7, [P("Given below are some statements regarding growth hormone (GH) secretion in humans."),
  P("A. Fasting increases GH secretion.<br>B. REM sleep decreases GH secretion.<br>C. Cortisol increases GH secretion.<br>D. Hypoglycemia decreases GH secretion."),
  P("Which one of the options given below represents both correct statements?")],
  ["A and B", "B and C", "C and D", "A and D"],
  E("A is true: fasting (protein or energy deficit) stimulates GH. B is true: the largest GH pulse comes with slow-wave (stage N3) sleep, while REM sleep is associated with low GH output. GH thus follows a metabolic logic of mobilising fuel when glucose and fatty acids are low (Guyton &amp; Hall, ch. 76).",
    {"2": "C is false: glucocorticoids <i>inhibit</i> GH secretion (via somatostatin), and chronic excess stunts growth.", "3": "C and D are false.", "4": "D is false: hypoglycaemia is a potent GH stimulus (the basis of the insulin tolerance test)."})),
# C43
Q("C", 10, [P("A parasitoid infects a host to complete its life cycle. Which of the following life-history traits typically characterizes this parasitoid, assuming that only one parasitoid infects one host?")],
  ["Intrinsic rate of population growth faster than hosts; Eventually fatal for the host", "Intrinsic rate of population growth slower than hosts; Immediately fatal for the host", "Intrinsic rate of population growth comparable to hosts; Eventually fatal for the host", "Intrinsic rate of population growth faster than hosts; Immediately fatal for the host"],
  E("A parasitoid's larva develops in or on a single host, which it consumes and kills only at the end of its development (eventually fatal). With one parasitoid per host, each parasitoid generation is tied to a host generation: one host yields one parasitoid. Generation time and potential population growth are therefore of the same order as the host's, as assumed in Nicholson–Bailey host–parasitoid dynamics (Godfray 1994, <i>Parasitoids</i>).",
    {"1": "With a one-to-one host–parasitoid relationship, the parasitoid cannot outgrow its host population.", "2": "Death is not immediate; the host stays alive while the larva develops (unlike predation).", "4": "Wrong on both growth rate and timing of death."})),
# C44
Q("C", 7, [P("When blood is forced into aorta from left ventricle during systole, a pressure wave is set up in aorta which is called pulse. Some features of the pulse are proposed in the following statements:"),
  P("A. The rate of travel of the pulse wave is lower than the velocity of blood flow in arteries.<br>B. The pulse wave moves slower with advancing age as the arteries become more rigid.<br>C. The pulse wave is strong when the stroke volume is large as in exercise.<br>D. The strength of the pulse depends on the magnitude of pulse pressure and not on the mean arterial pressure."),
  P("Which one of the following options represents the combination of correct statements?")],
  ["A, B, C and D", "B, C and D only", "C and D only", "A only"],
  E("C is true: a larger stroke volume raises pulse pressure, so the pulse feels strong. D is true: the palpable pulse reflects pulse pressure (systolic − diastolic), not mean pressure.",
    {"1": "A and B are false: pulse-wave velocity (~4–5 m/s in the aorta, 7–10 m/s peripherally) far exceeds blood velocity (&lt;0.5 m/s), and stiffer arteries in old age conduct the wave <i>faster</i> (PWV is the clinical index of arterial stiffness).", "2": "B is false.", "4": "A is false."})),
]
