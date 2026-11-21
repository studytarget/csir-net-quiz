from h import *

Q_B = [
# B1
Q("B", 10, [P("Which one of the following is the most significant factor that explains the evolution of iteroparity in animals?")],
  ["Slower developmental rates over their lifespan", "Predictable environmental conditions", "Low adult survival rates", "Cost per reproductive event is high"],
  E("Iteroparity (repeated breeding) is favoured where adults can expect to survive to breed again and where the environment is stable and predictable, so that reserving resources for future bouts pays off. This is the classic association of iteroparity with stable, density-regulated (K-type) environments, as opposed to semelparity in unpredictable or high-adult-mortality settings (Cole 1954; Charnov &amp; Schaffer 1973; Stearns 1992).",
    {"1": "Developmental rate influences age at maturity, not the choice between one and many breeding bouts.",
     "3": "Low adult survival favours <i>semelparity</i>: if an adult is unlikely to survive, it should invest everything in one bout.",
     "4": "A high fixed cost per breeding event also favours semelparity (one large bout amortises the cost)."})),
# B2
Q("B", 8, [P("In a population with the ABO blood group system, if the frequency of the allele I<sup>A</sup> is 0.3, the frequency of the allele I<sup>B</sup> is 0.2, and the frequency of the allele i is 0.5, what would be the expected percentage of population with blood group A, considering that the population is under Hardy-Weinberg equilibrium?")],
  ["9%", "24%", "39%", "42%"],
  E("Blood group A comprises I<sup>A</sup>I<sup>A</sup> and I<sup>A</sup>i. Under Hardy–Weinberg: p² + 2pr = 0.3² + 2(0.3)(0.5) = 0.09 + 0.30 = 0.39, i.e. 39%.",
    {"1": "9% is only the I<sup>A</sup>I<sup>A</sup> homozygotes (p²).",
     "2": "24% does not correspond to any ABO class here (blood group B would be q² + 2qr = 0.04 + 0.20 = 24%).",
     "4": "42% has no basis in these frequencies."})),
# B3
Q("B", 5, [P("Hormone pregnancy tests work by detecting the presence of the hormone, human chorionic gonadotropin (hCG) using immunoassay. Which types of cells will develop to produce hCG in pregnant females?")],
  ["Pluripotent stem cells", "Trophoblast cells", "Endometrial cells", "Granulosa cells"],
  E("hCG is secreted by the trophoblast, chiefly the syncytiotrophoblast that forms from the outer cell layer of the blastocyst during implantation. It maintains the corpus luteum (an LH-like action) until the placenta takes over progesterone production.",
    {"1": "The inner cell mass (pluripotent) forms the embryo proper and does not secrete hCG.",
     "3": "The endometrium is maternal tissue that becomes the decidua; it does not make hCG.",
     "4": "Granulosa cells are ovarian follicle cells that make oestrogen and inhibin."})),
# B4
Q("B", 3, [P("Match the columns:"),
  MATCH([["A. DnaB", "i. Pol α/primase"], ["B. DnaC", "ii. Cdc6"], ["C. β clamp", "iii. PCNA"], ["D. DnaG", "iv. MCM complex"]],
        ("Column X: <i>E. coli</i> genes involved in replication", "Column Y: Functional eukaryotic orthologues")),
  P("Which one of the following options represents all correct matches between Column X and Column Y?")],
  ["A (i) B (ii) C (iii) D (iv)", "A (iv) B (i) C (ii) D (iii)", "A (iv) B (ii) C (iii) D (i)", "A (ii) B (iv) C (iii) D (i)"],
  E("DnaB is the replicative helicase, the functional counterpart of the MCM2–7 complex (iv). DnaC loads DnaB onto DNA, as Cdc6 (with Cdt1) loads MCM (ii). The β sliding clamp corresponds to PCNA (iii). DnaG is the primase, the counterpart of Pol α/primase (i).",
    {"1": "Makes DnaB a primase and DnaG a helicase.", "2": "Mismatches all four pairs.", "4": "Swaps the helicase (MCM) and its loader (Cdc6)."})),
# B5
Q("B", 5, [P("The regeneration of a severed Axolotl limb is mediated by which one of the following cellular responses to injury?")],
  ["Blastema formation", "Transdifferentiation", "Induced pluripotency", "Stem cell dedifferentiation"],
  E("After amputation, the wound epidermis forms an apical epithelial cap and underlying cells accumulate as a <b>blastema</b>, a mass of lineage-restricted progenitors that proliferates and re-patterns the missing limb (epimorphic regeneration). Lineage tracing shows blastema cells largely keep their tissue memory rather than becoming pluripotent (Kragl et al. 2009, <i>Nature</i> 460:60–65).",
    {"2": "Transdifferentiation (e.g. lens regeneration from the dorsal iris in newts) is not the main mechanism of limb regeneration.",
     "3": "Blastema cells do not revert to pluripotency.",
     "4": "Dedifferentiation contributes cells to the blastema, but the organising response named for limb regeneration is blastema formation."})),
# B6
Q("B", 2, [P("A transmembrane receptor protein (X) and a transmembrane protein bound to the actin cytoskeleton (Y) with fluorescent tags were expressed in a cell. A fluorescence recovery after photobleaching (FRAP) experiment was performed on these proteins. Which one of the following options represents the most likely outcome of this experiment?")],
  ["Fluorescence of both proteins will be recovered at the same rate.", "Fluorescence of X will be recovered later than Y.", "Fluorescence of Y will be recovered later than X.", "Being membrane proteins, no recovery of fluorescence is expected."],
  E("FRAP recovery depends on lateral diffusion of unbleached molecules into the bleached area. A freely diffusing receptor (X) recovers quickly, whereas a protein tethered to the cortical actin cytoskeleton (Y) has restricted mobility and a larger immobile fraction, so it recovers more slowly and less completely.",
    {"1": "Cytoskeletal tethering clearly reduces mobility, so the rates differ.", "2": "This reverses the expected order.", "4": "Membrane proteins do diffuse laterally (fluid-mosaic model), so recovery occurs."})),
# B7
Q("B", 2, [P("Dynein is a microtubule-dependent motor protein essential for cellular processes. Which one of the following statements related to dynein function is INCORRECT?")],
  ["It helps in cilia and flagella beating.", "It transports organelles in anterograde direction.", "It participates in spindle assembly and positioning.", "It interacts with dynactin for efficient transport."],
  E("Cytoplasmic dynein is a minus-end-directed motor. In axons it carries cargo <b>retrogradely</b> (towards the cell body); anterograde (plus-end) transport is done by most kinesins.",
    {"1": "Correct: axonemal dyneins slide outer doublets to bend cilia and flagella.", "3": "Correct: dynein focuses spindle poles and pulls on astral microtubules from the cortex.", "4": "Correct: dynactin (with an adaptor such as BICD2) activates dynein and increases its processivity."})),
# B8
Q("B", 14, [P("Which of the following molecular marker techniques uses a single primer in a PCR reaction for identifying polymorphisms between genotypes?")],
  ["SSR (Simple sequence repeats)", "AFLP (Amplified fragment length polymorphism)", "RAPD (Randomly amplified polymorphic DNA)", "SCAR (Sequence characterized amplified regions)"],
  E("RAPD uses a single short (~10-mer) arbitrary primer at low annealing stringency; fragments arise wherever the primer binds on both strands within amplifiable distance (Williams et al. 1990, <i>Nucleic Acids Res</i> 18:6531).",
    {"1": "SSR markers use a pair of locus-specific primers flanking the repeat.", "2": "AFLP uses adaptor-specific primer pairs after restriction-ligation.", "4": "SCARs are locus-specific primer pairs designed from cloned RAPD/AFLP bands."})),
# B9
Q("B", 1, [P("Which one of the following statements with regard to glyoxylate cycle is INCORRECT?")],
  ["It is absent in humans.", "It occurs in specialized microsomes called glyoxysomes.", "This cycle allows for the synthesis of sugars from fatty acids.", "It involves enzymes of both the glyoxysome and the mitochondrion."],
  E("Glyoxysomes are specialised <b>peroxisomes</b> (microbodies) of germinating oil seeds. \"Microsomes\" are vesicles of fragmented ER produced by cell homogenisation, so calling glyoxysomes microsomes is incorrect.",
    {"1": "Correct: vertebrates lack isocitrate lyase and malate synthase.", "3": "Correct: by bypassing the two decarboxylations of the TCA cycle, acetyl-CoA yields net succinate/oxaloacetate for gluconeogenesis.", "4": "Correct: succinate made in the glyoxysome is converted to malate/oxaloacetate in mitochondria."})),
# B10
Q("B", 2, [P("Which one of the following statements regarding cytoskeleton proteins is INCORRECT?")],
  ["Actin and tubulin proteins appear to have arisen from single-copy genes, present before multicellular eukaryotes diverged.", "Tubulin specifically binds ATP, while actin binds preferentially to GTP.", "FtsZ, a tubulin relative, forms a filamentous ring needed to effect cell division in certain prokaryotic species.", "MreB, an actin relative, forms filaments required for the cell shape in certain prokaryotic species."],
  E("It is the other way round: tubulin is a GTPase (β-tubulin hydrolyses GTP) and actin binds and hydrolyses ATP.",
    {"1": "Correct: both are ancient, highly conserved families traceable to the common eukaryotic ancestor.", "3": "Correct: FtsZ forms the Z-ring at the division site.", "4": "Correct: MreB filaments direct lateral cell-wall synthesis in rod-shaped bacteria."})),
# B11
Q("B", 3, [P("A novel organism synthesizes proteins using ribosomes from the C-terminal end to the N-terminal end rather than the usual direction (N- to C-terminus). Which main chain atom will be the nucleophile for the reaction to form peptide bonds?")],
  ["Nitrogen of the amine group", "Carbon of the carboxyl group", "Oxygen of the carboxyl group", "Alpha-carbon (Cα)"],
  E("A peptide bond always forms by nucleophilic attack of an α-amino nitrogen on an activated carbonyl carbon. Reversing the direction only changes which partner carries which group: the free amine at the N-terminus of the growing chain would attack the ester-activated carbonyl of the incoming aminoacyl-tRNA. The nucleophile is still the amine nitrogen.",
    {"2": "The carbonyl carbon is the electrophile, not the nucleophile.", "3": "Carboxyl oxygen does not form the amide bond.", "4": "Cα is not nucleophilic."})),
# B12
Q("B", 10, [P("Many marine mammals communicate over several kilometres in the ocean. This is due to")],
  ["their ability to communicate using ultrasound.", "the higher density of water compared to air.", "lower oxygen levels in the open ocean.", "water filtering out high-frequency sounds."],
  E("Water is far denser and less compressible than air, so sound travels about 4.5 times faster (~1500 m s⁻¹) and is attenuated much less, especially at low frequencies. Baleen whales exploit this with low-frequency calls that propagate over very long distances, aided by the SOFAR channel.",
    {"1": "Ultrasound (used in echolocation) attenuates fastest, so it is short-range.", "3": "Oxygen level has no bearing on sound propagation.", "4": "Water does absorb high frequencies more, but that is a consequence of propagation in water, not the reason long-distance communication is possible."})),
# B13
Q("B", 8, [P("A mutation in a Drosophila gene causes a reduction in eye size, if animals are grown at 29°C but not at 18°C. This happens even if the animals bear a single copy of this mutation. Based on this information, this mutation can be described as:")],
  ["Temperature insensitive, dominant", "Temperature sensitive, recessive", "Temperature insensitive, recessive", "Temperature sensitive, dominant"],
  E("The phenotype appears at the restrictive temperature (29 °C) but not at the permissive one (18 °C), so it is temperature-sensitive. It is expressed in heterozygotes carrying a single copy, so it is dominant.",
    {"1": "The phenotype depends on temperature.", "2": "One copy is enough, so it is not recessive.", "3": "Wrong on both counts."})),
# B14
Q("B", 3, [P("The majority of modifications on histone molecules happen at their ____")],
  ["N-terminal tail.", "C-terminal tail.", "Globular core.", "Spread equally throughout the polypeptide."],
  E("Most post-translational marks (acetylation, methylation, phosphorylation of lysine, arginine and serine residues) lie on the flexible N-terminal tails, which protrude from the nucleosome and are accessible to writers and readers.",
    {"2": "C-terminal marks exist (e.g. H2A K119ub, H2B K120ub) but are fewer.", "3": "Core marks (e.g. H3K56ac, H3K79me) exist but are a minority.", "4": "Modifications are concentrated in the tails."})),
# B15
Q("B", 10, [P("Within a broadly distributed taxonomic clade, populations and species of larger size are generally found in colder environments, while populations and species of smaller size are typically found in warmer regions. This observation is commonly referred to as:")],
  ["Allen's rule", "Bergmann's rule", "Gause's rule", "Gloger's rule"],
  E("Bergmann's rule (1847): larger body size in colder climates, explained by a lower surface-area-to-volume ratio that reduces heat loss.",
    {"1": "Allen's rule concerns shorter appendages (ears, limbs) in colder climates.", "3": "Gause's rule is competitive exclusion.", "4": "Gloger's rule relates darker pigmentation to warm, humid climates."})),
# B16
Q("B", 4, [P("The CaM Kinase II acts as a molecular memory device as well as a frequency decoder of Ca<sup>2+</sup> oscillation. Which one of the following statements regarding CaM Kinase II is INCORRECT?")],
  ["CaM Kinase II activity increases as a function of Ca<sup>2+</sup> pulse frequency.", "CaM Kinase II requires Ca<sup>2+</sup> and Calmodulin to remain in an active state.", "A brain-specific CaM Kinase II knockout mouse will have difficulty in remembering where things are.", "The molecular memory function is lost in an autophosphorylation defective CaM Kinase II."],
  E("Once activated, neighbouring subunits of the dodecameric holoenzyme autophosphorylate each other on Thr286 (αCaMKII). This makes the kinase <b>autonomous</b>: it stays active after Ca²⁺/calmodulin has dissociated. That persistence is the basis of its \"memory\", so the statement that it needs Ca²⁺/CaM to remain active is incorrect.",
    {"1": "Correct: higher pulse frequency leaves less time for dephosphorylation between pulses, so autonomous activity accumulates (De Koninck &amp; Schulman 1998).", "3": "Correct: αCaMKII-null mice are impaired in hippocampal spatial learning (Silva et al. 1992).", "4": "Correct: the T286A mutant loses autonomy, LTP and spatial learning (Giese et al. 1998)."})),
# B17
Q("B", 7, [P("Which one of the following acetylcholine receptors is located in the nodal tissue of heart?")],
  ["M<sub>3</sub>", "N<sub>M</sub>", "M<sub>2</sub>", "M<sub>4</sub>"],
  E("SA and AV nodal cells express M<sub>2</sub> muscarinic receptors (G<sub>i/o</sub>-coupled). Vagal ACh released onto them opens GIRK (I<sub>K,ACh</sub>) channels and lowers cAMP, slowing heart rate and AV conduction.",
    {"1": "M<sub>3</sub> receptors are on smooth muscle, glands and endothelium.", "2": "N<sub>M</sub> receptors are on the skeletal-muscle end plate.", "4": "M<sub>4</sub> receptors are mainly in the CNS."})),
# B18
Q("B", 10, [P("Cleaner fish remove parasites from larger fish. Which evolutionary mechanism most likely maintains this interaction?")],
  ["Kin selection", "Mutualism", "Direct competition", "Character displacement"],
  E("Both partners gain: the cleaner (e.g. <i>Labroides dimidiatus</i>) gets food and the client loses parasites. Interspecific reciprocal benefit is mutualism, stabilised by partner choice and punishment of cheating cleaners that bite mucus (Bshary &amp; Grutter 2006, <i>Nature</i> 441:975).",
    {"1": "Kin selection requires relatedness; the partners belong to different species.", "3": "There is no shared limiting resource being contested.", "4": "Character displacement concerns competing species diverging."})),
# B19
Q("B", 6, [P("Which one of the following microbes is an obligate biotroph?")],
  ["<i>Botrytis cinerea</i>", "<i>Phytophthora infestans</i>", "<i>Puccinia graminis</i>", "<i>Trichoderma harzianum</i>"],
  E("Rust fungi such as <i>Puccinia graminis</i> (stem rust of wheat) can grow and complete their life cycle only on living host tissue, feeding through haustoria. They cannot be cultured on ordinary media: they are obligate biotrophs.",
    {"1": "<i>Botrytis</i> (grey mould) is a classic necrotroph.", "2": "<i>Phytophthora infestans</i> is a hemibiotroph and can be cultured.", "4": "<i>Trichoderma</i> is a free-living saprotroph and mycoparasite used in biocontrol."})),
# B20
Q("B", 10, [P("<i>Saara hardwickii</i>, a spiny-tailed lizard, is a diurnal, ground-dwelling species currently known from the Indian subcontinent. It is endemic to which one of the following habitats?")],
  ["Rainforests of Eastern Himalayas", "Dry deciduous forests of central India", "Moist deciduous forests of Western Ghats", "Thar desert of India"],
  E("The Indian spiny-tailed lizard is an arid-zone, burrow-dwelling herbivorous agamid of the Thar Desert and adjoining arid plains of Rajasthan, Gujarat and Pakistan.",
    {"1": "It is not a forest species.", "2": "It is not a forest species.", "3": "It is not a forest species."})),
# B21
Q("B", 7, [P("Which one of the following is generated in skeletal muscle cells by the single quanta of acetylcholine released from the motor nerve terminals?")],
  ["Inhibitory post-synaptic potential", "Inhibitory junction potential", "Endplate potential", "Miniature endplate potential"],
  E("Fatt &amp; Katz (1952) recorded small (~0.5–1 mV) spontaneous depolarisations at the resting end plate, each produced by one vesicle (quantum) of ACh. These are miniature endplate potentials. A nerve impulse releases ~100+ quanta together to give the full endplate potential.",
    {"1": "ACh at the vertebrate neuromuscular junction is excitatory (nicotinic).", "2": "Inhibitory junction potentials occur in smooth muscle, not vertebrate skeletal muscle.", "3": "The EPP is the summed response to many quanta."})),
# B22
Q("B", 7, [P("Which one of the following statements about human chorionic gonadotropin is INCORRECT?")],
  ["It contains galactose and hexosamine.", "Its α-subunit is identical in TSH.", "Its β-subunit is smaller than α-subunit in size.", "It is primarily luteinizing in nature."],
  E("hCG β (145 amino acids, with a long glycosylated C-terminal extension) is <b>larger</b> than the α-subunit (92 amino acids).",
    {"1": "Correct: hCG is a heavily glycosylated glycoprotein (N- and O-linked chains containing galactose, hexosamines and sialic acid).", "2": "Correct: hCG, LH, FSH and TSH share the same α-subunit (CGA gene); the β-subunit confers specificity.", "4": "Correct: hCG acts on the LH/CG receptor and rescues the corpus luteum."})),
# B23
Q("B", 2, [P("Which one of the following is NOT a major phospholipid in mammalian plasma membrane?")],
  ["Phosphatidylinositol", "Phosphatidylserine", "Sphingomyelin", "Cholesterol"],
  E("NTA's key gives phosphatidylinositol. Standard texts (Alberts, <i>Molecular Biology of the Cell</i>) list four major phospholipids of mammalian plasma membranes: phosphatidylcholine, phosphatidylethanolamine, phosphatidylserine and sphingomyelin. Together they make up more than half the membrane lipid. PI and its phosphorylated forms are functionally vital but quantitatively minor (a few percent).",
    {"2": "PS is one of the four major phospholipids (concentrated in the inner leaflet).", "3": "Sphingomyelin is a major phospholipid of the outer leaflet.", "4": "Cholesterol is a major membrane lipid but a sterol, not a phospholipid."},
    ["Strictly, cholesterol is also \"not a major phospholipid\". The question intends a phospholipid that is not quantitatively major, and NTA's final key accepts only option 1."])),
# B24
Q("B", 13, [P("Which experiment would best validate the bioremediation potential of a microbial strain degrading oil spills in seawater?")],
  ["Using seawater without oil contamination to monitor microbial growth.", "Testing microbial growth in seawater with added nutrients but no oil.", "Monitoring oil concentration in a system inoculated with microbes versus an uninoculated system.", "Comparing microbial growth in aerated versus non-aerated seawater samples."],
  E("Bioremediation is shown by the disappearance of the pollutant attributable to the organism. That requires measuring hydrocarbon concentration over time in inoculated microcosms against an uninoculated (or sterile) control, which separates biodegradation from evaporation, dispersion and abiotic loss.",
    {"1": "Without oil there is nothing to degrade.", "2": "Growth on nutrients alone does not show oil degradation.", "4": "This tests oxygen requirement, not degradation of the pollutant."})),
# B25
Q("B", 8, [P("UV mutagenesis was performed to isolate mutants of the <i>lacZ</i> gene. The mutation rate of this gene is 1 × 10<sup>−4</sup> per cell division. Assuming that an <i>E. coli</i> culture was initiated from a culture density of 1 × 10<sup>2</sup> cells and grown to a density of 1 × 10<sup>6</sup> cells, how many <i>lacZ</i> mutants are expected in this population?")],
  ["~1", "~10", "~100", "~1000"],
  E("NTA's final key is ~1. This corresponds to multiplying the mutation rate by the <i>fold</i> increase in cell number: (10<sup>6</sup>/10<sup>2</sup>) × 10<sup>−4</sup> = 10<sup>4</sup> × 10<sup>−4</sup> ≈ 1.",
    None,
    ["Caution, for your own understanding: in standard fluctuation-analysis terms, the number of cell divisions needed to grow from 10² to 10⁶ cells is N − N₀ ≈ 10⁶. The expected number of mutational <i>events</i> is therefore μ(N − N₀) ≈ 10⁻⁴ × 10⁶ ≈ 100. Because early mutants keep dividing, the expected number of mutant <i>cells</i> is larger still, ≈ μN·ln(N/N₀) (Luria &amp; Delbrück 1943; Lea &amp; Coulson 1949). The key is followed here for scoring, but the textbook expectation is ~100 events."])),
# B26
Q("B", 4, [P("Fill in the blanks:"), P("Glioblastomas, oligodendrogliomas, and astrocytomas harbour mutations in isocitrate dehydrogenase (IDH). The IDH mutations found in these cancers cause the enzyme to convert isocitrate into the oncometabolite, _____, which accumulates in cancer cells. This oncometabolite works by inhibiting several enzymes that require _____ for their function.")],
  ["2-hydroxyglutarate, succinate", "2-hydroxybutyrate, α-ketoglutarate", "2-hydroxyglutarate, 2-hydroxybutyrate", "2-hydroxyglutarate, α-ketoglutarate"],
  E("Heterozygous IDH1 R132 / IDH2 R172 mutations give the enzyme a neomorphic activity: it reduces α-KG to D-2-hydroxyglutarate (Dang et al. 2009, <i>Nature</i> 462:739). D-2HG is a structural analogue of α-KG and competitively inhibits α-KG-dependent dioxygenases, including TET DNA demethylases and JmjC histone demethylases. The result is a hypermethylated (G-CIMP) state (Xu et al. 2011, <i>Cancer Cell</i> 19:17).",
    {"1": "Succinate is a product of these dioxygenases (and itself an oncometabolite in SDH-deficient tumours), not their co-substrate.", "2": "2-Hydroxybutyrate is unrelated to IDH.", "3": "2-Hydroxybutyrate is not a dioxygenase co-substrate."})),
# B27
Q("B", 9, [P("The order Psilotales can be identified by which one of the following characteristics?")],
  ["Leafless and rootless body with a dichotomously branching stem", "Very large fronds, some reaching 4.5 m or more in length", "Scale leaves that are borne in whorls at the node", "A plant body that consists of microphylls and roots only"],
  E("<i>Psilotum</i> (whisk fern) has no true roots (only a rhizome with rhizoids and mycorrhizae) and no true leaves (only tiny enations), with a dichotomously branching aerial stem bearing synangia.",
    {"2": "Very large fronds describe marattioid or tree ferns.", "3": "Whorled scale leaves at nodes describe <i>Equisetum</i>.", "4": "Microphylls with roots describe lycophytes (<i>Lycopodium</i>, <i>Selaginella</i>)."})),
# B28
Q("B", 14, [P("Which one of the following techniques can identify acetylation on a lysine residue of a protein?")],
  ["Mass spectrometry", "SDS-PAGE", "Light scattering", "CD spectroscopy"],
  E("Lysine acetylation adds 42.011 Da. In tandem MS of proteolytic peptides, this mass shift is detected and localised to a specific residue from b/y fragment ions; acetyl-lysine also gives a diagnostic immonium ion at m/z 126.",
    {"2": "SDS-PAGE cannot resolve a 42 Da change or identify the residue.", "3": "Light scattering reports size and oligomeric state.", "4": "CD spectroscopy reports secondary structure."})),
# B29
Q("B", 7, [P("Which one of the following blood cell types is formed from megakaryocyte during development of blood cells from bone marrow?")],
  ["Monocytes", "Neutrophils", "Eosinophils", "Platelets"],
  E("Polyploid megakaryocytes extend proplatelet processes into marrow sinusoids and shed platelets (thrombocytes) into the circulation, under thrombopoietin control.",
    {"1": "Monocytes come from monoblasts.", "2": "Neutrophils come from myeloblasts.", "3": "Eosinophils come from myeloblasts."})),
# B30
Q("B", 3, [P("Which one of the following modifications in their native system does NOT lead to translation inhibition?")],
  ["Nucleotide addition resulting in incorporation of a stem-loop structure in the mRNA upstream of the Shine-Dalgarno sequence.", "Nucleotide addition resulting in the Shine-Dalgarno sequence being a part of a stem-loop structure in the mRNA.", "Expression of an eIF2 mutant that mimics its phosphorylated state.", "Mutation that leads to decrease in the processivity of capping enzyme that leaves numerous mRNAs devoid of CAP structure."],
  E("Bacterial 30S subunits bind directly at the Shine–Dalgarno/start-codon region, so a hairpin placed <i>upstream</i> of the SD, outside the ribosome footprint, leaves initiation essentially unaffected.",
    {"2": "Sequestering the SD in a stem-loop blocks 30S binding (the riboswitch and thermometer principle).", "3": "Phospho-eIF2α tightly binds and inhibits eIF2B, depleting eIF2·GTP·Met-tRNA<sub>i</sub> and inhibiting global translation.", "4": "Uncapped mRNAs are not recognised by eIF4E and are also degraded, so cap-dependent translation falls."})),
# B31
Q("B", 4, [P("Which one of the following statements about peripheral lymph nodes is INCORRECT?")],
  ["They contain fibroblast reticular cells that form a conduit system to guide cell movement within the node.", "They are responsible for immune responses to blood-borne pathogens.", "T cells encounter antigen presented on dendritic cells in the paracortex of lymph nodes.", "They contain B cells in special areas called follicles."],
  E("Lymph nodes filter <b>lymph</b> and respond to antigens arriving from tissues via afferent lymphatics. Blood-borne antigens are filtered by the <b>spleen</b>.",
    {"1": "Correct: the FRC network and conduits guide T cells and DCs and channel small antigens.", "3": "Correct: the paracortex is the T-cell zone where DCs present antigen.", "4": "Correct: B cells reside in cortical follicles and form germinal centres."})),
# B32
Q("B", 10, [P("As per the India State of Forest Report 2021, the percentage cover of 'very dense forests' as a component of the country's total geographical area is:")],
  ["3.04", "9.33", "9.44", "21.71"],
  E("ISFR 2021 (Forest Survey of India): very dense forest (canopy density ≥70%) covers 99,779 km², i.e. 3.04% of India's geographical area.",
    {"2": "9.33% is moderately dense forest.", "3": "9.44% matches no ISFR 2021 class (open forest is 9.34%).", "4": "21.71% is total forest cover (VDF + MDF + OF)."})),
# B33
Q("B", 9, [P("Which one of the following morphological characters can help you differentiate Leptosporangiate ferns from the Eusporangiate ferns?")],
  ["Presence and absence of sporangium", "Ploidy of the spores", "The number of cells from which the sporangium is formed", "The total number of alternations of generations recorded in a single life cycle"],
  E("A leptosporangium develops from a <b>single</b> superficial initial cell and has a one-cell-thick wall, few spores and an annulus. A eusporangium arises from <b>several</b> initials and has a multilayered wall and many spores (Goebel's classical distinction).",
    {"1": "Both groups have sporangia.", "2": "Spores are haploid in both.", "4": "Both show one alternation of generations per life cycle."})),
# B34
Q("B", 3, [P("Which one of the following statements about RNA polymerase in eukaryotes is INCORRECT?")],
  ["RNA polymerase I synthesizes 18S, 5.8S and 28S rRNAs.", "RNA polymerase II synthesizes messenger RNA (mRNA).", "RNA polymerase II requires a sigma factor (σ) to initiate transcription.", "RNA polymerase III synthesizes 5S rRNA and tRNA."],
  E("σ factors belong to bacterial RNA polymerase. Eukaryotic Pol II is recruited by general transcription factors (TFIIA, B, D, E, F and H) and Mediator.",
    {"1": "Correct: Pol I transcribes the 45S pre-rRNA, processed into 18S, 5.8S and 28S.", "2": "Correct.", "4": "Correct: Pol III also makes U6 snRNA and 7SL RNA."})),
# B35
Q("B", 2, [P("Which one of the following is likely to enter a pure phospholipid bilayer?")],
  ["CO<sub>2</sub> and Diethyl urea", "Water and Glucose", "Lysine and Ethanol", "Urea and Chloride ions"],
  E("Permeability of a protein-free bilayer rises with hydrophobicity and small size. CO₂ is a small non-polar gas and crosses readily. Diethylurea is much more lipophilic than urea and permeates far faster: the classic Collander–Overton series (Alberts, Fig. 11-1) shows permeability rising as hydrophobic ethyl groups are added to urea.",
    {"2": "Water permeates slowly, but glucose essentially does not.", "3": "Lysine is a charged amino acid and cannot cross.", "4": "Chloride, an ion, is essentially impermeant; urea crosses only slowly."})),
# B36
Q("B", 1, [P("The Citric acid cycle (TCA) operates only in the presence of molecular oxygen (O<sub>2</sub>). This is because")],
  ["O<sub>2</sub> activates enzymatic dehydrogenation reactions in the cycle.", "O<sub>2</sub> accepts electrons from electron transport chain, allowing reoxidation of NADH to NAD<sup>+</sup>.", "O<sub>2</sub> removes toxic by-products of the TCA cycle.", "O<sub>2</sub> activates ATP synthase."],
  E("No TCA step uses O₂ directly. The cycle needs a continuous supply of NAD⁺ and FAD for its four dehydrogenations. These are regenerated only when the electron transport chain passes electrons to O₂ (complex IV). Without O₂, NADH accumulates and the cycle stops.",
    {"1": "O₂ does not activate the dehydrogenases.", "3": "The TCA cycle makes no toxic by-product that O₂ removes.", "4": "ATP synthase is driven by the proton-motive force, not activated by O₂."})),
# B37
Q("B", 3, [P("Two types of mutant <i>E. coli</i> were identified: in the hypermethylation mutant (type A), DNA is methylated at the GATC sequences as soon as daughter DNA is synthesized; and in the second type, GATC sequences are never methylated (type B)."), P("Which mutant will have a greater effect on the MMR system, leading to the accumulation of spontaneous mutations?")],
  ["Type A &gt; Type B", "Type B &gt; Type A", "Type A = Type B", "Type B mutants will not accumulate spontaneous mutations"],
  E("MutH nicks the <b>unmethylated</b> strand of a hemimethylated GATC, which directs repair to the newly made strand. If the new strand is methylated immediately (Dam overproduction), the transient hemimethylated window disappears and MutH has no signal, so mismatches escape repair. Dam-overproducing strains are strong mutators (Herman &amp; Modrich 1981, <i>J Bacteriol</i> 145:644). In <i>dam</i>⁻ cells (type B), MutH can still nick either unmethylated strand. Repair then becomes non-directional, so about half of corrections are \"right\", and the mutator effect is milder.",
    {"2": "Unmethylated DNA still allows (undirected) repair, so the effect is weaker.", "3": "The effects differ in magnitude.", "4": "<i>dam</i>⁻ mutants do show a modest mutator phenotype."})),
# B38
Q("B", 5, [P("Which one of the following statements regarding mutations in the mitochondria during aging is INCORRECT?")],
  ["Mutations in mitochondrial genome lead to defects in energy production.", "The mutation rate in mitochondria is much higher than that in the nucleus.", "Mutations reduce ROS production since electron transport is faulty.", "There is an enhanced rate of apoptosis in cells with mutant mitochondria."],
  E("Defective respiratory complexes cause electron leakage, so ROS production generally <b>increases</b>. This feeds the \"vicious cycle\" of the mitochondrial free-radical theory of aging.",
    {"1": "Correct: mtDNA encodes 13 OXPHOS subunits.", "2": "Correct: mtDNA lacks protective histones, sits near ROS sources and has limited repair; its mutation rate is roughly 10–20× that of nuclear DNA.", "4": "Correct: dysfunctional mitochondria release cytochrome <i>c</i> more readily; the mtDNA-mutator (PolgA) mouse shows increased apoptosis and premature aging (Kujoth et al. 2005, <i>Science</i> 309:481)."})),
# B39
Q("B", 4, [P("Live vaccines are generally used to protect against which one of the following viruses?")],
  ["Hepatitis A", "Hepatitis B", "Rabies", "Smallpox"],
  E("Smallpox was eradicated using a live vaccinia virus vaccine, the archetypal live viral vaccine.",
    {"1": "Hepatitis A vaccines in general use are inactivated (formalin-killed); live attenuated HAV vaccines exist in China but are not the norm.", "2": "Hepatitis B vaccine is a recombinant HBsAg subunit vaccine.", "3": "Rabies vaccines (e.g. HDCV, PCECV) are inactivated."})),
# B40
Q("B", 9, [P("Which one of the following is an example of character displacement?")],
  ["Two sympatric lizards with similar morphologies consume the same insects.", "Two sympatric birds evolve distinct beak shapes to consume seeds of different plants.", "A predator evolves higher visual acuity to catch camouflaged prey.", "Two plant species have similar flower shapes to attract the same pollinators."],
  E("Character displacement (Brown &amp; Wilson 1956) is greater divergence of traits in sympatry than in allopatry, driven by competition for shared resources. The textbook case is beak depth in Galápagos ground finches (<i>Geospiza fortis</i> and <i>G. fuliginosa</i>; Grant &amp; Grant 2006, <i>Science</i> 313:224).",
    {"1": "This describes overlap and competition without divergence.", "3": "This is predator–prey coevolution (an arms race).", "4": "This is convergence (pollinator-mediated), the opposite of displacement."})),
# B41
Q("B", 8, [P("The disease phenylketonuria is caused by the null allele of the gene phenylalanine hydroxylase (PAH). This is an example of a recessive mutation. Which one of the following terms is the best description of the wild type allele of PAH?")],
  ["Gain-of-function", "Haplosufficient", "Epistatic", "Allele with additive effect"],
  E("Heterozygous carriers are unaffected, so one functional PAH allele makes enough enzyme. This is haplosufficiency, the usual reason loss-of-function alleles of enzymes are recessive (Kacser &amp; Burns 1981).",
    {"1": "The wild-type allele is the normal function, not a gain.", "3": "Epistasis describes interaction between different genes.", "4": "An additive allele would make heterozygotes intermediate."})),
# B42
Q("B", 5, [P("Which is the correct hierarchy of gene activity in early Drosophila segmentation?")],
  ["Gap, pair-rule, segment polarity, maternal", "Maternal, gap, pair-rule, segment polarity", "Maternal, pair-rule, gap, segment polarity", "Segment polarity, pair-rule, gap, maternal"],
  E("Maternal effect gradients (Bicoid, Nanos, Hunchback, Caudal) regulate gap genes (<i>hb</i>, <i>Kr</i>, <i>kni</i>, <i>gt</i>). Gap proteins regulate the stripes of pair-rule genes (<i>eve</i>, <i>ftz</i>), which in turn set up the segment-polarity genes (<i>en</i>, <i>wg</i>, <i>hh</i>) (Nüsslein-Volhard &amp; Wieschaus 1980).",
    {"1": "Maternal genes act first, not last.", "3": "Gap genes act before pair-rule genes.", "4": "This is the reverse order."})),
# B43
Q("B", 5, [P("The epigenetic regulators DEMETER (DME) and MEDEA (MEA) act synergistically to repress endosperm development in the absence of double fertilization during seed development in Arabidopsis. Which one of the following options is the correct enzymatic function of DME and MEA?")],
  ["DME is a DNA glycosylase; MEA is a DNA methyl transferase.", "DME is a DNA methyl transferase; MEA is a histone methyl transferase.", "DME is a histone methyl transferase; MEA is a DNA methyl transferase.", "DME is a DNA glycosylase; MEA is a histone methyl transferase."],
  E("DME is a 5-methylcytosine DNA glycosylase that removes methylation (base-excision demethylation) in the central cell (Choi et al. 2002, <i>Cell</i> 110:33). MEA is the SET-domain H3K27 methyltransferase of the FIS-PRC2 complex (homologous to E(z)), which represses autonomous endosperm proliferation.",
    {"1": "MEA methylates histones, not DNA.", "2": "DME removes rather than adds DNA methylation.", "3": "Both functions are swapped."})),
# B44
Q("B", 8, [P("The dominant and recessive alleles of a gene are 'A' and 'a', respectively. In 1000 offspring, if 500 are 'aa' and 500 are of the other genotypes, which one of the following is the most likely combination of parental genotypes?")],
  ["Aa and Aa", "AA and Aa", "Aa and aa", "AA and aa"],
  E("A 1:1 ratio of Aa : aa is the testcross ratio, Aa × aa.",
    {"1": "Aa × Aa gives 25% aa.", "2": "AA × Aa gives no aa.", "4": "AA × aa gives only Aa."})),
# B45
Q("B", 9, [P("What type of invertebrate fossils, commonly found in the Spiti Valley of India, are characteristic of the Cambrian era?")],
  ["Ammonites", "Trilobites", "Mosquitoes", "Glossopteris"],
  E("Trilobites are the index fossils of the Cambrian. The Parahio Valley section in Spiti (Tethyan Himalaya) yields rich Cambrian trilobite faunas.",
    {"1": "Ammonites (abundant in Spiti's Jurassic Spiti Shale) are Mesozoic.", "3": "Mosquitoes are Mesozoic and later insects, not characteristic Spiti fossils.", "4": "<i>Glossopteris</i> is a Permian seed-fern (a plant), not an invertebrate."})),
# B46
Q("B", 1, [P("Which one of the following types of interactions will be predominantly contributing to the stability of a nucleosome?")],
  ["Hydrogen bonds between DNA base pairs and serine/threonine residues of histones.", "van der Waal's interactions between DNA base pairs and hydrophobic residues of histones.", "Hydrogen bonds between DNA phosphate backbone and the main chain atoms of histones.", "Electrostatic interactions involving DNA phosphate backbone and lysine residues of histones."],
  E("Histone–DNA contacts in the nucleosome are largely sequence-independent and backbone-mediated. The dominant energetic contribution is electrostatic, between basic Lys/Arg side chains and the phosphate backbone, which neutralises its charge so the DNA can wrap 1.65 times around the octamer (Luger et al. 1997, <i>Nature</i> 389:251).",
    {"1": "Base-specific hydrogen bonds would make binding sequence-specific; nucleosomes are not.", "2": "The bases face inward and do not form a hydrophobic interface with histones.", "3": "Main-chain amide–phosphate hydrogen bonds do occur (at the 14 contact sites) but contribute less than the lysine/arginine electrostatics."})),
# B47
Q("B", 1, [P("Which one of the following statements is true regarding β-oxidation of fatty acids?")],
  ["It occurs in the intermembrane space (IMS) region of mitochondria.", "All the reactions are same for the saturated and unsaturated fatty acids.", "Fatty acids are oxidized at C-3 position to remove a two-carbon unit.", "Lipoprotein lipase catalyzes the first step."],
  E("The β-carbon (C-3) is oxidised to a ketone (via dehydrogenation, hydration and a second dehydrogenation). Thiolase then cleaves between C-2 and C-3, releasing acetyl-CoA.",
    {"1": "β-Oxidation is in the mitochondrial matrix (and in peroxisomes).", "2": "Unsaturated fatty acids need extra enzymes (enoyl-CoA isomerase, 2,4-dienoyl-CoA reductase).", "4": "The first step is acyl-CoA dehydrogenase; lipoprotein lipase hydrolyses triglycerides in the capillaries."})),
# B48
Q("B", 6, [P("Which one of the following events occurs during the light reaction of photosynthesis and directly contributes to the formation of ATP?")],
  ["Splitting of water molecules into oxygen, protons, and electrons", "Transfer of electrons from Photosystem I to NADP<sup>+</sup> to form NADPH", "Carbon fixation by the enzyme RuBisCO in the stroma", "Establishment of a proton gradient across the thylakoid membrane"],
  E("ATP synthesis by CF₀CF₁ ATP synthase is driven <i>directly</i> by the proton-motive force across the thylakoid membrane (Mitchell's chemiosmosis; Jagendorf's acid-bath experiment, 1966).",
    {"1": "Water splitting contributes lumenal protons, but it is the resulting gradient that drives the synthase.", "2": "NADP⁺ reduction consumes stromal protons and makes NADPH, not ATP.", "3": "Carbon fixation is a dark (Calvin–Benson) reaction that consumes ATP."})),
# B49
Q("B", 6, [P("Which of the following Vitamin B complex derivatives constitute the chromophore of the blue light photoreceptor cryptochrome in plants?")],
  ["B3 and B12", "B2 and B9", "B2 and B12", "B3 and B9"],
  E("Cryptochromes bind FAD (from riboflavin, vitamin B2) as the catalytic chromophore and 5,10-methenyltetrahydrofolate (MTHF, from folate, vitamin B9) as the light-harvesting antenna. This architecture is inherited from photolyases (Ahmad &amp; Cashmore 1993, <i>Nature</i> 366:162).",
    {"1": "B3 (NAD) and B12 (cobalamin) are not cryptochrome chromophores.", "3": "B12 is not involved.", "4": "B3 is not involved."})),
# B50
Q("B", 9, [P("Tectonic uplift can alter the drainage patterns of rivers, thereby isolating populations of many species. Population isolation of this kind results from which one of the following processes?")],
  ["Dispersal", "Vicariance", "Range expansion", "Competitive exclusion"],
  E("Vicariance is the splitting of a once-continuous population by a new geographic barrier (here, river drainages rearranged by uplift), without the organisms moving.",
    {"1": "Dispersal is the movement of organisms across an existing barrier.", "3": "Range expansion is the opposite of isolation.", "4": "Competitive exclusion is a biotic interaction, not geographic isolation."})),
]
