---
layout: default
title: Probenecid
parent: 僅模型預測 (L5)
nav_order: 1084
evidence_level: L5
indication_count: 3
---

# Probenecid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Probenecid: From Undocumented Original Indication to Renal Hypouricemia

## One-Sentence Summary

> Probenecid's originally approved indication is not documented in this evidence pack (data gap), and its mechanism of action record is also missing.
> The TxGNN model predicts it may be relevant to **Renal Hypouricemia**, but the supporting literature describes probenecid being used as a **diagnostic reagent** to characterize this condition rather than as a treatment for it — the direction of the drug's known uricosuric effect (increasing urate excretion) runs counter to what a hypouricemic patient would need.
> Currently **0 clinical trials** and **20 publications** touch on this pairing, none of which are therapeutic trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (blocking data gap; see DG001/DG002) |
| Predicted New Indication | Renal Hypouricemia (hypouricemia, renal) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 (mechanistic/case-report literature only; no clinical trials; literature uses probenecid as a diagnostic test agent, not a therapeutic one) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for probenecid is not available in this evidence pack (DG002). Based on the pharmacological behavior documented across the collected literature, probenecid acts as a **uricosuric agent** — it inhibits renal tubular reabsorption of urate, thereby *increasing* urinary uric acid excretion and lowering serum urate. This is precisely the mechanism that has historically made it useful in the opposite clinical context (hyperuricemia/gout), and it is also why probenecid appears repeatedly in the literature here as the "**probenecid test**" — a pharmacological probe used to differentiate subtypes of renal urate-transport defects, not as a treatment.

Renal hypouricemia is a condition defined by **already low serum uric acid** caused by defective urate reabsorption (commonly URAT1/SLC22A12 loss-of-function) or enhanced tubular secretion. Administering a drug that further promotes urate excretion would, mechanistically, be expected to worsen rather than correct this condition, and several of the case reports below explicitly show variable or paradoxical urate-clearance responses to probenecid in these patients rather than any therapeutic benefit.

Taken together, this TxGNN prediction most likely reflects a strong **network/co-occurrence association** between probenecid and the urate-transport pathway implicated in renal hypouricemia (since the drug is a standard diagnostic tool for this exact disease), rather than a genuine repurposing opportunity. This should be treated as a caution flag rather than a promising lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia etiologies for rheumatologists; frames renal causes and diagnostic work-up |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Case series | J Am Soc Nephrol | Clinical/molecular analysis of 32 patients with SLC22A12 (URAT1) mutations; correlates genotype with urate clearance |
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review | Molecular Genetics and Metabolism | Reviews hereditary renal hypouricemia caused by URAT1 loss-of-function mutations |
| [3813739](https://pubmed.ncbi.nlm.nih.gov/3813739/) | 1987 | Case series | Archives of Internal Medicine | 7 diabetic patients with renal hypouricemia; increased urate clearance via pyrazinamide-suppressible pathway |
| [8976099](https://pubmed.ncbi.nlm.nih.gov/8976099/) | 1996 | Review | Nihon Rinsho | Classification review of hyperuricemia/hypouricemia metabolic abnormalities |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Case report | American Journal of Kidney Diseases | Renal hypouricemia with exercise-induced ARF; discusses prevention, cites probenecid/pyrazinamide as diagnostic agents |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Case report | Nephron | Familial hypouricemia showing **attenuated** urate-clearance response to both probenecid and pyrazinamide (diagnostic use) |
| [8341392](https://pubmed.ncbi.nlm.nih.gov/8341392/) | 1993 | Case report | Nephron | Novel renal hypouricemia subtype with **no response** to probenecid, pyrazinamide, furosemide, or prednisolone |
| [7099326](https://pubmed.ncbi.nlm.nih.gov/7099326/) | 1982 | Case report | Nephron | Familial renal hypouricemia in which probenecid **paradoxically decreased** urate excretion |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | Case report | Nephron | Renal hypouricemia with urolithiasis; probenecid increased urate clearance during diagnostic testing, but urolithiasis was treated with urine alkalinization, not probenecid |

---

## US Market Information

Probenecid currently holds no license records in this dataset — `taiwan_regulatory.market_status` is "Not Marketed" and `total_licenses` = 0. No authorization table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: retrieval of TFDA-equivalent warnings/contraindications for probenecid is flagged in this evidence pack as a **blocking data gap (DG001)** — this must be resolved before any S1 safety screening can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A blocking data gap (DG001 — missing label warnings/contraindications) prevents any safety pre-screening.
- The mechanistic direction of probenecid (promotes urate excretion) is inconsistent with treating renal hypouricemia (a low-urate state); the supporting literature uses probenecid solely as a diagnostic reagent, not as therapy.
- The two lower-ranked predictions from this same evidence pack (Lesch-Nyhan syndrome, HGPRT partial deficiency) were independently scored L5/Hold for the same reason — both are hyperuricemia-driving conditions where increasing urate excretion is mechanistically undesirable and could worsen urate nephrolithiasis risk.

**To proceed, the following is needed:**
- Resolve DG001: obtain probenecid's approved label warnings/contraindications from a regulatory source (e.g., TFDA/FDA label PDF)
- Resolve DG002: obtain verified mechanism of action and the drug's actual original approved indication(s) from DrugBank or equivalent
- Independent pharmacological review of whether the TxGNN score for "renal hypouricemia" reflects a diagnostic-marker artifact rather than a therapeutic signal
- Search for any controlled or observational studies that test probenecid as an actual *treatment* (not a diagnostic challenge test) for this population, if any exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

