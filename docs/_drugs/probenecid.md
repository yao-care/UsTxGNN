---
layout: default
title: Probenecid
parent: Moderate Evidence (L3-L4)
nav_order: 1084
evidence_level: L4
indication_count: 3
---

# Probenecid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Probenecid: From Gout (Hyperuricemia) to Renal Hypouricemia

## One-Sentence Summary

Probenecid is an oral uricosuric drug that lowers serum uric acid. It is best known for treating gout and hyperuricemia, although the license records provided do not list an indication.
The TxGNN model predicts it may be effective for **Renal Hypouricemia**, but there are **0 clinical trials** and **19 publications**, and none of the publications tests probenecid as a treatment.
This prediction is most likely a false positive driven by a shared urate-transport pathway.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout / hyperuricemia (general drug knowledge; the US license records provided contain no indication text) |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 10 (all listed licenses are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Probenecid is a uricosuric that inhibits the renal urate transporter URAT1 (SLC22A12) and organic anion transporters (OATs). This blocks urate reabsorption in the proximal tubule and lowers serum urate.

The high score most likely reflects a knowledge-graph link between probenecid and urate transport genes (URAT1/SLC22A12, GLUT9/SLC2A9). It is not a therapeutic rationale. Renal hypouricemia is a state of excess urate excretion, usually caused by loss-of-function variants in URAT1 or GLUT9. Giving a drug that further increases urate excretion would be expected to worsen the condition.

The literature is consistent with this reading. Probenecid appears in these papers as a diagnostic probe of tubular urate handling. Patients with a defective reabsorption pathway show a blunted or paradoxical response to it (for example PMID 854144, 8341392 and 7099326). Hypouricemia patients are also at risk of exercise-induced acute renal failure and urolithiasis, which further argues against adding a uricosuric.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The 10 most relevant publications are listed below. Reviews and cohort studies come first, followed by case reports where probenecid was used as a diagnostic probe.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review | Mol Genet Metab | Hereditary renal hypouricemia is mostly caused by loss-of-function SLC22A12 (URAT1) mutations that impair urate reabsorption |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clin Rheumatol | Narrative review of the causes and clinical approach to hypouricemia (serum urate < 2 mg/dL) |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort | J Am Soc Nephrol | 32 Japanese patients with renal hypouricemia; clinical features correlated with URAT1 gene variants |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Case report/Review | Am J Kidney Dis | Renal hypouricemia with recurrent exercise-induced acute renal failure; prevention discussed with a literature review |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Case report | Nephron | Familial hypouricemia with a proximal tubular defect; uric acid clearance responded only weakly to probenecid and pyrazinamide |
| [8341392](https://pubmed.ncbi.nlm.nih.gov/8341392/) | 1993 | Case report | Nephron | Novel renal hypouricemia type with drug-insensitive secretion and defective reabsorption; no urate response to probenecid |
| [7099326](https://pubmed.ncbi.nlm.nih.gov/7099326/) | 1982 | Case report | Nephron | Familial renal hypouricemia with idiopathic edema; urate excretion paradoxically decreased after probenecid |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | Case report | Nephron | Hypouricemia from enhanced tubular urate secretion with urolithiasis; probenecid markedly raised urate clearance; stones were managed with urine alkalization |
| [8533596](https://pubmed.ncbi.nlm.nih.gov/8533596/) | 1995 | Case report | Acta Paediatr Jpn | Adolescent with acute renal failure after exercise; probenecid and pyrazinamide tests showed a total defect of urate reabsorption |
| [7933674](https://pubmed.ncbi.nlm.nih.gov/7933674/) | 1994 | Case report | Nihon Jinzo Gakkai Shi | Incomplete combined defect of urate reabsorption; urate excretion rose only minimally after probenecid |

## US Market Information

The license records provided contain no approved-indication text. Five of the 10 licenses are shown.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA080966 | Probenecid | Tablet, film coated | Lannett Company, Inc. |
| ANDA084442 | Probenecid | Tablet, film coated | Actavis Pharma, Inc. |
| ANDA080966 | Probenecid | Tablet, film coated | Marlex Pharmaceuticals Inc |
| ANDA080966 | Probenecid | Tablet, film coated | Bryant Ranch Prepack |
| ANDA217020 | Probenecid | Tablet | Bryant Ranch Prepack |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.73%), but no clinical trials exist and no publication tests probenecid as a treatment for renal hypouricemia. The mechanism argues against benefit. Probenecid increases urinary urate excretion in a condition already defined by excess urate loss, which could raise the risk of exercise-induced acute renal failure and urolithiasis. The other two predictions, Lesch-Nyhan syndrome (99.39%) and partial HPRT deficiency (99.37%), have no supporting trials or literature. Both involve urate overproduction, where a uricosuric increases stone and nephropathy risk and xanthine oxidase inhibition is the appropriate approach.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- Evidence that probenecid could benefit patients with renal hypouricemia, for example a plausible therapeutic hypothesis beyond its use as a diagnostic probe
- A review of whether these graph-based predictions reflect pathway association rather than treatment benefit

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

