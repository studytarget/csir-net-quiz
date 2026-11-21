from h import *

Q_C3 = [
# C45
Q("C", 4, [P("The statements below are made about some animal pathogens that may evade innate and inflammatory responses by the following mechanisms:"),
  P("A. The flagellin of Proteobacteria has a mutation that prevents it from being recognized by Toll-like receptors (TLRs).<br>B. The lipopolysaccharides of <i>Helicobacter</i> have mutations that prevent it from being recognized by TLRs.<br>C. <i>M. tuberculosis</i> escapes from the phagosome to the cytosol, thereby avoiding degradation by lysosomal enzymes.<br>D. Influenza virus produces Yop protein that inhibits inflammasome activity.<br>E. <i>S. typhi</i> encodes a protein that binds Type I IFNs and prevents them from binding to the IFN receptor."),
  P("Which one of the following options represents the combination of all correct statements?")],
  ["B and C", "A and C", "D and E", "A and B"],
  E("NTA's key is A and B. Both describe altered pathogen-associated molecular patterns that are poorly recognised by TLR5 (flagellin) and TLR4 (lipid A of LPS), as tabulated in standard immunology texts (Kuby Immunology, innate immunity chapter).",
    {"1": "C is the wrong organism: phagosome escape into the cytosol is the textbook strategy of <i>Listeria</i>; the classic <i>M. tuberculosis</i> strategy is blocking phagosome–lysosome fusion.", "2": "C is false (see option 1).", "3": "D and E name the wrong organisms: Yop proteins belong to <i>Yersinia</i>, and soluble interferon-binding decoys are made by poxviruses."})),
# C46
Q("C", 3, [P("A lac-lambda hybrid system is developed to study the λ-repressor protein, in which the λ <i>cI</i> gene is under the control of <i>E. coli lac</i> promoter and operator, and the <i>lacZ</i> gene is under the control of λ-P<sub>RM</sub> promoter and O<sub>R</sub> operator of λ-phage. Both the plasmids are introduced in <i>E. coli</i> and the concentrations of the proteins are determined upon the addition of IPTG."),
  IMG("C46", "Two plasmids: lac promoter-operator driving lambda cI, and PRM with OR1-3 driving lacZ. Four graphs of protein against IPTG, with lambda repressor rising linearly in each. LacZ: A rises linearly; B falls linearly; C rises sigmoidally to a plateau; D stays high then falls"),
  P("Which graph correctly represents the expected results?")],
  ["A", "B", "C", "D"],
  E("IPTG induces the <i>lac</i> promoter, so λ repressor rises steadily with IPTG. P<sub>RM</sub> is weak on its own and is <b>activated</b> by repressor bound cooperatively at O<sub>R</sub>1 and O<sub>R</sub>2, which contacts RNA polymerase. Because binding is cooperative, LacZ expression rises sigmoidally once repressor passes a threshold, then levels off (graph C) (Ptashne, <i>A Genetic Switch</i>).",
    {"1": "A straight-line LacZ response ignores cooperative activation.", "2": "Repressor activates P<sub>RM</sub>; it does not shut it off.", "4": "Same error as B."},
    ["At very high repressor levels, occupancy of O<sub>R</sub>3 would eventually repress P<sub>RM</sub>; the graph covers the activation range."])),
# C47
Q("C", 2, [P("Actin dynamics in cells is dependent on several actin-binding proteins. Given below are actin-binding proteins in Column X and their typical function in Column Y."),
  MATCH([["A. Formin", "I. Nucleates assembly to form a branched network"], ["B. Arp2/3 complex", "II. Stabilizes filament, modulates binding of other accessory proteins"], ["C. Cofilin", "III. Nucleates assembly and remains associated with the growing plus end"], ["D. Tropomyosin", "IV. Binds ADP-actin filaments, accelerates disassembly"]]),
  P("Which one of the following options represents all correct matches between Column X and Column Y?")],
  ["A-(I) B-(II) C-(IV) D-(III)", "A-(III) B-(I) C-(IV) D-(II)", "A-(III) B-(II) C-(IV) D-(I)", "A-(II) B-(I) C-(IV) D-(III)"],
  E("Formins nucleate unbranched filaments and ride the growing barbed end (III). Arp2/3 nucleates branches at 70° on existing filaments (I). Cofilin binds ADP-actin, severs and speeds disassembly (IV). Tropomyosin lies along filaments, stabilising them and gating myosin and other binders (II).",
    {"1": "Swaps formin with Arp2/3 and puts tropomyosin as a nucleator.", "3": "Makes Arp2/3 a stabiliser and tropomyosin a nucleator.", "4": "Makes formin a stabiliser."})),
]
